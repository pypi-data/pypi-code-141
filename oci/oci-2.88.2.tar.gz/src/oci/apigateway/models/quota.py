# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Quota(object):
    """
    Quota policy for a usage plan.
    """

    #: A constant which can be used with the unit property of a Quota.
    #: This constant has a value of "MINUTE"
    UNIT_MINUTE = "MINUTE"

    #: A constant which can be used with the unit property of a Quota.
    #: This constant has a value of "HOUR"
    UNIT_HOUR = "HOUR"

    #: A constant which can be used with the unit property of a Quota.
    #: This constant has a value of "DAY"
    UNIT_DAY = "DAY"

    #: A constant which can be used with the unit property of a Quota.
    #: This constant has a value of "WEEK"
    UNIT_WEEK = "WEEK"

    #: A constant which can be used with the unit property of a Quota.
    #: This constant has a value of "MONTH"
    UNIT_MONTH = "MONTH"

    #: A constant which can be used with the reset_policy property of a Quota.
    #: This constant has a value of "CALENDAR"
    RESET_POLICY_CALENDAR = "CALENDAR"

    #: A constant which can be used with the operation_on_breach property of a Quota.
    #: This constant has a value of "REJECT"
    OPERATION_ON_BREACH_REJECT = "REJECT"

    #: A constant which can be used with the operation_on_breach property of a Quota.
    #: This constant has a value of "ALLOW"
    OPERATION_ON_BREACH_ALLOW = "ALLOW"

    def __init__(self, **kwargs):
        """
        Initializes a new Quota object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this Quota.
        :type value: int

        :param unit:
            The value to assign to the unit property of this Quota.
            Allowed values for this property are: "MINUTE", "HOUR", "DAY", "WEEK", "MONTH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit: str

        :param reset_policy:
            The value to assign to the reset_policy property of this Quota.
            Allowed values for this property are: "CALENDAR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type reset_policy: str

        :param operation_on_breach:
            The value to assign to the operation_on_breach property of this Quota.
            Allowed values for this property are: "REJECT", "ALLOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_on_breach: str

        """
        self.swagger_types = {
            'value': 'int',
            'unit': 'str',
            'reset_policy': 'str',
            'operation_on_breach': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'unit': 'unit',
            'reset_policy': 'resetPolicy',
            'operation_on_breach': 'operationOnBreach'
        }

        self._value = None
        self._unit = None
        self._reset_policy = None
        self._operation_on_breach = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Quota.
        The number of requests that can be made per time period.


        :return: The value of this Quota.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Quota.
        The number of requests that can be made per time period.


        :param value: The value of this Quota.
        :type: int
        """
        self._value = value

    @property
    def unit(self):
        """
        **[Required]** Gets the unit of this Quota.
        The unit of time over which quotas are calculated.
        Example: `MINUTE` or `MONTH`

        Allowed values for this property are: "MINUTE", "HOUR", "DAY", "WEEK", "MONTH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit of this Quota.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this Quota.
        The unit of time over which quotas are calculated.
        Example: `MINUTE` or `MONTH`


        :param unit: The unit of this Quota.
        :type: str
        """
        allowed_values = ["MINUTE", "HOUR", "DAY", "WEEK", "MONTH"]
        if not value_allowed_none_or_none_sentinel(unit, allowed_values):
            unit = 'UNKNOWN_ENUM_VALUE'
        self._unit = unit

    @property
    def reset_policy(self):
        """
        **[Required]** Gets the reset_policy of this Quota.
        The policy that controls when quotas will reset.
        Example: `CALENDAR`

        Allowed values for this property are: "CALENDAR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The reset_policy of this Quota.
        :rtype: str
        """
        return self._reset_policy

    @reset_policy.setter
    def reset_policy(self, reset_policy):
        """
        Sets the reset_policy of this Quota.
        The policy that controls when quotas will reset.
        Example: `CALENDAR`


        :param reset_policy: The reset_policy of this Quota.
        :type: str
        """
        allowed_values = ["CALENDAR"]
        if not value_allowed_none_or_none_sentinel(reset_policy, allowed_values):
            reset_policy = 'UNKNOWN_ENUM_VALUE'
        self._reset_policy = reset_policy

    @property
    def operation_on_breach(self):
        """
        **[Required]** Gets the operation_on_breach of this Quota.
        What the usage plan will do when a quota is breached:
        `REJECT` will allow no further requests
        `ALLOW` will continue to allow further requests

        Allowed values for this property are: "REJECT", "ALLOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_on_breach of this Quota.
        :rtype: str
        """
        return self._operation_on_breach

    @operation_on_breach.setter
    def operation_on_breach(self, operation_on_breach):
        """
        Sets the operation_on_breach of this Quota.
        What the usage plan will do when a quota is breached:
        `REJECT` will allow no further requests
        `ALLOW` will continue to allow further requests


        :param operation_on_breach: The operation_on_breach of this Quota.
        :type: str
        """
        allowed_values = ["REJECT", "ALLOW"]
        if not value_allowed_none_or_none_sentinel(operation_on_breach, allowed_values):
            operation_on_breach = 'UNKNOWN_ENUM_VALUE'
        self._operation_on_breach = operation_on_breach

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
