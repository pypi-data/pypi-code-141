# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GetManifestResponse(object):
    """
    The response returned for the get manifest call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GetManifestResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param serialized_manifest:
            The value to assign to the serialized_manifest property of this GetManifestResponse.
        :type serialized_manifest: str

        """
        self.swagger_types = {
            'serialized_manifest': 'str'
        }

        self.attribute_map = {
            'serialized_manifest': 'serializedManifest'
        }

        self._serialized_manifest = None

    @property
    def serialized_manifest(self):
        """
        Gets the serialized_manifest of this GetManifestResponse.
        The serialized manifest response.


        :return: The serialized_manifest of this GetManifestResponse.
        :rtype: str
        """
        return self._serialized_manifest

    @serialized_manifest.setter
    def serialized_manifest(self, serialized_manifest):
        """
        Sets the serialized_manifest of this GetManifestResponse.
        The serialized manifest response.


        :param serialized_manifest: The serialized_manifest of this GetManifestResponse.
        :type: str
        """
        self._serialized_manifest = serialized_manifest

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
