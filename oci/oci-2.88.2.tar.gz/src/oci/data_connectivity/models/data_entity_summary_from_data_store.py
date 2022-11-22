# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_entity_summary import DataEntitySummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataEntitySummaryFromDataStore(DataEntitySummary):
    """
    The view entity data entity details.
    """

    #: A constant which can be used with the entity_type property of a DataEntitySummaryFromDataStore.
    #: This constant has a value of "TABLE"
    ENTITY_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the entity_type property of a DataEntitySummaryFromDataStore.
    #: This constant has a value of "VIEW"
    ENTITY_TYPE_VIEW = "VIEW"

    #: A constant which can be used with the entity_type property of a DataEntitySummaryFromDataStore.
    #: This constant has a value of "FILE"
    ENTITY_TYPE_FILE = "FILE"

    #: A constant which can be used with the entity_type property of a DataEntitySummaryFromDataStore.
    #: This constant has a value of "SQL"
    ENTITY_TYPE_SQL = "SQL"

    #: A constant which can be used with the entity_type property of a DataEntitySummaryFromDataStore.
    #: This constant has a value of "DATA_STORE"
    ENTITY_TYPE_DATA_STORE = "DATA_STORE"

    #: A constant which can be used with the entity_type property of a DataEntitySummaryFromDataStore.
    #: This constant has a value of "MESSAGE"
    ENTITY_TYPE_MESSAGE = "MESSAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new DataEntitySummaryFromDataStore object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.DataEntitySummaryFromDataStore.model_type` attribute
        of this class is ``DATA_STORE_ENTITY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataEntitySummaryFromDataStore.
            Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY", "DERIVED_ENTITY", "MESSAGE_ENTITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param metadata:
            The value to assign to the metadata property of this DataEntitySummaryFromDataStore.
        :type metadata: oci.data_connectivity.models.ObjectMetadata

        :param key:
            The value to assign to the key property of this DataEntitySummaryFromDataStore.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataEntitySummaryFromDataStore.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DataEntitySummaryFromDataStore.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this DataEntitySummaryFromDataStore.
        :type name: str

        :param description:
            The value to assign to the description property of this DataEntitySummaryFromDataStore.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this DataEntitySummaryFromDataStore.
        :type object_version: int

        :param external_key:
            The value to assign to the external_key property of this DataEntitySummaryFromDataStore.
        :type external_key: str

        :param shape:
            The value to assign to the shape property of this DataEntitySummaryFromDataStore.
        :type shape: oci.data_connectivity.models.Shape

        :param shape_id:
            The value to assign to the shape_id property of this DataEntitySummaryFromDataStore.
        :type shape_id: str

        :param entity_type:
            The value to assign to the entity_type property of this DataEntitySummaryFromDataStore.
            Allowed values for this property are: "TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param other_type_label:
            The value to assign to the other_type_label property of this DataEntitySummaryFromDataStore.
        :type other_type_label: str

        :param unique_keys:
            The value to assign to the unique_keys property of this DataEntitySummaryFromDataStore.
        :type unique_keys: list[oci.data_connectivity.models.UniqueKey]

        :param foreign_keys:
            The value to assign to the foreign_keys property of this DataEntitySummaryFromDataStore.
        :type foreign_keys: list[oci.data_connectivity.models.ForeignKey]

        :param resource_name:
            The value to assign to the resource_name property of this DataEntitySummaryFromDataStore.
        :type resource_name: str

        :param object_status:
            The value to assign to the object_status property of this DataEntitySummaryFromDataStore.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataEntitySummaryFromDataStore.
        :type identifier: str

        :param filters:
            The value to assign to the filters property of this DataEntitySummaryFromDataStore.
        :type filters: str

        :param is_effective_date_disabled:
            The value to assign to the is_effective_date_disabled property of this DataEntitySummaryFromDataStore.
        :type is_effective_date_disabled: bool

        :param is_flex_data_store:
            The value to assign to the is_flex_data_store property of this DataEntitySummaryFromDataStore.
        :type is_flex_data_store: bool

        :param is_silent_error:
            The value to assign to the is_silent_error property of this DataEntitySummaryFromDataStore.
        :type is_silent_error: bool

        :param supports_incremental:
            The value to assign to the supports_incremental property of this DataEntitySummaryFromDataStore.
        :type supports_incremental: bool

        """
        self.swagger_types = {
            'model_type': 'str',
            'metadata': 'ObjectMetadata',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'external_key': 'str',
            'shape': 'Shape',
            'shape_id': 'str',
            'entity_type': 'str',
            'other_type_label': 'str',
            'unique_keys': 'list[UniqueKey]',
            'foreign_keys': 'list[ForeignKey]',
            'resource_name': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'filters': 'str',
            'is_effective_date_disabled': 'bool',
            'is_flex_data_store': 'bool',
            'is_silent_error': 'bool',
            'supports_incremental': 'bool'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'metadata': 'metadata',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'external_key': 'externalKey',
            'shape': 'shape',
            'shape_id': 'shapeId',
            'entity_type': 'entityType',
            'other_type_label': 'otherTypeLabel',
            'unique_keys': 'uniqueKeys',
            'foreign_keys': 'foreignKeys',
            'resource_name': 'resourceName',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'filters': 'filters',
            'is_effective_date_disabled': 'isEffectiveDateDisabled',
            'is_flex_data_store': 'isFlexDataStore',
            'is_silent_error': 'isSilentError',
            'supports_incremental': 'supportsIncremental'
        }

        self._model_type = None
        self._metadata = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._external_key = None
        self._shape = None
        self._shape_id = None
        self._entity_type = None
        self._other_type_label = None
        self._unique_keys = None
        self._foreign_keys = None
        self._resource_name = None
        self._object_status = None
        self._identifier = None
        self._filters = None
        self._is_effective_date_disabled = None
        self._is_flex_data_store = None
        self._is_silent_error = None
        self._supports_incremental = None
        self._model_type = 'DATA_STORE_ENTITY'

    @property
    def key(self):
        """
        Gets the key of this DataEntitySummaryFromDataStore.
        The object key.


        :return: The key of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataEntitySummaryFromDataStore.
        The object key.


        :param key: The key of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this DataEntitySummaryFromDataStore.
        The model version of the object.


        :return: The model_version of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DataEntitySummaryFromDataStore.
        The model version of the object.


        :param model_version: The model_version of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this DataEntitySummaryFromDataStore.

        :return: The parent_ref of this DataEntitySummaryFromDataStore.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this DataEntitySummaryFromDataStore.

        :param parent_ref: The parent_ref of this DataEntitySummaryFromDataStore.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this DataEntitySummaryFromDataStore.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataEntitySummaryFromDataStore.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DataEntitySummaryFromDataStore.
        Detailed description of the object.


        :return: The description of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataEntitySummaryFromDataStore.
        Detailed description of the object.


        :param description: The description of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this DataEntitySummaryFromDataStore.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this DataEntitySummaryFromDataStore.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this DataEntitySummaryFromDataStore.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this DataEntitySummaryFromDataStore.
        :type: int
        """
        self._object_version = object_version

    @property
    def external_key(self):
        """
        Gets the external_key of this DataEntitySummaryFromDataStore.
        The external key of the object.


        :return: The external_key of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this DataEntitySummaryFromDataStore.
        The external key of the object.


        :param external_key: The external_key of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._external_key = external_key

    @property
    def shape(self):
        """
        Gets the shape of this DataEntitySummaryFromDataStore.

        :return: The shape of this DataEntitySummaryFromDataStore.
        :rtype: oci.data_connectivity.models.Shape
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DataEntitySummaryFromDataStore.

        :param shape: The shape of this DataEntitySummaryFromDataStore.
        :type: oci.data_connectivity.models.Shape
        """
        self._shape = shape

    @property
    def shape_id(self):
        """
        Gets the shape_id of this DataEntitySummaryFromDataStore.
        The shape ID.


        :return: The shape_id of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """
        Sets the shape_id of this DataEntitySummaryFromDataStore.
        The shape ID.


        :param shape_id: The shape_id of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._shape_id = shape_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this DataEntitySummaryFromDataStore.
        The entity type.

        Allowed values for this property are: "TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_type of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this DataEntitySummaryFromDataStore.
        The entity type.


        :param entity_type: The entity_type of this DataEntitySummaryFromDataStore.
        :type: str
        """
        allowed_values = ["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            entity_type = 'UNKNOWN_ENUM_VALUE'
        self._entity_type = entity_type

    @property
    def other_type_label(self):
        """
        Gets the other_type_label of this DataEntitySummaryFromDataStore.
        Specifies other type label.


        :return: The other_type_label of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._other_type_label

    @other_type_label.setter
    def other_type_label(self, other_type_label):
        """
        Sets the other_type_label of this DataEntitySummaryFromDataStore.
        Specifies other type label.


        :param other_type_label: The other_type_label of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._other_type_label = other_type_label

    @property
    def unique_keys(self):
        """
        Gets the unique_keys of this DataEntitySummaryFromDataStore.
        An array of unique keys.


        :return: The unique_keys of this DataEntitySummaryFromDataStore.
        :rtype: list[oci.data_connectivity.models.UniqueKey]
        """
        return self._unique_keys

    @unique_keys.setter
    def unique_keys(self, unique_keys):
        """
        Sets the unique_keys of this DataEntitySummaryFromDataStore.
        An array of unique keys.


        :param unique_keys: The unique_keys of this DataEntitySummaryFromDataStore.
        :type: list[oci.data_connectivity.models.UniqueKey]
        """
        self._unique_keys = unique_keys

    @property
    def foreign_keys(self):
        """
        Gets the foreign_keys of this DataEntitySummaryFromDataStore.
        An array of foreign keys.


        :return: The foreign_keys of this DataEntitySummaryFromDataStore.
        :rtype: list[oci.data_connectivity.models.ForeignKey]
        """
        return self._foreign_keys

    @foreign_keys.setter
    def foreign_keys(self, foreign_keys):
        """
        Sets the foreign_keys of this DataEntitySummaryFromDataStore.
        An array of foreign keys.


        :param foreign_keys: The foreign_keys of this DataEntitySummaryFromDataStore.
        :type: list[oci.data_connectivity.models.ForeignKey]
        """
        self._foreign_keys = foreign_keys

    @property
    def resource_name(self):
        """
        Gets the resource_name of this DataEntitySummaryFromDataStore.
        The resource name.


        :return: The resource_name of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this DataEntitySummaryFromDataStore.
        The resource name.


        :param resource_name: The resource_name of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def object_status(self):
        """
        Gets the object_status of this DataEntitySummaryFromDataStore.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this DataEntitySummaryFromDataStore.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DataEntitySummaryFromDataStore.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this DataEntitySummaryFromDataStore.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this DataEntitySummaryFromDataStore.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :return: The identifier of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DataEntitySummaryFromDataStore.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._identifier = identifier

    @property
    def filters(self):
        """
        Gets the filters of this DataEntitySummaryFromDataStore.
        Query filter for the extract. It can be null.


        :return: The filters of this DataEntitySummaryFromDataStore.
        :rtype: str
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this DataEntitySummaryFromDataStore.
        Query filter for the extract. It can be null.


        :param filters: The filters of this DataEntitySummaryFromDataStore.
        :type: str
        """
        self._filters = filters

    @property
    def is_effective_date_disabled(self):
        """
        Gets the is_effective_date_disabled of this DataEntitySummaryFromDataStore.
        It shows whether the effective date is disabled.


        :return: The is_effective_date_disabled of this DataEntitySummaryFromDataStore.
        :rtype: bool
        """
        return self._is_effective_date_disabled

    @is_effective_date_disabled.setter
    def is_effective_date_disabled(self, is_effective_date_disabled):
        """
        Sets the is_effective_date_disabled of this DataEntitySummaryFromDataStore.
        It shows whether the effective date is disabled.


        :param is_effective_date_disabled: The is_effective_date_disabled of this DataEntitySummaryFromDataStore.
        :type: bool
        """
        self._is_effective_date_disabled = is_effective_date_disabled

    @property
    def is_flex_data_store(self):
        """
        Gets the is_flex_data_store of this DataEntitySummaryFromDataStore.
        Is a flex data store. Metadata CSV will be generated for a flex data store.


        :return: The is_flex_data_store of this DataEntitySummaryFromDataStore.
        :rtype: bool
        """
        return self._is_flex_data_store

    @is_flex_data_store.setter
    def is_flex_data_store(self, is_flex_data_store):
        """
        Sets the is_flex_data_store of this DataEntitySummaryFromDataStore.
        Is a flex data store. Metadata CSV will be generated for a flex data store.


        :param is_flex_data_store: The is_flex_data_store of this DataEntitySummaryFromDataStore.
        :type: bool
        """
        self._is_flex_data_store = is_flex_data_store

    @property
    def is_silent_error(self):
        """
        Gets the is_silent_error of this DataEntitySummaryFromDataStore.
        Should the VO failure fail the whole batch?


        :return: The is_silent_error of this DataEntitySummaryFromDataStore.
        :rtype: bool
        """
        return self._is_silent_error

    @is_silent_error.setter
    def is_silent_error(self, is_silent_error):
        """
        Sets the is_silent_error of this DataEntitySummaryFromDataStore.
        Should the VO failure fail the whole batch?


        :param is_silent_error: The is_silent_error of this DataEntitySummaryFromDataStore.
        :type: bool
        """
        self._is_silent_error = is_silent_error

    @property
    def supports_incremental(self):
        """
        Gets the supports_incremental of this DataEntitySummaryFromDataStore.
        It shows whether the datastore supports incremental extract.


        :return: The supports_incremental of this DataEntitySummaryFromDataStore.
        :rtype: bool
        """
        return self._supports_incremental

    @supports_incremental.setter
    def supports_incremental(self, supports_incremental):
        """
        Sets the supports_incremental of this DataEntitySummaryFromDataStore.
        It shows whether the datastore supports incremental extract.


        :param supports_incremental: The supports_incremental of this DataEntitySummaryFromDataStore.
        :type: bool
        """
        self._supports_incremental = supports_incremental

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
