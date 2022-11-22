# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_type_tablespace_details import TargetTypeTablespaceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ADBServerlesTablespaceDetails(TargetTypeTablespaceDetails):
    """
    Migration tablespace settings valid for ADB-D target type using remap feature
    """

    #: A constant which can be used with the remap_target property of a ADBServerlesTablespaceDetails.
    #: This constant has a value of "DATA"
    REMAP_TARGET_DATA = "DATA"

    def __init__(self, **kwargs):
        """
        Initializes a new ADBServerlesTablespaceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.ADBServerlesTablespaceDetails.target_type` attribute
        of this class is ``ADB_S_REMAP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this ADBServerlesTablespaceDetails.
            Allowed values for this property are: "ADB_S_REMAP", "ADB_D_REMAP", "ADB_D_AUTOCREATE", "NON_ADB_REMAP", "NON_ADB_AUTOCREATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_type: str

        :param remap_target:
            The value to assign to the remap_target property of this ADBServerlesTablespaceDetails.
            Allowed values for this property are: "DATA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type remap_target: str

        """
        self.swagger_types = {
            'target_type': 'str',
            'remap_target': 'str'
        }

        self.attribute_map = {
            'target_type': 'targetType',
            'remap_target': 'remapTarget'
        }

        self._target_type = None
        self._remap_target = None
        self._target_type = 'ADB_S_REMAP'

    @property
    def remap_target(self):
        """
        Gets the remap_target of this ADBServerlesTablespaceDetails.
        Name of tablespace at target to which the source database tablespace need to be remapped.

        Allowed values for this property are: "DATA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The remap_target of this ADBServerlesTablespaceDetails.
        :rtype: str
        """
        return self._remap_target

    @remap_target.setter
    def remap_target(self, remap_target):
        """
        Sets the remap_target of this ADBServerlesTablespaceDetails.
        Name of tablespace at target to which the source database tablespace need to be remapped.


        :param remap_target: The remap_target of this ADBServerlesTablespaceDetails.
        :type: str
        """
        allowed_values = ["DATA"]
        if not value_allowed_none_or_none_sentinel(remap_target, allowed_values):
            remap_target = 'UNKNOWN_ENUM_VALUE'
        self._remap_target = remap_target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
