# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStreamDetails(object):
    """
    Updatable information for a module stream
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStreamDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this ModuleStreamDetails.
        :type module_name: str

        :param stream_name:
            The value to assign to the stream_name property of this ModuleStreamDetails.
        :type stream_name: str

        """
        self.swagger_types = {
            'module_name': 'str',
            'stream_name': 'str'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'stream_name': 'streamName'
        }

        self._module_name = None
        self._stream_name = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStreamDetails.
        The name of a module


        :return: The module_name of this ModuleStreamDetails.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStreamDetails.
        The name of a module


        :param module_name: The module_name of this ModuleStreamDetails.
        :type: str
        """
        self._module_name = module_name

    @property
    def stream_name(self):
        """
        **[Required]** Gets the stream_name of this ModuleStreamDetails.
        The name of a stream of the specified module


        :return: The stream_name of this ModuleStreamDetails.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ModuleStreamDetails.
        The name of a stream of the specified module


        :param stream_name: The stream_name of this ModuleStreamDetails.
        :type: str
        """
        self._stream_name = stream_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
