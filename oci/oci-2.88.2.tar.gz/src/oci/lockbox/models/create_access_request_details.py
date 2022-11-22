# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAccessRequestDetails(object):
    """
    The configuration details for a new access request.
    We don't accept a compartmentId parameter because it is implied to be the same as the lockbox as a subsidiary resource.
    The requestorId is also based on the caller user info.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAccessRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lockbox_id:
            The value to assign to the lockbox_id property of this CreateAccessRequestDetails.
        :type lockbox_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateAccessRequestDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateAccessRequestDetails.
        :type description: str

        :param context:
            The value to assign to the context property of this CreateAccessRequestDetails.
        :type context: dict(str, str)

        :param access_duration:
            The value to assign to the access_duration property of this CreateAccessRequestDetails.
        :type access_duration: str

        """
        self.swagger_types = {
            'lockbox_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'context': 'dict(str, str)',
            'access_duration': 'str'
        }

        self.attribute_map = {
            'lockbox_id': 'lockboxId',
            'display_name': 'displayName',
            'description': 'description',
            'context': 'context',
            'access_duration': 'accessDuration'
        }

        self._lockbox_id = None
        self._display_name = None
        self._description = None
        self._context = None
        self._access_duration = None

    @property
    def lockbox_id(self):
        """
        **[Required]** Gets the lockbox_id of this CreateAccessRequestDetails.
        The unique identifier (OCID) of the lockbox box that the access request is associated with which is immutable.


        :return: The lockbox_id of this CreateAccessRequestDetails.
        :rtype: str
        """
        return self._lockbox_id

    @lockbox_id.setter
    def lockbox_id(self, lockbox_id):
        """
        Sets the lockbox_id of this CreateAccessRequestDetails.
        The unique identifier (OCID) of the lockbox box that the access request is associated with which is immutable.


        :param lockbox_id: The lockbox_id of this CreateAccessRequestDetails.
        :type: str
        """
        self._lockbox_id = lockbox_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAccessRequestDetails.
        The name of the access request.


        :return: The display_name of this CreateAccessRequestDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAccessRequestDetails.
        The name of the access request.


        :param display_name: The display_name of this CreateAccessRequestDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateAccessRequestDetails.
        The rationale for requesting the access request.


        :return: The description of this CreateAccessRequestDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAccessRequestDetails.
        The rationale for requesting the access request.


        :param description: The description of this CreateAccessRequestDetails.
        :type: str
        """
        self._description = description

    @property
    def context(self):
        """
        Gets the context of this CreateAccessRequestDetails.
        The context object containing the access request specific details.


        :return: The context of this CreateAccessRequestDetails.
        :rtype: dict(str, str)
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this CreateAccessRequestDetails.
        The context object containing the access request specific details.


        :param context: The context of this CreateAccessRequestDetails.
        :type: dict(str, str)
        """
        self._context = context

    @property
    def access_duration(self):
        """
        **[Required]** Gets the access_duration of this CreateAccessRequestDetails.
        The maximum amount of time operator has access to associated resources.


        :return: The access_duration of this CreateAccessRequestDetails.
        :rtype: str
        """
        return self._access_duration

    @access_duration.setter
    def access_duration(self, access_duration):
        """
        Sets the access_duration of this CreateAccessRequestDetails.
        The maximum amount of time operator has access to associated resources.


        :param access_duration: The access_duration of this CreateAccessRequestDetails.
        :type: str
        """
        self._access_duration = access_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
