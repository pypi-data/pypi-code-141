# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMigrationAssetDetails(object):
    """
    Details of the new migration asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMigrationAssetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateMigrationAssetDetails.
        :type display_name: str

        :param inventory_asset_id:
            The value to assign to the inventory_asset_id property of this CreateMigrationAssetDetails.
        :type inventory_asset_id: str

        :param migration_id:
            The value to assign to the migration_id property of this CreateMigrationAssetDetails.
        :type migration_id: str

        :param replication_schedule_id:
            The value to assign to the replication_schedule_id property of this CreateMigrationAssetDetails.
        :type replication_schedule_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateMigrationAssetDetails.
        :type availability_domain: str

        :param replication_compartment_id:
            The value to assign to the replication_compartment_id property of this CreateMigrationAssetDetails.
        :type replication_compartment_id: str

        :param snap_shot_bucket_name:
            The value to assign to the snap_shot_bucket_name property of this CreateMigrationAssetDetails.
        :type snap_shot_bucket_name: str

        :param depends_on:
            The value to assign to the depends_on property of this CreateMigrationAssetDetails.
        :type depends_on: list[str]

        """
        self.swagger_types = {
            'display_name': 'str',
            'inventory_asset_id': 'str',
            'migration_id': 'str',
            'replication_schedule_id': 'str',
            'availability_domain': 'str',
            'replication_compartment_id': 'str',
            'snap_shot_bucket_name': 'str',
            'depends_on': 'list[str]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'inventory_asset_id': 'inventoryAssetId',
            'migration_id': 'migrationId',
            'replication_schedule_id': 'replicationScheduleId',
            'availability_domain': 'availabilityDomain',
            'replication_compartment_id': 'replicationCompartmentId',
            'snap_shot_bucket_name': 'snapShotBucketName',
            'depends_on': 'dependsOn'
        }

        self._display_name = None
        self._inventory_asset_id = None
        self._migration_id = None
        self._replication_schedule_id = None
        self._availability_domain = None
        self._replication_compartment_id = None
        self._snap_shot_bucket_name = None
        self._depends_on = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMigrationAssetDetails.
        A user-friendly name. If empty, then source asset name will be used. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateMigrationAssetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMigrationAssetDetails.
        A user-friendly name. If empty, then source asset name will be used. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateMigrationAssetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def inventory_asset_id(self):
        """
        **[Required]** Gets the inventory_asset_id of this CreateMigrationAssetDetails.
        OCID of an asset for an inventory.


        :return: The inventory_asset_id of this CreateMigrationAssetDetails.
        :rtype: str
        """
        return self._inventory_asset_id

    @inventory_asset_id.setter
    def inventory_asset_id(self, inventory_asset_id):
        """
        Sets the inventory_asset_id of this CreateMigrationAssetDetails.
        OCID of an asset for an inventory.


        :param inventory_asset_id: The inventory_asset_id of this CreateMigrationAssetDetails.
        :type: str
        """
        self._inventory_asset_id = inventory_asset_id

    @property
    def migration_id(self):
        """
        **[Required]** Gets the migration_id of this CreateMigrationAssetDetails.
        OCID of the associated migration.


        :return: The migration_id of this CreateMigrationAssetDetails.
        :rtype: str
        """
        return self._migration_id

    @migration_id.setter
    def migration_id(self, migration_id):
        """
        Sets the migration_id of this CreateMigrationAssetDetails.
        OCID of the associated migration.


        :param migration_id: The migration_id of this CreateMigrationAssetDetails.
        :type: str
        """
        self._migration_id = migration_id

    @property
    def replication_schedule_id(self):
        """
        Gets the replication_schedule_id of this CreateMigrationAssetDetails.
        Replication schedule identifier


        :return: The replication_schedule_id of this CreateMigrationAssetDetails.
        :rtype: str
        """
        return self._replication_schedule_id

    @replication_schedule_id.setter
    def replication_schedule_id(self, replication_schedule_id):
        """
        Sets the replication_schedule_id of this CreateMigrationAssetDetails.
        Replication schedule identifier


        :param replication_schedule_id: The replication_schedule_id of this CreateMigrationAssetDetails.
        :type: str
        """
        self._replication_schedule_id = replication_schedule_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateMigrationAssetDetails.
        Availability domain


        :return: The availability_domain of this CreateMigrationAssetDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateMigrationAssetDetails.
        Availability domain


        :param availability_domain: The availability_domain of this CreateMigrationAssetDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def replication_compartment_id(self):
        """
        **[Required]** Gets the replication_compartment_id of this CreateMigrationAssetDetails.
        Replication compartment identifier


        :return: The replication_compartment_id of this CreateMigrationAssetDetails.
        :rtype: str
        """
        return self._replication_compartment_id

    @replication_compartment_id.setter
    def replication_compartment_id(self, replication_compartment_id):
        """
        Sets the replication_compartment_id of this CreateMigrationAssetDetails.
        Replication compartment identifier


        :param replication_compartment_id: The replication_compartment_id of this CreateMigrationAssetDetails.
        :type: str
        """
        self._replication_compartment_id = replication_compartment_id

    @property
    def snap_shot_bucket_name(self):
        """
        **[Required]** Gets the snap_shot_bucket_name of this CreateMigrationAssetDetails.
        Name of snapshot bucket


        :return: The snap_shot_bucket_name of this CreateMigrationAssetDetails.
        :rtype: str
        """
        return self._snap_shot_bucket_name

    @snap_shot_bucket_name.setter
    def snap_shot_bucket_name(self, snap_shot_bucket_name):
        """
        Sets the snap_shot_bucket_name of this CreateMigrationAssetDetails.
        Name of snapshot bucket


        :param snap_shot_bucket_name: The snap_shot_bucket_name of this CreateMigrationAssetDetails.
        :type: str
        """
        self._snap_shot_bucket_name = snap_shot_bucket_name

    @property
    def depends_on(self):
        """
        Gets the depends_on of this CreateMigrationAssetDetails.
        List of migration assets that depends on this asset.


        :return: The depends_on of this CreateMigrationAssetDetails.
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """
        Sets the depends_on of this CreateMigrationAssetDetails.
        List of migration assets that depends on this asset.


        :param depends_on: The depends_on of this CreateMigrationAssetDetails.
        :type: list[str]
        """
        self._depends_on = depends_on

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
