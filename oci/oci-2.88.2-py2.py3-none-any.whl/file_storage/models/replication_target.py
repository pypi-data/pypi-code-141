# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicationTarget(object):
    """
    Replication targets are associated with a primary resource called a :class:`Replication`
    located in another availability domain in the same or different region.
    The replication retrieves the delta of data between two snapshots of a source file system
    and sends it to the associated `ReplicationTarget`,  which applies it to the target
    file system.
    All operations (except `DELETE`) must be done using the associated replication resource.
    Deleting a `ReplicationTarget` allows the target file system to be exported.
    Deleting a `ReplicationTarget` does not delete the associated `Replication` resource, but places it in a `FAILED` state.
    For more information, see `File System Replication`__.

    __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/FSreplication.htm
    """

    #: A constant which can be used with the lifecycle_state property of a ReplicationTarget.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ReplicationTarget.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ReplicationTarget.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ReplicationTarget.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ReplicationTarget.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the delta_status property of a ReplicationTarget.
    #: This constant has a value of "IDLE"
    DELTA_STATUS_IDLE = "IDLE"

    #: A constant which can be used with the delta_status property of a ReplicationTarget.
    #: This constant has a value of "CAPTURING"
    DELTA_STATUS_CAPTURING = "CAPTURING"

    #: A constant which can be used with the delta_status property of a ReplicationTarget.
    #: This constant has a value of "APPLYING"
    DELTA_STATUS_APPLYING = "APPLYING"

    #: A constant which can be used with the delta_status property of a ReplicationTarget.
    #: This constant has a value of "SERVICE_ERROR"
    DELTA_STATUS_SERVICE_ERROR = "SERVICE_ERROR"

    #: A constant which can be used with the delta_status property of a ReplicationTarget.
    #: This constant has a value of "USER_ERROR"
    DELTA_STATUS_USER_ERROR = "USER_ERROR"

    #: A constant which can be used with the delta_status property of a ReplicationTarget.
    #: This constant has a value of "FAILED"
    DELTA_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the delta_status property of a ReplicationTarget.
    #: This constant has a value of "TRANSFERRING"
    DELTA_STATUS_TRANSFERRING = "TRANSFERRING"

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicationTarget object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this ReplicationTarget.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ReplicationTarget.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this ReplicationTarget.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ReplicationTarget.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this ReplicationTarget.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this ReplicationTarget.
        :type time_created: datetime

        :param source_id:
            The value to assign to the source_id property of this ReplicationTarget.
        :type source_id: str

        :param target_id:
            The value to assign to the target_id property of this ReplicationTarget.
        :type target_id: str

        :param replication_id:
            The value to assign to the replication_id property of this ReplicationTarget.
        :type replication_id: str

        :param last_snapshot_id:
            The value to assign to the last_snapshot_id property of this ReplicationTarget.
        :type last_snapshot_id: str

        :param recovery_point_time:
            The value to assign to the recovery_point_time property of this ReplicationTarget.
        :type recovery_point_time: datetime

        :param delta_status:
            The value to assign to the delta_status property of this ReplicationTarget.
            Allowed values for this property are: "IDLE", "CAPTURING", "APPLYING", "SERVICE_ERROR", "USER_ERROR", "FAILED", "TRANSFERRING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type delta_status: str

        :param delta_progress:
            The value to assign to the delta_progress property of this ReplicationTarget.
        :type delta_progress: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ReplicationTarget.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ReplicationTarget.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ReplicationTarget.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'source_id': 'str',
            'target_id': 'str',
            'replication_id': 'str',
            'last_snapshot_id': 'str',
            'recovery_point_time': 'datetime',
            'delta_status': 'str',
            'delta_progress': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'source_id': 'sourceId',
            'target_id': 'targetId',
            'replication_id': 'replicationId',
            'last_snapshot_id': 'lastSnapshotId',
            'recovery_point_time': 'recoveryPointTime',
            'delta_status': 'deltaStatus',
            'delta_progress': 'deltaProgress',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._id = None
        self._lifecycle_state = None
        self._display_name = None
        self._time_created = None
        self._source_id = None
        self._target_id = None
        self._replication_id = None
        self._last_snapshot_id = None
        self._recovery_point_time = None
        self._delta_status = None
        self._delta_progress = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_details = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this ReplicationTarget.
        The availability domain the replication resource is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this ReplicationTarget.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ReplicationTarget.
        The availability domain the replication resource is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this ReplicationTarget.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ReplicationTarget.
        The `OCID`__ of the compartment that contains the replication.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ReplicationTarget.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ReplicationTarget.
        The `OCID`__ of the compartment that contains the replication.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ReplicationTarget.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ReplicationTarget.
        The `OCID`__ of the replication.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ReplicationTarget.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReplicationTarget.
        The `OCID`__ of the replication.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ReplicationTarget.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ReplicationTarget.
        The current state of this replication.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ReplicationTarget.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ReplicationTarget.
        The current state of this replication.


        :param lifecycle_state: The lifecycle_state of this ReplicationTarget.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ReplicationTarget.
        A user-friendly name. This name is same as the replication display name for the associated resource.
        Example: `My Replication`


        :return: The display_name of this ReplicationTarget.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ReplicationTarget.
        A user-friendly name. This name is same as the replication display name for the associated resource.
        Example: `My Replication`


        :param display_name: The display_name of this ReplicationTarget.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ReplicationTarget.
        The date and time the replication target was created in target region.
        in `RFC 3339`__ timestamp format.
        Example: `2021-01-04T20:01:29.100Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ReplicationTarget.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ReplicationTarget.
        The date and time the replication target was created in target region.
        in `RFC 3339`__ timestamp format.
        Example: `2021-01-04T20:01:29.100Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ReplicationTarget.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def source_id(self):
        """
        **[Required]** Gets the source_id of this ReplicationTarget.
        The `OCID`__ of source filesystem.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_id of this ReplicationTarget.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this ReplicationTarget.
        The `OCID`__ of source filesystem.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this ReplicationTarget.
        :type: str
        """
        self._source_id = source_id

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this ReplicationTarget.
        The `OCID`__ of target filesystem.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The target_id of this ReplicationTarget.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this ReplicationTarget.
        The `OCID`__ of target filesystem.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param target_id: The target_id of this ReplicationTarget.
        :type: str
        """
        self._target_id = target_id

    @property
    def replication_id(self):
        """
        **[Required]** Gets the replication_id of this ReplicationTarget.
        The `OCID`__ of replication.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The replication_id of this ReplicationTarget.
        :rtype: str
        """
        return self._replication_id

    @replication_id.setter
    def replication_id(self, replication_id):
        """
        Sets the replication_id of this ReplicationTarget.
        The `OCID`__ of replication.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param replication_id: The replication_id of this ReplicationTarget.
        :type: str
        """
        self._replication_id = replication_id

    @property
    def last_snapshot_id(self):
        """
        Gets the last_snapshot_id of this ReplicationTarget.
        The `OCID`__ of the last snapshot snapshot which was completely applied to the target file system.
        Empty while the initial snapshot is being applied.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_snapshot_id of this ReplicationTarget.
        :rtype: str
        """
        return self._last_snapshot_id

    @last_snapshot_id.setter
    def last_snapshot_id(self, last_snapshot_id):
        """
        Sets the last_snapshot_id of this ReplicationTarget.
        The `OCID`__ of the last snapshot snapshot which was completely applied to the target file system.
        Empty while the initial snapshot is being applied.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_snapshot_id: The last_snapshot_id of this ReplicationTarget.
        :type: str
        """
        self._last_snapshot_id = last_snapshot_id

    @property
    def recovery_point_time(self):
        """
        Gets the recovery_point_time of this ReplicationTarget.
        The snapshotTime of the most recent recoverable replication snapshot
        in `RFC 3339`__ timestamp format.
        Example: `2021-04-04T20:01:29.100Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The recovery_point_time of this ReplicationTarget.
        :rtype: datetime
        """
        return self._recovery_point_time

    @recovery_point_time.setter
    def recovery_point_time(self, recovery_point_time):
        """
        Sets the recovery_point_time of this ReplicationTarget.
        The snapshotTime of the most recent recoverable replication snapshot
        in `RFC 3339`__ timestamp format.
        Example: `2021-04-04T20:01:29.100Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param recovery_point_time: The recovery_point_time of this ReplicationTarget.
        :type: datetime
        """
        self._recovery_point_time = recovery_point_time

    @property
    def delta_status(self):
        """
        Gets the delta_status of this ReplicationTarget.
        The current state of the snapshot during replication operations.

        Allowed values for this property are: "IDLE", "CAPTURING", "APPLYING", "SERVICE_ERROR", "USER_ERROR", "FAILED", "TRANSFERRING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The delta_status of this ReplicationTarget.
        :rtype: str
        """
        return self._delta_status

    @delta_status.setter
    def delta_status(self, delta_status):
        """
        Sets the delta_status of this ReplicationTarget.
        The current state of the snapshot during replication operations.


        :param delta_status: The delta_status of this ReplicationTarget.
        :type: str
        """
        allowed_values = ["IDLE", "CAPTURING", "APPLYING", "SERVICE_ERROR", "USER_ERROR", "FAILED", "TRANSFERRING"]
        if not value_allowed_none_or_none_sentinel(delta_status, allowed_values):
            delta_status = 'UNKNOWN_ENUM_VALUE'
        self._delta_status = delta_status

    @property
    def delta_progress(self):
        """
        Gets the delta_progress of this ReplicationTarget.
        Percentage progress of the current replication cycle.


        :return: The delta_progress of this ReplicationTarget.
        :rtype: int
        """
        return self._delta_progress

    @delta_progress.setter
    def delta_progress(self, delta_progress):
        """
        Sets the delta_progress of this ReplicationTarget.
        Percentage progress of the current replication cycle.


        :param delta_progress: The delta_progress of this ReplicationTarget.
        :type: int
        """
        self._delta_progress = delta_progress

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ReplicationTarget.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ReplicationTarget.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ReplicationTarget.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ReplicationTarget.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ReplicationTarget.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ReplicationTarget.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ReplicationTarget.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ReplicationTarget.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ReplicationTarget.
        Additional information about the current `lifecycleState`.


        :return: The lifecycle_details of this ReplicationTarget.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ReplicationTarget.
        Additional information about the current `lifecycleState`.


        :param lifecycle_details: The lifecycle_details of this ReplicationTarget.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
