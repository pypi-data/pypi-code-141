# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDedicatedVantagePointDetails(object):
    """
    Details of the request body used to create a new dedicated vantage point.
    """

    #: A constant which can be used with the status property of a CreateDedicatedVantagePointDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a CreateDedicatedVantagePointDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDedicatedVantagePointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDedicatedVantagePointDetails.
        :type display_name: str

        :param dvp_stack_details:
            The value to assign to the dvp_stack_details property of this CreateDedicatedVantagePointDetails.
        :type dvp_stack_details: oci.apm_synthetics.models.DvpStackDetails

        :param region:
            The value to assign to the region property of this CreateDedicatedVantagePointDetails.
        :type region: str

        :param status:
            The value to assign to the status property of this CreateDedicatedVantagePointDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type status: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDedicatedVantagePointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDedicatedVantagePointDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'dvp_stack_details': 'DvpStackDetails',
            'region': 'str',
            'status': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'dvp_stack_details': 'dvpStackDetails',
            'region': 'region',
            'status': 'status',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._dvp_stack_details = None
        self._region = None
        self._status = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDedicatedVantagePointDetails.
        Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.


        :return: The display_name of this CreateDedicatedVantagePointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDedicatedVantagePointDetails.
        Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this CreateDedicatedVantagePointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def dvp_stack_details(self):
        """
        **[Required]** Gets the dvp_stack_details of this CreateDedicatedVantagePointDetails.

        :return: The dvp_stack_details of this CreateDedicatedVantagePointDetails.
        :rtype: oci.apm_synthetics.models.DvpStackDetails
        """
        return self._dvp_stack_details

    @dvp_stack_details.setter
    def dvp_stack_details(self, dvp_stack_details):
        """
        Sets the dvp_stack_details of this CreateDedicatedVantagePointDetails.

        :param dvp_stack_details: The dvp_stack_details of this CreateDedicatedVantagePointDetails.
        :type: oci.apm_synthetics.models.DvpStackDetails
        """
        self._dvp_stack_details = dvp_stack_details

    @property
    def region(self):
        """
        **[Required]** Gets the region of this CreateDedicatedVantagePointDetails.
        Name of the region.


        :return: The region of this CreateDedicatedVantagePointDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CreateDedicatedVantagePointDetails.
        Name of the region.


        :param region: The region of this CreateDedicatedVantagePointDetails.
        :type: str
        """
        self._region = region

    @property
    def status(self):
        """
        Gets the status of this CreateDedicatedVantagePointDetails.
        Status of the dedicated vantage point.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The status of this CreateDedicatedVantagePointDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CreateDedicatedVantagePointDetails.
        Status of the dedicated vantage point.


        :param status: The status of this CreateDedicatedVantagePointDetails.
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
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDedicatedVantagePointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDedicatedVantagePointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDedicatedVantagePointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDedicatedVantagePointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDedicatedVantagePointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDedicatedVantagePointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDedicatedVantagePointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDedicatedVantagePointDetails.
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
