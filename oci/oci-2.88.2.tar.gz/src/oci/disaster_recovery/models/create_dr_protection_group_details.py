# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrProtectionGroupDetails(object):
    """
    The details for creating a DR Protection Group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrProtectionGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDrProtectionGroupDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateDrProtectionGroupDetails.
        :type display_name: str

        :param log_location:
            The value to assign to the log_location property of this CreateDrProtectionGroupDetails.
        :type log_location: oci.disaster_recovery.models.CreateObjectStorageLogLocationDetails

        :param association:
            The value to assign to the association property of this CreateDrProtectionGroupDetails.
        :type association: oci.disaster_recovery.models.AssociateDrProtectionGroupDetails

        :param members:
            The value to assign to the members property of this CreateDrProtectionGroupDetails.
        :type members: list[oci.disaster_recovery.models.CreateDrProtectionGroupMemberDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDrProtectionGroupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDrProtectionGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'log_location': 'CreateObjectStorageLogLocationDetails',
            'association': 'AssociateDrProtectionGroupDetails',
            'members': 'list[CreateDrProtectionGroupMemberDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'log_location': 'logLocation',
            'association': 'association',
            'members': 'members',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._log_location = None
        self._association = None
        self._members = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDrProtectionGroupDetails.
        The OCID of the compartment in which to create the DR Protection Group.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :return: The compartment_id of this CreateDrProtectionGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDrProtectionGroupDetails.
        The OCID of the compartment in which to create the DR Protection Group.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :param compartment_id: The compartment_id of this CreateDrProtectionGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDrProtectionGroupDetails.
        The display name of the DR Protection Group.

        Example: `EBS PHX DRPG`


        :return: The display_name of this CreateDrProtectionGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDrProtectionGroupDetails.
        The display name of the DR Protection Group.

        Example: `EBS PHX DRPG`


        :param display_name: The display_name of this CreateDrProtectionGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def log_location(self):
        """
        **[Required]** Gets the log_location of this CreateDrProtectionGroupDetails.

        :return: The log_location of this CreateDrProtectionGroupDetails.
        :rtype: oci.disaster_recovery.models.CreateObjectStorageLogLocationDetails
        """
        return self._log_location

    @log_location.setter
    def log_location(self, log_location):
        """
        Sets the log_location of this CreateDrProtectionGroupDetails.

        :param log_location: The log_location of this CreateDrProtectionGroupDetails.
        :type: oci.disaster_recovery.models.CreateObjectStorageLogLocationDetails
        """
        self._log_location = log_location

    @property
    def association(self):
        """
        Gets the association of this CreateDrProtectionGroupDetails.

        :return: The association of this CreateDrProtectionGroupDetails.
        :rtype: oci.disaster_recovery.models.AssociateDrProtectionGroupDetails
        """
        return self._association

    @association.setter
    def association(self, association):
        """
        Sets the association of this CreateDrProtectionGroupDetails.

        :param association: The association of this CreateDrProtectionGroupDetails.
        :type: oci.disaster_recovery.models.AssociateDrProtectionGroupDetails
        """
        self._association = association

    @property
    def members(self):
        """
        Gets the members of this CreateDrProtectionGroupDetails.
        A list of DR Protection Group members.


        :return: The members of this CreateDrProtectionGroupDetails.
        :rtype: list[oci.disaster_recovery.models.CreateDrProtectionGroupMemberDetails]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this CreateDrProtectionGroupDetails.
        A list of DR Protection Group members.


        :param members: The members of this CreateDrProtectionGroupDetails.
        :type: list[oci.disaster_recovery.models.CreateDrProtectionGroupMemberDetails]
        """
        self._members = members

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDrProtectionGroupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :return: The freeform_tags of this CreateDrProtectionGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDrProtectionGroupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :param freeform_tags: The freeform_tags of this CreateDrProtectionGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDrProtectionGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The defined_tags of this CreateDrProtectionGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDrProtectionGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param defined_tags: The defined_tags of this CreateDrProtectionGroupDetails.
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
