# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMigrationPlanDetails(object):
    """
    The information about the new migration plan.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMigrationPlanDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateMigrationPlanDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMigrationPlanDetails.
        :type compartment_id: str

        :param migration_id:
            The value to assign to the migration_id property of this CreateMigrationPlanDetails.
        :type migration_id: str

        :param source_migration_plan_id:
            The value to assign to the source_migration_plan_id property of this CreateMigrationPlanDetails.
        :type source_migration_plan_id: str

        :param strategies:
            The value to assign to the strategies property of this CreateMigrationPlanDetails.
        :type strategies: list[oci.cloud_migrations.models.ResourceAssessmentStrategy]

        :param target_environments:
            The value to assign to the target_environments property of this CreateMigrationPlanDetails.
        :type target_environments: list[oci.cloud_migrations.models.TargetEnvironment]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMigrationPlanDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMigrationPlanDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'migration_id': 'str',
            'source_migration_plan_id': 'str',
            'strategies': 'list[ResourceAssessmentStrategy]',
            'target_environments': 'list[TargetEnvironment]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'migration_id': 'migrationId',
            'source_migration_plan_id': 'sourceMigrationPlanId',
            'strategies': 'strategies',
            'target_environments': 'targetEnvironments',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._migration_id = None
        self._source_migration_plan_id = None
        self._strategies = None
        self._target_environments = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateMigrationPlanDetails.
        Migration plan identifier


        :return: The display_name of this CreateMigrationPlanDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMigrationPlanDetails.
        Migration plan identifier


        :param display_name: The display_name of this CreateMigrationPlanDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMigrationPlanDetails.
        Compartment identifier


        :return: The compartment_id of this CreateMigrationPlanDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMigrationPlanDetails.
        Compartment identifier


        :param compartment_id: The compartment_id of this CreateMigrationPlanDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def migration_id(self):
        """
        **[Required]** Gets the migration_id of this CreateMigrationPlanDetails.
        The OCID of the associated migration.


        :return: The migration_id of this CreateMigrationPlanDetails.
        :rtype: str
        """
        return self._migration_id

    @migration_id.setter
    def migration_id(self, migration_id):
        """
        Sets the migration_id of this CreateMigrationPlanDetails.
        The OCID of the associated migration.


        :param migration_id: The migration_id of this CreateMigrationPlanDetails.
        :type: str
        """
        self._migration_id = migration_id

    @property
    def source_migration_plan_id(self):
        """
        Gets the source_migration_plan_id of this CreateMigrationPlanDetails.
        Source migraiton plan ID to be cloned.


        :return: The source_migration_plan_id of this CreateMigrationPlanDetails.
        :rtype: str
        """
        return self._source_migration_plan_id

    @source_migration_plan_id.setter
    def source_migration_plan_id(self, source_migration_plan_id):
        """
        Sets the source_migration_plan_id of this CreateMigrationPlanDetails.
        Source migraiton plan ID to be cloned.


        :param source_migration_plan_id: The source_migration_plan_id of this CreateMigrationPlanDetails.
        :type: str
        """
        self._source_migration_plan_id = source_migration_plan_id

    @property
    def strategies(self):
        """
        Gets the strategies of this CreateMigrationPlanDetails.
        List of strategies for the resources to be migrated.


        :return: The strategies of this CreateMigrationPlanDetails.
        :rtype: list[oci.cloud_migrations.models.ResourceAssessmentStrategy]
        """
        return self._strategies

    @strategies.setter
    def strategies(self, strategies):
        """
        Sets the strategies of this CreateMigrationPlanDetails.
        List of strategies for the resources to be migrated.


        :param strategies: The strategies of this CreateMigrationPlanDetails.
        :type: list[oci.cloud_migrations.models.ResourceAssessmentStrategy]
        """
        self._strategies = strategies

    @property
    def target_environments(self):
        """
        Gets the target_environments of this CreateMigrationPlanDetails.
        List of target environments.


        :return: The target_environments of this CreateMigrationPlanDetails.
        :rtype: list[oci.cloud_migrations.models.TargetEnvironment]
        """
        return self._target_environments

    @target_environments.setter
    def target_environments(self, target_environments):
        """
        Sets the target_environments of this CreateMigrationPlanDetails.
        List of target environments.


        :param target_environments: The target_environments of this CreateMigrationPlanDetails.
        :type: list[oci.cloud_migrations.models.TargetEnvironment]
        """
        self._target_environments = target_environments

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMigrationPlanDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMigrationPlanDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMigrationPlanDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMigrationPlanDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMigrationPlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMigrationPlanDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMigrationPlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMigrationPlanDetails.
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
