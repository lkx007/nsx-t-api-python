# coding: utf-8

"""
    NSX-T Manager API

    VMware NSX-T Manager REST API  # noqa: E501

    OpenAPI spec version: 2.5.1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class X509Certificate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ecdsa_ec_field_f2mks': 'list[int]',
        'version': 'str',
        'is_ca': 'bool',
        'signature_algorithm': 'str',
        'ecdsa_public_key_a': 'str',
        'rsa_public_key_exponent': 'str',
        'ecdsa_ec_field_f2mm': 'int',
        'issuer_cn': 'str',
        'subject_cn': 'str',
        'ecdsa_public_key_order': 'str',
        'ecdsa_ec_field_f2mrp': 'str',
        'public_key_length': 'int',
        'not_before': 'int',
        'ecdsa_ec_field_f2pp': 'str',
        'issuer': 'str',
        'ecdsa_public_key_b': 'str',
        'rsa_public_key_modulus': 'str',
        'dsa_public_key_y': 'str',
        'ecdsa_public_key_cofactor': 'int',
        'not_after': 'int',
        'dsa_public_key_q': 'str',
        'dsa_public_key_p': 'str',
        'ecdsa_public_key_generator_y': 'str',
        'ecdsa_public_key_generator_x': 'str',
        'public_key_algo': 'str',
        'is_valid': 'bool',
        'ecdsa_public_key_seed': 'list[str]',
        'signature': 'str',
        'serial_number': 'str',
        'dsa_public_key_g': 'str',
        'subject': 'str',
        'ecdsa_ec_field': 'str',
        'ecdsa_curve_name': 'str'
    }

    attribute_map = {
        'ecdsa_ec_field_f2mks': 'ecdsa_ec_field_f2mks',
        'version': 'version',
        'is_ca': 'is_ca',
        'signature_algorithm': 'signature_algorithm',
        'ecdsa_public_key_a': 'ecdsa_public_key_a',
        'rsa_public_key_exponent': 'rsa_public_key_exponent',
        'ecdsa_ec_field_f2mm': 'ecdsa_ec_field_f2mm',
        'issuer_cn': 'issuer_cn',
        'subject_cn': 'subject_cn',
        'ecdsa_public_key_order': 'ecdsa_public_key_order',
        'ecdsa_ec_field_f2mrp': 'ecdsa_ec_field_f2mrp',
        'public_key_length': 'public_key_length',
        'not_before': 'not_before',
        'ecdsa_ec_field_f2pp': 'ecdsa_ec_field_f2pp',
        'issuer': 'issuer',
        'ecdsa_public_key_b': 'ecdsa_public_key_b',
        'rsa_public_key_modulus': 'rsa_public_key_modulus',
        'dsa_public_key_y': 'dsa_public_key_y',
        'ecdsa_public_key_cofactor': 'ecdsa_public_key_cofactor',
        'not_after': 'not_after',
        'dsa_public_key_q': 'dsa_public_key_q',
        'dsa_public_key_p': 'dsa_public_key_p',
        'ecdsa_public_key_generator_y': 'ecdsa_public_key_generator_y',
        'ecdsa_public_key_generator_x': 'ecdsa_public_key_generator_x',
        'public_key_algo': 'public_key_algo',
        'is_valid': 'is_valid',
        'ecdsa_public_key_seed': 'ecdsa_public_key_seed',
        'signature': 'signature',
        'serial_number': 'serial_number',
        'dsa_public_key_g': 'dsa_public_key_g',
        'subject': 'subject',
        'ecdsa_ec_field': 'ecdsa_ec_field',
        'ecdsa_curve_name': 'ecdsa_curve_name'
    }

    def __init__(self, ecdsa_ec_field_f2mks=None, version=None, is_ca=None, signature_algorithm=None, ecdsa_public_key_a=None, rsa_public_key_exponent=None, ecdsa_ec_field_f2mm=None, issuer_cn=None, subject_cn=None, ecdsa_public_key_order=None, ecdsa_ec_field_f2mrp=None, public_key_length=None, not_before=None, ecdsa_ec_field_f2pp=None, issuer=None, ecdsa_public_key_b=None, rsa_public_key_modulus=None, dsa_public_key_y=None, ecdsa_public_key_cofactor=None, not_after=None, dsa_public_key_q=None, dsa_public_key_p=None, ecdsa_public_key_generator_y=None, ecdsa_public_key_generator_x=None, public_key_algo=None, is_valid=None, ecdsa_public_key_seed=None, signature=None, serial_number=None, dsa_public_key_g=None, subject=None, ecdsa_ec_field=None, ecdsa_curve_name=None):  # noqa: E501
        """X509Certificate - a model defined in Swagger"""  # noqa: E501
        self._ecdsa_ec_field_f2mks = None
        self._version = None
        self._is_ca = None
        self._signature_algorithm = None
        self._ecdsa_public_key_a = None
        self._rsa_public_key_exponent = None
        self._ecdsa_ec_field_f2mm = None
        self._issuer_cn = None
        self._subject_cn = None
        self._ecdsa_public_key_order = None
        self._ecdsa_ec_field_f2mrp = None
        self._public_key_length = None
        self._not_before = None
        self._ecdsa_ec_field_f2pp = None
        self._issuer = None
        self._ecdsa_public_key_b = None
        self._rsa_public_key_modulus = None
        self._dsa_public_key_y = None
        self._ecdsa_public_key_cofactor = None
        self._not_after = None
        self._dsa_public_key_q = None
        self._dsa_public_key_p = None
        self._ecdsa_public_key_generator_y = None
        self._ecdsa_public_key_generator_x = None
        self._public_key_algo = None
        self._is_valid = None
        self._ecdsa_public_key_seed = None
        self._signature = None
        self._serial_number = None
        self._dsa_public_key_g = None
        self._subject = None
        self._ecdsa_ec_field = None
        self._ecdsa_curve_name = None
        self.discriminator = None
        if ecdsa_ec_field_f2mks is not None:
            self.ecdsa_ec_field_f2mks = ecdsa_ec_field_f2mks
        if version is not None:
            self.version = version
        if is_ca is not None:
            self.is_ca = is_ca
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if ecdsa_public_key_a is not None:
            self.ecdsa_public_key_a = ecdsa_public_key_a
        if rsa_public_key_exponent is not None:
            self.rsa_public_key_exponent = rsa_public_key_exponent
        if ecdsa_ec_field_f2mm is not None:
            self.ecdsa_ec_field_f2mm = ecdsa_ec_field_f2mm
        if issuer_cn is not None:
            self.issuer_cn = issuer_cn
        if subject_cn is not None:
            self.subject_cn = subject_cn
        if ecdsa_public_key_order is not None:
            self.ecdsa_public_key_order = ecdsa_public_key_order
        if ecdsa_ec_field_f2mrp is not None:
            self.ecdsa_ec_field_f2mrp = ecdsa_ec_field_f2mrp
        if public_key_length is not None:
            self.public_key_length = public_key_length
        if not_before is not None:
            self.not_before = not_before
        if ecdsa_ec_field_f2pp is not None:
            self.ecdsa_ec_field_f2pp = ecdsa_ec_field_f2pp
        if issuer is not None:
            self.issuer = issuer
        if ecdsa_public_key_b is not None:
            self.ecdsa_public_key_b = ecdsa_public_key_b
        if rsa_public_key_modulus is not None:
            self.rsa_public_key_modulus = rsa_public_key_modulus
        if dsa_public_key_y is not None:
            self.dsa_public_key_y = dsa_public_key_y
        if ecdsa_public_key_cofactor is not None:
            self.ecdsa_public_key_cofactor = ecdsa_public_key_cofactor
        if not_after is not None:
            self.not_after = not_after
        if dsa_public_key_q is not None:
            self.dsa_public_key_q = dsa_public_key_q
        if dsa_public_key_p is not None:
            self.dsa_public_key_p = dsa_public_key_p
        if ecdsa_public_key_generator_y is not None:
            self.ecdsa_public_key_generator_y = ecdsa_public_key_generator_y
        if ecdsa_public_key_generator_x is not None:
            self.ecdsa_public_key_generator_x = ecdsa_public_key_generator_x
        if public_key_algo is not None:
            self.public_key_algo = public_key_algo
        if is_valid is not None:
            self.is_valid = is_valid
        if ecdsa_public_key_seed is not None:
            self.ecdsa_public_key_seed = ecdsa_public_key_seed
        if signature is not None:
            self.signature = signature
        if serial_number is not None:
            self.serial_number = serial_number
        if dsa_public_key_g is not None:
            self.dsa_public_key_g = dsa_public_key_g
        if subject is not None:
            self.subject = subject
        if ecdsa_ec_field is not None:
            self.ecdsa_ec_field = ecdsa_ec_field
        if ecdsa_curve_name is not None:
            self.ecdsa_curve_name = ecdsa_curve_name

    @property
    def ecdsa_ec_field_f2mks(self):
        """Gets the ecdsa_ec_field_f2mks of this X509Certificate.  # noqa: E501

        The order of the middle term(s) of the reduction polynomial in elliptic curve (EC) | characteristic 2 finite field.| Contents of this array are copied to protect against subsequent modification in ECDSA.  # noqa: E501

        :return: The ecdsa_ec_field_f2mks of this X509Certificate.  # noqa: E501
        :rtype: list[int]
        """
        return self._ecdsa_ec_field_f2mks

    @ecdsa_ec_field_f2mks.setter
    def ecdsa_ec_field_f2mks(self, ecdsa_ec_field_f2mks):
        """Sets the ecdsa_ec_field_f2mks of this X509Certificate.

        The order of the middle term(s) of the reduction polynomial in elliptic curve (EC) | characteristic 2 finite field.| Contents of this array are copied to protect against subsequent modification in ECDSA.  # noqa: E501

        :param ecdsa_ec_field_f2mks: The ecdsa_ec_field_f2mks of this X509Certificate.  # noqa: E501
        :type: list[int]
        """

        self._ecdsa_ec_field_f2mks = ecdsa_ec_field_f2mks

    @property
    def version(self):
        """Gets the version of this X509Certificate.  # noqa: E501

        Certificate version (default v1)  # noqa: E501

        :return: The version of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this X509Certificate.

        Certificate version (default v1)  # noqa: E501

        :param version: The version of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def is_ca(self):
        """Gets the is_ca of this X509Certificate.  # noqa: E501

        True if this is a CA certificate.  # noqa: E501

        :return: The is_ca of this X509Certificate.  # noqa: E501
        :rtype: bool
        """
        return self._is_ca

    @is_ca.setter
    def is_ca(self, is_ca):
        """Sets the is_ca of this X509Certificate.

        True if this is a CA certificate.  # noqa: E501

        :param is_ca: The is_ca of this X509Certificate.  # noqa: E501
        :type: bool
        """

        self._is_ca = is_ca

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this X509Certificate.  # noqa: E501

        the algorithm used by the Certificate Authority to sign the certificate  # noqa: E501

        :return: The signature_algorithm of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this X509Certificate.

        the algorithm used by the Certificate Authority to sign the certificate  # noqa: E501

        :param signature_algorithm: The signature_algorithm of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._signature_algorithm = signature_algorithm

    @property
    def ecdsa_public_key_a(self):
        """Gets the ecdsa_public_key_a of this X509Certificate.  # noqa: E501

        The first coefficient of this elliptic curve in ECDSA.  # noqa: E501

        :return: The ecdsa_public_key_a of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._ecdsa_public_key_a

    @ecdsa_public_key_a.setter
    def ecdsa_public_key_a(self, ecdsa_public_key_a):
        """Sets the ecdsa_public_key_a of this X509Certificate.

        The first coefficient of this elliptic curve in ECDSA.  # noqa: E501

        :param ecdsa_public_key_a: The ecdsa_public_key_a of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._ecdsa_public_key_a = ecdsa_public_key_a

    @property
    def rsa_public_key_exponent(self):
        """Gets the rsa_public_key_exponent of this X509Certificate.  # noqa: E501

        An RSA public key is made up of the modulus and the public exponent. Exponent is a power number  # noqa: E501

        :return: The rsa_public_key_exponent of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._rsa_public_key_exponent

    @rsa_public_key_exponent.setter
    def rsa_public_key_exponent(self, rsa_public_key_exponent):
        """Sets the rsa_public_key_exponent of this X509Certificate.

        An RSA public key is made up of the modulus and the public exponent. Exponent is a power number  # noqa: E501

        :param rsa_public_key_exponent: The rsa_public_key_exponent of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._rsa_public_key_exponent = rsa_public_key_exponent

    @property
    def ecdsa_ec_field_f2mm(self):
        """Gets the ecdsa_ec_field_f2mm of this X509Certificate.  # noqa: E501

        The first coefficient of this elliptic curve in elliptic curve (EC) | characteristic 2 finite field for ECDSA.  # noqa: E501

        :return: The ecdsa_ec_field_f2mm of this X509Certificate.  # noqa: E501
        :rtype: int
        """
        return self._ecdsa_ec_field_f2mm

    @ecdsa_ec_field_f2mm.setter
    def ecdsa_ec_field_f2mm(self, ecdsa_ec_field_f2mm):
        """Sets the ecdsa_ec_field_f2mm of this X509Certificate.

        The first coefficient of this elliptic curve in elliptic curve (EC) | characteristic 2 finite field for ECDSA.  # noqa: E501

        :param ecdsa_ec_field_f2mm: The ecdsa_ec_field_f2mm of this X509Certificate.  # noqa: E501
        :type: int
        """

        self._ecdsa_ec_field_f2mm = ecdsa_ec_field_f2mm

    @property
    def issuer_cn(self):
        """Gets the issuer_cn of this X509Certificate.  # noqa: E501

        the certificate issuer's common name  # noqa: E501

        :return: The issuer_cn of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._issuer_cn

    @issuer_cn.setter
    def issuer_cn(self, issuer_cn):
        """Sets the issuer_cn of this X509Certificate.

        the certificate issuer's common name  # noqa: E501

        :param issuer_cn: The issuer_cn of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._issuer_cn = issuer_cn

    @property
    def subject_cn(self):
        """Gets the subject_cn of this X509Certificate.  # noqa: E501

        the certificate owner's common name  # noqa: E501

        :return: The subject_cn of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._subject_cn

    @subject_cn.setter
    def subject_cn(self, subject_cn):
        """Sets the subject_cn of this X509Certificate.

        the certificate owner's common name  # noqa: E501

        :param subject_cn: The subject_cn of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._subject_cn = subject_cn

    @property
    def ecdsa_public_key_order(self):
        """Gets the ecdsa_public_key_order of this X509Certificate.  # noqa: E501

        The order of generator G in ECDSA.  # noqa: E501

        :return: The ecdsa_public_key_order of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._ecdsa_public_key_order

    @ecdsa_public_key_order.setter
    def ecdsa_public_key_order(self, ecdsa_public_key_order):
        """Sets the ecdsa_public_key_order of this X509Certificate.

        The order of generator G in ECDSA.  # noqa: E501

        :param ecdsa_public_key_order: The ecdsa_public_key_order of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._ecdsa_public_key_order = ecdsa_public_key_order

    @property
    def ecdsa_ec_field_f2mrp(self):
        """Gets the ecdsa_ec_field_f2mrp of this X509Certificate.  # noqa: E501

        The value whose i-th bit corresponds to the i-th coefficient of the reduction polynomial | in elliptic curve (EC) characteristic 2 finite field for ECDSA.  # noqa: E501

        :return: The ecdsa_ec_field_f2mrp of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._ecdsa_ec_field_f2mrp

    @ecdsa_ec_field_f2mrp.setter
    def ecdsa_ec_field_f2mrp(self, ecdsa_ec_field_f2mrp):
        """Sets the ecdsa_ec_field_f2mrp of this X509Certificate.

        The value whose i-th bit corresponds to the i-th coefficient of the reduction polynomial | in elliptic curve (EC) characteristic 2 finite field for ECDSA.  # noqa: E501

        :param ecdsa_ec_field_f2mrp: The ecdsa_ec_field_f2mrp of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._ecdsa_ec_field_f2mrp = ecdsa_ec_field_f2mrp

    @property
    def public_key_length(self):
        """Gets the public_key_length of this X509Certificate.  # noqa: E501

        size measured in bits of the public/private keys used in a cryptographic algorithm  # noqa: E501

        :return: The public_key_length of this X509Certificate.  # noqa: E501
        :rtype: int
        """
        return self._public_key_length

    @public_key_length.setter
    def public_key_length(self, public_key_length):
        """Sets the public_key_length of this X509Certificate.

        size measured in bits of the public/private keys used in a cryptographic algorithm  # noqa: E501

        :param public_key_length: The public_key_length of this X509Certificate.  # noqa: E501
        :type: int
        """

        self._public_key_length = public_key_length

    @property
    def not_before(self):
        """Gets the not_before of this X509Certificate.  # noqa: E501

        the time in epoch milliseconds at which the certificate becomes valid  # noqa: E501

        :return: The not_before of this X509Certificate.  # noqa: E501
        :rtype: int
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this X509Certificate.

        the time in epoch milliseconds at which the certificate becomes valid  # noqa: E501

        :param not_before: The not_before of this X509Certificate.  # noqa: E501
        :type: int
        """

        self._not_before = not_before

    @property
    def ecdsa_ec_field_f2pp(self):
        """Gets the ecdsa_ec_field_f2pp of this X509Certificate.  # noqa: E501

        The specified prime for the elliptic curve prime finite field in ECDSA.  # noqa: E501

        :return: The ecdsa_ec_field_f2pp of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._ecdsa_ec_field_f2pp

    @ecdsa_ec_field_f2pp.setter
    def ecdsa_ec_field_f2pp(self, ecdsa_ec_field_f2pp):
        """Sets the ecdsa_ec_field_f2pp of this X509Certificate.

        The specified prime for the elliptic curve prime finite field in ECDSA.  # noqa: E501

        :param ecdsa_ec_field_f2pp: The ecdsa_ec_field_f2pp of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._ecdsa_ec_field_f2pp = ecdsa_ec_field_f2pp

    @property
    def issuer(self):
        """Gets the issuer of this X509Certificate.  # noqa: E501

        the certificate issuers complete distinguished name  # noqa: E501

        :return: The issuer of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this X509Certificate.

        the certificate issuers complete distinguished name  # noqa: E501

        :param issuer: The issuer of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def ecdsa_public_key_b(self):
        """Gets the ecdsa_public_key_b of this X509Certificate.  # noqa: E501

        The second coefficient of this elliptic curve in ECDSA.  # noqa: E501

        :return: The ecdsa_public_key_b of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._ecdsa_public_key_b

    @ecdsa_public_key_b.setter
    def ecdsa_public_key_b(self, ecdsa_public_key_b):
        """Sets the ecdsa_public_key_b of this X509Certificate.

        The second coefficient of this elliptic curve in ECDSA.  # noqa: E501

        :param ecdsa_public_key_b: The ecdsa_public_key_b of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._ecdsa_public_key_b = ecdsa_public_key_b

    @property
    def rsa_public_key_modulus(self):
        """Gets the rsa_public_key_modulus of this X509Certificate.  # noqa: E501

        An RSA public key is made up of the modulus and the public exponent. Modulus is wrap around number  # noqa: E501

        :return: The rsa_public_key_modulus of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._rsa_public_key_modulus

    @rsa_public_key_modulus.setter
    def rsa_public_key_modulus(self, rsa_public_key_modulus):
        """Sets the rsa_public_key_modulus of this X509Certificate.

        An RSA public key is made up of the modulus and the public exponent. Modulus is wrap around number  # noqa: E501

        :param rsa_public_key_modulus: The rsa_public_key_modulus of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._rsa_public_key_modulus = rsa_public_key_modulus

    @property
    def dsa_public_key_y(self):
        """Gets the dsa_public_key_y of this X509Certificate.  # noqa: E501

        One of the DSA cryptogaphic algorithm's strength parameters  # noqa: E501

        :return: The dsa_public_key_y of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._dsa_public_key_y

    @dsa_public_key_y.setter
    def dsa_public_key_y(self, dsa_public_key_y):
        """Sets the dsa_public_key_y of this X509Certificate.

        One of the DSA cryptogaphic algorithm's strength parameters  # noqa: E501

        :param dsa_public_key_y: The dsa_public_key_y of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._dsa_public_key_y = dsa_public_key_y

    @property
    def ecdsa_public_key_cofactor(self):
        """Gets the ecdsa_public_key_cofactor of this X509Certificate.  # noqa: E501

        The co-factor in ECDSA.  # noqa: E501

        :return: The ecdsa_public_key_cofactor of this X509Certificate.  # noqa: E501
        :rtype: int
        """
        return self._ecdsa_public_key_cofactor

    @ecdsa_public_key_cofactor.setter
    def ecdsa_public_key_cofactor(self, ecdsa_public_key_cofactor):
        """Sets the ecdsa_public_key_cofactor of this X509Certificate.

        The co-factor in ECDSA.  # noqa: E501

        :param ecdsa_public_key_cofactor: The ecdsa_public_key_cofactor of this X509Certificate.  # noqa: E501
        :type: int
        """

        self._ecdsa_public_key_cofactor = ecdsa_public_key_cofactor

    @property
    def not_after(self):
        """Gets the not_after of this X509Certificate.  # noqa: E501

        the time in epoch milliseconds at which the certificate becomes invalid  # noqa: E501

        :return: The not_after of this X509Certificate.  # noqa: E501
        :rtype: int
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this X509Certificate.

        the time in epoch milliseconds at which the certificate becomes invalid  # noqa: E501

        :param not_after: The not_after of this X509Certificate.  # noqa: E501
        :type: int
        """

        self._not_after = not_after

    @property
    def dsa_public_key_q(self):
        """Gets the dsa_public_key_q of this X509Certificate.  # noqa: E501

        One of the DSA cryptogaphic algorithm's strength parameters, sub-prime  # noqa: E501

        :return: The dsa_public_key_q of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._dsa_public_key_q

    @dsa_public_key_q.setter
    def dsa_public_key_q(self, dsa_public_key_q):
        """Sets the dsa_public_key_q of this X509Certificate.

        One of the DSA cryptogaphic algorithm's strength parameters, sub-prime  # noqa: E501

        :param dsa_public_key_q: The dsa_public_key_q of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._dsa_public_key_q = dsa_public_key_q

    @property
    def dsa_public_key_p(self):
        """Gets the dsa_public_key_p of this X509Certificate.  # noqa: E501

        One of the DSA cryptogaphic algorithm's strength parameters, prime  # noqa: E501

        :return: The dsa_public_key_p of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._dsa_public_key_p

    @dsa_public_key_p.setter
    def dsa_public_key_p(self, dsa_public_key_p):
        """Sets the dsa_public_key_p of this X509Certificate.

        One of the DSA cryptogaphic algorithm's strength parameters, prime  # noqa: E501

        :param dsa_public_key_p: The dsa_public_key_p of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._dsa_public_key_p = dsa_public_key_p

    @property
    def ecdsa_public_key_generator_y(self):
        """Gets the ecdsa_public_key_generator_y of this X509Certificate.  # noqa: E501

        y co-ordinate of G (the generator which is also known as the base point) in ECDSA.  # noqa: E501

        :return: The ecdsa_public_key_generator_y of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._ecdsa_public_key_generator_y

    @ecdsa_public_key_generator_y.setter
    def ecdsa_public_key_generator_y(self, ecdsa_public_key_generator_y):
        """Sets the ecdsa_public_key_generator_y of this X509Certificate.

        y co-ordinate of G (the generator which is also known as the base point) in ECDSA.  # noqa: E501

        :param ecdsa_public_key_generator_y: The ecdsa_public_key_generator_y of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._ecdsa_public_key_generator_y = ecdsa_public_key_generator_y

    @property
    def ecdsa_public_key_generator_x(self):
        """Gets the ecdsa_public_key_generator_x of this X509Certificate.  # noqa: E501

        x co-ordinate of G (the generator which is also known as the base point) in ECDSA.  # noqa: E501

        :return: The ecdsa_public_key_generator_x of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._ecdsa_public_key_generator_x

    @ecdsa_public_key_generator_x.setter
    def ecdsa_public_key_generator_x(self, ecdsa_public_key_generator_x):
        """Sets the ecdsa_public_key_generator_x of this X509Certificate.

        x co-ordinate of G (the generator which is also known as the base point) in ECDSA.  # noqa: E501

        :param ecdsa_public_key_generator_x: The ecdsa_public_key_generator_x of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._ecdsa_public_key_generator_x = ecdsa_public_key_generator_x

    @property
    def public_key_algo(self):
        """Gets the public_key_algo of this X509Certificate.  # noqa: E501

        Cryptographic algorithm used by the public key for data encryption.  # noqa: E501

        :return: The public_key_algo of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._public_key_algo

    @public_key_algo.setter
    def public_key_algo(self, public_key_algo):
        """Sets the public_key_algo of this X509Certificate.

        Cryptographic algorithm used by the public key for data encryption.  # noqa: E501

        :param public_key_algo: The public_key_algo of this X509Certificate.  # noqa: E501
        :type: str
        """
        allowed_values = ["RSA", "DSA", "ECDSA"]  # noqa: E501
        if public_key_algo not in allowed_values:
            raise ValueError(
                "Invalid value for `public_key_algo` ({0}), must be one of {1}"  # noqa: E501
                .format(public_key_algo, allowed_values)
            )

        self._public_key_algo = public_key_algo

    @property
    def is_valid(self):
        """Gets the is_valid of this X509Certificate.  # noqa: E501

        True if this certificate is valid.  # noqa: E501

        :return: The is_valid of this X509Certificate.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this X509Certificate.

        True if this certificate is valid.  # noqa: E501

        :param is_valid: The is_valid of this X509Certificate.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def ecdsa_public_key_seed(self):
        """Gets the ecdsa_public_key_seed of this X509Certificate.  # noqa: E501

        The bytes used during curve generation for later validation in ECDSA.| Contents of this array are copied to protect against subsequent modification.  # noqa: E501

        :return: The ecdsa_public_key_seed of this X509Certificate.  # noqa: E501
        :rtype: list[str]
        """
        return self._ecdsa_public_key_seed

    @ecdsa_public_key_seed.setter
    def ecdsa_public_key_seed(self, ecdsa_public_key_seed):
        """Sets the ecdsa_public_key_seed of this X509Certificate.

        The bytes used during curve generation for later validation in ECDSA.| Contents of this array are copied to protect against subsequent modification.  # noqa: E501

        :param ecdsa_public_key_seed: The ecdsa_public_key_seed of this X509Certificate.  # noqa: E501
        :type: list[str]
        """

        self._ecdsa_public_key_seed = ecdsa_public_key_seed

    @property
    def signature(self):
        """Gets the signature of this X509Certificate.  # noqa: E501

        the signature value(the raw signature bits) used for signing and validate the cert  # noqa: E501

        :return: The signature of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this X509Certificate.

        the signature value(the raw signature bits) used for signing and validate the cert  # noqa: E501

        :param signature: The signature of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def serial_number(self):
        """Gets the serial_number of this X509Certificate.  # noqa: E501

        certificate's serial number  # noqa: E501

        :return: The serial_number of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this X509Certificate.

        certificate's serial number  # noqa: E501

        :param serial_number: The serial_number of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def dsa_public_key_g(self):
        """Gets the dsa_public_key_g of this X509Certificate.  # noqa: E501

        One of the DSA cryptogaphic algorithm's strength parameters, base  # noqa: E501

        :return: The dsa_public_key_g of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._dsa_public_key_g

    @dsa_public_key_g.setter
    def dsa_public_key_g(self, dsa_public_key_g):
        """Sets the dsa_public_key_g of this X509Certificate.

        One of the DSA cryptogaphic algorithm's strength parameters, base  # noqa: E501

        :param dsa_public_key_g: The dsa_public_key_g of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._dsa_public_key_g = dsa_public_key_g

    @property
    def subject(self):
        """Gets the subject of this X509Certificate.  # noqa: E501

        the certificate owners complete distinguished name  # noqa: E501

        :return: The subject of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this X509Certificate.

        the certificate owners complete distinguished name  # noqa: E501

        :param subject: The subject of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def ecdsa_ec_field(self):
        """Gets the ecdsa_ec_field of this X509Certificate.  # noqa: E501

        Represents an elliptic curve (EC) finite field in ECDSA.  # noqa: E501

        :return: The ecdsa_ec_field of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._ecdsa_ec_field

    @ecdsa_ec_field.setter
    def ecdsa_ec_field(self, ecdsa_ec_field):
        """Sets the ecdsa_ec_field of this X509Certificate.

        Represents an elliptic curve (EC) finite field in ECDSA.  # noqa: E501

        :param ecdsa_ec_field: The ecdsa_ec_field of this X509Certificate.  # noqa: E501
        :type: str
        """
        allowed_values = ["F2M", "FP"]  # noqa: E501
        if ecdsa_ec_field not in allowed_values:
            raise ValueError(
                "Invalid value for `ecdsa_ec_field` ({0}), must be one of {1}"  # noqa: E501
                .format(ecdsa_ec_field, allowed_values)
            )

        self._ecdsa_ec_field = ecdsa_ec_field

    @property
    def ecdsa_curve_name(self):
        """Gets the ecdsa_curve_name of this X509Certificate.  # noqa: E501

        The Curve name for the ECDSA certificate.  # noqa: E501

        :return: The ecdsa_curve_name of this X509Certificate.  # noqa: E501
        :rtype: str
        """
        return self._ecdsa_curve_name

    @ecdsa_curve_name.setter
    def ecdsa_curve_name(self, ecdsa_curve_name):
        """Sets the ecdsa_curve_name of this X509Certificate.

        The Curve name for the ECDSA certificate.  # noqa: E501

        :param ecdsa_curve_name: The ecdsa_curve_name of this X509Certificate.  # noqa: E501
        :type: str
        """

        self._ecdsa_curve_name = ecdsa_curve_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(X509Certificate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, X509Certificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
