# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MessageSummary(object):
    """
    Deployment message Summary.
    """

    #: A constant which can be used with the deployment_message_status property of a MessageSummary.
    #: This constant has a value of "INFO"
    DEPLOYMENT_MESSAGE_STATUS_INFO = "INFO"

    #: A constant which can be used with the deployment_message_status property of a MessageSummary.
    #: This constant has a value of "WARNING"
    DEPLOYMENT_MESSAGE_STATUS_WARNING = "WARNING"

    #: A constant which can be used with the deployment_message_status property of a MessageSummary.
    #: This constant has a value of "ERROR"
    DEPLOYMENT_MESSAGE_STATUS_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new MessageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MessageSummary.
        :type id: str

        :param deployment_message:
            The value to assign to the deployment_message property of this MessageSummary.
        :type deployment_message: str

        :param deployment_message_status:
            The value to assign to the deployment_message_status property of this MessageSummary.
            Allowed values for this property are: "INFO", "WARNING", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_message_status: str

        """
        self.swagger_types = {
            'id': 'str',
            'deployment_message': 'str',
            'deployment_message_status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'deployment_message': 'deploymentMessage',
            'deployment_message_status': 'deploymentMessageStatus'
        }

        self._id = None
        self._deployment_message = None
        self._deployment_message_status = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MessageSummary.
        The deployment Message Id.


        :return: The id of this MessageSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MessageSummary.
        The deployment Message Id.


        :param id: The id of this MessageSummary.
        :type: str
        """
        self._id = id

    @property
    def deployment_message(self):
        """
        **[Required]** Gets the deployment_message of this MessageSummary.
        The deployment Message in plain text with optional HTML anchor tags.


        :return: The deployment_message of this MessageSummary.
        :rtype: str
        """
        return self._deployment_message

    @deployment_message.setter
    def deployment_message(self, deployment_message):
        """
        Sets the deployment_message of this MessageSummary.
        The deployment Message in plain text with optional HTML anchor tags.


        :param deployment_message: The deployment_message of this MessageSummary.
        :type: str
        """
        self._deployment_message = deployment_message

    @property
    def deployment_message_status(self):
        """
        **[Required]** Gets the deployment_message_status of this MessageSummary.
        The deployment Message Status.

        Allowed values for this property are: "INFO", "WARNING", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_message_status of this MessageSummary.
        :rtype: str
        """
        return self._deployment_message_status

    @deployment_message_status.setter
    def deployment_message_status(self, deployment_message_status):
        """
        Sets the deployment_message_status of this MessageSummary.
        The deployment Message Status.


        :param deployment_message_status: The deployment_message_status of this MessageSummary.
        :type: str
        """
        allowed_values = ["INFO", "WARNING", "ERROR"]
        if not value_allowed_none_or_none_sentinel(deployment_message_status, allowed_values):
            deployment_message_status = 'UNKNOWN_ENUM_VALUE'
        self._deployment_message_status = deployment_message_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
