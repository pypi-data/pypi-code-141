# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateJobRunDetails(object):
    """
    Parameters needed to create a new job run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateJobRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param project_id:
            The value to assign to the project_id property of this CreateJobRunDetails.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateJobRunDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateJobRunDetails.
        :type display_name: str

        :param job_id:
            The value to assign to the job_id property of this CreateJobRunDetails.
        :type job_id: str

        :param job_configuration_override_details:
            The value to assign to the job_configuration_override_details property of this CreateJobRunDetails.
        :type job_configuration_override_details: oci.data_science.models.JobConfigurationDetails

        :param job_log_configuration_override_details:
            The value to assign to the job_log_configuration_override_details property of this CreateJobRunDetails.
        :type job_log_configuration_override_details: oci.data_science.models.JobLogConfigurationDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateJobRunDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateJobRunDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'project_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'job_id': 'str',
            'job_configuration_override_details': 'JobConfigurationDetails',
            'job_log_configuration_override_details': 'JobLogConfigurationDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'job_id': 'jobId',
            'job_configuration_override_details': 'jobConfigurationOverrideDetails',
            'job_log_configuration_override_details': 'jobLogConfigurationOverrideDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._project_id = None
        self._compartment_id = None
        self._display_name = None
        self._job_id = None
        self._job_configuration_override_details = None
        self._job_log_configuration_override_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateJobRunDetails.
        The `OCID`__ of the project to associate the job with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this CreateJobRunDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateJobRunDetails.
        The `OCID`__ of the project to associate the job with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this CreateJobRunDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateJobRunDetails.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateJobRunDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateJobRunDetails.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateJobRunDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateJobRunDetails.
        A user-friendly display name for the resource.


        :return: The display_name of this CreateJobRunDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateJobRunDetails.
        A user-friendly display name for the resource.


        :param display_name: The display_name of this CreateJobRunDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def job_id(self):
        """
        **[Required]** Gets the job_id of this CreateJobRunDetails.
        The `OCID`__ of the job to create a run for.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The job_id of this CreateJobRunDetails.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this CreateJobRunDetails.
        The `OCID`__ of the job to create a run for.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param job_id: The job_id of this CreateJobRunDetails.
        :type: str
        """
        self._job_id = job_id

    @property
    def job_configuration_override_details(self):
        """
        Gets the job_configuration_override_details of this CreateJobRunDetails.

        :return: The job_configuration_override_details of this CreateJobRunDetails.
        :rtype: oci.data_science.models.JobConfigurationDetails
        """
        return self._job_configuration_override_details

    @job_configuration_override_details.setter
    def job_configuration_override_details(self, job_configuration_override_details):
        """
        Sets the job_configuration_override_details of this CreateJobRunDetails.

        :param job_configuration_override_details: The job_configuration_override_details of this CreateJobRunDetails.
        :type: oci.data_science.models.JobConfigurationDetails
        """
        self._job_configuration_override_details = job_configuration_override_details

    @property
    def job_log_configuration_override_details(self):
        """
        Gets the job_log_configuration_override_details of this CreateJobRunDetails.

        :return: The job_log_configuration_override_details of this CreateJobRunDetails.
        :rtype: oci.data_science.models.JobLogConfigurationDetails
        """
        return self._job_log_configuration_override_details

    @job_log_configuration_override_details.setter
    def job_log_configuration_override_details(self, job_log_configuration_override_details):
        """
        Sets the job_log_configuration_override_details of this CreateJobRunDetails.

        :param job_log_configuration_override_details: The job_log_configuration_override_details of this CreateJobRunDetails.
        :type: oci.data_science.models.JobLogConfigurationDetails
        """
        self._job_log_configuration_override_details = job_log_configuration_override_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateJobRunDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateJobRunDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateJobRunDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateJobRunDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateJobRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateJobRunDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateJobRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateJobRunDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
