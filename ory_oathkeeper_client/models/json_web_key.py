# coding: utf-8

"""
    ORY Oathkeeper

    ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.  # noqa: E501

    The version of the OpenAPI document: v0.38.5-beta.1
    Contact: hi@ory.am
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_oathkeeper_client.configuration import Configuration


class JsonWebKey(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'alg': 'str',
        'crv': 'str',
        'd': 'str',
        'dp': 'str',
        'dq': 'str',
        'e': 'str',
        'k': 'str',
        'kid': 'str',
        'kty': 'str',
        'n': 'str',
        'p': 'str',
        'q': 'str',
        'qi': 'str',
        'use': 'str',
        'x': 'str',
        'x5c': 'list[str]',
        'y': 'str'
    }

    attribute_map = {
        'alg': 'alg',
        'crv': 'crv',
        'd': 'd',
        'dp': 'dp',
        'dq': 'dq',
        'e': 'e',
        'k': 'k',
        'kid': 'kid',
        'kty': 'kty',
        'n': 'n',
        'p': 'p',
        'q': 'q',
        'qi': 'qi',
        'use': 'use',
        'x': 'x',
        'x5c': 'x5c',
        'y': 'y'
    }

    def __init__(self, alg=None, crv=None, d=None, dp=None, dq=None, e=None, k=None, kid=None, kty=None, n=None, p=None, q=None, qi=None, use=None, x=None, x5c=None, y=None, local_vars_configuration=None):  # noqa: E501
        """JsonWebKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alg = None
        self._crv = None
        self._d = None
        self._dp = None
        self._dq = None
        self._e = None
        self._k = None
        self._kid = None
        self._kty = None
        self._n = None
        self._p = None
        self._q = None
        self._qi = None
        self._use = None
        self._x = None
        self._x5c = None
        self._y = None
        self.discriminator = None

        if alg is not None:
            self.alg = alg
        if crv is not None:
            self.crv = crv
        if d is not None:
            self.d = d
        if dp is not None:
            self.dp = dp
        if dq is not None:
            self.dq = dq
        if e is not None:
            self.e = e
        if k is not None:
            self.k = k
        if kid is not None:
            self.kid = kid
        if kty is not None:
            self.kty = kty
        if n is not None:
            self.n = n
        if p is not None:
            self.p = p
        if q is not None:
            self.q = q
        if qi is not None:
            self.qi = qi
        if use is not None:
            self.use = use
        if x is not None:
            self.x = x
        if x5c is not None:
            self.x5c = x5c
        if y is not None:
            self.y = y

    @property
    def alg(self):
        """Gets the alg of this JsonWebKey.  # noqa: E501

        The \"alg\" (algorithm) parameter identifies the algorithm intended for use with the key.  The values used should either be registered in the IANA \"JSON Web Signature and Encryption Algorithms\" registry established by [JWA] or be a value that contains a Collision- Resistant Name.  # noqa: E501

        :return: The alg of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this JsonWebKey.

        The \"alg\" (algorithm) parameter identifies the algorithm intended for use with the key.  The values used should either be registered in the IANA \"JSON Web Signature and Encryption Algorithms\" registry established by [JWA] or be a value that contains a Collision- Resistant Name.  # noqa: E501

        :param alg: The alg of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._alg = alg

    @property
    def crv(self):
        """Gets the crv of this JsonWebKey.  # noqa: E501


        :return: The crv of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._crv

    @crv.setter
    def crv(self, crv):
        """Sets the crv of this JsonWebKey.


        :param crv: The crv of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._crv = crv

    @property
    def d(self):
        """Gets the d of this JsonWebKey.  # noqa: E501


        :return: The d of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._d

    @d.setter
    def d(self, d):
        """Sets the d of this JsonWebKey.


        :param d: The d of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._d = d

    @property
    def dp(self):
        """Gets the dp of this JsonWebKey.  # noqa: E501


        :return: The dp of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._dp

    @dp.setter
    def dp(self, dp):
        """Sets the dp of this JsonWebKey.


        :param dp: The dp of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._dp = dp

    @property
    def dq(self):
        """Gets the dq of this JsonWebKey.  # noqa: E501


        :return: The dq of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._dq

    @dq.setter
    def dq(self, dq):
        """Sets the dq of this JsonWebKey.


        :param dq: The dq of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._dq = dq

    @property
    def e(self):
        """Gets the e of this JsonWebKey.  # noqa: E501


        :return: The e of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._e

    @e.setter
    def e(self, e):
        """Sets the e of this JsonWebKey.


        :param e: The e of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._e = e

    @property
    def k(self):
        """Gets the k of this JsonWebKey.  # noqa: E501


        :return: The k of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._k

    @k.setter
    def k(self, k):
        """Sets the k of this JsonWebKey.


        :param k: The k of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._k = k

    @property
    def kid(self):
        """Gets the kid of this JsonWebKey.  # noqa: E501

        The \"kid\" (key ID) parameter is used to match a specific key.  This is used, for instance, to choose among a set of keys within a JWK Set during key rollover.  The structure of the \"kid\" value is unspecified.  When \"kid\" values are used within a JWK Set, different keys within the JWK Set SHOULD use distinct \"kid\" values.  (One example in which different keys might use the same \"kid\" value is if they have different \"kty\" (key type) values but are considered to be equivalent alternatives by the application using them.)  The \"kid\" value is a case-sensitive string.  # noqa: E501

        :return: The kid of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this JsonWebKey.

        The \"kid\" (key ID) parameter is used to match a specific key.  This is used, for instance, to choose among a set of keys within a JWK Set during key rollover.  The structure of the \"kid\" value is unspecified.  When \"kid\" values are used within a JWK Set, different keys within the JWK Set SHOULD use distinct \"kid\" values.  (One example in which different keys might use the same \"kid\" value is if they have different \"kty\" (key type) values but are considered to be equivalent alternatives by the application using them.)  The \"kid\" value is a case-sensitive string.  # noqa: E501

        :param kid: The kid of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._kid = kid

    @property
    def kty(self):
        """Gets the kty of this JsonWebKey.  # noqa: E501

        The \"kty\" (key type) parameter identifies the cryptographic algorithm family used with the key, such as \"RSA\" or \"EC\". \"kty\" values should either be registered in the IANA \"JSON Web Key Types\" registry established by [JWA] or be a value that contains a Collision- Resistant Name.  The \"kty\" value is a case-sensitive string.  # noqa: E501

        :return: The kty of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._kty

    @kty.setter
    def kty(self, kty):
        """Sets the kty of this JsonWebKey.

        The \"kty\" (key type) parameter identifies the cryptographic algorithm family used with the key, such as \"RSA\" or \"EC\". \"kty\" values should either be registered in the IANA \"JSON Web Key Types\" registry established by [JWA] or be a value that contains a Collision- Resistant Name.  The \"kty\" value is a case-sensitive string.  # noqa: E501

        :param kty: The kty of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._kty = kty

    @property
    def n(self):
        """Gets the n of this JsonWebKey.  # noqa: E501


        :return: The n of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this JsonWebKey.


        :param n: The n of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._n = n

    @property
    def p(self):
        """Gets the p of this JsonWebKey.  # noqa: E501


        :return: The p of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._p

    @p.setter
    def p(self, p):
        """Sets the p of this JsonWebKey.


        :param p: The p of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._p = p

    @property
    def q(self):
        """Gets the q of this JsonWebKey.  # noqa: E501


        :return: The q of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._q

    @q.setter
    def q(self, q):
        """Sets the q of this JsonWebKey.


        :param q: The q of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._q = q

    @property
    def qi(self):
        """Gets the qi of this JsonWebKey.  # noqa: E501


        :return: The qi of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._qi

    @qi.setter
    def qi(self, qi):
        """Sets the qi of this JsonWebKey.


        :param qi: The qi of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._qi = qi

    @property
    def use(self):
        """Gets the use of this JsonWebKey.  # noqa: E501

        The \"use\" (public key use) parameter identifies the intended use of the public key. The \"use\" parameter is employed to indicate whether a public key is used for encrypting data or verifying the signature on data. Values are commonly \"sig\" (signature) or \"enc\" (encryption).  # noqa: E501

        :return: The use of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._use

    @use.setter
    def use(self, use):
        """Sets the use of this JsonWebKey.

        The \"use\" (public key use) parameter identifies the intended use of the public key. The \"use\" parameter is employed to indicate whether a public key is used for encrypting data or verifying the signature on data. Values are commonly \"sig\" (signature) or \"enc\" (encryption).  # noqa: E501

        :param use: The use of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._use = use

    @property
    def x(self):
        """Gets the x of this JsonWebKey.  # noqa: E501


        :return: The x of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this JsonWebKey.


        :param x: The x of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._x = x

    @property
    def x5c(self):
        """Gets the x5c of this JsonWebKey.  # noqa: E501

        The \"x5c\" (X.509 certificate chain) parameter contains a chain of one or more PKIX certificates [RFC5280].  The certificate chain is represented as a JSON array of certificate value strings.  Each string in the array is a base64-encoded (Section 4 of [RFC4648] -- not base64url-encoded) DER [ITU.X690.1994] PKIX certificate value. The PKIX certificate containing the key value MUST be the first certificate.  # noqa: E501

        :return: The x5c of this JsonWebKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._x5c

    @x5c.setter
    def x5c(self, x5c):
        """Sets the x5c of this JsonWebKey.

        The \"x5c\" (X.509 certificate chain) parameter contains a chain of one or more PKIX certificates [RFC5280].  The certificate chain is represented as a JSON array of certificate value strings.  Each string in the array is a base64-encoded (Section 4 of [RFC4648] -- not base64url-encoded) DER [ITU.X690.1994] PKIX certificate value. The PKIX certificate containing the key value MUST be the first certificate.  # noqa: E501

        :param x5c: The x5c of this JsonWebKey.  # noqa: E501
        :type: list[str]
        """

        self._x5c = x5c

    @property
    def y(self):
        """Gets the y of this JsonWebKey.  # noqa: E501


        :return: The y of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this JsonWebKey.


        :param y: The y of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._y = y

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JsonWebKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonWebKey):
            return True

        return self.to_dict() != other.to_dict()
