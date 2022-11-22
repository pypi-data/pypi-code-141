# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetEnvironment(object):
    """
    Description of the target environment.
    """

    #: A constant which can be used with the target_environment_type property of a TargetEnvironment.
    #: This constant has a value of "VM_TARGET_ENV"
    TARGET_ENVIRONMENT_TYPE_VM_TARGET_ENV = "VM_TARGET_ENV"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetEnvironment object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_migrations.models.VmTargetEnvironment`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_compartment_id:
            The value to assign to the target_compartment_id property of this TargetEnvironment.
        :type target_compartment_id: str

        :param target_environment_type:
            The value to assign to the target_environment_type property of this TargetEnvironment.
            Allowed values for this property are: "VM_TARGET_ENV", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_environment_type: str

        """
        self.swagger_types = {
            'target_compartment_id': 'str',
            'target_environment_type': 'str'
        }

        self.attribute_map = {
            'target_compartment_id': 'targetCompartmentId',
            'target_environment_type': 'targetEnvironmentType'
        }

        self._target_compartment_id = None
        self._target_environment_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['targetEnvironmentType']

        if type == 'VM_TARGET_ENV':
            return 'VmTargetEnvironment'
        else:
            return 'TargetEnvironment'

    @property
    def target_compartment_id(self):
        """
        Gets the target_compartment_id of this TargetEnvironment.
        Target compartment identifier


        :return: The target_compartment_id of this TargetEnvironment.
        :rtype: str
        """
        return self._target_compartment_id

    @target_compartment_id.setter
    def target_compartment_id(self, target_compartment_id):
        """
        Sets the target_compartment_id of this TargetEnvironment.
        Target compartment identifier


        :param target_compartment_id: The target_compartment_id of this TargetEnvironment.
        :type: str
        """
        self._target_compartment_id = target_compartment_id

    @property
    def target_environment_type(self):
        """
        **[Required]** Gets the target_environment_type of this TargetEnvironment.
        The type of target environment.

        Allowed values for this property are: "VM_TARGET_ENV", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target_environment_type of this TargetEnvironment.
        :rtype: str
        """
        return self._target_environment_type

    @target_environment_type.setter
    def target_environment_type(self, target_environment_type):
        """
        Sets the target_environment_type of this TargetEnvironment.
        The type of target environment.


        :param target_environment_type: The target_environment_type of this TargetEnvironment.
        :type: str
        """
        allowed_values = ["VM_TARGET_ENV"]
        if not value_allowed_none_or_none_sentinel(target_environment_type, allowed_values):
            target_environment_type = 'UNKNOWN_ENUM_VALUE'
        self._target_environment_type = target_environment_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
