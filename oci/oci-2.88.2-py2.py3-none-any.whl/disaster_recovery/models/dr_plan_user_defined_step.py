# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrPlanUserDefinedStep(object):
    """
    The details for a user-defined step in a DR Plan.
    """

    #: A constant which can be used with the step_type property of a DrPlanUserDefinedStep.
    #: This constant has a value of "RUN_OBJECTSTORE_SCRIPT_PRECHECK"
    STEP_TYPE_RUN_OBJECTSTORE_SCRIPT_PRECHECK = "RUN_OBJECTSTORE_SCRIPT_PRECHECK"

    #: A constant which can be used with the step_type property of a DrPlanUserDefinedStep.
    #: This constant has a value of "RUN_LOCAL_SCRIPT_PRECHECK"
    STEP_TYPE_RUN_LOCAL_SCRIPT_PRECHECK = "RUN_LOCAL_SCRIPT_PRECHECK"

    #: A constant which can be used with the step_type property of a DrPlanUserDefinedStep.
    #: This constant has a value of "INVOKE_FUNCTION_PRECHECK"
    STEP_TYPE_INVOKE_FUNCTION_PRECHECK = "INVOKE_FUNCTION_PRECHECK"

    #: A constant which can be used with the step_type property of a DrPlanUserDefinedStep.
    #: This constant has a value of "RUN_OBJECTSTORE_SCRIPT"
    STEP_TYPE_RUN_OBJECTSTORE_SCRIPT = "RUN_OBJECTSTORE_SCRIPT"

    #: A constant which can be used with the step_type property of a DrPlanUserDefinedStep.
    #: This constant has a value of "RUN_LOCAL_SCRIPT"
    STEP_TYPE_RUN_LOCAL_SCRIPT = "RUN_LOCAL_SCRIPT"

    #: A constant which can be used with the step_type property of a DrPlanUserDefinedStep.
    #: This constant has a value of "INVOKE_FUNCTION"
    STEP_TYPE_INVOKE_FUNCTION = "INVOKE_FUNCTION"

    def __init__(self, **kwargs):
        """
        Initializes a new DrPlanUserDefinedStep object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.disaster_recovery.models.InvokeFunctionStep`
        * :class:`~oci.disaster_recovery.models.InvokeFunctionPrecheckStep`
        * :class:`~oci.disaster_recovery.models.RunLocalScriptUserDefinedStep`
        * :class:`~oci.disaster_recovery.models.LocalScriptPrecheckStep`
        * :class:`~oci.disaster_recovery.models.ObjectStoreScriptPrecheckStep`
        * :class:`~oci.disaster_recovery.models.RunObjectStoreScriptUserDefinedStep`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_type:
            The value to assign to the step_type property of this DrPlanUserDefinedStep.
            Allowed values for this property are: "RUN_OBJECTSTORE_SCRIPT_PRECHECK", "RUN_LOCAL_SCRIPT_PRECHECK", "INVOKE_FUNCTION_PRECHECK", "RUN_OBJECTSTORE_SCRIPT", "RUN_LOCAL_SCRIPT", "INVOKE_FUNCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type step_type: str

        """
        self.swagger_types = {
            'step_type': 'str'
        }

        self.attribute_map = {
            'step_type': 'stepType'
        }

        self._step_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['stepType']

        if type == 'INVOKE_FUNCTION':
            return 'InvokeFunctionStep'

        if type == 'INVOKE_FUNCTION_PRECHECK':
            return 'InvokeFunctionPrecheckStep'

        if type == 'RUN_LOCAL_SCRIPT':
            return 'RunLocalScriptUserDefinedStep'

        if type == 'RUN_LOCAL_SCRIPT_PRECHECK':
            return 'LocalScriptPrecheckStep'

        if type == 'RUN_OBJECTSTORE_SCRIPT_PRECHECK':
            return 'ObjectStoreScriptPrecheckStep'

        if type == 'RUN_OBJECTSTORE_SCRIPT':
            return 'RunObjectStoreScriptUserDefinedStep'
        else:
            return 'DrPlanUserDefinedStep'

    @property
    def step_type(self):
        """
        **[Required]** Gets the step_type of this DrPlanUserDefinedStep.
        The type of the step.

          RUN_OBJECTSTORE_SCRIPT_PRECHECK - A step which performs a precheck on a script stored
            in Oracle Object Storage Service

          RUN_LOCAL_SCRIPT_PRECHECK - A step which performs a precheck on a script which resides
            locally on a compute instance

          INVOKE_FUNCTION_PRECHECK - A step which performs a precheck on an Oracle Function.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

          RUN_OBJECTSTORE_SCRIPT - A step which runs a script stored in
            Oracle Object Storage Service

          RUN_LOCAL_SCRIPT - A step which runs a script that resides locally
            on a compute instance

          INVOKE_FUNCTION - A step which invokes an Oracle Function.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

        Allowed values for this property are: "RUN_OBJECTSTORE_SCRIPT_PRECHECK", "RUN_LOCAL_SCRIPT_PRECHECK", "INVOKE_FUNCTION_PRECHECK", "RUN_OBJECTSTORE_SCRIPT", "RUN_LOCAL_SCRIPT", "INVOKE_FUNCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The step_type of this DrPlanUserDefinedStep.
        :rtype: str
        """
        return self._step_type

    @step_type.setter
    def step_type(self, step_type):
        """
        Sets the step_type of this DrPlanUserDefinedStep.
        The type of the step.

          RUN_OBJECTSTORE_SCRIPT_PRECHECK - A step which performs a precheck on a script stored
            in Oracle Object Storage Service

          RUN_LOCAL_SCRIPT_PRECHECK - A step which performs a precheck on a script which resides
            locally on a compute instance

          INVOKE_FUNCTION_PRECHECK - A step which performs a precheck on an Oracle Function.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

          RUN_OBJECTSTORE_SCRIPT - A step which runs a script stored in
            Oracle Object Storage Service

          RUN_LOCAL_SCRIPT - A step which runs a script that resides locally
            on a compute instance

          INVOKE_FUNCTION - A step which invokes an Oracle Function.
            See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.


        :param step_type: The step_type of this DrPlanUserDefinedStep.
        :type: str
        """
        allowed_values = ["RUN_OBJECTSTORE_SCRIPT_PRECHECK", "RUN_LOCAL_SCRIPT_PRECHECK", "INVOKE_FUNCTION_PRECHECK", "RUN_OBJECTSTORE_SCRIPT", "RUN_LOCAL_SCRIPT", "INVOKE_FUNCTION"]
        if not value_allowed_none_or_none_sentinel(step_type, allowed_values):
            step_type = 'UNKNOWN_ENUM_VALUE'
        self._step_type = step_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
