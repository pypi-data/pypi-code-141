# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAlertPolicyDetails(object):
    """
    The details used to create a new alert policy.
    """

    #: A constant which can be used with the alert_policy_type property of a CreateAlertPolicyDetails.
    #: This constant has a value of "AUDITING"
    ALERT_POLICY_TYPE_AUDITING = "AUDITING"

    #: A constant which can be used with the alert_policy_type property of a CreateAlertPolicyDetails.
    #: This constant has a value of "SECURITY_ASSESSMENT"
    ALERT_POLICY_TYPE_SECURITY_ASSESSMENT = "SECURITY_ASSESSMENT"

    #: A constant which can be used with the alert_policy_type property of a CreateAlertPolicyDetails.
    #: This constant has a value of "USER_ASSESSMENT"
    ALERT_POLICY_TYPE_USER_ASSESSMENT = "USER_ASSESSMENT"

    #: A constant which can be used with the severity property of a CreateAlertPolicyDetails.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a CreateAlertPolicyDetails.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a CreateAlertPolicyDetails.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a CreateAlertPolicyDetails.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    #: A constant which can be used with the severity property of a CreateAlertPolicyDetails.
    #: This constant has a value of "EVALUATE"
    SEVERITY_EVALUATE = "EVALUATE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAlertPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param alert_policy_type:
            The value to assign to the alert_policy_type property of this CreateAlertPolicyDetails.
            Allowed values for this property are: "AUDITING", "SECURITY_ASSESSMENT", "USER_ASSESSMENT"
        :type alert_policy_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateAlertPolicyDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateAlertPolicyDetails.
        :type description: str

        :param severity:
            The value to assign to the severity property of this CreateAlertPolicyDetails.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "EVALUATE"
        :type severity: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAlertPolicyDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAlertPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAlertPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'alert_policy_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'severity': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'alert_policy_type': 'alertPolicyType',
            'display_name': 'displayName',
            'description': 'description',
            'severity': 'severity',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._alert_policy_type = None
        self._display_name = None
        self._description = None
        self._severity = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def alert_policy_type(self):
        """
        **[Required]** Gets the alert_policy_type of this CreateAlertPolicyDetails.
        Indicates the Data Safe feature the alert policy belongs to

        Allowed values for this property are: "AUDITING", "SECURITY_ASSESSMENT", "USER_ASSESSMENT"


        :return: The alert_policy_type of this CreateAlertPolicyDetails.
        :rtype: str
        """
        return self._alert_policy_type

    @alert_policy_type.setter
    def alert_policy_type(self, alert_policy_type):
        """
        Sets the alert_policy_type of this CreateAlertPolicyDetails.
        Indicates the Data Safe feature the alert policy belongs to


        :param alert_policy_type: The alert_policy_type of this CreateAlertPolicyDetails.
        :type: str
        """
        allowed_values = ["AUDITING", "SECURITY_ASSESSMENT", "USER_ASSESSMENT"]
        if not value_allowed_none_or_none_sentinel(alert_policy_type, allowed_values):
            raise ValueError(
                "Invalid value for `alert_policy_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._alert_policy_type = alert_policy_type

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAlertPolicyDetails.
        The display name of the alert policy. The name does not have to be unique, and it's changeable.


        :return: The display_name of this CreateAlertPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAlertPolicyDetails.
        The display name of the alert policy. The name does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateAlertPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateAlertPolicyDetails.
        The description of the alert policy.


        :return: The description of this CreateAlertPolicyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAlertPolicyDetails.
        The description of the alert policy.


        :param description: The description of this CreateAlertPolicyDetails.
        :type: str
        """
        self._description = description

    @property
    def severity(self):
        """
        **[Required]** Gets the severity of this CreateAlertPolicyDetails.
        Severity level of the alert raised by this policy.

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "EVALUATE"


        :return: The severity of this CreateAlertPolicyDetails.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this CreateAlertPolicyDetails.
        Severity level of the alert raised by this policy.


        :param severity: The severity of this CreateAlertPolicyDetails.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "EVALUATE"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            raise ValueError(
                "Invalid value for `severity`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._severity = severity

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAlertPolicyDetails.
        The OCID of the compartment where you want to create the alert policy.


        :return: The compartment_id of this CreateAlertPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAlertPolicyDetails.
        The OCID of the compartment where you want to create the alert policy.


        :param compartment_id: The compartment_id of this CreateAlertPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAlertPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAlertPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAlertPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAlertPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAlertPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAlertPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAlertPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAlertPolicyDetails.
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
