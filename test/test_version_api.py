# coding: utf-8

"""
    ORY Oathkeeper

    ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.

    The version of the OpenAPI document: v0.40.8
    Contact: hi@ory.am
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_oathkeeper_client.api.version_api import VersionApi


class TestVersionApi(unittest.TestCase):
    """VersionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VersionApi()

    def tearDown(self) -> None:
        pass

    def test_get_version(self) -> None:
        """Test case for get_version

        Get service version
        """
        pass


if __name__ == '__main__':
    unittest.main()
