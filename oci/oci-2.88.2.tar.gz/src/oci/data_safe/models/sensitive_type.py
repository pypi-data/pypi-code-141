# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SensitiveType(object):
    """
    A sensitive type defines a particular type or class of sensitive data. It can be a basic sensitive type with regular
    expressions or a sensitive category. While sensitive types are used for data discovery, sensitive categories are used
    for logically grouping the related or similar sensitive types. `Learn more`__.

    __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/sensitive-types.html#GUID-45A5A3CB-5B67-4C75-9ACC-DD511D14E7C4
    """

    #: A constant which can be used with the entity_type property of a SensitiveType.
    #: This constant has a value of "SENSITIVE_TYPE"
    ENTITY_TYPE_SENSITIVE_TYPE = "SENSITIVE_TYPE"

    #: A constant which can be used with the entity_type property of a SensitiveType.
    #: This constant has a value of "SENSITIVE_CATEGORY"
    ENTITY_TYPE_SENSITIVE_CATEGORY = "SENSITIVE_CATEGORY"

    #: A constant which can be used with the lifecycle_state property of a SensitiveType.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SensitiveType.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SensitiveType.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SensitiveType.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SensitiveType.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SensitiveType.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the source property of a SensitiveType.
    #: This constant has a value of "ORACLE"
    SOURCE_ORACLE = "ORACLE"

    #: A constant which can be used with the source property of a SensitiveType.
    #: This constant has a value of "USER"
    SOURCE_USER = "USER"

    def __init__(self, **kwargs):
        """
        Initializes a new SensitiveType object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_safe.models.SensitiveTypePattern`
        * :class:`~oci.data_safe.models.SensitiveCategory`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SensitiveType.
        :type id: str

        :param entity_type:
            The value to assign to the entity_type property of this SensitiveType.
            Allowed values for this property are: "SENSITIVE_TYPE", "SENSITIVE_CATEGORY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param display_name:
            The value to assign to the display_name property of this SensitiveType.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SensitiveType.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SensitiveType.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param short_name:
            The value to assign to the short_name property of this SensitiveType.
        :type short_name: str

        :param source:
            The value to assign to the source property of this SensitiveType.
            Allowed values for this property are: "ORACLE", "USER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source: str

        :param time_created:
            The value to assign to the time_created property of this SensitiveType.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SensitiveType.
        :type time_updated: datetime

        :param description:
            The value to assign to the description property of this SensitiveType.
        :type description: str

        :param parent_category_id:
            The value to assign to the parent_category_id property of this SensitiveType.
        :type parent_category_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SensitiveType.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SensitiveType.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SensitiveType.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'entity_type': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'short_name': 'str',
            'source': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'description': 'str',
            'parent_category_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'entity_type': 'entityType',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'short_name': 'shortName',
            'source': 'source',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'description': 'description',
            'parent_category_id': 'parentCategoryId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._entity_type = None
        self._display_name = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._short_name = None
        self._source = None
        self._time_created = None
        self._time_updated = None
        self._description = None
        self._parent_category_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entityType']

        if type == 'SENSITIVE_TYPE':
            return 'SensitiveTypePattern'

        if type == 'SENSITIVE_CATEGORY':
            return 'SensitiveCategory'
        else:
            return 'SensitiveType'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SensitiveType.
        The OCID of the sensitive type.


        :return: The id of this SensitiveType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SensitiveType.
        The OCID of the sensitive type.


        :param id: The id of this SensitiveType.
        :type: str
        """
        self._id = id

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this SensitiveType.
        The entity type. It can be either a sensitive type with regular expressions or a sensitive category used for
        grouping similar sensitive types.

        Allowed values for this property are: "SENSITIVE_TYPE", "SENSITIVE_CATEGORY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_type of this SensitiveType.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this SensitiveType.
        The entity type. It can be either a sensitive type with regular expressions or a sensitive category used for
        grouping similar sensitive types.


        :param entity_type: The entity_type of this SensitiveType.
        :type: str
        """
        allowed_values = ["SENSITIVE_TYPE", "SENSITIVE_CATEGORY"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            entity_type = 'UNKNOWN_ENUM_VALUE'
        self._entity_type = entity_type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SensitiveType.
        The display name of the sensitive type.


        :return: The display_name of this SensitiveType.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SensitiveType.
        The display name of the sensitive type.


        :param display_name: The display_name of this SensitiveType.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SensitiveType.
        The OCID of the compartment that contains the sensitive type.


        :return: The compartment_id of this SensitiveType.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SensitiveType.
        The OCID of the compartment that contains the sensitive type.


        :param compartment_id: The compartment_id of this SensitiveType.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SensitiveType.
        The current state of the sensitive type.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SensitiveType.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SensitiveType.
        The current state of the sensitive type.


        :param lifecycle_state: The lifecycle_state of this SensitiveType.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def short_name(self):
        """
        Gets the short_name of this SensitiveType.
        The short name of the sensitive type.


        :return: The short_name of this SensitiveType.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this SensitiveType.
        The short name of the sensitive type.


        :param short_name: The short_name of this SensitiveType.
        :type: str
        """
        self._short_name = short_name

    @property
    def source(self):
        """
        **[Required]** Gets the source of this SensitiveType.
        Specifies whether the sensitive type is user-defined or predefined.

        Allowed values for this property are: "ORACLE", "USER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source of this SensitiveType.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this SensitiveType.
        Specifies whether the sensitive type is user-defined or predefined.


        :param source: The source of this SensitiveType.
        :type: str
        """
        allowed_values = ["ORACLE", "USER"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            source = 'UNKNOWN_ENUM_VALUE'
        self._source = source

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SensitiveType.
        The date and time the sensitive type was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this SensitiveType.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SensitiveType.
        The date and time the sensitive type was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this SensitiveType.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this SensitiveType.
        The date and time the sensitive type was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this SensitiveType.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SensitiveType.
        The date and time the sensitive type was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this SensitiveType.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def description(self):
        """
        Gets the description of this SensitiveType.
        The description of the sensitive type.


        :return: The description of this SensitiveType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SensitiveType.
        The description of the sensitive type.


        :param description: The description of this SensitiveType.
        :type: str
        """
        self._description = description

    @property
    def parent_category_id(self):
        """
        Gets the parent_category_id of this SensitiveType.
        The OCID of the parent sensitive category.


        :return: The parent_category_id of this SensitiveType.
        :rtype: str
        """
        return self._parent_category_id

    @parent_category_id.setter
    def parent_category_id(self, parent_category_id):
        """
        Sets the parent_category_id of this SensitiveType.
        The OCID of the parent sensitive category.


        :param parent_category_id: The parent_category_id of this SensitiveType.
        :type: str
        """
        self._parent_category_id = parent_category_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SensitiveType.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SensitiveType.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SensitiveType.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SensitiveType.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SensitiveType.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SensitiveType.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SensitiveType.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SensitiveType.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SensitiveType.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this SensitiveType.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SensitiveType.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this SensitiveType.
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
