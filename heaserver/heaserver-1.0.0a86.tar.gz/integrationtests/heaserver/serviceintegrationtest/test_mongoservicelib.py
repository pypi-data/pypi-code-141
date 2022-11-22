from heaserver.service.testcase.microservicetestcase import MicroserviceTestCase
from heaserver.service.testcase.dockermongo import DockerMongoManager, RealRegistryContainerConfig
from heaserver.service.db import database
from heaserver.service.testcase.testenv import MicroserviceContainerConfig
from heaobject.user import NONE_USER
from heaobject.volume import DEFAULT_FILE_SYSTEM, Volume, DefaultFileSystem
from heaobject.registry import Resource

from typing import Dict, List, Any

fixtures: Dict[str, List[Dict[str, Any]]] = {
    'components': [],
    'volumes': [
        {
            'id': '666f6f2d6261722d71757578',
            'created': None,
            'derived_by': None,
            'derived_from': [],
            'description': None,
            'display_name': 'HEA Root',
            'invites': [],
            'modified': None,
            'name': 'heaobject.volume.DefaultFileSystem^DEFAULT_FILE_SYSTEM',
            'owner': NONE_USER,
            'shares': [],
            'source': None,
            'type': 'heaobject.volume.Volume',
            'version': None,
            'file_system_type': DefaultFileSystem.get_type_name(),
            'file_system_name': DEFAULT_FILE_SYSTEM,
            'credential_id': '666f6f2d6261722d71757578',
            'folder_id': None,
            'mime_type': 'application/x.volume'
        }
    ],
    'credentials': [
        {
            'id': '666f6f2d6261722d71757578',
            'created': None,
            'derived_by': None,
            'derived_from': [],
            'description': None,
            'display_name': 'HEA Root',
            'invites': [],
            'modified': None,
            'name': 'root',
            'owner': NONE_USER,
            'shares': [],
            'source': None,
            'type': 'heaobject.keychain.Credentials',
            'version': None,
            'where': None,
            'account': None,
            'password': None
        }
    ]
}

volume_microservice = MicroserviceContainerConfig(
    image='registry.gitlab.com/huntsman-cancer-institute/risr/hea/heaserver-volumes:1.0.0a10', port=8080,
    check_path='/volumes', db_manager_cls=DockerMongoManager,
    resources=[Resource(resource_type_name='heaobject.volume.Volume',
                        base_path='/volumes',
                        file_system_name=DEFAULT_FILE_SYSTEM),
               Resource(resource_type_name='heaobject.volume.FileSystem',
                        base_path='/filesystems',
                        file_system_name=DEFAULT_FILE_SYSTEM)])
keychain_microservice = MicroserviceContainerConfig(
    image='registry.gitlab.com/huntsman-cancer-institute/risr/hea/heaserver-keychain:1.0.0a4', port=8080,
    check_path='/credentials', db_manager_cls=DockerMongoManager,
    resources=[Resource(resource_type_name='heaobject.keychain.Credentials',
                        base_path='/credentials',
                        file_system_name=DEFAULT_FILE_SYSTEM)])


class KeychainTestCase(MicroserviceTestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(coll='credentials', desktop_objects=fixtures, db_manager_cls=DockerMongoManager,
                         methodName=methodName,
                         registry_docker_image=RealRegistryContainerConfig(
                             image='registry.gitlab.com/huntsman-cancer-institute/risr/hea/heaserver-registry:1.0.0a24'),
                         other_docker_images=[volume_microservice, keychain_microservice])

    async def test_get_credential(self):
        volume = Volume()
        volume.from_dict(fixtures['volumes'][0])
        credential = await database._get_credentials(self.app, volume)
        self.assertEqual(fixtures['credentials'][0], credential.to_dict() if credential is not None else None)


class VolumeTestCase(MicroserviceTestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(coll='volumes', desktop_objects=fixtures, db_manager_cls=DockerMongoManager,
                         methodName=methodName, registry_docker_image=RealRegistryContainerConfig(
                image='registry.gitlab.com/huntsman-cancer-institute/risr/hea/heaserver-registry:1.0.0a24'),
                         other_docker_images=[volume_microservice, keychain_microservice])

    async def test_get_volume(self):
        volume, _ = await database._get_volume(self.app, '666f6f2d6261722d71757578')
        self.assertEqual(fixtures['volumes'][0], volume.to_dict() if volume is not None else None)
