"""
    Cosmo Tech Plaform API

    Cosmo Tech Platform API  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: platform@cosmotech.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import cosmotech_api
from cosmotech_api.api.solution_api import SolutionApi  # noqa: E501


class TestSolutionApi(unittest.TestCase):
    """SolutionApi unit test stubs"""

    def setUp(self):
        self.api = SolutionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_or_replace_parameter_groups(self):
        """Test case for add_or_replace_parameter_groups

        Add Parameter Groups. Any item with the same ID will be overwritten  # noqa: E501
        """
        pass

    def test_add_or_replace_parameters(self):
        """Test case for add_or_replace_parameters

        Add Parameters. Any item with the same ID will be overwritten  # noqa: E501
        """
        pass

    def test_add_or_replace_run_templates(self):
        """Test case for add_or_replace_run_templates

        Add Run Templates. Any item with the same ID will be overwritten  # noqa: E501
        """
        pass

    def test_create_solution(self):
        """Test case for create_solution

        Register a new solution  # noqa: E501
        """
        pass

    def test_delete_solution(self):
        """Test case for delete_solution

        Delete a solution  # noqa: E501
        """
        pass

    def test_delete_solution_run_template(self):
        """Test case for delete_solution_run_template

        Remove the specified Solution Run Template  # noqa: E501
        """
        pass

    def test_download_run_template_handler(self):
        """Test case for download_run_template_handler

        Download a Run Template step handler zip file  # noqa: E501
        """
        pass

    def test_find_all_solutions(self):
        """Test case for find_all_solutions

        List all Solutions  # noqa: E501
        """
        pass

    def test_find_solution_by_id(self):
        """Test case for find_solution_by_id

        Get the details of a solution  # noqa: E501
        """
        pass

    def test_remove_all_run_templates(self):
        """Test case for remove_all_run_templates

        Remove all Run Templates from the Solution specified  # noqa: E501
        """
        pass

    def test_remove_all_solution_parameter_groups(self):
        """Test case for remove_all_solution_parameter_groups

        Remove all Parameter Groups from the Solution specified  # noqa: E501
        """
        pass

    def test_remove_all_solution_parameters(self):
        """Test case for remove_all_solution_parameters

        Remove all Parameters from the Solution specified  # noqa: E501
        """
        pass

    def test_update_solution(self):
        """Test case for update_solution

        Update a solution  # noqa: E501
        """
        pass

    def test_update_solution_run_template(self):
        """Test case for update_solution_run_template

        Update the specified Solution Run Template  # noqa: E501
        """
        pass

    def test_upload_run_template_handler(self):
        """Test case for upload_run_template_handler

        Upload a Run Template step handler zip file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
