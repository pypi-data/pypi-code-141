# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateJobDetails(object):
    """
    The details required to create a job.
    """

    #: A constant which can be used with the database_sub_type property of a CreateJobDetails.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a CreateJobDetails.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a CreateJobDetails.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the database_sub_type property of a CreateJobDetails.
    #: This constant has a value of "ACD"
    DATABASE_SUB_TYPE_ACD = "ACD"

    #: A constant which can be used with the database_sub_type property of a CreateJobDetails.
    #: This constant has a value of "ADB"
    DATABASE_SUB_TYPE_ADB = "ADB"

    #: A constant which can be used with the job_type property of a CreateJobDetails.
    #: This constant has a value of "SQL"
    JOB_TYPE_SQL = "SQL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateJobDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.CreateSqlJobDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateJobDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateJobDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateJobDetails.
        :type compartment_id: str

        :param managed_database_group_id:
            The value to assign to the managed_database_group_id property of this CreateJobDetails.
        :type managed_database_group_id: str

        :param managed_database_id:
            The value to assign to the managed_database_id property of this CreateJobDetails.
        :type managed_database_id: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this CreateJobDetails.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB"
        :type database_sub_type: str

        :param schedule_type:
            The value to assign to the schedule_type property of this CreateJobDetails.
        :type schedule_type: str

        :param job_type:
            The value to assign to the job_type property of this CreateJobDetails.
            Allowed values for this property are: "SQL"
        :type job_type: str

        :param timeout:
            The value to assign to the timeout property of this CreateJobDetails.
        :type timeout: str

        :param result_location:
            The value to assign to the result_location property of this CreateJobDetails.
        :type result_location: oci.database_management.models.JobExecutionResultLocation

        :param schedule_details:
            The value to assign to the schedule_details property of this CreateJobDetails.
        :type schedule_details: oci.database_management.models.JobScheduleDetails

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'managed_database_group_id': 'str',
            'managed_database_id': 'str',
            'database_sub_type': 'str',
            'schedule_type': 'str',
            'job_type': 'str',
            'timeout': 'str',
            'result_location': 'JobExecutionResultLocation',
            'schedule_details': 'JobScheduleDetails'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'managed_database_group_id': 'managedDatabaseGroupId',
            'managed_database_id': 'managedDatabaseId',
            'database_sub_type': 'databaseSubType',
            'schedule_type': 'scheduleType',
            'job_type': 'jobType',
            'timeout': 'timeout',
            'result_location': 'resultLocation',
            'schedule_details': 'scheduleDetails'
        }

        self._name = None
        self._description = None
        self._compartment_id = None
        self._managed_database_group_id = None
        self._managed_database_id = None
        self._database_sub_type = None
        self._schedule_type = None
        self._job_type = None
        self._timeout = None
        self._result_location = None
        self._schedule_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['jobType']

        if type == 'SQL':
            return 'CreateSqlJobDetails'
        else:
            return 'CreateJobDetails'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateJobDetails.
        The name of the job. Valid characters are uppercase or lowercase letters,
        numbers, and \"_\". The name of the job cannot be modified. It must be unique
        in the compartment and must begin with an alphabetic character.


        :return: The name of this CreateJobDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateJobDetails.
        The name of the job. Valid characters are uppercase or lowercase letters,
        numbers, and \"_\". The name of the job cannot be modified. It must be unique
        in the compartment and must begin with an alphabetic character.


        :param name: The name of this CreateJobDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateJobDetails.
        The description of the job.


        :return: The description of this CreateJobDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateJobDetails.
        The description of the job.


        :param description: The description of this CreateJobDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateJobDetails.
        The `OCID`__ of the compartment in which the job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateJobDetails.
        The `OCID`__ of the compartment in which the job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def managed_database_group_id(self):
        """
        Gets the managed_database_group_id of this CreateJobDetails.
        The `OCID`__ of the Managed Database Group where the job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_group_id of this CreateJobDetails.
        :rtype: str
        """
        return self._managed_database_group_id

    @managed_database_group_id.setter
    def managed_database_group_id(self, managed_database_group_id):
        """
        Sets the managed_database_group_id of this CreateJobDetails.
        The `OCID`__ of the Managed Database Group where the job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_group_id: The managed_database_group_id of this CreateJobDetails.
        :type: str
        """
        self._managed_database_group_id = managed_database_group_id

    @property
    def managed_database_id(self):
        """
        Gets the managed_database_id of this CreateJobDetails.
        The `OCID`__ of the Managed Database where the job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_id of this CreateJobDetails.
        :rtype: str
        """
        return self._managed_database_id

    @managed_database_id.setter
    def managed_database_id(self, managed_database_id):
        """
        Sets the managed_database_id of this CreateJobDetails.
        The `OCID`__ of the Managed Database where the job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_id: The managed_database_id of this CreateJobDetails.
        :type: str
        """
        self._managed_database_id = managed_database_id

    @property
    def database_sub_type(self):
        """
        Gets the database_sub_type of this CreateJobDetails.
        The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB"


        :return: The database_sub_type of this CreateJobDetails.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this CreateJobDetails.
        The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.


        :param database_sub_type: The database_sub_type of this CreateJobDetails.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB", "ACD", "ADB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            raise ValueError(
                "Invalid value for `database_sub_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._database_sub_type = database_sub_type

    @property
    def schedule_type(self):
        """
        **[Required]** Gets the schedule_type of this CreateJobDetails.
        The schedule type of the job.


        :return: The schedule_type of this CreateJobDetails.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this CreateJobDetails.
        The schedule type of the job.


        :param schedule_type: The schedule_type of this CreateJobDetails.
        :type: str
        """
        self._schedule_type = schedule_type

    @property
    def job_type(self):
        """
        **[Required]** Gets the job_type of this CreateJobDetails.
        The type of job.

        Allowed values for this property are: "SQL"


        :return: The job_type of this CreateJobDetails.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this CreateJobDetails.
        The type of job.


        :param job_type: The job_type of this CreateJobDetails.
        :type: str
        """
        allowed_values = ["SQL"]
        if not value_allowed_none_or_none_sentinel(job_type, allowed_values):
            raise ValueError(
                "Invalid value for `job_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._job_type = job_type

    @property
    def timeout(self):
        """
        Gets the timeout of this CreateJobDetails.
        The job timeout duration, which is expressed like \"1h 10m 15s\".


        :return: The timeout of this CreateJobDetails.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this CreateJobDetails.
        The job timeout duration, which is expressed like \"1h 10m 15s\".


        :param timeout: The timeout of this CreateJobDetails.
        :type: str
        """
        self._timeout = timeout

    @property
    def result_location(self):
        """
        Gets the result_location of this CreateJobDetails.

        :return: The result_location of this CreateJobDetails.
        :rtype: oci.database_management.models.JobExecutionResultLocation
        """
        return self._result_location

    @result_location.setter
    def result_location(self, result_location):
        """
        Sets the result_location of this CreateJobDetails.

        :param result_location: The result_location of this CreateJobDetails.
        :type: oci.database_management.models.JobExecutionResultLocation
        """
        self._result_location = result_location

    @property
    def schedule_details(self):
        """
        Gets the schedule_details of this CreateJobDetails.

        :return: The schedule_details of this CreateJobDetails.
        :rtype: oci.database_management.models.JobScheduleDetails
        """
        return self._schedule_details

    @schedule_details.setter
    def schedule_details(self, schedule_details):
        """
        Sets the schedule_details of this CreateJobDetails.

        :param schedule_details: The schedule_details of this CreateJobDetails.
        :type: oci.database_management.models.JobScheduleDetails
        """
        self._schedule_details = schedule_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
