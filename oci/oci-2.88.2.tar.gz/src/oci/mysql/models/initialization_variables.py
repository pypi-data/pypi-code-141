# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InitializationVariables(object):
    """
    User-defined service variables set only at DB system initialization. These variables cannot be changed later at runtime.
    """

    #: A constant which can be used with the lower_case_table_names property of a InitializationVariables.
    #: This constant has a value of "CASE_SENSITIVE"
    LOWER_CASE_TABLE_NAMES_CASE_SENSITIVE = "CASE_SENSITIVE"

    #: A constant which can be used with the lower_case_table_names property of a InitializationVariables.
    #: This constant has a value of "CASE_INSENSITIVE_LOWERCASE"
    LOWER_CASE_TABLE_NAMES_CASE_INSENSITIVE_LOWERCASE = "CASE_INSENSITIVE_LOWERCASE"

    def __init__(self, **kwargs):
        """
        Initializes a new InitializationVariables object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lower_case_table_names:
            The value to assign to the lower_case_table_names property of this InitializationVariables.
            Allowed values for this property are: "CASE_SENSITIVE", "CASE_INSENSITIVE_LOWERCASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lower_case_table_names: str

        """
        self.swagger_types = {
            'lower_case_table_names': 'str'
        }

        self.attribute_map = {
            'lower_case_table_names': 'lowerCaseTableNames'
        }

        self._lower_case_table_names = None

    @property
    def lower_case_table_names(self):
        """
        Gets the lower_case_table_names of this InitializationVariables.
        Represents the MySQL server system variable lower_case_table_names (https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_lower_case_table_names).

        lowerCaseTableNames controls case-sensitivity of tables and schema names and how they are stored in the DB System.

        Valid values are:
          - CASE_SENSITIVE - (default) Table and schema name comparisons are case-sensitive and stored as specified. (lower_case_table_names=0)
          - CASE_INSENSITIVE_LOWERCASE - Table and schema name comparisons are not case-sensitive and stored in lowercase. (lower_case_table_names=1)

        Allowed values for this property are: "CASE_SENSITIVE", "CASE_INSENSITIVE_LOWERCASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lower_case_table_names of this InitializationVariables.
        :rtype: str
        """
        return self._lower_case_table_names

    @lower_case_table_names.setter
    def lower_case_table_names(self, lower_case_table_names):
        """
        Sets the lower_case_table_names of this InitializationVariables.
        Represents the MySQL server system variable lower_case_table_names (https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_lower_case_table_names).

        lowerCaseTableNames controls case-sensitivity of tables and schema names and how they are stored in the DB System.

        Valid values are:
          - CASE_SENSITIVE - (default) Table and schema name comparisons are case-sensitive and stored as specified. (lower_case_table_names=0)
          - CASE_INSENSITIVE_LOWERCASE - Table and schema name comparisons are not case-sensitive and stored in lowercase. (lower_case_table_names=1)


        :param lower_case_table_names: The lower_case_table_names of this InitializationVariables.
        :type: str
        """
        allowed_values = ["CASE_SENSITIVE", "CASE_INSENSITIVE_LOWERCASE"]
        if not value_allowed_none_or_none_sentinel(lower_case_table_names, allowed_values):
            lower_case_table_names = 'UNKNOWN_ENUM_VALUE'
        self._lower_case_table_names = lower_case_table_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
