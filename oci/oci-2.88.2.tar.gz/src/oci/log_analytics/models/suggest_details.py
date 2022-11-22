# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SuggestDetails(object):
    """
    Typeahead input.
    """

    #: A constant which can be used with the sub_system property of a SuggestDetails.
    #: This constant has a value of "LOG"
    SUB_SYSTEM_LOG = "LOG"

    def __init__(self, **kwargs):
        """
        Initializes a new SuggestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this SuggestDetails.
        :type compartment_id: str

        :param compartment_id_in_subtree:
            The value to assign to the compartment_id_in_subtree property of this SuggestDetails.
        :type compartment_id_in_subtree: bool

        :param query_string:
            The value to assign to the query_string property of this SuggestDetails.
        :type query_string: str

        :param sub_system:
            The value to assign to the sub_system property of this SuggestDetails.
            Allowed values for this property are: "LOG"
        :type sub_system: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'compartment_id_in_subtree': 'bool',
            'query_string': 'str',
            'sub_system': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'compartment_id_in_subtree': 'compartmentIdInSubtree',
            'query_string': 'queryString',
            'sub_system': 'subSystem'
        }

        self._compartment_id = None
        self._compartment_id_in_subtree = None
        self._query_string = None
        self._sub_system = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SuggestDetails.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this SuggestDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SuggestDetails.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this SuggestDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compartment_id_in_subtree(self):
        """
        Gets the compartment_id_in_subtree of this SuggestDetails.
        Flag to search all child compartments of the compartment Id specified in the compartmentId query parameter.


        :return: The compartment_id_in_subtree of this SuggestDetails.
        :rtype: bool
        """
        return self._compartment_id_in_subtree

    @compartment_id_in_subtree.setter
    def compartment_id_in_subtree(self, compartment_id_in_subtree):
        """
        Sets the compartment_id_in_subtree of this SuggestDetails.
        Flag to search all child compartments of the compartment Id specified in the compartmentId query parameter.


        :param compartment_id_in_subtree: The compartment_id_in_subtree of this SuggestDetails.
        :type: bool
        """
        self._compartment_id_in_subtree = compartment_id_in_subtree

    @property
    def query_string(self):
        """
        **[Required]** Gets the query_string of this SuggestDetails.
        Query seeking suggestions for.


        :return: The query_string of this SuggestDetails.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """
        Sets the query_string of this SuggestDetails.
        Query seeking suggestions for.


        :param query_string: The query_string of this SuggestDetails.
        :type: str
        """
        self._query_string = query_string

    @property
    def sub_system(self):
        """
        **[Required]** Gets the sub_system of this SuggestDetails.
        Default subsystem to qualify fields with in the queryString if not specified.

        Allowed values for this property are: "LOG"


        :return: The sub_system of this SuggestDetails.
        :rtype: str
        """
        return self._sub_system

    @sub_system.setter
    def sub_system(self, sub_system):
        """
        Sets the sub_system of this SuggestDetails.
        Default subsystem to qualify fields with in the queryString if not specified.


        :param sub_system: The sub_system of this SuggestDetails.
        :type: str
        """
        allowed_values = ["LOG"]
        if not value_allowed_none_or_none_sentinel(sub_system, allowed_values):
            raise ValueError(
                "Invalid value for `sub_system`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sub_system = sub_system

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
