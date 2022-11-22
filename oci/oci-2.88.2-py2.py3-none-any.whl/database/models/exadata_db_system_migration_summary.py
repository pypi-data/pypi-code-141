# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataDbSystemMigrationSummary(object):
    """
    Information about the Exadata DB system migration. The migration is used to move the Exadata Cloud Service instance from the DB system resource model to the new cloud Exadata infrastructure resource model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataDbSystemMigrationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_system_id:
            The value to assign to the db_system_id property of this ExadataDbSystemMigrationSummary.
        :type db_system_id: str

        :param cloud_vm_cluster_id:
            The value to assign to the cloud_vm_cluster_id property of this ExadataDbSystemMigrationSummary.
        :type cloud_vm_cluster_id: str

        :param cloud_exadata_infrastructure_id:
            The value to assign to the cloud_exadata_infrastructure_id property of this ExadataDbSystemMigrationSummary.
        :type cloud_exadata_infrastructure_id: str

        """
        self.swagger_types = {
            'db_system_id': 'str',
            'cloud_vm_cluster_id': 'str',
            'cloud_exadata_infrastructure_id': 'str'
        }

        self.attribute_map = {
            'db_system_id': 'dbSystemId',
            'cloud_vm_cluster_id': 'cloudVmClusterId',
            'cloud_exadata_infrastructure_id': 'cloudExadataInfrastructureId'
        }

        self._db_system_id = None
        self._cloud_vm_cluster_id = None
        self._cloud_exadata_infrastructure_id = None

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this ExadataDbSystemMigrationSummary.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_system_id of this ExadataDbSystemMigrationSummary.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this ExadataDbSystemMigrationSummary.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_system_id: The db_system_id of this ExadataDbSystemMigrationSummary.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def cloud_vm_cluster_id(self):
        """
        **[Required]** Gets the cloud_vm_cluster_id of this ExadataDbSystemMigrationSummary.
        The `OCID`__ of the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_vm_cluster_id of this ExadataDbSystemMigrationSummary.
        :rtype: str
        """
        return self._cloud_vm_cluster_id

    @cloud_vm_cluster_id.setter
    def cloud_vm_cluster_id(self, cloud_vm_cluster_id):
        """
        Sets the cloud_vm_cluster_id of this ExadataDbSystemMigrationSummary.
        The `OCID`__ of the cloud VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_vm_cluster_id: The cloud_vm_cluster_id of this ExadataDbSystemMigrationSummary.
        :type: str
        """
        self._cloud_vm_cluster_id = cloud_vm_cluster_id

    @property
    def cloud_exadata_infrastructure_id(self):
        """
        **[Required]** Gets the cloud_exadata_infrastructure_id of this ExadataDbSystemMigrationSummary.
        The `OCID`__ of the cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_exadata_infrastructure_id of this ExadataDbSystemMigrationSummary.
        :rtype: str
        """
        return self._cloud_exadata_infrastructure_id

    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(self, cloud_exadata_infrastructure_id):
        """
        Sets the cloud_exadata_infrastructure_id of this ExadataDbSystemMigrationSummary.
        The `OCID`__ of the cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_exadata_infrastructure_id: The cloud_exadata_infrastructure_id of this ExadataDbSystemMigrationSummary.
        :type: str
        """
        self._cloud_exadata_infrastructure_id = cloud_exadata_infrastructure_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
