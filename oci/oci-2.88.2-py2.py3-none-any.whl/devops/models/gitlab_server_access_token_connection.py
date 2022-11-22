# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GitlabServerAccessTokenConnection(Connection):
    """
    The properties that define a connection of the type `GITLAB_SERVER_ACCESS_TOKEN`.
    This type corresponds to a connection in GitLab self-hosted server that is authenticated with a
    personal access token.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GitlabServerAccessTokenConnection object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.GitlabServerAccessTokenConnection.connection_type` attribute
        of this class is ``GITLAB_SERVER_ACCESS_TOKEN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GitlabServerAccessTokenConnection.
        :type id: str

        :param description:
            The value to assign to the description property of this GitlabServerAccessTokenConnection.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this GitlabServerAccessTokenConnection.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GitlabServerAccessTokenConnection.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this GitlabServerAccessTokenConnection.
        :type project_id: str

        :param connection_type:
            The value to assign to the connection_type property of this GitlabServerAccessTokenConnection.
            Allowed values for this property are: "GITHUB_ACCESS_TOKEN", "GITLAB_ACCESS_TOKEN", "GITLAB_SERVER_ACCESS_TOKEN", "BITBUCKET_SERVER_ACCESS_TOKEN", "BITBUCKET_CLOUD_APP_PASSWORD", "VBS_ACCESS_TOKEN"
        :type connection_type: str

        :param time_created:
            The value to assign to the time_created property of this GitlabServerAccessTokenConnection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this GitlabServerAccessTokenConnection.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GitlabServerAccessTokenConnection.
            Allowed values for this property are: "ACTIVE"
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GitlabServerAccessTokenConnection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GitlabServerAccessTokenConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this GitlabServerAccessTokenConnection.
        :type system_tags: dict(str, dict(str, object))

        :param access_token:
            The value to assign to the access_token property of this GitlabServerAccessTokenConnection.
        :type access_token: str

        :param base_url:
            The value to assign to the base_url property of this GitlabServerAccessTokenConnection.
        :type base_url: str

        :param tls_verify_config:
            The value to assign to the tls_verify_config property of this GitlabServerAccessTokenConnection.
        :type tls_verify_config: oci.devops.models.TlsVerifyConfig

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'project_id': 'str',
            'connection_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'access_token': 'str',
            'base_url': 'str',
            'tls_verify_config': 'TlsVerifyConfig'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'connection_type': 'connectionType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'access_token': 'accessToken',
            'base_url': 'baseUrl',
            'tls_verify_config': 'tlsVerifyConfig'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._compartment_id = None
        self._project_id = None
        self._connection_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._access_token = None
        self._base_url = None
        self._tls_verify_config = None
        self._connection_type = 'GITLAB_SERVER_ACCESS_TOKEN'

    @property
    def access_token(self):
        """
        **[Required]** Gets the access_token of this GitlabServerAccessTokenConnection.
        The OCID of personal access token saved in secret store.


        :return: The access_token of this GitlabServerAccessTokenConnection.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this GitlabServerAccessTokenConnection.
        The OCID of personal access token saved in secret store.


        :param access_token: The access_token of this GitlabServerAccessTokenConnection.
        :type: str
        """
        self._access_token = access_token

    @property
    def base_url(self):
        """
        **[Required]** Gets the base_url of this GitlabServerAccessTokenConnection.
        The baseUrl of the hosted GitLabServer.


        :return: The base_url of this GitlabServerAccessTokenConnection.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """
        Sets the base_url of this GitlabServerAccessTokenConnection.
        The baseUrl of the hosted GitLabServer.


        :param base_url: The base_url of this GitlabServerAccessTokenConnection.
        :type: str
        """
        self._base_url = base_url

    @property
    def tls_verify_config(self):
        """
        Gets the tls_verify_config of this GitlabServerAccessTokenConnection.

        :return: The tls_verify_config of this GitlabServerAccessTokenConnection.
        :rtype: oci.devops.models.TlsVerifyConfig
        """
        return self._tls_verify_config

    @tls_verify_config.setter
    def tls_verify_config(self, tls_verify_config):
        """
        Sets the tls_verify_config of this GitlabServerAccessTokenConnection.

        :param tls_verify_config: The tls_verify_config of this GitlabServerAccessTokenConnection.
        :type: oci.devops.models.TlsVerifyConfig
        """
        self._tls_verify_config = tls_verify_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
