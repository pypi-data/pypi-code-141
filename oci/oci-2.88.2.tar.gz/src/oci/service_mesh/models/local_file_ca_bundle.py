# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .ca_bundle import CaBundle
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LocalFileCaBundle(CaBundle):
    """
    CA Bundle from the filesystem.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LocalFileCaBundle object with values from keyword arguments. The default value of the :py:attr:`~oci.service_mesh.models.LocalFileCaBundle.type` attribute
        of this class is ``LOCAL_FILE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this LocalFileCaBundle.
            Allowed values for this property are: "OCI_CERTIFICATES", "LOCAL_FILE"
        :type type: str

        :param secret_name:
            The value to assign to the secret_name property of this LocalFileCaBundle.
        :type secret_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'secret_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'secret_name': 'secretName'
        }

        self._type = None
        self._secret_name = None
        self._type = 'LOCAL_FILE'

    @property
    def secret_name(self):
        """
        Gets the secret_name of this LocalFileCaBundle.
        Name of the secret.
        For Kubernetes this will be the name of an opaque Kubernetes secret with key ca.crt.
        For other platforms the secret must be mounted at: /etc/oci/secrets/${secretName}/ca.crt


        :return: The secret_name of this LocalFileCaBundle.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """
        Sets the secret_name of this LocalFileCaBundle.
        Name of the secret.
        For Kubernetes this will be the name of an opaque Kubernetes secret with key ca.crt.
        For other platforms the secret must be mounted at: /etc/oci/secrets/${secretName}/ca.crt


        :param secret_name: The secret_name of this LocalFileCaBundle.
        :type: str
        """
        self._secret_name = secret_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
