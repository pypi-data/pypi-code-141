# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .backup_event_details import BackupEventDetails
from .backup_opensearch_cluster_details import BackupOpensearchClusterDetails
from .change_opensearch_cluster_backup_compartment_details import ChangeOpensearchClusterBackupCompartmentDetails
from .change_opensearch_cluster_compartment_details import ChangeOpensearchClusterCompartmentDetails
from .create_opensearch_cluster_details import CreateOpensearchClusterDetails
from .export_opensearch_cluster_backup_details import ExportOpensearchClusterBackupDetails
from .get_manifest_response import GetManifestResponse
from .opensearch_cluster import OpensearchCluster
from .opensearch_cluster_backup import OpensearchClusterBackup
from .opensearch_cluster_backup_collection import OpensearchClusterBackupCollection
from .opensearch_cluster_backup_summary import OpensearchClusterBackupSummary
from .opensearch_cluster_collection import OpensearchClusterCollection
from .opensearch_cluster_summary import OpensearchClusterSummary
from .opensearch_versions_collection import OpensearchVersionsCollection
from .opensearch_versions_summary import OpensearchVersionsSummary
from .resize_opensearch_cluster_horizontal_details import ResizeOpensearchClusterHorizontalDetails
from .resize_opensearch_cluster_vertical_details import ResizeOpensearchClusterVerticalDetails
from .restore_opensearch_cluster_backup_details import RestoreOpensearchClusterBackupDetails
from .restore_opensearch_cluster_details import RestoreOpensearchClusterDetails
from .update_checkin_details import UpdateCheckinDetails
from .update_cluster_hardened_image_details import UpdateClusterHardenedImageDetails
from .update_cluster_status_details import UpdateClusterStatusDetails
from .update_opensearch_cluster_backup_details import UpdateOpensearchClusterBackupDetails
from .update_opensearch_cluster_details import UpdateOpensearchClusterDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource

# Maps type names to classes for opensearch services.
opensearch_type_mapping = {
    "BackupEventDetails": BackupEventDetails,
    "BackupOpensearchClusterDetails": BackupOpensearchClusterDetails,
    "ChangeOpensearchClusterBackupCompartmentDetails": ChangeOpensearchClusterBackupCompartmentDetails,
    "ChangeOpensearchClusterCompartmentDetails": ChangeOpensearchClusterCompartmentDetails,
    "CreateOpensearchClusterDetails": CreateOpensearchClusterDetails,
    "ExportOpensearchClusterBackupDetails": ExportOpensearchClusterBackupDetails,
    "GetManifestResponse": GetManifestResponse,
    "OpensearchCluster": OpensearchCluster,
    "OpensearchClusterBackup": OpensearchClusterBackup,
    "OpensearchClusterBackupCollection": OpensearchClusterBackupCollection,
    "OpensearchClusterBackupSummary": OpensearchClusterBackupSummary,
    "OpensearchClusterCollection": OpensearchClusterCollection,
    "OpensearchClusterSummary": OpensearchClusterSummary,
    "OpensearchVersionsCollection": OpensearchVersionsCollection,
    "OpensearchVersionsSummary": OpensearchVersionsSummary,
    "ResizeOpensearchClusterHorizontalDetails": ResizeOpensearchClusterHorizontalDetails,
    "ResizeOpensearchClusterVerticalDetails": ResizeOpensearchClusterVerticalDetails,
    "RestoreOpensearchClusterBackupDetails": RestoreOpensearchClusterBackupDetails,
    "RestoreOpensearchClusterDetails": RestoreOpensearchClusterDetails,
    "UpdateCheckinDetails": UpdateCheckinDetails,
    "UpdateClusterHardenedImageDetails": UpdateClusterHardenedImageDetails,
    "UpdateClusterStatusDetails": UpdateClusterStatusDetails,
    "UpdateOpensearchClusterBackupDetails": UpdateOpensearchClusterBackupDetails,
    "UpdateOpensearchClusterDetails": UpdateOpensearchClusterDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource
}
