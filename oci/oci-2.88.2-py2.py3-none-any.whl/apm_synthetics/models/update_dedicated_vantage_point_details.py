# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDedicatedVantagePointDetails(object):
    """
    Details of the request body used to update a dedicated vantage point.
    """

    #: A constant which can be used with the status property of a UpdateDedicatedVantagePointDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a UpdateDedicatedVantagePointDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDedicatedVantagePointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this UpdateDedicatedVantagePointDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type status: str

        :param dvp_stack_details:
            The value to assign to the dvp_stack_details property of this UpdateDedicatedVantagePointDetails.
        :type dvp_stack_details: oci.apm_synthetics.models.DvpStackDetails

        :param region:
            The value to assign to the region property of this UpdateDedicatedVantagePointDetails.
        :type region: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDedicatedVantagePointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDedicatedVantagePointDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'status': 'str',
            'dvp_stack_details': 'DvpStackDetails',
            'region': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'status': 'status',
            'dvp_stack_details': 'dvpStackDetails',
            'region': 'region',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._status = None
        self._dvp_stack_details = None
        self._region = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def status(self):
        """
        Gets the status of this UpdateDedicatedVantagePointDetails.
        Status of the dedicated vantage point.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The status of this UpdateDedicatedVantagePointDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateDedicatedVantagePointDetails.
        Status of the dedicated vantage point.


        :param status: The status of this UpdateDedicatedVantagePointDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def dvp_stack_details(self):
        """
        Gets the dvp_stack_details of this UpdateDedicatedVantagePointDetails.

        :return: The dvp_stack_details of this UpdateDedicatedVantagePointDetails.
        :rtype: oci.apm_synthetics.models.DvpStackDetails
        """
        return self._dvp_stack_details

    @dvp_stack_details.setter
    def dvp_stack_details(self, dvp_stack_details):
        """
        Sets the dvp_stack_details of this UpdateDedicatedVantagePointDetails.

        :param dvp_stack_details: The dvp_stack_details of this UpdateDedicatedVantagePointDetails.
        :type: oci.apm_synthetics.models.DvpStackDetails
        """
        self._dvp_stack_details = dvp_stack_details

    @property
    def region(self):
        """
        Gets the region of this UpdateDedicatedVantagePointDetails.
        Name of the region.


        :return: The region of this UpdateDedicatedVantagePointDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this UpdateDedicatedVantagePointDetails.
        Name of the region.


        :param region: The region of this UpdateDedicatedVantagePointDetails.
        :type: str
        """
        self._region = region

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDedicatedVantagePointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateDedicatedVantagePointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDedicatedVantagePointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateDedicatedVantagePointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDedicatedVantagePointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDedicatedVantagePointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDedicatedVantagePointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDedicatedVantagePointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
