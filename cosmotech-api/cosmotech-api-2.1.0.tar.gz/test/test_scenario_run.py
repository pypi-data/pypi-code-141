"""
    Cosmo Tech Plaform API

    Cosmo Tech Platform API  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: platform@cosmotech.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import cosmotech_api
from cosmotech_api.model.run_template_parameter_value import RunTemplateParameterValue
from cosmotech_api.model.scenario_run_container import ScenarioRunContainer
from cosmotech_api.model.scenario_run_state import ScenarioRunState
globals()['RunTemplateParameterValue'] = RunTemplateParameterValue
globals()['ScenarioRunContainer'] = ScenarioRunContainer
globals()['ScenarioRunState'] = ScenarioRunState
from cosmotech_api.model.scenario_run import ScenarioRun


class TestScenarioRun(unittest.TestCase):
    """ScenarioRun unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScenarioRun(self):
        """Test ScenarioRun"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ScenarioRun()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
