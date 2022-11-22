# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAssetSourceDetails(object):
    """
    The information about the new asset source.
    """

    #: A constant which can be used with the type property of a UpdateAssetSourceDetails.
    #: This constant has a value of "VMWARE"
    TYPE_VMWARE = "VMWARE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAssetSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_bridge.models.UpdateVmWareAssetSourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateAssetSourceDetails.
            Allowed values for this property are: "VMWARE"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateAssetSourceDetails.
        :type display_name: str

        :param assets_compartment_id:
            The value to assign to the assets_compartment_id property of this UpdateAssetSourceDetails.
        :type assets_compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAssetSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAssetSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this UpdateAssetSourceDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'assets_compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'assets_compartment_id': 'assetsCompartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._type = None
        self._display_name = None
        self._assets_compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'VMWARE':
            return 'UpdateVmWareAssetSourceDetails'
        else:
            return 'UpdateAssetSourceDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this UpdateAssetSourceDetails.
        Source type.

        Allowed values for this property are: "VMWARE"


        :return: The type of this UpdateAssetSourceDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateAssetSourceDetails.
        Source type.


        :param type: The type of this UpdateAssetSourceDetails.
        :type: str
        """
        allowed_values = ["VMWARE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAssetSourceDetails.
        A user-friendly name for the asset source. Does not have to be unique, and it's mutable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateAssetSourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAssetSourceDetails.
        A user-friendly name for the asset source. Does not have to be unique, and it's mutable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateAssetSourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def assets_compartment_id(self):
        """
        Gets the assets_compartment_id of this UpdateAssetSourceDetails.
        The `OCID`__ of the compartment that is going to be used to create assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The assets_compartment_id of this UpdateAssetSourceDetails.
        :rtype: str
        """
        return self._assets_compartment_id

    @assets_compartment_id.setter
    def assets_compartment_id(self, assets_compartment_id):
        """
        Sets the assets_compartment_id of this UpdateAssetSourceDetails.
        The `OCID`__ of the compartment that is going to be used to create assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param assets_compartment_id: The assets_compartment_id of this UpdateAssetSourceDetails.
        :type: str
        """
        self._assets_compartment_id = assets_compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAssetSourceDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAssetSourceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAssetSourceDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAssetSourceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAssetSourceDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAssetSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAssetSourceDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAssetSourceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this UpdateAssetSourceDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this UpdateAssetSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this UpdateAssetSourceDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this UpdateAssetSourceDetails.
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
