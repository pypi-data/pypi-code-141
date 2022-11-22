# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionAssignmentDetails(object):
    """
    The information about a new Connection Assignment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionAssignmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_id:
            The value to assign to the connection_id property of this CreateConnectionAssignmentDetails.
        :type connection_id: str

        :param deployment_id:
            The value to assign to the deployment_id property of this CreateConnectionAssignmentDetails.
        :type deployment_id: str

        """
        self.swagger_types = {
            'connection_id': 'str',
            'deployment_id': 'str'
        }

        self.attribute_map = {
            'connection_id': 'connectionId',
            'deployment_id': 'deploymentId'
        }

        self._connection_id = None
        self._deployment_id = None

    @property
    def connection_id(self):
        """
        **[Required]** Gets the connection_id of this CreateConnectionAssignmentDetails.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The connection_id of this CreateConnectionAssignmentDetails.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this CreateConnectionAssignmentDetails.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param connection_id: The connection_id of this CreateConnectionAssignmentDetails.
        :type: str
        """
        self._connection_id = connection_id

    @property
    def deployment_id(self):
        """
        **[Required]** Gets the deployment_id of this CreateConnectionAssignmentDetails.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this CreateConnectionAssignmentDetails.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this CreateConnectionAssignmentDetails.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this CreateConnectionAssignmentDetails.
        :type: str
        """
        self._deployment_id = deployment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
