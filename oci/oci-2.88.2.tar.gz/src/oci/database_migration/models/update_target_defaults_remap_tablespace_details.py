# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_target_type_tablespace_details import UpdateTargetTypeTablespaceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetDefaultsRemapTablespaceDetails(UpdateTargetTypeTablespaceDetails):
    """
    Migration tablespace settings valid for TARGET_DEFAULTS_REMAP target type. The service will compute the targetType
    that corresponds to the targetDatabaseConnectionId type, and set the corresponding default values. When target type is ADB_S,
    ADB_D or NON_ADB the default will be set to remap feature ADB_S_REMAP, ADB_D_REMAP or NON_ADB_REMAP.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetDefaultsRemapTablespaceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.UpdateTargetDefaultsRemapTablespaceDetails.target_type` attribute
        of this class is ``TARGET_DEFAULTS_REMAP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this UpdateTargetDefaultsRemapTablespaceDetails.
            Allowed values for this property are: "ADB_S_REMAP", "ADB_D_REMAP", "ADB_D_AUTOCREATE", "NON_ADB_REMAP", "NON_ADB_AUTOCREATE", "TARGET_DEFAULTS_REMAP", "TARGET_DEFAULTS_AUTOCREATE"
        :type target_type: str

        """
        self.swagger_types = {
            'target_type': 'str'
        }

        self.attribute_map = {
            'target_type': 'targetType'
        }

        self._target_type = None
        self._target_type = 'TARGET_DEFAULTS_REMAP'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
