# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociationDetails(object):
    """
    The information about monitored resource association.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssociationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_resource_id:
            The value to assign to the source_resource_id property of this AssociationDetails.
        :type source_resource_id: str

        :param association_type:
            The value to assign to the association_type property of this AssociationDetails.
        :type association_type: str

        """
        self.swagger_types = {
            'source_resource_id': 'str',
            'association_type': 'str'
        }

        self.attribute_map = {
            'source_resource_id': 'sourceResourceId',
            'association_type': 'associationType'
        }

        self._source_resource_id = None
        self._association_type = None

    @property
    def source_resource_id(self):
        """
        **[Required]** Gets the source_resource_id of this AssociationDetails.
        Source Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_resource_id of this AssociationDetails.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        """
        Sets the source_resource_id of this AssociationDetails.
        Source Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_resource_id: The source_resource_id of this AssociationDetails.
        :type: str
        """
        self._source_resource_id = source_resource_id

    @property
    def association_type(self):
        """
        **[Required]** Gets the association_type of this AssociationDetails.
        Association Type


        :return: The association_type of this AssociationDetails.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """
        Sets the association_type of this AssociationDetails.
        Association Type


        :param association_type: The association_type of this AssociationDetails.
        :type: str
        """
        self._association_type = association_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
