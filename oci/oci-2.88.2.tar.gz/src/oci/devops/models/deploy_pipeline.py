# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployPipeline(object):
    """
    A set of stages whose predecessor relation forms a directed acyclic graph.
    """

    #: A constant which can be used with the lifecycle_state property of a DeployPipeline.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DeployPipeline.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DeployPipeline.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DeployPipeline.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DeployPipeline.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DeployPipeline.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DeployPipeline.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DeployPipeline object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DeployPipeline.
        :type id: str

        :param description:
            The value to assign to the description property of this DeployPipeline.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this DeployPipeline.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this DeployPipeline.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DeployPipeline.
        :type compartment_id: str

        :param deploy_pipeline_artifacts:
            The value to assign to the deploy_pipeline_artifacts property of this DeployPipeline.
        :type deploy_pipeline_artifacts: oci.devops.models.DeployPipelineArtifactCollection

        :param deploy_pipeline_environments:
            The value to assign to the deploy_pipeline_environments property of this DeployPipeline.
        :type deploy_pipeline_environments: oci.devops.models.DeployPipelineEnvironmentCollection

        :param time_created:
            The value to assign to the time_created property of this DeployPipeline.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DeployPipeline.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DeployPipeline.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DeployPipeline.
        :type lifecycle_details: str

        :param deploy_pipeline_parameters:
            The value to assign to the deploy_pipeline_parameters property of this DeployPipeline.
        :type deploy_pipeline_parameters: oci.devops.models.DeployPipelineParameterCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DeployPipeline.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DeployPipeline.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DeployPipeline.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'deploy_pipeline_artifacts': 'DeployPipelineArtifactCollection',
            'deploy_pipeline_environments': 'DeployPipelineEnvironmentCollection',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deploy_pipeline_parameters': 'DeployPipelineParameterCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'deploy_pipeline_artifacts': 'deployPipelineArtifacts',
            'deploy_pipeline_environments': 'deployPipelineEnvironments',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deploy_pipeline_parameters': 'deployPipelineParameters',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._compartment_id = None
        self._deploy_pipeline_artifacts = None
        self._deploy_pipeline_environments = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deploy_pipeline_parameters = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DeployPipeline.
        Unique identifier that is immutable on creation.


        :return: The id of this DeployPipeline.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeployPipeline.
        Unique identifier that is immutable on creation.


        :param id: The id of this DeployPipeline.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this DeployPipeline.
        Optional description about the deployment pipeline.


        :return: The description of this DeployPipeline.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeployPipeline.
        Optional description about the deployment pipeline.


        :param description: The description of this DeployPipeline.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this DeployPipeline.
        Deployment pipeline display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this DeployPipeline.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeployPipeline.
        Deployment pipeline display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this DeployPipeline.
        :type: str
        """
        self._display_name = display_name

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this DeployPipeline.
        The OCID of a project.


        :return: The project_id of this DeployPipeline.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this DeployPipeline.
        The OCID of a project.


        :param project_id: The project_id of this DeployPipeline.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DeployPipeline.
        The OCID of the compartment where the pipeline is created.


        :return: The compartment_id of this DeployPipeline.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DeployPipeline.
        The OCID of the compartment where the pipeline is created.


        :param compartment_id: The compartment_id of this DeployPipeline.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def deploy_pipeline_artifacts(self):
        """
        Gets the deploy_pipeline_artifacts of this DeployPipeline.

        :return: The deploy_pipeline_artifacts of this DeployPipeline.
        :rtype: oci.devops.models.DeployPipelineArtifactCollection
        """
        return self._deploy_pipeline_artifacts

    @deploy_pipeline_artifacts.setter
    def deploy_pipeline_artifacts(self, deploy_pipeline_artifacts):
        """
        Sets the deploy_pipeline_artifacts of this DeployPipeline.

        :param deploy_pipeline_artifacts: The deploy_pipeline_artifacts of this DeployPipeline.
        :type: oci.devops.models.DeployPipelineArtifactCollection
        """
        self._deploy_pipeline_artifacts = deploy_pipeline_artifacts

    @property
    def deploy_pipeline_environments(self):
        """
        Gets the deploy_pipeline_environments of this DeployPipeline.

        :return: The deploy_pipeline_environments of this DeployPipeline.
        :rtype: oci.devops.models.DeployPipelineEnvironmentCollection
        """
        return self._deploy_pipeline_environments

    @deploy_pipeline_environments.setter
    def deploy_pipeline_environments(self, deploy_pipeline_environments):
        """
        Sets the deploy_pipeline_environments of this DeployPipeline.

        :param deploy_pipeline_environments: The deploy_pipeline_environments of this DeployPipeline.
        :type: oci.devops.models.DeployPipelineEnvironmentCollection
        """
        self._deploy_pipeline_environments = deploy_pipeline_environments

    @property
    def time_created(self):
        """
        Gets the time_created of this DeployPipeline.
        Time the deployment pipeline was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this DeployPipeline.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DeployPipeline.
        Time the deployment pipeline was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this DeployPipeline.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DeployPipeline.
        Time the deployment pipeline was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this DeployPipeline.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DeployPipeline.
        Time the deployment pipeline was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this DeployPipeline.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DeployPipeline.
        The current state of the deployment pipeline.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DeployPipeline.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DeployPipeline.
        The current state of the deployment pipeline.


        :param lifecycle_state: The lifecycle_state of this DeployPipeline.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DeployPipeline.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DeployPipeline.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DeployPipeline.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DeployPipeline.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def deploy_pipeline_parameters(self):
        """
        **[Required]** Gets the deploy_pipeline_parameters of this DeployPipeline.

        :return: The deploy_pipeline_parameters of this DeployPipeline.
        :rtype: oci.devops.models.DeployPipelineParameterCollection
        """
        return self._deploy_pipeline_parameters

    @deploy_pipeline_parameters.setter
    def deploy_pipeline_parameters(self, deploy_pipeline_parameters):
        """
        Sets the deploy_pipeline_parameters of this DeployPipeline.

        :param deploy_pipeline_parameters: The deploy_pipeline_parameters of this DeployPipeline.
        :type: oci.devops.models.DeployPipelineParameterCollection
        """
        self._deploy_pipeline_parameters = deploy_pipeline_parameters

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DeployPipeline.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DeployPipeline.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DeployPipeline.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DeployPipeline.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DeployPipeline.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DeployPipeline.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DeployPipeline.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DeployPipeline.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DeployPipeline.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DeployPipeline.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DeployPipeline.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DeployPipeline.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
