# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TableStatisticSummary(object):
    """
    The summary of table statistics statuses, which includes status categories such as Stale, Not Stale, and No Stats,
    the number of table statistics grouped by status category, and the percentage of objects with a particular status.
    """

    #: A constant which can be used with the type property of a TableStatisticSummary.
    #: This constant has a value of "NO_STATS"
    TYPE_NO_STATS = "NO_STATS"

    #: A constant which can be used with the type property of a TableStatisticSummary.
    #: This constant has a value of "STALE"
    TYPE_STALE = "STALE"

    #: A constant which can be used with the type property of a TableStatisticSummary.
    #: This constant has a value of "NOT_STALE"
    TYPE_NOT_STALE = "NOT_STALE"

    def __init__(self, **kwargs):
        """
        Initializes a new TableStatisticSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TableStatisticSummary.
            Allowed values for this property are: "NO_STATS", "STALE", "NOT_STALE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param count:
            The value to assign to the count property of this TableStatisticSummary.
        :type count: int

        :param percentage:
            The value to assign to the percentage property of this TableStatisticSummary.
        :type percentage: float

        """
        self.swagger_types = {
            'type': 'str',
            'count': 'int',
            'percentage': 'float'
        }

        self.attribute_map = {
            'type': 'type',
            'count': 'count',
            'percentage': 'percentage'
        }

        self._type = None
        self._count = None
        self._percentage = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this TableStatisticSummary.
        The valid status categories of table statistics.

        Allowed values for this property are: "NO_STATS", "STALE", "NOT_STALE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this TableStatisticSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TableStatisticSummary.
        The valid status categories of table statistics.


        :param type: The type of this TableStatisticSummary.
        :type: str
        """
        allowed_values = ["NO_STATS", "STALE", "NOT_STALE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def count(self):
        """
        **[Required]** Gets the count of this TableStatisticSummary.
        The number of objects aggregated by status category.


        :return: The count of this TableStatisticSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this TableStatisticSummary.
        The number of objects aggregated by status category.


        :param count: The count of this TableStatisticSummary.
        :type: int
        """
        self._count = count

    @property
    def percentage(self):
        """
        **[Required]** Gets the percentage of this TableStatisticSummary.
        The percentage of objects with a particular status.


        :return: The percentage of this TableStatisticSummary.
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this TableStatisticSummary.
        The percentage of objects with a particular status.


        :param percentage: The percentage of this TableStatisticSummary.
        :type: float
        """
        self._percentage = percentage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
