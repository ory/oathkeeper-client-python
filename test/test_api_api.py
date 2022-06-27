"""
    ORY Oathkeeper

    ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.  # noqa: E501

    The version of the OpenAPI document: v0.39.0
    Contact: hi@ory.am
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_oathkeeper_client
from ory_oathkeeper_client.api.api_api import ApiApi  # noqa: E501


class TestApiApi(unittest.TestCase):
    """ApiApi unit test stubs"""

    def setUp(self):
        self.api = ApiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_decisions(self):
        """Test case for decisions

        Access Control Decision API  # noqa: E501
        """
        pass

    def test_get_rule(self):
        """Test case for get_rule

        Retrieve a rule  # noqa: E501
        """
        pass

    def test_get_version(self):
        """Test case for get_version

        Get service version  # noqa: E501
        """
        pass

    def test_get_well_known_json_web_keys(self):
        """Test case for get_well_known_json_web_keys

        Lists cryptographic keys  # noqa: E501
        """
        pass

    def test_is_instance_alive(self):
        """Test case for is_instance_alive

        Check alive status  # noqa: E501
        """
        pass

    def test_is_instance_ready(self):
        """Test case for is_instance_ready

        Check readiness status  # noqa: E501
        """
        pass

    def test_list_rules(self):
        """Test case for list_rules

        List all rules  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
