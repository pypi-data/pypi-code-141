# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrgDetails(object):
    """
    UpdateDrgDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrgDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDrgDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param default_drg_route_tables:
            The value to assign to the default_drg_route_tables property of this UpdateDrgDetails.
        :type default_drg_route_tables: oci.vn_monitoring.models.DefaultDrgRouteTables

        :param display_name:
            The value to assign to the display_name property of this UpdateDrgDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDrgDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'default_drg_route_tables': 'DefaultDrgRouteTables',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'default_drg_route_tables': 'defaultDrgRouteTables',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags'
        }

        self._defined_tags = None
        self._default_drg_route_tables = None
        self._display_name = None
        self._freeform_tags = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDrgDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDrgDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDrgDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDrgDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def default_drg_route_tables(self):
        """
        Gets the default_drg_route_tables of this UpdateDrgDetails.

        :return: The default_drg_route_tables of this UpdateDrgDetails.
        :rtype: oci.vn_monitoring.models.DefaultDrgRouteTables
        """
        return self._default_drg_route_tables

    @default_drg_route_tables.setter
    def default_drg_route_tables(self, default_drg_route_tables):
        """
        Sets the default_drg_route_tables of this UpdateDrgDetails.

        :param default_drg_route_tables: The default_drg_route_tables of this UpdateDrgDetails.
        :type: oci.vn_monitoring.models.DefaultDrgRouteTables
        """
        self._default_drg_route_tables = default_drg_route_tables

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDrgDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateDrgDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDrgDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDrgDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDrgDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateDrgDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDrgDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateDrgDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
