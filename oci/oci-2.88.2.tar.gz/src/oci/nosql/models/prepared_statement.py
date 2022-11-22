# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PreparedStatement(object):
    """
    The result of query preparation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PreparedStatement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param statement:
            The value to assign to the statement property of this PreparedStatement.
        :type statement: str

        :param query_plan:
            The value to assign to the query_plan property of this PreparedStatement.
        :type query_plan: object

        :param usage:
            The value to assign to the usage property of this PreparedStatement.
        :type usage: oci.nosql.models.RequestUsage

        """
        self.swagger_types = {
            'statement': 'str',
            'query_plan': 'object',
            'usage': 'RequestUsage'
        }

        self.attribute_map = {
            'statement': 'statement',
            'query_plan': 'queryPlan',
            'usage': 'usage'
        }

        self._statement = None
        self._query_plan = None
        self._usage = None

    @property
    def statement(self):
        """
        Gets the statement of this PreparedStatement.
        A base64-encoded, compiled and parameterized version of
        a SQL statement.


        :return: The statement of this PreparedStatement.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """
        Sets the statement of this PreparedStatement.
        A base64-encoded, compiled and parameterized version of
        a SQL statement.


        :param statement: The statement of this PreparedStatement.
        :type: str
        """
        self._statement = statement

    @property
    def query_plan(self):
        """
        Gets the query_plan of this PreparedStatement.
        A representation of the query plan as a schema-less JSON object.


        :return: The query_plan of this PreparedStatement.
        :rtype: object
        """
        return self._query_plan

    @query_plan.setter
    def query_plan(self, query_plan):
        """
        Sets the query_plan of this PreparedStatement.
        A representation of the query plan as a schema-less JSON object.


        :param query_plan: The query_plan of this PreparedStatement.
        :type: object
        """
        self._query_plan = query_plan

    @property
    def usage(self):
        """
        Gets the usage of this PreparedStatement.

        :return: The usage of this PreparedStatement.
        :rtype: oci.nosql.models.RequestUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this PreparedStatement.

        :param usage: The usage of this PreparedStatement.
        :type: oci.nosql.models.RequestUsage
        """
        self._usage = usage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
