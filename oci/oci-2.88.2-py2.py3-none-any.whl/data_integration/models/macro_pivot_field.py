# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MacroPivotField(object):
    """
    MacroPivotField is used for the PivotField with macro expressions. It can contain the rules according to the macro pattern/attribute added and create new fields according to the PivotKeyValues
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MacroPivotField object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_use_source_type:
            The value to assign to the is_use_source_type property of this MacroPivotField.
        :type is_use_source_type: bool

        :param expr:
            The value to assign to the expr property of this MacroPivotField.
        :type expr: oci.data_integration.models.Expression

        :param use_type:
            The value to assign to the use_type property of this MacroPivotField.
        :type use_type: oci.data_integration.models.ConfiguredType

        :param type:
            The value to assign to the type property of this MacroPivotField.
        :type type: oci.data_integration.models.BaseType

        :param column_name_pattern:
            The value to assign to the column_name_pattern property of this MacroPivotField.
        :type column_name_pattern: str

        """
        self.swagger_types = {
            'is_use_source_type': 'bool',
            'expr': 'Expression',
            'use_type': 'ConfiguredType',
            'type': 'BaseType',
            'column_name_pattern': 'str'
        }

        self.attribute_map = {
            'is_use_source_type': 'isUseSourceType',
            'expr': 'expr',
            'use_type': 'useType',
            'type': 'type',
            'column_name_pattern': 'columnNamePattern'
        }

        self._is_use_source_type = None
        self._expr = None
        self._use_type = None
        self._type = None
        self._column_name_pattern = None

    @property
    def is_use_source_type(self):
        """
        Gets the is_use_source_type of this MacroPivotField.
        Specifies whether the type of macro fields is inferred from an expression or useType (false) or the source field (true).


        :return: The is_use_source_type of this MacroPivotField.
        :rtype: bool
        """
        return self._is_use_source_type

    @is_use_source_type.setter
    def is_use_source_type(self, is_use_source_type):
        """
        Sets the is_use_source_type of this MacroPivotField.
        Specifies whether the type of macro fields is inferred from an expression or useType (false) or the source field (true).


        :param is_use_source_type: The is_use_source_type of this MacroPivotField.
        :type: bool
        """
        self._is_use_source_type = is_use_source_type

    @property
    def expr(self):
        """
        Gets the expr of this MacroPivotField.

        :return: The expr of this MacroPivotField.
        :rtype: oci.data_integration.models.Expression
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """
        Sets the expr of this MacroPivotField.

        :param expr: The expr of this MacroPivotField.
        :type: oci.data_integration.models.Expression
        """
        self._expr = expr

    @property
    def use_type(self):
        """
        Gets the use_type of this MacroPivotField.

        :return: The use_type of this MacroPivotField.
        :rtype: oci.data_integration.models.ConfiguredType
        """
        return self._use_type

    @use_type.setter
    def use_type(self, use_type):
        """
        Sets the use_type of this MacroPivotField.

        :param use_type: The use_type of this MacroPivotField.
        :type: oci.data_integration.models.ConfiguredType
        """
        self._use_type = use_type

    @property
    def type(self):
        """
        Gets the type of this MacroPivotField.

        :return: The type of this MacroPivotField.
        :rtype: oci.data_integration.models.BaseType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MacroPivotField.

        :param type: The type of this MacroPivotField.
        :type: oci.data_integration.models.BaseType
        """
        self._type = type

    @property
    def column_name_pattern(self):
        """
        Gets the column_name_pattern of this MacroPivotField.
        column name pattern can be used to generate the name structure of the generated columns. By default column names are of %PIVOT_KEY_VALUE% or %MACRO_INPUT%_%PIVOT_KEY_VALUE%, but we can change it something by passing something like MY_PREFIX%PIVOT_KEY_VALUE%MY_SUFFIX or MY_PREFIX%MACRO_INPUT%_%PIVOT_KEY_VALUE%MY_SUFFIX which will add custom prefix and suffix to the column name.


        :return: The column_name_pattern of this MacroPivotField.
        :rtype: str
        """
        return self._column_name_pattern

    @column_name_pattern.setter
    def column_name_pattern(self, column_name_pattern):
        """
        Sets the column_name_pattern of this MacroPivotField.
        column name pattern can be used to generate the name structure of the generated columns. By default column names are of %PIVOT_KEY_VALUE% or %MACRO_INPUT%_%PIVOT_KEY_VALUE%, but we can change it something by passing something like MY_PREFIX%PIVOT_KEY_VALUE%MY_SUFFIX or MY_PREFIX%MACRO_INPUT%_%PIVOT_KEY_VALUE%MY_SUFFIX which will add custom prefix and suffix to the column name.


        :param column_name_pattern: The column_name_pattern of this MacroPivotField.
        :type: str
        """
        self._column_name_pattern = column_name_pattern

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
