# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrProtectionGroupDetails(object):
    """
    The details for updating a DR Protection Group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrProtectionGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDrProtectionGroupDetails.
        :type display_name: str

        :param log_location:
            The value to assign to the log_location property of this UpdateDrProtectionGroupDetails.
        :type log_location: oci.disaster_recovery.models.UpdateObjectStorageLogLocationDetails

        :param members:
            The value to assign to the members property of this UpdateDrProtectionGroupDetails.
        :type members: list[oci.disaster_recovery.models.UpdateDrProtectionGroupMemberDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDrProtectionGroupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDrProtectionGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'log_location': 'UpdateObjectStorageLogLocationDetails',
            'members': 'list[UpdateDrProtectionGroupMemberDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'log_location': 'logLocation',
            'members': 'members',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._log_location = None
        self._members = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDrProtectionGroupDetails.
        The display name of the DR Protection Group.

        Example: `EBS PHX DRPG`


        :return: The display_name of this UpdateDrProtectionGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDrProtectionGroupDetails.
        The display name of the DR Protection Group.

        Example: `EBS PHX DRPG`


        :param display_name: The display_name of this UpdateDrProtectionGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def log_location(self):
        """
        Gets the log_location of this UpdateDrProtectionGroupDetails.

        :return: The log_location of this UpdateDrProtectionGroupDetails.
        :rtype: oci.disaster_recovery.models.UpdateObjectStorageLogLocationDetails
        """
        return self._log_location

    @log_location.setter
    def log_location(self, log_location):
        """
        Sets the log_location of this UpdateDrProtectionGroupDetails.

        :param log_location: The log_location of this UpdateDrProtectionGroupDetails.
        :type: oci.disaster_recovery.models.UpdateObjectStorageLogLocationDetails
        """
        self._log_location = log_location

    @property
    def members(self):
        """
        Gets the members of this UpdateDrProtectionGroupDetails.
        A list of DR Protection Group members.


        :return: The members of this UpdateDrProtectionGroupDetails.
        :rtype: list[oci.disaster_recovery.models.UpdateDrProtectionGroupMemberDetails]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this UpdateDrProtectionGroupDetails.
        A list of DR Protection Group members.


        :param members: The members of this UpdateDrProtectionGroupDetails.
        :type: list[oci.disaster_recovery.models.UpdateDrProtectionGroupMemberDetails]
        """
        self._members = members

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDrProtectionGroupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :return: The freeform_tags of this UpdateDrProtectionGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDrProtectionGroupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :param freeform_tags: The freeform_tags of this UpdateDrProtectionGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDrProtectionGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The defined_tags of this UpdateDrProtectionGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDrProtectionGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param defined_tags: The defined_tags of this UpdateDrProtectionGroupDetails.
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
