"""
    ORY Oathkeeper

    ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.  # noqa: E501

    The version of the OpenAPI document: v0.38.19-beta.1
    Contact: hi@ory.am
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_oathkeeper_client
from ory_oathkeeper_client.model.rule_handler import RuleHandler
from ory_oathkeeper_client.model.rule_match import RuleMatch
from ory_oathkeeper_client.model.upstream import Upstream
globals()['RuleHandler'] = RuleHandler
globals()['RuleMatch'] = RuleMatch
globals()['Upstream'] = Upstream
from ory_oathkeeper_client.model.rule import Rule


class TestRule(unittest.TestCase):
    """Rule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRule(self):
        """Test Rule"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Rule()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
