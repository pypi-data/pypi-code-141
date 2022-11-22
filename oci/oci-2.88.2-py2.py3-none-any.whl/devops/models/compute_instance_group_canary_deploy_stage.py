# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage import DeployStage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupCanaryDeployStage(DeployStage):
    """
    Specifies the Instance Group Canary deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupCanaryDeployStage object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ComputeInstanceGroupCanaryDeployStage.deploy_stage_type` attribute
        of this class is ``COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ComputeInstanceGroupCanaryDeployStage.
        :type id: str

        :param description:
            The value to assign to the description property of this ComputeInstanceGroupCanaryDeployStage.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this ComputeInstanceGroupCanaryDeployStage.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this ComputeInstanceGroupCanaryDeployStage.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this ComputeInstanceGroupCanaryDeployStage.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ComputeInstanceGroupCanaryDeployStage.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this ComputeInstanceGroupCanaryDeployStage.
            Allowed values for this property are: "WAIT", "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL", "OKE_BLUE_GREEN_DEPLOYMENT", "OKE_BLUE_GREEN_TRAFFIC_SHIFT", "OKE_CANARY_DEPLOYMENT", "OKE_CANARY_TRAFFIC_SHIFT", "OKE_CANARY_APPROVAL", "OKE_DEPLOYMENT", "DEPLOY_FUNCTION", "INVOKE_FUNCTION", "LOAD_BALANCER_TRAFFIC_SHIFT", "MANUAL_APPROVAL", "OKE_HELM_CHART_DEPLOYMENT"
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this ComputeInstanceGroupCanaryDeployStage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ComputeInstanceGroupCanaryDeployStage.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ComputeInstanceGroupCanaryDeployStage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ComputeInstanceGroupCanaryDeployStage.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this ComputeInstanceGroupCanaryDeployStage.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ComputeInstanceGroupCanaryDeployStage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ComputeInstanceGroupCanaryDeployStage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ComputeInstanceGroupCanaryDeployStage.
        :type system_tags: dict(str, dict(str, object))

        :param compute_instance_group_deploy_environment_id:
            The value to assign to the compute_instance_group_deploy_environment_id property of this ComputeInstanceGroupCanaryDeployStage.
        :type compute_instance_group_deploy_environment_id: str

        :param deployment_spec_deploy_artifact_id:
            The value to assign to the deployment_spec_deploy_artifact_id property of this ComputeInstanceGroupCanaryDeployStage.
        :type deployment_spec_deploy_artifact_id: str

        :param deploy_artifact_ids:
            The value to assign to the deploy_artifact_ids property of this ComputeInstanceGroupCanaryDeployStage.
        :type deploy_artifact_ids: list[str]

        :param rollout_policy:
            The value to assign to the rollout_policy property of this ComputeInstanceGroupCanaryDeployStage.
        :type rollout_policy: oci.devops.models.ComputeInstanceGroupRolloutPolicy

        :param test_load_balancer_config:
            The value to assign to the test_load_balancer_config property of this ComputeInstanceGroupCanaryDeployStage.
        :type test_load_balancer_config: oci.devops.models.LoadBalancerConfig

        :param production_load_balancer_config:
            The value to assign to the production_load_balancer_config property of this ComputeInstanceGroupCanaryDeployStage.
        :type production_load_balancer_config: oci.devops.models.LoadBalancerConfig

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'deploy_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'compute_instance_group_deploy_environment_id': 'str',
            'deployment_spec_deploy_artifact_id': 'str',
            'deploy_artifact_ids': 'list[str]',
            'rollout_policy': 'ComputeInstanceGroupRolloutPolicy',
            'test_load_balancer_config': 'LoadBalancerConfig',
            'production_load_balancer_config': 'LoadBalancerConfig'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'deploy_stage_type': 'deployStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'compute_instance_group_deploy_environment_id': 'computeInstanceGroupDeployEnvironmentId',
            'deployment_spec_deploy_artifact_id': 'deploymentSpecDeployArtifactId',
            'deploy_artifact_ids': 'deployArtifactIds',
            'rollout_policy': 'rolloutPolicy',
            'test_load_balancer_config': 'testLoadBalancerConfig',
            'production_load_balancer_config': 'productionLoadBalancerConfig'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._deploy_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._compute_instance_group_deploy_environment_id = None
        self._deployment_spec_deploy_artifact_id = None
        self._deploy_artifact_ids = None
        self._rollout_policy = None
        self._test_load_balancer_config = None
        self._production_load_balancer_config = None
        self._deploy_stage_type = 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT'

    @property
    def compute_instance_group_deploy_environment_id(self):
        """
        **[Required]** Gets the compute_instance_group_deploy_environment_id of this ComputeInstanceGroupCanaryDeployStage.
        A compute instance group environment OCID for Canary deployment.


        :return: The compute_instance_group_deploy_environment_id of this ComputeInstanceGroupCanaryDeployStage.
        :rtype: str
        """
        return self._compute_instance_group_deploy_environment_id

    @compute_instance_group_deploy_environment_id.setter
    def compute_instance_group_deploy_environment_id(self, compute_instance_group_deploy_environment_id):
        """
        Sets the compute_instance_group_deploy_environment_id of this ComputeInstanceGroupCanaryDeployStage.
        A compute instance group environment OCID for Canary deployment.


        :param compute_instance_group_deploy_environment_id: The compute_instance_group_deploy_environment_id of this ComputeInstanceGroupCanaryDeployStage.
        :type: str
        """
        self._compute_instance_group_deploy_environment_id = compute_instance_group_deploy_environment_id

    @property
    def deployment_spec_deploy_artifact_id(self):
        """
        **[Required]** Gets the deployment_spec_deploy_artifact_id of this ComputeInstanceGroupCanaryDeployStage.
        The OCID of the artifact that contains the deployment specification.


        :return: The deployment_spec_deploy_artifact_id of this ComputeInstanceGroupCanaryDeployStage.
        :rtype: str
        """
        return self._deployment_spec_deploy_artifact_id

    @deployment_spec_deploy_artifact_id.setter
    def deployment_spec_deploy_artifact_id(self, deployment_spec_deploy_artifact_id):
        """
        Sets the deployment_spec_deploy_artifact_id of this ComputeInstanceGroupCanaryDeployStage.
        The OCID of the artifact that contains the deployment specification.


        :param deployment_spec_deploy_artifact_id: The deployment_spec_deploy_artifact_id of this ComputeInstanceGroupCanaryDeployStage.
        :type: str
        """
        self._deployment_spec_deploy_artifact_id = deployment_spec_deploy_artifact_id

    @property
    def deploy_artifact_ids(self):
        """
        Gets the deploy_artifact_ids of this ComputeInstanceGroupCanaryDeployStage.
        The list of file artifact OCIDs to deploy.


        :return: The deploy_artifact_ids of this ComputeInstanceGroupCanaryDeployStage.
        :rtype: list[str]
        """
        return self._deploy_artifact_ids

    @deploy_artifact_ids.setter
    def deploy_artifact_ids(self, deploy_artifact_ids):
        """
        Sets the deploy_artifact_ids of this ComputeInstanceGroupCanaryDeployStage.
        The list of file artifact OCIDs to deploy.


        :param deploy_artifact_ids: The deploy_artifact_ids of this ComputeInstanceGroupCanaryDeployStage.
        :type: list[str]
        """
        self._deploy_artifact_ids = deploy_artifact_ids

    @property
    def rollout_policy(self):
        """
        **[Required]** Gets the rollout_policy of this ComputeInstanceGroupCanaryDeployStage.

        :return: The rollout_policy of this ComputeInstanceGroupCanaryDeployStage.
        :rtype: oci.devops.models.ComputeInstanceGroupRolloutPolicy
        """
        return self._rollout_policy

    @rollout_policy.setter
    def rollout_policy(self, rollout_policy):
        """
        Sets the rollout_policy of this ComputeInstanceGroupCanaryDeployStage.

        :param rollout_policy: The rollout_policy of this ComputeInstanceGroupCanaryDeployStage.
        :type: oci.devops.models.ComputeInstanceGroupRolloutPolicy
        """
        self._rollout_policy = rollout_policy

    @property
    def test_load_balancer_config(self):
        """
        Gets the test_load_balancer_config of this ComputeInstanceGroupCanaryDeployStage.

        :return: The test_load_balancer_config of this ComputeInstanceGroupCanaryDeployStage.
        :rtype: oci.devops.models.LoadBalancerConfig
        """
        return self._test_load_balancer_config

    @test_load_balancer_config.setter
    def test_load_balancer_config(self, test_load_balancer_config):
        """
        Sets the test_load_balancer_config of this ComputeInstanceGroupCanaryDeployStage.

        :param test_load_balancer_config: The test_load_balancer_config of this ComputeInstanceGroupCanaryDeployStage.
        :type: oci.devops.models.LoadBalancerConfig
        """
        self._test_load_balancer_config = test_load_balancer_config

    @property
    def production_load_balancer_config(self):
        """
        **[Required]** Gets the production_load_balancer_config of this ComputeInstanceGroupCanaryDeployStage.

        :return: The production_load_balancer_config of this ComputeInstanceGroupCanaryDeployStage.
        :rtype: oci.devops.models.LoadBalancerConfig
        """
        return self._production_load_balancer_config

    @production_load_balancer_config.setter
    def production_load_balancer_config(self, production_load_balancer_config):
        """
        Sets the production_load_balancer_config of this ComputeInstanceGroupCanaryDeployStage.

        :param production_load_balancer_config: The production_load_balancer_config of this ComputeInstanceGroupCanaryDeployStage.
        :type: oci.devops.models.LoadBalancerConfig
        """
        self._production_load_balancer_config = production_load_balancer_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
