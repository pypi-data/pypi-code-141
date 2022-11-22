# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeHostInsightsTopProcessesUsageCollection(object):
    """
    Top level response object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeHostInsightsTopProcessesUsageCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this SummarizeHostInsightsTopProcessesUsageCollection.
        :type timestamp: datetime

        :param items:
            The value to assign to the items property of this SummarizeHostInsightsTopProcessesUsageCollection.
        :type items: list[oci.opsi.models.TopProcessesUsage]

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'items': 'list[TopProcessesUsage]'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'items': 'items'
        }

        self._timestamp = None
        self._items = None

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this SummarizeHostInsightsTopProcessesUsageCollection.
        The start timestamp that was passed into the request.


        :return: The timestamp of this SummarizeHostInsightsTopProcessesUsageCollection.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this SummarizeHostInsightsTopProcessesUsageCollection.
        The start timestamp that was passed into the request.


        :param timestamp: The timestamp of this SummarizeHostInsightsTopProcessesUsageCollection.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def items(self):
        """
        **[Required]** Gets the items of this SummarizeHostInsightsTopProcessesUsageCollection.
        List of usage data samples for a top process on a specific date.


        :return: The items of this SummarizeHostInsightsTopProcessesUsageCollection.
        :rtype: list[oci.opsi.models.TopProcessesUsage]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SummarizeHostInsightsTopProcessesUsageCollection.
        List of usage data samples for a top process on a specific date.


        :param items: The items of this SummarizeHostInsightsTopProcessesUsageCollection.
        :type: list[oci.opsi.models.TopProcessesUsage]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
