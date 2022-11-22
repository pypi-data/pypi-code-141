# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_performance_metric_group import HostPerformanceMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostTopProcesses(HostPerformanceMetricGroup):
    """
    Top Processes metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostTopProcesses object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostTopProcesses.metric_name` attribute
        of this class is ``HOST_TOP_PROCESSES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostTopProcesses.
            Allowed values for this property are: "HOST_CPU_USAGE", "HOST_MEMORY_USAGE", "HOST_NETWORK_ACTIVITY_SUMMARY", "HOST_TOP_PROCESSES"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostTopProcesses.
        :type time_collected: datetime

        :param pid:
            The value to assign to the pid property of this HostTopProcesses.
        :type pid: float

        :param user_name:
            The value to assign to the user_name property of this HostTopProcesses.
        :type user_name: str

        :param memory_utilization_percent:
            The value to assign to the memory_utilization_percent property of this HostTopProcesses.
        :type memory_utilization_percent: float

        :param cpu_utilization_percent:
            The value to assign to the cpu_utilization_percent property of this HostTopProcesses.
        :type cpu_utilization_percent: float

        :param cpu_usage_in_seconds:
            The value to assign to the cpu_usage_in_seconds property of this HostTopProcesses.
        :type cpu_usage_in_seconds: float

        :param command:
            The value to assign to the command property of this HostTopProcesses.
        :type command: str

        :param virtual_memory_in_mbs:
            The value to assign to the virtual_memory_in_mbs property of this HostTopProcesses.
        :type virtual_memory_in_mbs: float

        :param physical_memory_in_mbs:
            The value to assign to the physical_memory_in_mbs property of this HostTopProcesses.
        :type physical_memory_in_mbs: float

        :param start_time:
            The value to assign to the start_time property of this HostTopProcesses.
        :type start_time: datetime

        :param total_processes:
            The value to assign to the total_processes property of this HostTopProcesses.
        :type total_processes: float

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'pid': 'float',
            'user_name': 'str',
            'memory_utilization_percent': 'float',
            'cpu_utilization_percent': 'float',
            'cpu_usage_in_seconds': 'float',
            'command': 'str',
            'virtual_memory_in_mbs': 'float',
            'physical_memory_in_mbs': 'float',
            'start_time': 'datetime',
            'total_processes': 'float'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'pid': 'pid',
            'user_name': 'userName',
            'memory_utilization_percent': 'memoryUtilizationPercent',
            'cpu_utilization_percent': 'cpuUtilizationPercent',
            'cpu_usage_in_seconds': 'cpuUsageInSeconds',
            'command': 'command',
            'virtual_memory_in_mbs': 'virtualMemoryInMBs',
            'physical_memory_in_mbs': 'physicalMemoryInMBs',
            'start_time': 'startTime',
            'total_processes': 'totalProcesses'
        }

        self._metric_name = None
        self._time_collected = None
        self._pid = None
        self._user_name = None
        self._memory_utilization_percent = None
        self._cpu_utilization_percent = None
        self._cpu_usage_in_seconds = None
        self._command = None
        self._virtual_memory_in_mbs = None
        self._physical_memory_in_mbs = None
        self._start_time = None
        self._total_processes = None
        self._metric_name = 'HOST_TOP_PROCESSES'

    @property
    def pid(self):
        """
        Gets the pid of this HostTopProcesses.
        process id


        :return: The pid of this HostTopProcesses.
        :rtype: float
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this HostTopProcesses.
        process id


        :param pid: The pid of this HostTopProcesses.
        :type: float
        """
        self._pid = pid

    @property
    def user_name(self):
        """
        Gets the user_name of this HostTopProcesses.
        User that started the process


        :return: The user_name of this HostTopProcesses.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this HostTopProcesses.
        User that started the process


        :param user_name: The user_name of this HostTopProcesses.
        :type: str
        """
        self._user_name = user_name

    @property
    def memory_utilization_percent(self):
        """
        Gets the memory_utilization_percent of this HostTopProcesses.
        Memory utilization percentage


        :return: The memory_utilization_percent of this HostTopProcesses.
        :rtype: float
        """
        return self._memory_utilization_percent

    @memory_utilization_percent.setter
    def memory_utilization_percent(self, memory_utilization_percent):
        """
        Sets the memory_utilization_percent of this HostTopProcesses.
        Memory utilization percentage


        :param memory_utilization_percent: The memory_utilization_percent of this HostTopProcesses.
        :type: float
        """
        self._memory_utilization_percent = memory_utilization_percent

    @property
    def cpu_utilization_percent(self):
        """
        Gets the cpu_utilization_percent of this HostTopProcesses.
        CPU utilization percentage


        :return: The cpu_utilization_percent of this HostTopProcesses.
        :rtype: float
        """
        return self._cpu_utilization_percent

    @cpu_utilization_percent.setter
    def cpu_utilization_percent(self, cpu_utilization_percent):
        """
        Sets the cpu_utilization_percent of this HostTopProcesses.
        CPU utilization percentage


        :param cpu_utilization_percent: The cpu_utilization_percent of this HostTopProcesses.
        :type: float
        """
        self._cpu_utilization_percent = cpu_utilization_percent

    @property
    def cpu_usage_in_seconds(self):
        """
        Gets the cpu_usage_in_seconds of this HostTopProcesses.
        CPU usage in seconds


        :return: The cpu_usage_in_seconds of this HostTopProcesses.
        :rtype: float
        """
        return self._cpu_usage_in_seconds

    @cpu_usage_in_seconds.setter
    def cpu_usage_in_seconds(self, cpu_usage_in_seconds):
        """
        Sets the cpu_usage_in_seconds of this HostTopProcesses.
        CPU usage in seconds


        :param cpu_usage_in_seconds: The cpu_usage_in_seconds of this HostTopProcesses.
        :type: float
        """
        self._cpu_usage_in_seconds = cpu_usage_in_seconds

    @property
    def command(self):
        """
        Gets the command of this HostTopProcesses.
        Command line executed for the process


        :return: The command of this HostTopProcesses.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this HostTopProcesses.
        Command line executed for the process


        :param command: The command of this HostTopProcesses.
        :type: str
        """
        self._command = command

    @property
    def virtual_memory_in_mbs(self):
        """
        Gets the virtual_memory_in_mbs of this HostTopProcesses.
        Virtual memory in megabytes


        :return: The virtual_memory_in_mbs of this HostTopProcesses.
        :rtype: float
        """
        return self._virtual_memory_in_mbs

    @virtual_memory_in_mbs.setter
    def virtual_memory_in_mbs(self, virtual_memory_in_mbs):
        """
        Sets the virtual_memory_in_mbs of this HostTopProcesses.
        Virtual memory in megabytes


        :param virtual_memory_in_mbs: The virtual_memory_in_mbs of this HostTopProcesses.
        :type: float
        """
        self._virtual_memory_in_mbs = virtual_memory_in_mbs

    @property
    def physical_memory_in_mbs(self):
        """
        Gets the physical_memory_in_mbs of this HostTopProcesses.
        Physical memory in megabytes


        :return: The physical_memory_in_mbs of this HostTopProcesses.
        :rtype: float
        """
        return self._physical_memory_in_mbs

    @physical_memory_in_mbs.setter
    def physical_memory_in_mbs(self, physical_memory_in_mbs):
        """
        Sets the physical_memory_in_mbs of this HostTopProcesses.
        Physical memory in megabytes


        :param physical_memory_in_mbs: The physical_memory_in_mbs of this HostTopProcesses.
        :type: float
        """
        self._physical_memory_in_mbs = physical_memory_in_mbs

    @property
    def start_time(self):
        """
        Gets the start_time of this HostTopProcesses.
        Process Start Time
        Example: `\"2020-03-31T00:00:00.000Z\"`


        :return: The start_time of this HostTopProcesses.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this HostTopProcesses.
        Process Start Time
        Example: `\"2020-03-31T00:00:00.000Z\"`


        :param start_time: The start_time of this HostTopProcesses.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def total_processes(self):
        """
        Gets the total_processes of this HostTopProcesses.
        Number of processes running at the time of collection


        :return: The total_processes of this HostTopProcesses.
        :rtype: float
        """
        return self._total_processes

    @total_processes.setter
    def total_processes(self, total_processes):
        """
        Sets the total_processes of this HostTopProcesses.
        Number of processes running at the time of collection


        :param total_processes: The total_processes of this HostTopProcesses.
        :type: float
        """
        self._total_processes = total_processes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
