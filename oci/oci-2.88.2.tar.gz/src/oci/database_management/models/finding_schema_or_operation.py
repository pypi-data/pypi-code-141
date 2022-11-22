# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FindingSchemaOrOperation(object):
    """
    The findings of the Optimizer Statistics Advisor.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FindingSchemaOrOperation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operations:
            The value to assign to the operations property of this FindingSchemaOrOperation.
        :type operations: list[str]

        :param schemas:
            The value to assign to the schemas property of this FindingSchemaOrOperation.
        :type schemas: list[oci.database_management.models.SchemaDefinition]

        """
        self.swagger_types = {
            'operations': 'list[str]',
            'schemas': 'list[SchemaDefinition]'
        }

        self.attribute_map = {
            'operations': 'operations',
            'schemas': 'schemas'
        }

        self._operations = None
        self._schemas = None

    @property
    def operations(self):
        """
        Gets the operations of this FindingSchemaOrOperation.
        The list of operation details.


        :return: The operations of this FindingSchemaOrOperation.
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        Sets the operations of this FindingSchemaOrOperation.
        The list of operation details.


        :param operations: The operations of this FindingSchemaOrOperation.
        :type: list[str]
        """
        self._operations = operations

    @property
    def schemas(self):
        """
        Gets the schemas of this FindingSchemaOrOperation.
        The names of the impacted database schemas and their objects.


        :return: The schemas of this FindingSchemaOrOperation.
        :rtype: list[oci.database_management.models.SchemaDefinition]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this FindingSchemaOrOperation.
        The names of the impacted database schemas and their objects.


        :param schemas: The schemas of this FindingSchemaOrOperation.
        :type: list[oci.database_management.models.SchemaDefinition]
        """
        self._schemas = schemas

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
