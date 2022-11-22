"""Connectivity to a MongoDB database for HEA resources.

A MongoDB collection name may only be used by one microservice in a database instance. In addition, for microservices
with content, the collections <collection_name>.files and <collection_name>.chunks will be used for storing the
content. The following collection names are used by existing HEA microservices and are reserved:

folders
folder_items
data_adapters
components
properties
volumes
organizations
"""
from contextlib import contextmanager
from motor import motor_asyncio
from aiohttp import web
from copy import deepcopy

from .mongoexpr import mongo_expr, sub_filter_expr
from ..heaobjectsupport import PermissionGroup, has_permissions
from ..aiohttp import RequestFileLikeWrapper
import bson
import pymongo
from bson.codec_options import CodecOptions
import logging
import configparser
from typing import Optional, List, Dict, Any, IO, Generator
from heaobject import user, root
from pymongo.results import UpdateResult, DeleteResult
from .database import Database, MicroserviceDatabaseManager
from yarl import URL
from motor.motor_asyncio import AsyncIOMotorGridFSBucket
from ..response import SupportsAsyncRead
from gridfs.errors import NoFile
from bson import ObjectId

_codec_options = CodecOptions(tz_aware=True)


class Mongo(Database):
    """
    Connectivity to a MongoDB database for HEA resources.
    """

    def __init__(self, config: Optional[configparser.ConfigParser],
                 connection_string: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 database_name: Optional[str] = None,
                 **kwargs) -> None:
        """
        Performs initialization.

        :param config: a configparser.ConfigParser object, which should have a MongoDB section with two properties:

                ConnectionString = the MongoDB connection string, default is http://localhost:5432
                Name = the database name, default is heaserver

                If the MongoDB section is missing or config argument is None, the default database name will be heaserver, and
                the default connection string will be http://localhost:27017.
        :param connection_string: an optional MongoDB connection string that will override any database connection
        string in a provided config file.
        :param username: an optional user name that will override any user name in the connection string.
        :param password: an optional password that will override any password in the connection string.
        :param database_name: an optional database name that will override any database name in a provided config file.
        """
        super().__init__(config, **kwargs)
        logger = logging.getLogger(__name__)

        default_connection_string = 'mongodb://heauser:heauser@localhost:27017/hea'

        config_section = Mongo.get_config_section()
        if config and config_section in config:
            logger.debug('Parsing MongoDB section of config file')
            database_section = config[config_section]
            if connection_string is not None:
                conn_url = URL(connection_string)
            else:
                connection_string = database_section.get('ConnectionString', default_connection_string)
                conn_url = URL(connection_string)
            if username is not None:
                conn_url = conn_url.with_user(username)
            if password is not None:
                conn_url = conn_url.with_password(password)
            logger.debug('\tUsing connection string %s', conn_url.with_password('xxxxxxxx'))
            if database_name is not None:
                name = database_name
            else:
                name = database_section.get('Name')
            client = motor_asyncio.AsyncIOMotorClient(str(conn_url))
            logger.debug('\tUsing database %s', name or 'default from connection string')
            self.__connection_pool = client.get_database(name=name)
        else:
            if connection_string is not None:
                conn_url = URL(connection_string)
            else:
                conn_url = URL(default_connection_string)
            if username is not None:
                conn_url = conn_url.with_user(username)
            if password is not None:
                conn_url = conn_url.with_password(password)
            logger.debug('\tUsing connection string %s',
                         str(conn_url.with_password('xxxxxxxx')) if conn_url.password is None else str(conn_url))
            client = motor_asyncio.AsyncIOMotorClient(str(conn_url))
            if database_name is not None:
                self.__connection_pool = client.get_database(name=database_name)
            else:
                self.__connection_pool = client.get_database()

    @classmethod
    def get_config_section(cls) -> str:
        return 'MongoDB'

    async def get(self, request: web.Request, collection: str, var_parts=None, mongoattributes=None,
                  sub: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Gets an object from the database.

        :param request: the aiohttp Request object (required).
        :param collection: the mockmongo collection (required).
        :param var_parts: the names of the dynamic resource's variable parts (required).
        :param mongoattributes: the attribute to query by. The default value is None. If None, the var_parts will be
        used as the attributes to query by.
        :param sub: the user to filter by.
        :return: a HEA name-value pair dict, or None if not found.
        """
        logger = logging.getLogger(__name__)
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        try:
            extra_ = sub_filter_expr(sub or user.NONE_USER,
                                     permissions=[perm.name for perm in PermissionGroup.GETTER_PERMS.perms])
            q = Mongo.__replace_object_ids(mongo_expr(request,
                                                      var_parts,
                                                      mongoattributes,
                                                      extra_))
            logger.debug('Query is %s', q)
            result = await coll.find_one(q)
            if result is not None:
                result['id'] = str(result['_id'])
                del result['_id']
            logger.debug('Got from mongo: %s', result)
            return result
        except bson.errors.InvalidId as e:
            logger.debug('Skipped mongo query: %s', e)
            return None

    async def get_content(self, request: web.Request, collection: str, var_parts=None, mongoattributes=None,
                          sub: Optional[str] = None) -> Optional[SupportsAsyncRead]:
        """
        Handles getting a HEA object's associated content.

        :param request: the HTTP request. Required.
        :param collection: the Mongo collection name. Required.
        :param var_parts: See heaserver.service.db.mongoexpr.mongo_expr.
        :param mongoattributes: See heaserver.service.db.mongoexpr.mongo_expr.
        :param sub: the user to filter by. Defaults to None.
        :return: a Response with the requested HEA object or Not Found.
        """
        obj = await self.get(request, collection, var_parts, mongoattributes, sub)
        if obj is None:
            return None
        fs = self.__new_gridfs_bucket(collection)
        try:
            return await fs.open_download_stream(ObjectId(request.match_info['id']))
        except NoFile:
            return None

    async def get_all(self, request: web.Request, collection: str, var_parts=None, mongoattributes=None,
                      sub: Optional[str] = None) -> List[root.HEAObjectDict]:
        """
        Handle a get request.

        :param request: the HTTP request (required).
        :param collection: the MongoDB collection containing the requested object (required).
        :param var_parts: the names of the dynamic resource's variable parts (required).
        :param mongoattributes: the attributes to query by. The default value is None. If None, the var_parts will be
        used as the attributes to query by.
        :param sub: the user to filter by.
        :return: an iterator of HEA name-value pair dicts with the results of the mockmongo query.
        """
        logger = logging.getLogger(__name__)
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        if var_parts is not None or mongoattributes is not None:
            q = Mongo.__replace_object_ids(mongo_expr(request,
                                                      var_parts,
                                                      mongoattributes,
                                                      sub_filter_expr(sub or user.NONE_USER,
                                                                      permissions=[perm.name for perm in
                                                                                   PermissionGroup.GETTER_PERMS.perms]))
                                           )
            logger.debug('Query is %s', q)
            results = await coll.find(q).to_list(10)
        else:
            q = sub_filter_expr(sub or user.NONE_USER,
                                permissions=[perm.name for perm in PermissionGroup.GETTER_PERMS.perms])
            logger.debug('Query is %s', q)
            results = await coll.find(q).to_list(10)
        for result in results:
            result['id'] = str(result['_id'])
            del result['_id']
        logger.debug('Got from mongo: %s', results)
        return results

    async def empty(self, request: web.Request, collection: str, var_parts=None, mongoattributes=None,
                    sub: Optional[str] = None) -> bool:
        """
        Returns whether there are no results returned from the query.

        :param request: the HTTP request (required).
        :param collection: the MongoDB collection containing the requested object (required).
        :param var_parts: the names of the dynamic resource's variable parts (required).
        :param mongoattributes: the attributes to query by. The default value is None. If None, the var_parts will be
        used as the attributes to query by.
        :param sub: the user to filter by.
        :return: True or False.
        """
        logger = logging.getLogger(__name__)
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        if var_parts is not None or mongoattributes is not None:
            q = Mongo.__replace_object_ids(mongo_expr(request,
                                                      var_parts,
                                                      mongoattributes,
                                                      sub_filter_expr(sub or user.NONE_USER,
                                                                      permissions=[perm.name for perm in
                                                                                   PermissionGroup.GETTER_PERMS.perms]))
                                           )
            logger.debug('Query is %s', q)
            result = await coll.find_one(q) is None
        else:
            q = sub_filter_expr(sub or user.NONE_USER,
                                permissions=[perm.name for perm in PermissionGroup.GETTER_PERMS.perms])
            logger.debug('Query is %s', q)
            result = await coll.find_one(q) is None
        logger.debug('Got from mongo: %s', result)
        return result

    async def post(self, request: web.Request, obj: root.DesktopObject, collection: str,
                   default_content: Optional[IO] = None) -> Optional[str]:
        """
        Handle a post request.

        :param request: the HTTP request (required).
        :param obj: the HEAObject instance to post.
        :param collection: the MongoDB collection containing the requested object (required).
        :param default_content: the content the HEA object will have once the object has been posted. If None, the
        object will not have content.
        :return: the generated id of the created object, or None if the object could not be inserted or was None.
        """
        return await self.insert(obj, collection, default_content)

    async def insert(self, obj: root.DesktopObject, collection: str, default_content: Optional[IO] = None):
        """
        Insert a desktop object into the database, with its content if provided.

        :param obj: the HEAObject instance to post.
        :param collection: the MongoDB collection containing the requested object (required).
        :param default_content: the content the HEA object will have once the object has been posted. If None, the
        object will not have content.
        :return: the generated id of the created object, or None if the object could not be inserted or was None.
        """
        if obj is None:
            return None
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        try:
            result = await coll.insert_one(document=obj.to_dict())
            if result and default_content is not None:
                fs = self.__new_gridfs_bucket(collection)
                await fs.upload_from_stream_with_id(ObjectId(obj.id), obj.display_name, default_content)
            return str(result.inserted_id)
        except (pymongo.errors.DuplicateKeyError, NoFile):
            return None

    async def put(self, request: web.Request, obj: root.HEAObject, collection: str, sub: Optional[str] = None) -> \
        Optional[UpdateResult]:
        """
        Handle a put request.

        :param request: the HTTP request (required).
        :param obj: the HEAObject instance to put.
        :param collection: the MongoDB collection containing the requested object (required).
        :param sub: the user to filter by. Defaults to None.
        :return: an instance of pymongo.results.UpdateResult.
        """
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        try:
            extra_ = sub_filter_expr(sub or user.NONE_USER,
                                     permissions=[perm.name for perm in PermissionGroup.PUTTER_PERMS.perms])
            mongo_expr_ = Mongo.__replace_object_ids(mongo_expr(request, 'id', extra=extra_))
            return await coll.replace_one(mongo_expr_, replace_id_with_object_id(obj.to_dict()))
        except bson.errors.InvalidId:
            return None

    async def put_content(self, request: web.Request, collection: str, sub: Optional[str] = None) -> bool:
        """
        Handle a put request of an HEA object's content.

        :param request: the HTTP request (required).
        :param collection: the MongoDB collection containing the requested object (required).
        :param sub: the user to filter by. Defaults to None.
        :return: Whether or not it was successful.
        """
        obj = await self.get(request, collection, var_parts=['id'], sub=sub)
        if obj is None:
            return False
        desktop_obj = root.desktop_object_from_dict(obj)
        if not has_permissions(desktop_obj, sub, PermissionGroup.PUTTER_PERMS.perms):
            return False
        try:
            fs = self.__new_gridfs_bucket(collection)
            fileobj = RequestFileLikeWrapper(request)
            fileobj.initialize()
            failed = True
            try:
                await fs.upload_from_stream_with_id(ObjectId(request.match_info['id']), obj['display_name'], fileobj)
                fileobj.close()
                failed = False
            except Exception as e:
                if failed:
                    try:
                        fileobj.close()
                    except:
                        pass
                raise e
            return True
        except NoFile:
            # Delete orphaned chunks from gridfs if an error occurred
            return False

    async def delete(self, request: web.Request, collection: str, var_parts=None, mongoattributes=None,
                     sub: Optional[str] = None) -> Optional[DeleteResult]:
        """
        Handle a delete request.

        :param request: the HTTP request.
        :param collection: the MongoDB collection containing the requested object (required).
        :param var_parts: See heaserver.service.db.mongoexpr.mongo_expr.
        :param mongoattributes: See heaserver.service.db.mongoexpr.mongo_expr.
        :param sub: the user to filter by. Defaults to None.
        :return: an instance of pymongo.results.DeleteResult.
        """
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        try:
            extra_ = sub_filter_expr(sub or user.NONE_USER,
                                     permissions=[perm.name for perm in PermissionGroup.DELETER_PERMS.perms])
            mongo_expr_ = Mongo.__replace_object_ids(mongo_expr(request, var_parts, mongoattributes, extra_))
            result = await coll.delete_many(mongo_expr_)
            if result:
                fs = self.__new_gridfs_bucket(collection)
                try:
                    await fs.delete(ObjectId(request.match_info['id']))
                except NoFile:
                    pass
                finally:
                    return result
        except bson.errors.InvalidId:
            pass
        return None

    @staticmethod
    def __replace_object_ids(filter_criteria) -> Dict[str, Any]:
        """
        Replaces all "id" fields with string value with an "_id" field with its bson.objectid.ObjectId value.

        :param filter_criteria: a MongoDB filter
        :return: a deep copy of the same filter, with string id fields replaced with ObjectId _id fields.
        :raises bson.errors.InvalidId: if any id fields are not a 12-byte input or a 24-character hex string.
        """
        logger = logging.getLogger(__name__)
        logger.debug('Input: %s', filter_criteria)

        def do_replace(filter_criteria_):
            result_ = {}
            for nm, val in filter_criteria_.items():
                if nm == 'id':
                    result_['_id'] = bson.objectid.ObjectId(val)
                elif isinstance(val, dict):
                    result_[nm] = do_replace(val)
                else:
                    result_[nm] = deepcopy(val)
            return result_

        result = do_replace(filter_criteria)
        logger.debug('Output: %s', result)
        return result

    def __new_gridfs_bucket(self, bucket: str) -> AsyncIOMotorGridFSBucket:
        return AsyncIOMotorGridFSBucket(self.__connection_pool, bucket)


def replace_id_with_object_id(obj: Dict[str, Any]):
    """
    Returns a shallow copy of the provided dict with any id key replaced by an _id key with an ObjectId value.
    :param obj: a HEA object as a dict.
    :return: a newly created dict.
    """
    if 'id' in obj:
        f_ = dict(obj)
        f_['_id'] = bson.ObjectId(f_.pop('id', None))
        return f_
    else:
        return dict(obj)


class MongoManager(MicroserviceDatabaseManager):
    """
    Database manager for a MongoDB database.
    """

    @contextmanager
    def database(self, config: configparser.ConfigParser = None) -> Generator[Mongo, None, None]:
        yield Mongo(config)
