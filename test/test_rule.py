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

from ory_oathkeeper_client.models.rule import Rule

class TestRule(unittest.TestCase):
    """Rule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Rule:
        """Test Rule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Rule`
        """
        model = Rule()
        if include_optional:
            return Rule(
                authenticators = [
                    ory_oathkeeper_client.models.rule_handler.ruleHandler(
                        config = ory_oathkeeper_client.models.config.config(), 
                        handler = '', )
                    ],
                authorizer = ory_oathkeeper_client.models.rule_handler.ruleHandler(
                    config = ory_oathkeeper_client.models.config.config(), 
                    handler = '', ),
                description = '',
                id = '',
                match = ory_oathkeeper_client.models.rule_match.ruleMatch(
                    methods = [
                        ''
                        ], 
                    url = '', ),
                mutators = [
                    ory_oathkeeper_client.models.rule_handler.ruleHandler(
                        config = ory_oathkeeper_client.models.config.config(), 
                        handler = '', )
                    ],
                upstream = ory_oathkeeper_client.models.upstream.Upstream(
                    preserve_host = True, 
                    strip_path = '', 
                    url = '', )
            )
        else:
            return Rule(
        )
        """

    def testRule(self):
        """Test Rule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
