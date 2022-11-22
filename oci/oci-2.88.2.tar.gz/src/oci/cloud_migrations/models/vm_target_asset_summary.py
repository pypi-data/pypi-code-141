# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_asset_summary import TargetAssetSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmTargetAssetSummary(TargetAssetSummary):
    """
    Summary of the VM target asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmTargetAssetSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_migrations.models.VmTargetAssetSummary.type` attribute
        of this class is ``INSTANCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VmTargetAssetSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this VmTargetAssetSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VmTargetAssetSummary.
        :type lifecycle_state: str

        :param migration_plan_id:
            The value to assign to the migration_plan_id property of this VmTargetAssetSummary.
        :type migration_plan_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VmTargetAssetSummary.
        :type compartment_id: str

        :param created_resource_id:
            The value to assign to the created_resource_id property of this VmTargetAssetSummary.
        :type created_resource_id: str

        :param type:
            The value to assign to the type property of this VmTargetAssetSummary.
            Allowed values for this property are: "INSTANCE"
        :type type: str

        :param is_excluded_from_execution:
            The value to assign to the is_excluded_from_execution property of this VmTargetAssetSummary.
        :type is_excluded_from_execution: bool

        :param compatibility_messages:
            The value to assign to the compatibility_messages property of this VmTargetAssetSummary.
        :type compatibility_messages: list[oci.cloud_migrations.models.CompatibilityMessage]

        :param estimated_cost:
            The value to assign to the estimated_cost property of this VmTargetAssetSummary.
        :type estimated_cost: oci.cloud_migrations.models.CostEstimation

        :param time_created:
            The value to assign to the time_created property of this VmTargetAssetSummary.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this VmTargetAssetSummary.
        :type lifecycle_details: str

        :param time_updated:
            The value to assign to the time_updated property of this VmTargetAssetSummary.
        :type time_updated: datetime

        :param time_assessed:
            The value to assign to the time_assessed property of this VmTargetAssetSummary.
        :type time_assessed: datetime

        :param migration_asset:
            The value to assign to the migration_asset property of this VmTargetAssetSummary.
        :type migration_asset: oci.cloud_migrations.models.MigrationAssetSummary

        :param preferred_shape_type:
            The value to assign to the preferred_shape_type property of this VmTargetAssetSummary.
        :type preferred_shape_type: str

        :param block_volumes_performance:
            The value to assign to the block_volumes_performance property of this VmTargetAssetSummary.
        :type block_volumes_performance: int

        :param ms_license:
            The value to assign to the ms_license property of this VmTargetAssetSummary.
        :type ms_license: str

        :param user_spec:
            The value to assign to the user_spec property of this VmTargetAssetSummary.
        :type user_spec: oci.cloud_migrations.models.LaunchInstanceDetails

        :param recommended_spec:
            The value to assign to the recommended_spec property of this VmTargetAssetSummary.
        :type recommended_spec: oci.cloud_migrations.models.LaunchInstanceDetails

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'migration_plan_id': 'str',
            'compartment_id': 'str',
            'created_resource_id': 'str',
            'type': 'str',
            'is_excluded_from_execution': 'bool',
            'compatibility_messages': 'list[CompatibilityMessage]',
            'estimated_cost': 'CostEstimation',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'time_updated': 'datetime',
            'time_assessed': 'datetime',
            'migration_asset': 'MigrationAssetSummary',
            'preferred_shape_type': 'str',
            'block_volumes_performance': 'int',
            'ms_license': 'str',
            'user_spec': 'LaunchInstanceDetails',
            'recommended_spec': 'LaunchInstanceDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'migration_plan_id': 'migrationPlanId',
            'compartment_id': 'compartmentId',
            'created_resource_id': 'createdResourceId',
            'type': 'type',
            'is_excluded_from_execution': 'isExcludedFromExecution',
            'compatibility_messages': 'compatibilityMessages',
            'estimated_cost': 'estimatedCost',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'time_updated': 'timeUpdated',
            'time_assessed': 'timeAssessed',
            'migration_asset': 'migrationAsset',
            'preferred_shape_type': 'preferredShapeType',
            'block_volumes_performance': 'blockVolumesPerformance',
            'ms_license': 'msLicense',
            'user_spec': 'userSpec',
            'recommended_spec': 'recommendedSpec'
        }

        self._id = None
        self._display_name = None
        self._lifecycle_state = None
        self._migration_plan_id = None
        self._compartment_id = None
        self._created_resource_id = None
        self._type = None
        self._is_excluded_from_execution = None
        self._compatibility_messages = None
        self._estimated_cost = None
        self._time_created = None
        self._lifecycle_details = None
        self._time_updated = None
        self._time_assessed = None
        self._migration_asset = None
        self._preferred_shape_type = None
        self._block_volumes_performance = None
        self._ms_license = None
        self._user_spec = None
        self._recommended_spec = None
        self._type = 'INSTANCE'

    @property
    def preferred_shape_type(self):
        """
        **[Required]** Gets the preferred_shape_type of this VmTargetAssetSummary.
        The preferred VM shape type that you provide.


        :return: The preferred_shape_type of this VmTargetAssetSummary.
        :rtype: str
        """
        return self._preferred_shape_type

    @preferred_shape_type.setter
    def preferred_shape_type(self, preferred_shape_type):
        """
        Sets the preferred_shape_type of this VmTargetAssetSummary.
        The preferred VM shape type that you provide.


        :param preferred_shape_type: The preferred_shape_type of this VmTargetAssetSummary.
        :type: str
        """
        self._preferred_shape_type = preferred_shape_type

    @property
    def block_volumes_performance(self):
        """
        Gets the block_volumes_performance of this VmTargetAssetSummary.
        Performance of the block volumes.


        :return: The block_volumes_performance of this VmTargetAssetSummary.
        :rtype: int
        """
        return self._block_volumes_performance

    @block_volumes_performance.setter
    def block_volumes_performance(self, block_volumes_performance):
        """
        Sets the block_volumes_performance of this VmTargetAssetSummary.
        Performance of the block volumes.


        :param block_volumes_performance: The block_volumes_performance of this VmTargetAssetSummary.
        :type: int
        """
        self._block_volumes_performance = block_volumes_performance

    @property
    def ms_license(self):
        """
        Gets the ms_license of this VmTargetAssetSummary.
        Microsoft license for VM configuration.


        :return: The ms_license of this VmTargetAssetSummary.
        :rtype: str
        """
        return self._ms_license

    @ms_license.setter
    def ms_license(self, ms_license):
        """
        Sets the ms_license of this VmTargetAssetSummary.
        Microsoft license for VM configuration.


        :param ms_license: The ms_license of this VmTargetAssetSummary.
        :type: str
        """
        self._ms_license = ms_license

    @property
    def user_spec(self):
        """
        **[Required]** Gets the user_spec of this VmTargetAssetSummary.

        :return: The user_spec of this VmTargetAssetSummary.
        :rtype: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        return self._user_spec

    @user_spec.setter
    def user_spec(self, user_spec):
        """
        Sets the user_spec of this VmTargetAssetSummary.

        :param user_spec: The user_spec of this VmTargetAssetSummary.
        :type: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        self._user_spec = user_spec

    @property
    def recommended_spec(self):
        """
        **[Required]** Gets the recommended_spec of this VmTargetAssetSummary.

        :return: The recommended_spec of this VmTargetAssetSummary.
        :rtype: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        return self._recommended_spec

    @recommended_spec.setter
    def recommended_spec(self, recommended_spec):
        """
        Sets the recommended_spec of this VmTargetAssetSummary.

        :param recommended_spec: The recommended_spec of this VmTargetAssetSummary.
        :type: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        self._recommended_spec = recommended_spec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
