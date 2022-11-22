# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrPlanSummary(object):
    """
    Summary information about a DR Plan Execution.
    """

    #: A constant which can be used with the type property of a DrPlanSummary.
    #: This constant has a value of "SWITCHOVER"
    TYPE_SWITCHOVER = "SWITCHOVER"

    #: A constant which can be used with the type property of a DrPlanSummary.
    #: This constant has a value of "FAILOVER"
    TYPE_FAILOVER = "FAILOVER"

    #: A constant which can be used with the lifecycle_state property of a DrPlanSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DrPlanSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DrPlanSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DrPlanSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DrPlanSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DrPlanSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DrPlanSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DrPlanSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new DrPlanSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DrPlanSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DrPlanSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DrPlanSummary.
        :type display_name: str

        :param type:
            The value to assign to the type property of this DrPlanSummary.
            Allowed values for this property are: "SWITCHOVER", "FAILOVER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param dr_protection_group_id:
            The value to assign to the dr_protection_group_id property of this DrPlanSummary.
        :type dr_protection_group_id: str

        :param peer_dr_protection_group_id:
            The value to assign to the peer_dr_protection_group_id property of this DrPlanSummary.
        :type peer_dr_protection_group_id: str

        :param peer_region:
            The value to assign to the peer_region property of this DrPlanSummary.
        :type peer_region: str

        :param time_created:
            The value to assign to the time_created property of this DrPlanSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DrPlanSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DrPlanSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param life_cycle_details:
            The value to assign to the life_cycle_details property of this DrPlanSummary.
        :type life_cycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DrPlanSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DrPlanSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DrPlanSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'type': 'str',
            'dr_protection_group_id': 'str',
            'peer_dr_protection_group_id': 'str',
            'peer_region': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'life_cycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'type': 'type',
            'dr_protection_group_id': 'drProtectionGroupId',
            'peer_dr_protection_group_id': 'peerDrProtectionGroupId',
            'peer_region': 'peerRegion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'life_cycle_details': 'lifeCycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._type = None
        self._dr_protection_group_id = None
        self._peer_dr_protection_group_id = None
        self._peer_region = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._life_cycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrPlanSummary.
        The OCID of this DR Plan.

        Example: `ocid1.drplan.oc1.iad.exampleocid2`


        :return: The id of this DrPlanSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrPlanSummary.
        The OCID of this DR Plan.

        Example: `ocid1.drplan.oc1.iad.exampleocid2`


        :param id: The id of this DrPlanSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DrPlanSummary.
        The OCID of the compartment containing the DR Plan.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :return: The compartment_id of this DrPlanSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DrPlanSummary.
        The OCID of the compartment containing the DR Plan.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :param compartment_id: The compartment_id of this DrPlanSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DrPlanSummary.
        The display name of this DR Plan.

        Example: `EBS Switchover PHX to IAD`


        :return: The display_name of this DrPlanSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrPlanSummary.
        The display name of this DR Plan.

        Example: `EBS Switchover PHX to IAD`


        :param display_name: The display_name of this DrPlanSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DrPlanSummary.
        The type of this DR Plan.

        Allowed values for this property are: "SWITCHOVER", "FAILOVER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DrPlanSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DrPlanSummary.
        The type of this DR Plan.


        :param type: The type of this DrPlanSummary.
        :type: str
        """
        allowed_values = ["SWITCHOVER", "FAILOVER"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def dr_protection_group_id(self):
        """
        **[Required]** Gets the dr_protection_group_id of this DrPlanSummary.
        The OCID of the DR Protection Group with which this DR Plan is associated.

        Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`


        :return: The dr_protection_group_id of this DrPlanSummary.
        :rtype: str
        """
        return self._dr_protection_group_id

    @dr_protection_group_id.setter
    def dr_protection_group_id(self, dr_protection_group_id):
        """
        Sets the dr_protection_group_id of this DrPlanSummary.
        The OCID of the DR Protection Group with which this DR Plan is associated.

        Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`


        :param dr_protection_group_id: The dr_protection_group_id of this DrPlanSummary.
        :type: str
        """
        self._dr_protection_group_id = dr_protection_group_id

    @property
    def peer_dr_protection_group_id(self):
        """
        **[Required]** Gets the peer_dr_protection_group_id of this DrPlanSummary.
        The OCID of peer (remote) DR Protection Group associated with this plan execution's
        DR Protection Group.

        Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid1`


        :return: The peer_dr_protection_group_id of this DrPlanSummary.
        :rtype: str
        """
        return self._peer_dr_protection_group_id

    @peer_dr_protection_group_id.setter
    def peer_dr_protection_group_id(self, peer_dr_protection_group_id):
        """
        Sets the peer_dr_protection_group_id of this DrPlanSummary.
        The OCID of peer (remote) DR Protection Group associated with this plan execution's
        DR Protection Group.

        Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid1`


        :param peer_dr_protection_group_id: The peer_dr_protection_group_id of this DrPlanSummary.
        :type: str
        """
        self._peer_dr_protection_group_id = peer_dr_protection_group_id

    @property
    def peer_region(self):
        """
        **[Required]** Gets the peer_region of this DrPlanSummary.
        The region of the peer (remote) DR Protection Group.

        Example: `us-phoenix-1`


        :return: The peer_region of this DrPlanSummary.
        :rtype: str
        """
        return self._peer_region

    @peer_region.setter
    def peer_region(self, peer_region):
        """
        Sets the peer_region of this DrPlanSummary.
        The region of the peer (remote) DR Protection Group.

        Example: `us-phoenix-1`


        :param peer_region: The peer_region of this DrPlanSummary.
        :type: str
        """
        self._peer_region = peer_region

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DrPlanSummary.
        The date and time the DR Plan was created. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_created of this DrPlanSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DrPlanSummary.
        The date and time the DR Plan was created. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_created: The time_created of this DrPlanSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this DrPlanSummary.
        The date and time the DR Plan was updated. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_updated of this DrPlanSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DrPlanSummary.
        The date and time the DR Plan was updated. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_updated: The time_updated of this DrPlanSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DrPlanSummary.
        The current state of the DR Plan.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DrPlanSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DrPlanSummary.
        The current state of the DR Plan.


        :param lifecycle_state: The lifecycle_state of this DrPlanSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def life_cycle_details(self):
        """
        Gets the life_cycle_details of this DrPlanSummary.
        A message describing the DR Plan's current state in more detail.


        :return: The life_cycle_details of this DrPlanSummary.
        :rtype: str
        """
        return self._life_cycle_details

    @life_cycle_details.setter
    def life_cycle_details(self, life_cycle_details):
        """
        Sets the life_cycle_details of this DrPlanSummary.
        A message describing the DR Plan's current state in more detail.


        :param life_cycle_details: The life_cycle_details of this DrPlanSummary.
        :type: str
        """
        self._life_cycle_details = life_cycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DrPlanSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :return: The freeform_tags of this DrPlanSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DrPlanSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :param freeform_tags: The freeform_tags of this DrPlanSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DrPlanSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The defined_tags of this DrPlanSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DrPlanSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param defined_tags: The defined_tags of this DrPlanSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DrPlanSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DrPlanSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DrPlanSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DrPlanSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
