# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMigrationDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMigrationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateMigrationDetails.
        :type display_name: str

        :param replication_schedule_id:
            The value to assign to the replication_schedule_id property of this UpdateMigrationDetails.
        :type replication_schedule_id: str

        :param is_completed:
            The value to assign to the is_completed property of this UpdateMigrationDetails.
        :type is_completed: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMigrationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMigrationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'replication_schedule_id': 'str',
            'is_completed': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'replication_schedule_id': 'replicationScheduleId',
            'is_completed': 'isCompleted',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._replication_schedule_id = None
        self._is_completed = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMigrationDetails.
        Migration identifier


        :return: The display_name of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMigrationDetails.
        Migration identifier


        :param display_name: The display_name of this UpdateMigrationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def replication_schedule_id(self):
        """
        Gets the replication_schedule_id of this UpdateMigrationDetails.
        Replication schedule identifier


        :return: The replication_schedule_id of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._replication_schedule_id

    @replication_schedule_id.setter
    def replication_schedule_id(self, replication_schedule_id):
        """
        Sets the replication_schedule_id of this UpdateMigrationDetails.
        Replication schedule identifier


        :param replication_schedule_id: The replication_schedule_id of this UpdateMigrationDetails.
        :type: str
        """
        self._replication_schedule_id = replication_schedule_id

    @property
    def is_completed(self):
        """
        Gets the is_completed of this UpdateMigrationDetails.
        Indicates whether migration is marked as complete.


        :return: The is_completed of this UpdateMigrationDetails.
        :rtype: bool
        """
        return self._is_completed

    @is_completed.setter
    def is_completed(self, is_completed):
        """
        Sets the is_completed of this UpdateMigrationDetails.
        Indicates whether migration is marked as complete.


        :param is_completed: The is_completed of this UpdateMigrationDetails.
        :type: bool
        """
        self._is_completed = is_completed

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateMigrationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateMigrationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateMigrationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateMigrationDetails.
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
