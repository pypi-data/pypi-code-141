# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupSelector(object):
    """
    Defines how the instances in a instance group environment is selected.
    """

    #: A constant which can be used with the selector_type property of a ComputeInstanceGroupSelector.
    #: This constant has a value of "INSTANCE_IDS"
    SELECTOR_TYPE_INSTANCE_IDS = "INSTANCE_IDS"

    #: A constant which can be used with the selector_type property of a ComputeInstanceGroupSelector.
    #: This constant has a value of "INSTANCE_QUERY"
    SELECTOR_TYPE_INSTANCE_QUERY = "INSTANCE_QUERY"

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupSelector object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.ComputeInstanceGroupByIdsSelector`
        * :class:`~oci.devops.models.ComputeInstanceGroupByQuerySelector`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param selector_type:
            The value to assign to the selector_type property of this ComputeInstanceGroupSelector.
            Allowed values for this property are: "INSTANCE_IDS", "INSTANCE_QUERY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type selector_type: str

        """
        self.swagger_types = {
            'selector_type': 'str'
        }

        self.attribute_map = {
            'selector_type': 'selectorType'
        }

        self._selector_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['selectorType']

        if type == 'INSTANCE_IDS':
            return 'ComputeInstanceGroupByIdsSelector'

        if type == 'INSTANCE_QUERY':
            return 'ComputeInstanceGroupByQuerySelector'
        else:
            return 'ComputeInstanceGroupSelector'

    @property
    def selector_type(self):
        """
        **[Required]** Gets the selector_type of this ComputeInstanceGroupSelector.
        Defines the type of the instance selector for the group.

        Allowed values for this property are: "INSTANCE_IDS", "INSTANCE_QUERY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The selector_type of this ComputeInstanceGroupSelector.
        :rtype: str
        """
        return self._selector_type

    @selector_type.setter
    def selector_type(self, selector_type):
        """
        Sets the selector_type of this ComputeInstanceGroupSelector.
        Defines the type of the instance selector for the group.


        :param selector_type: The selector_type of this ComputeInstanceGroupSelector.
        :type: str
        """
        allowed_values = ["INSTANCE_IDS", "INSTANCE_QUERY"]
        if not value_allowed_none_or_none_sentinel(selector_type, allowed_values):
            selector_type = 'UNKNOWN_ENUM_VALUE'
        self._selector_type = selector_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
