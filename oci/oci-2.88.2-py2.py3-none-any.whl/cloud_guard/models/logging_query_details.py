# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoggingQueryDetails(object):
    """
    Additional details specific to the data source type (Sighting/Insight).
    """

    #: A constant which can be used with the logging_query_type property of a LoggingQueryDetails.
    #: This constant has a value of "INSIGHT"
    LOGGING_QUERY_TYPE_INSIGHT = "INSIGHT"

    def __init__(self, **kwargs):
        """
        Initializes a new LoggingQueryDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_guard.models.InsightTypeLoggingQueryDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param logging_query_type:
            The value to assign to the logging_query_type property of this LoggingQueryDetails.
            Allowed values for this property are: "INSIGHT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type logging_query_type: str

        """
        self.swagger_types = {
            'logging_query_type': 'str'
        }

        self.attribute_map = {
            'logging_query_type': 'loggingQueryType'
        }

        self._logging_query_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['loggingQueryType']

        if type == 'INSIGHT':
            return 'InsightTypeLoggingQueryDetails'
        else:
            return 'LoggingQueryDetails'

    @property
    def logging_query_type(self):
        """
        **[Required]** Gets the logging_query_type of this LoggingQueryDetails.
        Logging query type for data source (Sighting/Insight)

        Allowed values for this property are: "INSIGHT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The logging_query_type of this LoggingQueryDetails.
        :rtype: str
        """
        return self._logging_query_type

    @logging_query_type.setter
    def logging_query_type(self, logging_query_type):
        """
        Sets the logging_query_type of this LoggingQueryDetails.
        Logging query type for data source (Sighting/Insight)


        :param logging_query_type: The logging_query_type of this LoggingQueryDetails.
        :type: str
        """
        allowed_values = ["INSIGHT"]
        if not value_allowed_none_or_none_sentinel(logging_query_type, allowed_values):
            logging_query_type = 'UNKNOWN_ENUM_VALUE'
        self._logging_query_type = logging_query_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
