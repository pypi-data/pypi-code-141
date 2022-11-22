# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OptimizerStatisticsAdvisorExecutionSummary(object):
    """
    The summary of the Optimizer Statistics Advisor execution.
    """

    #: A constant which can be used with the status property of a OptimizerStatisticsAdvisorExecutionSummary.
    #: This constant has a value of "EXECUTING"
    STATUS_EXECUTING = "EXECUTING"

    #: A constant which can be used with the status property of a OptimizerStatisticsAdvisorExecutionSummary.
    #: This constant has a value of "COMPLETED"
    STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the status property of a OptimizerStatisticsAdvisorExecutionSummary.
    #: This constant has a value of "INTERRUPTED"
    STATUS_INTERRUPTED = "INTERRUPTED"

    #: A constant which can be used with the status property of a OptimizerStatisticsAdvisorExecutionSummary.
    #: This constant has a value of "CANCELLED"
    STATUS_CANCELLED = "CANCELLED"

    #: A constant which can be used with the status property of a OptimizerStatisticsAdvisorExecutionSummary.
    #: This constant has a value of "FATAL_ERROR"
    STATUS_FATAL_ERROR = "FATAL_ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new OptimizerStatisticsAdvisorExecutionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param task_name:
            The value to assign to the task_name property of this OptimizerStatisticsAdvisorExecutionSummary.
        :type task_name: str

        :param execution_name:
            The value to assign to the execution_name property of this OptimizerStatisticsAdvisorExecutionSummary.
        :type execution_name: str

        :param time_start:
            The value to assign to the time_start property of this OptimizerStatisticsAdvisorExecutionSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this OptimizerStatisticsAdvisorExecutionSummary.
        :type time_end: datetime

        :param status:
            The value to assign to the status property of this OptimizerStatisticsAdvisorExecutionSummary.
            Allowed values for this property are: "EXECUTING", "COMPLETED", "INTERRUPTED", "CANCELLED", "FATAL_ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_message:
            The value to assign to the status_message property of this OptimizerStatisticsAdvisorExecutionSummary.
        :type status_message: str

        :param error_message:
            The value to assign to the error_message property of this OptimizerStatisticsAdvisorExecutionSummary.
        :type error_message: str

        :param findings:
            The value to assign to the findings property of this OptimizerStatisticsAdvisorExecutionSummary.
        :type findings: int

        """
        self.swagger_types = {
            'task_name': 'str',
            'execution_name': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'status': 'str',
            'status_message': 'str',
            'error_message': 'str',
            'findings': 'int'
        }

        self.attribute_map = {
            'task_name': 'taskName',
            'execution_name': 'executionName',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'status': 'status',
            'status_message': 'statusMessage',
            'error_message': 'errorMessage',
            'findings': 'findings'
        }

        self._task_name = None
        self._execution_name = None
        self._time_start = None
        self._time_end = None
        self._status = None
        self._status_message = None
        self._error_message = None
        self._findings = None

    @property
    def task_name(self):
        """
        **[Required]** Gets the task_name of this OptimizerStatisticsAdvisorExecutionSummary.
        The name of the Optimizer Statistics Advisor task.


        :return: The task_name of this OptimizerStatisticsAdvisorExecutionSummary.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """
        Sets the task_name of this OptimizerStatisticsAdvisorExecutionSummary.
        The name of the Optimizer Statistics Advisor task.


        :param task_name: The task_name of this OptimizerStatisticsAdvisorExecutionSummary.
        :type: str
        """
        self._task_name = task_name

    @property
    def execution_name(self):
        """
        **[Required]** Gets the execution_name of this OptimizerStatisticsAdvisorExecutionSummary.
        The name of the Optimizer Statistics Advisor execution.


        :return: The execution_name of this OptimizerStatisticsAdvisorExecutionSummary.
        :rtype: str
        """
        return self._execution_name

    @execution_name.setter
    def execution_name(self, execution_name):
        """
        Sets the execution_name of this OptimizerStatisticsAdvisorExecutionSummary.
        The name of the Optimizer Statistics Advisor execution.


        :param execution_name: The execution_name of this OptimizerStatisticsAdvisorExecutionSummary.
        :type: str
        """
        self._execution_name = execution_name

    @property
    def time_start(self):
        """
        **[Required]** Gets the time_start of this OptimizerStatisticsAdvisorExecutionSummary.
        The start time of the time range to retrieve the Optimizer Statistics Advisor execution of a Managed Database
        in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :return: The time_start of this OptimizerStatisticsAdvisorExecutionSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this OptimizerStatisticsAdvisorExecutionSummary.
        The start time of the time range to retrieve the Optimizer Statistics Advisor execution of a Managed Database
        in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :param time_start: The time_start of this OptimizerStatisticsAdvisorExecutionSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        **[Required]** Gets the time_end of this OptimizerStatisticsAdvisorExecutionSummary.
        The end time of the time range to retrieve the Optimizer Statistics Advisor execution of a Managed Database
        in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :return: The time_end of this OptimizerStatisticsAdvisorExecutionSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this OptimizerStatisticsAdvisorExecutionSummary.
        The end time of the time range to retrieve the Optimizer Statistics Advisor execution of a Managed Database
        in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :param time_end: The time_end of this OptimizerStatisticsAdvisorExecutionSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def status(self):
        """
        **[Required]** Gets the status of this OptimizerStatisticsAdvisorExecutionSummary.
        The status of the Optimizer Statistics Advisor execution.

        Allowed values for this property are: "EXECUTING", "COMPLETED", "INTERRUPTED", "CANCELLED", "FATAL_ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this OptimizerStatisticsAdvisorExecutionSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this OptimizerStatisticsAdvisorExecutionSummary.
        The status of the Optimizer Statistics Advisor execution.


        :param status: The status of this OptimizerStatisticsAdvisorExecutionSummary.
        :type: str
        """
        allowed_values = ["EXECUTING", "COMPLETED", "INTERRUPTED", "CANCELLED", "FATAL_ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_message(self):
        """
        Gets the status_message of this OptimizerStatisticsAdvisorExecutionSummary.
        The Optimizer Statistics Advisor execution status message, if any.


        :return: The status_message of this OptimizerStatisticsAdvisorExecutionSummary.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this OptimizerStatisticsAdvisorExecutionSummary.
        The Optimizer Statistics Advisor execution status message, if any.


        :param status_message: The status_message of this OptimizerStatisticsAdvisorExecutionSummary.
        :type: str
        """
        self._status_message = status_message

    @property
    def error_message(self):
        """
        Gets the error_message of this OptimizerStatisticsAdvisorExecutionSummary.
        The errors in the Optimizer Statistics Advisor execution, if any.


        :return: The error_message of this OptimizerStatisticsAdvisorExecutionSummary.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this OptimizerStatisticsAdvisorExecutionSummary.
        The errors in the Optimizer Statistics Advisor execution, if any.


        :param error_message: The error_message of this OptimizerStatisticsAdvisorExecutionSummary.
        :type: str
        """
        self._error_message = error_message

    @property
    def findings(self):
        """
        Gets the findings of this OptimizerStatisticsAdvisorExecutionSummary.
        The number of findings generated by the Optimizer Statistics Advisor execution.


        :return: The findings of this OptimizerStatisticsAdvisorExecutionSummary.
        :rtype: int
        """
        return self._findings

    @findings.setter
    def findings(self, findings):
        """
        Sets the findings of this OptimizerStatisticsAdvisorExecutionSummary.
        The number of findings generated by the Optimizer Statistics Advisor execution.


        :param findings: The findings of this OptimizerStatisticsAdvisorExecutionSummary.
        :type: int
        """
        self._findings = findings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
