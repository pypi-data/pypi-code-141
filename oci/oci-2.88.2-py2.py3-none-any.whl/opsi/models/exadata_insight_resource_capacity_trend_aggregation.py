# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataInsightResourceCapacityTrendAggregation(object):
    """
    Resource Capacity samples
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataInsightResourceCapacityTrendAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param end_timestamp:
            The value to assign to the end_timestamp property of this ExadataInsightResourceCapacityTrendAggregation.
        :type end_timestamp: datetime

        :param capacity:
            The value to assign to the capacity property of this ExadataInsightResourceCapacityTrendAggregation.
        :type capacity: float

        :param total_host_capacity:
            The value to assign to the total_host_capacity property of this ExadataInsightResourceCapacityTrendAggregation.
        :type total_host_capacity: float

        """
        self.swagger_types = {
            'end_timestamp': 'datetime',
            'capacity': 'float',
            'total_host_capacity': 'float'
        }

        self.attribute_map = {
            'end_timestamp': 'endTimestamp',
            'capacity': 'capacity',
            'total_host_capacity': 'totalHostCapacity'
        }

        self._end_timestamp = None
        self._capacity = None
        self._total_host_capacity = None

    @property
    def end_timestamp(self):
        """
        **[Required]** Gets the end_timestamp of this ExadataInsightResourceCapacityTrendAggregation.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :return: The end_timestamp of this ExadataInsightResourceCapacityTrendAggregation.
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this ExadataInsightResourceCapacityTrendAggregation.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :param end_timestamp: The end_timestamp of this ExadataInsightResourceCapacityTrendAggregation.
        :type: datetime
        """
        self._end_timestamp = end_timestamp

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this ExadataInsightResourceCapacityTrendAggregation.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE) for a set of databases.


        :return: The capacity of this ExadataInsightResourceCapacityTrendAggregation.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this ExadataInsightResourceCapacityTrendAggregation.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE) for a set of databases.


        :param capacity: The capacity of this ExadataInsightResourceCapacityTrendAggregation.
        :type: float
        """
        self._capacity = capacity

    @property
    def total_host_capacity(self):
        """
        Gets the total_host_capacity of this ExadataInsightResourceCapacityTrendAggregation.
        The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.


        :return: The total_host_capacity of this ExadataInsightResourceCapacityTrendAggregation.
        :rtype: float
        """
        return self._total_host_capacity

    @total_host_capacity.setter
    def total_host_capacity(self, total_host_capacity):
        """
        Sets the total_host_capacity of this ExadataInsightResourceCapacityTrendAggregation.
        The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.


        :param total_host_capacity: The total_host_capacity of this ExadataInsightResourceCapacityTrendAggregation.
        :type: float
        """
        self._total_host_capacity = total_host_capacity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
