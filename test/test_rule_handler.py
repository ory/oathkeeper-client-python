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

from ory_oathkeeper_client.models.rule_handler import RuleHandler

class TestRuleHandler(unittest.TestCase):
    """RuleHandler unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleHandler:
        """Test RuleHandler
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleHandler`
        """
        model = RuleHandler()
        if include_optional:
            return RuleHandler(
                config = ory_oathkeeper_client.models.config.config(),
                handler = ''
            )
        else:
            return RuleHandler(
        )
        """

    def testRuleHandler(self):
        """Test RuleHandler"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
