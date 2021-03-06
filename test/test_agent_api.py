# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dohq_teamcity
from dohq_teamcity.api.agent_api import AgentApi  # noqa: E501
from dohq_teamcity.rest import ApiException


class TestAgentApi(unittest.TestCase):
    """AgentApi unit test stubs"""

    def setUp(self):
        self.api = dohq_teamcity.api.agent_api.AgentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_agent(self):
        """Test case for delete_agent

        """
        pass

    def test_ge_incompatible_build_types(self):
        """Test case for ge_incompatible_build_types

        """
        pass

    def test_get_agent_pool(self):
        """Test case for get_agent_pool

        """
        pass

    def test_get_authorized_info(self):
        """Test case for get_authorized_info

        """
        pass

    def test_get_compatible_build_types(self):
        """Test case for get_compatible_build_types

        """
        pass

    def test_get_enabled_info(self):
        """Test case for get_enabled_info

        """
        pass

    def test_serve_agent(self):
        """Test case for serve_agent

        """
        pass

    def test_serve_agent_field(self):
        """Test case for serve_agent_field

        """
        pass

    def test_serve_agents(self):
        """Test case for serve_agents

        """
        pass

    def test_set_agent_field(self):
        """Test case for set_agent_field

        """
        pass

    def test_set_agent_pool(self):
        """Test case for set_agent_pool

        """
        pass

    def test_set_authorized_info(self):
        """Test case for set_authorized_info

        """
        pass

    def test_set_enabled_info(self):
        """Test case for set_enabled_info

        """
        pass


if __name__ == '__main__':
    unittest.main()
