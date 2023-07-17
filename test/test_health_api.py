"""
    ORY Oathkeeper

    ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.  # noqa: E501

    The version of the OpenAPI document: v0.40.5
    Contact: hi@ory.am
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_oathkeeper_client
from ory_oathkeeper_client.api.health_api import HealthApi  # noqa: E501


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = HealthApi()  # noqa: E501

    def tearDown(self):
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


if __name__ == '__main__':
    unittest.main()
