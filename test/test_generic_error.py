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

from ory_oathkeeper_client.models.generic_error import GenericError

class TestGenericError(unittest.TestCase):
    """GenericError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericError:
        """Test GenericError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericError`
        """
        model = GenericError()
        if include_optional:
            return GenericError(
                code = 56,
                details = [
                    {
                        'key' : None
                        }
                    ],
                message = '',
                reason = '',
                request = '',
                status = ''
            )
        else:
            return GenericError(
        )
        """

    def testGenericError(self):
        """Test GenericError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
