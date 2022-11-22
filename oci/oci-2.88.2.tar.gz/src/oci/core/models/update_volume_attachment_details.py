# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVolumeAttachmentDetails(object):
    """
    details for updating a volume attachment.
    """

    #: A constant which can be used with the iscsi_login_state property of a UpdateVolumeAttachmentDetails.
    #: This constant has a value of "UNKNOWN"
    ISCSI_LOGIN_STATE_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the iscsi_login_state property of a UpdateVolumeAttachmentDetails.
    #: This constant has a value of "LOGGING_IN"
    ISCSI_LOGIN_STATE_LOGGING_IN = "LOGGING_IN"

    #: A constant which can be used with the iscsi_login_state property of a UpdateVolumeAttachmentDetails.
    #: This constant has a value of "LOGIN_SUCCEEDED"
    ISCSI_LOGIN_STATE_LOGIN_SUCCEEDED = "LOGIN_SUCCEEDED"

    #: A constant which can be used with the iscsi_login_state property of a UpdateVolumeAttachmentDetails.
    #: This constant has a value of "LOGIN_FAILED"
    ISCSI_LOGIN_STATE_LOGIN_FAILED = "LOGIN_FAILED"

    #: A constant which can be used with the iscsi_login_state property of a UpdateVolumeAttachmentDetails.
    #: This constant has a value of "LOGGING_OUT"
    ISCSI_LOGIN_STATE_LOGGING_OUT = "LOGGING_OUT"

    #: A constant which can be used with the iscsi_login_state property of a UpdateVolumeAttachmentDetails.
    #: This constant has a value of "LOGOUT_SUCCEEDED"
    ISCSI_LOGIN_STATE_LOGOUT_SUCCEEDED = "LOGOUT_SUCCEEDED"

    #: A constant which can be used with the iscsi_login_state property of a UpdateVolumeAttachmentDetails.
    #: This constant has a value of "LOGOUT_FAILED"
    ISCSI_LOGIN_STATE_LOGOUT_FAILED = "LOGOUT_FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVolumeAttachmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param iscsi_login_state:
            The value to assign to the iscsi_login_state property of this UpdateVolumeAttachmentDetails.
            Allowed values for this property are: "UNKNOWN", "LOGGING_IN", "LOGIN_SUCCEEDED", "LOGIN_FAILED", "LOGGING_OUT", "LOGOUT_SUCCEEDED", "LOGOUT_FAILED"
        :type iscsi_login_state: str

        """
        self.swagger_types = {
            'iscsi_login_state': 'str'
        }

        self.attribute_map = {
            'iscsi_login_state': 'iscsiLoginState'
        }

        self._iscsi_login_state = None

    @property
    def iscsi_login_state(self):
        """
        Gets the iscsi_login_state of this UpdateVolumeAttachmentDetails.
        The iscsi login state of the volume attachment. For a multipath volume attachment,
        all iscsi sessions need to be all logged-in or logged-out to be in logged-in or logged-out state.

        Allowed values for this property are: "UNKNOWN", "LOGGING_IN", "LOGIN_SUCCEEDED", "LOGIN_FAILED", "LOGGING_OUT", "LOGOUT_SUCCEEDED", "LOGOUT_FAILED"


        :return: The iscsi_login_state of this UpdateVolumeAttachmentDetails.
        :rtype: str
        """
        return self._iscsi_login_state

    @iscsi_login_state.setter
    def iscsi_login_state(self, iscsi_login_state):
        """
        Sets the iscsi_login_state of this UpdateVolumeAttachmentDetails.
        The iscsi login state of the volume attachment. For a multipath volume attachment,
        all iscsi sessions need to be all logged-in or logged-out to be in logged-in or logged-out state.


        :param iscsi_login_state: The iscsi_login_state of this UpdateVolumeAttachmentDetails.
        :type: str
        """
        allowed_values = ["UNKNOWN", "LOGGING_IN", "LOGIN_SUCCEEDED", "LOGIN_FAILED", "LOGGING_OUT", "LOGOUT_SUCCEEDED", "LOGOUT_FAILED"]
        if not value_allowed_none_or_none_sentinel(iscsi_login_state, allowed_values):
            raise ValueError(
                "Invalid value for `iscsi_login_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._iscsi_login_state = iscsi_login_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
