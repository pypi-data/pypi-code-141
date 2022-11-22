# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOciObjectStorageConnectionDetails(UpdateConnectionDetails):
    """
    The information to update a OCI Object Storage Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOciObjectStorageConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateOciObjectStorageConnectionDetails.connection_type` attribute
        of this class is ``OCI_OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateOciObjectStorageConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateOciObjectStorageConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateOciObjectStorageConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOciObjectStorageConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOciObjectStorageConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateOciObjectStorageConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateOciObjectStorageConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateOciObjectStorageConnectionDetails.
        :type nsg_ids: list[str]

        :param tenancy_id:
            The value to assign to the tenancy_id property of this UpdateOciObjectStorageConnectionDetails.
        :type tenancy_id: str

        :param region:
            The value to assign to the region property of this UpdateOciObjectStorageConnectionDetails.
        :type region: str

        :param user_id:
            The value to assign to the user_id property of this UpdateOciObjectStorageConnectionDetails.
        :type user_id: str

        :param private_key_file:
            The value to assign to the private_key_file property of this UpdateOciObjectStorageConnectionDetails.
        :type private_key_file: str

        :param public_key_fingerprint:
            The value to assign to the public_key_fingerprint property of this UpdateOciObjectStorageConnectionDetails.
        :type public_key_fingerprint: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'tenancy_id': 'str',
            'region': 'str',
            'user_id': 'str',
            'private_key_file': 'str',
            'public_key_fingerprint': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'tenancy_id': 'tenancyId',
            'region': 'region',
            'user_id': 'userId',
            'private_key_file': 'privateKeyFile',
            'public_key_fingerprint': 'publicKeyFingerprint'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._tenancy_id = None
        self._region = None
        self._user_id = None
        self._private_key_file = None
        self._public_key_fingerprint = None
        self._connection_type = 'OCI_OBJECT_STORAGE'

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this UpdateOciObjectStorageConnectionDetails.
        The `OCID`__ of the related OCI tenancy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tenancy_id of this UpdateOciObjectStorageConnectionDetails.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this UpdateOciObjectStorageConnectionDetails.
        The `OCID`__ of the related OCI tenancy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tenancy_id: The tenancy_id of this UpdateOciObjectStorageConnectionDetails.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def region(self):
        """
        Gets the region of this UpdateOciObjectStorageConnectionDetails.
        The name of the region. e.g.: us-ashburn-1


        :return: The region of this UpdateOciObjectStorageConnectionDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this UpdateOciObjectStorageConnectionDetails.
        The name of the region. e.g.: us-ashburn-1


        :param region: The region of this UpdateOciObjectStorageConnectionDetails.
        :type: str
        """
        self._region = region

    @property
    def user_id(self):
        """
        Gets the user_id of this UpdateOciObjectStorageConnectionDetails.
        The `OCID`__ of the OCI user who will access the Object Storage.
        The user must have write access to the bucket they want to connect to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The user_id of this UpdateOciObjectStorageConnectionDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UpdateOciObjectStorageConnectionDetails.
        The `OCID`__ of the OCI user who will access the Object Storage.
        The user must have write access to the bucket they want to connect to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param user_id: The user_id of this UpdateOciObjectStorageConnectionDetails.
        :type: str
        """
        self._user_id = user_id

    @property
    def private_key_file(self):
        """
        Gets the private_key_file of this UpdateOciObjectStorageConnectionDetails.
        The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :return: The private_key_file of this UpdateOciObjectStorageConnectionDetails.
        :rtype: str
        """
        return self._private_key_file

    @private_key_file.setter
    def private_key_file(self, private_key_file):
        """
        Sets the private_key_file of this UpdateOciObjectStorageConnectionDetails.
        The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :param private_key_file: The private_key_file of this UpdateOciObjectStorageConnectionDetails.
        :type: str
        """
        self._private_key_file = private_key_file

    @property
    def public_key_fingerprint(self):
        """
        Gets the public_key_fingerprint of this UpdateOciObjectStorageConnectionDetails.
        The fingerprint of the API Key of the user specified by the userId.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :return: The public_key_fingerprint of this UpdateOciObjectStorageConnectionDetails.
        :rtype: str
        """
        return self._public_key_fingerprint

    @public_key_fingerprint.setter
    def public_key_fingerprint(self, public_key_fingerprint):
        """
        Sets the public_key_fingerprint of this UpdateOciObjectStorageConnectionDetails.
        The fingerprint of the API Key of the user specified by the userId.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :param public_key_fingerprint: The public_key_fingerprint of this UpdateOciObjectStorageConnectionDetails.
        :type: str
        """
        self._public_key_fingerprint = public_key_fingerprint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
