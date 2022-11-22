# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSqlExecutionPlan(object):
    """
    A SQL execution plan.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSqlExecutionPlan object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan:
            The value to assign to the plan property of this SqlTuningAdvisorTaskSqlExecutionPlan.
        :type plan: list[oci.database_management.models.SqlTuningTaskSqlExecutionPlanStep]

        """
        self.swagger_types = {
            'plan': 'list[SqlTuningTaskSqlExecutionPlanStep]'
        }

        self.attribute_map = {
            'plan': 'plan'
        }

        self._plan = None

    @property
    def plan(self):
        """
        **[Required]** Gets the plan of this SqlTuningAdvisorTaskSqlExecutionPlan.
        A SQL execution plan as a list of steps.


        :return: The plan of this SqlTuningAdvisorTaskSqlExecutionPlan.
        :rtype: list[oci.database_management.models.SqlTuningTaskSqlExecutionPlanStep]
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """
        Sets the plan of this SqlTuningAdvisorTaskSqlExecutionPlan.
        A SQL execution plan as a list of steps.


        :param plan: The plan of this SqlTuningAdvisorTaskSqlExecutionPlan.
        :type: list[oci.database_management.models.SqlTuningTaskSqlExecutionPlanStep]
        """
        self._plan = plan

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
