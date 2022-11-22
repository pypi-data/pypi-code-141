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
from cosmotech_api.model.run_template import RunTemplate
from cosmotech_api.model.run_template_parameter import RunTemplateParameter
from cosmotech_api.model.run_template_parameter_group import RunTemplateParameterGroup
globals()['RunTemplate'] = RunTemplate
globals()['RunTemplateParameter'] = RunTemplateParameter
globals()['RunTemplateParameterGroup'] = RunTemplateParameterGroup
from cosmotech_api.model.solution import Solution


class TestSolution(unittest.TestCase):
    """Solution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSolution(self):
        """Test Solution"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Solution()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
