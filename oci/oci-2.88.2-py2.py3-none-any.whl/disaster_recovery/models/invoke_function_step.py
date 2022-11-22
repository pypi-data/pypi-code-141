# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dr_plan_user_defined_step import DrPlanUserDefinedStep
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvokeFunctionStep(DrPlanUserDefinedStep):
    """
    Invoke Oracle function step details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InvokeFunctionStep object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.InvokeFunctionStep.step_type` attribute
        of this class is ``INVOKE_FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_type:
            The value to assign to the step_type property of this InvokeFunctionStep.
            Allowed values for this property are: "RUN_OBJECTSTORE_SCRIPT_PRECHECK", "RUN_LOCAL_SCRIPT_PRECHECK", "INVOKE_FUNCTION_PRECHECK", "RUN_OBJECTSTORE_SCRIPT", "RUN_LOCAL_SCRIPT", "INVOKE_FUNCTION"
        :type step_type: str

        :param function_id:
            The value to assign to the function_id property of this InvokeFunctionStep.
        :type function_id: str

        :param function_region:
            The value to assign to the function_region property of this InvokeFunctionStep.
        :type function_region: str

        :param request_body:
            The value to assign to the request_body property of this InvokeFunctionStep.
        :type request_body: str

        """
        self.swagger_types = {
            'step_type': 'str',
            'function_id': 'str',
            'function_region': 'str',
            'request_body': 'str'
        }

        self.attribute_map = {
            'step_type': 'stepType',
            'function_id': 'functionId',
            'function_region': 'functionRegion',
            'request_body': 'requestBody'
        }

        self._step_type = None
        self._function_id = None
        self._function_region = None
        self._request_body = None
        self._step_type = 'INVOKE_FUNCTION'

    @property
    def function_id(self):
        """
        Gets the function_id of this InvokeFunctionStep.
        The OCID of function to be invoked.

        Example: `ocid1.fnfunc.oc1.iad.exampleocid2`


        :return: The function_id of this InvokeFunctionStep.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this InvokeFunctionStep.
        The OCID of function to be invoked.

        Example: `ocid1.fnfunc.oc1.iad.exampleocid2`


        :param function_id: The function_id of this InvokeFunctionStep.
        :type: str
        """
        self._function_id = function_id

    @property
    def function_region(self):
        """
        Gets the function_region of this InvokeFunctionStep.
        The region in which the function is deployed.

        Example: `us-ashburn-1`


        :return: The function_region of this InvokeFunctionStep.
        :rtype: str
        """
        return self._function_region

    @function_region.setter
    def function_region(self, function_region):
        """
        Sets the function_region of this InvokeFunctionStep.
        The region in which the function is deployed.

        Example: `us-ashburn-1`


        :param function_region: The function_region of this InvokeFunctionStep.
        :type: str
        """
        self._function_region = function_region

    @property
    def request_body(self):
        """
        Gets the request_body of this InvokeFunctionStep.
        The request body for the function.

        Example: `{ \"FnParam1\", \"FnParam2\" }`


        :return: The request_body of this InvokeFunctionStep.
        :rtype: str
        """
        return self._request_body

    @request_body.setter
    def request_body(self, request_body):
        """
        Sets the request_body of this InvokeFunctionStep.
        The request body for the function.

        Example: `{ \"FnParam1\", \"FnParam2\" }`


        :param request_body: The request_body of this InvokeFunctionStep.
        :type: str
        """
        self._request_body = request_body

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
