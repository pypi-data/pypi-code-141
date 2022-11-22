# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateReplicationScheduleDetails(object):
    """
    Information about replication schedule to be created.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateReplicationScheduleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateReplicationScheduleDetails.
        :type compartment_id: str

        :param execution_recurrences:
            The value to assign to the execution_recurrences property of this CreateReplicationScheduleDetails.
        :type execution_recurrences: str

        :param display_name:
            The value to assign to the display_name property of this CreateReplicationScheduleDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateReplicationScheduleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateReplicationScheduleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'execution_recurrences': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'execution_recurrences': 'executionRecurrences',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._execution_recurrences = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateReplicationScheduleDetails.
        The `OCID`__ of the compartment in which the replication schedule should be created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateReplicationScheduleDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateReplicationScheduleDetails.
        The `OCID`__ of the compartment in which the replication schedule should be created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateReplicationScheduleDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def execution_recurrences(self):
        """
        **[Required]** Gets the execution_recurrences of this CreateReplicationScheduleDetails.
        Recurrence specification for replication schedule execution.


        :return: The execution_recurrences of this CreateReplicationScheduleDetails.
        :rtype: str
        """
        return self._execution_recurrences

    @execution_recurrences.setter
    def execution_recurrences(self, execution_recurrences):
        """
        Sets the execution_recurrences of this CreateReplicationScheduleDetails.
        Recurrence specification for replication schedule execution.


        :param execution_recurrences: The execution_recurrences of this CreateReplicationScheduleDetails.
        :type: str
        """
        self._execution_recurrences = execution_recurrences

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateReplicationScheduleDetails.
        A user-friendly name for a replication schedule. Does not have to be unique, and is mutable. Avoid entering confidential information.


        :return: The display_name of this CreateReplicationScheduleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateReplicationScheduleDetails.
        A user-friendly name for a replication schedule. Does not have to be unique, and is mutable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateReplicationScheduleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateReplicationScheduleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateReplicationScheduleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateReplicationScheduleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateReplicationScheduleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateReplicationScheduleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateReplicationScheduleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateReplicationScheduleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateReplicationScheduleDetails.
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
