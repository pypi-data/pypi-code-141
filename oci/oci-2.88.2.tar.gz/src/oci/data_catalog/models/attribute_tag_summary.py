# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttributeTagSummary(object):
    """
    Summary of an entity attribute tag.
    """

    #: A constant which can be used with the lifecycle_state property of a AttributeTagSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AttributeTagSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AttributeTagSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AttributeTagSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AttributeTagSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AttributeTagSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AttributeTagSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AttributeTagSummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new AttributeTagSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_key:
            The value to assign to the attribute_key property of this AttributeTagSummary.
        :type attribute_key: str

        :param key:
            The value to assign to the key property of this AttributeTagSummary.
        :type key: str

        :param time_created:
            The value to assign to the time_created property of this AttributeTagSummary.
        :type time_created: datetime

        :param name:
            The value to assign to the name property of this AttributeTagSummary.
        :type name: str

        :param uri:
            The value to assign to the uri property of this AttributeTagSummary.
        :type uri: str

        :param term_key:
            The value to assign to the term_key property of this AttributeTagSummary.
        :type term_key: str

        :param term_path:
            The value to assign to the term_path property of this AttributeTagSummary.
        :type term_path: str

        :param term_description:
            The value to assign to the term_description property of this AttributeTagSummary.
        :type term_description: str

        :param glossary_key:
            The value to assign to the glossary_key property of this AttributeTagSummary.
        :type glossary_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AttributeTagSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'attribute_key': 'str',
            'key': 'str',
            'time_created': 'datetime',
            'name': 'str',
            'uri': 'str',
            'term_key': 'str',
            'term_path': 'str',
            'term_description': 'str',
            'glossary_key': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'attribute_key': 'attributeKey',
            'key': 'key',
            'time_created': 'timeCreated',
            'name': 'name',
            'uri': 'uri',
            'term_key': 'termKey',
            'term_path': 'termPath',
            'term_description': 'termDescription',
            'glossary_key': 'glossaryKey',
            'lifecycle_state': 'lifecycleState'
        }

        self._attribute_key = None
        self._key = None
        self._time_created = None
        self._name = None
        self._uri = None
        self._term_key = None
        self._term_path = None
        self._term_description = None
        self._glossary_key = None
        self._lifecycle_state = None

    @property
    def attribute_key(self):
        """
        Gets the attribute_key of this AttributeTagSummary.
        The unique key of the parent attribute.


        :return: The attribute_key of this AttributeTagSummary.
        :rtype: str
        """
        return self._attribute_key

    @attribute_key.setter
    def attribute_key(self, attribute_key):
        """
        Sets the attribute_key of this AttributeTagSummary.
        The unique key of the parent attribute.


        :param attribute_key: The attribute_key of this AttributeTagSummary.
        :type: str
        """
        self._attribute_key = attribute_key

    @property
    def key(self):
        """
        **[Required]** Gets the key of this AttributeTagSummary.
        Unique tag key that is immutable.


        :return: The key of this AttributeTagSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this AttributeTagSummary.
        Unique tag key that is immutable.


        :param key: The key of this AttributeTagSummary.
        :type: str
        """
        self._key = key

    @property
    def time_created(self):
        """
        Gets the time_created of this AttributeTagSummary.
        The date and time the tag was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AttributeTagSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AttributeTagSummary.
        The date and time the tag was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AttributeTagSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def name(self):
        """
        Gets the name of this AttributeTagSummary.
        Name of the tag that matches the term name.


        :return: The name of this AttributeTagSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AttributeTagSummary.
        Name of the tag that matches the term name.


        :param name: The name of this AttributeTagSummary.
        :type: str
        """
        self._name = name

    @property
    def uri(self):
        """
        Gets the uri of this AttributeTagSummary.
        URI to the tag instance in the API.


        :return: The uri of this AttributeTagSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this AttributeTagSummary.
        URI to the tag instance in the API.


        :param uri: The uri of this AttributeTagSummary.
        :type: str
        """
        self._uri = uri

    @property
    def term_key(self):
        """
        Gets the term_key of this AttributeTagSummary.
        Unique key of the related term.


        :return: The term_key of this AttributeTagSummary.
        :rtype: str
        """
        return self._term_key

    @term_key.setter
    def term_key(self, term_key):
        """
        Sets the term_key of this AttributeTagSummary.
        Unique key of the related term.


        :param term_key: The term_key of this AttributeTagSummary.
        :type: str
        """
        self._term_key = term_key

    @property
    def term_path(self):
        """
        Gets the term_path of this AttributeTagSummary.
        Path of the related term.


        :return: The term_path of this AttributeTagSummary.
        :rtype: str
        """
        return self._term_path

    @term_path.setter
    def term_path(self, term_path):
        """
        Sets the term_path of this AttributeTagSummary.
        Path of the related term.


        :param term_path: The term_path of this AttributeTagSummary.
        :type: str
        """
        self._term_path = term_path

    @property
    def term_description(self):
        """
        Gets the term_description of this AttributeTagSummary.
        Description of the related term.


        :return: The term_description of this AttributeTagSummary.
        :rtype: str
        """
        return self._term_description

    @term_description.setter
    def term_description(self, term_description):
        """
        Sets the term_description of this AttributeTagSummary.
        Description of the related term.


        :param term_description: The term_description of this AttributeTagSummary.
        :type: str
        """
        self._term_description = term_description

    @property
    def glossary_key(self):
        """
        Gets the glossary_key of this AttributeTagSummary.
        Unique id of the parent glossary of the term.


        :return: The glossary_key of this AttributeTagSummary.
        :rtype: str
        """
        return self._glossary_key

    @glossary_key.setter
    def glossary_key(self, glossary_key):
        """
        Sets the glossary_key of this AttributeTagSummary.
        Unique id of the parent glossary of the term.


        :param glossary_key: The glossary_key of this AttributeTagSummary.
        :type: str
        """
        self._glossary_key = glossary_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AttributeTagSummary.
        State of the Tag.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AttributeTagSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AttributeTagSummary.
        State of the Tag.


        :param lifecycle_state: The lifecycle_state of this AttributeTagSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
