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


class LbSslCipherInfo(object):
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
        'is_default': 'bool',
        'is_secure': 'bool',
        'cipher_group_labels': 'list[str]',
        'cipher': 'str'
    }

    attribute_map = {
        'is_default': 'is_default',
        'is_secure': 'is_secure',
        'cipher_group_labels': 'cipher_group_labels',
        'cipher': 'cipher'
    }

    def __init__(self, is_default=None, is_secure=None, cipher_group_labels=None, cipher=None):  # noqa: E501
        """LbSslCipherInfo - a model defined in Swagger"""  # noqa: E501
        self._is_default = None
        self._is_secure = None
        self._cipher_group_labels = None
        self._cipher = None
        self.discriminator = None
        self.is_default = is_default
        self.is_secure = is_secure
        if cipher_group_labels is not None:
            self.cipher_group_labels = cipher_group_labels
        self.cipher = cipher

    @property
    def is_default(self):
        """Gets the is_default of this LbSslCipherInfo.  # noqa: E501

        Default SSL cipher flag  # noqa: E501

        :return: The is_default of this LbSslCipherInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this LbSslCipherInfo.

        Default SSL cipher flag  # noqa: E501

        :param is_default: The is_default of this LbSslCipherInfo.  # noqa: E501
        :type: bool
        """
        if is_default is None:
            raise ValueError("Invalid value for `is_default`, must not be `None`")  # noqa: E501

        self._is_default = is_default

    @property
    def is_secure(self):
        """Gets the is_secure of this LbSslCipherInfo.  # noqa: E501

        Secure/insecure SSL cipher flag  # noqa: E501

        :return: The is_secure of this LbSslCipherInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_secure

    @is_secure.setter
    def is_secure(self, is_secure):
        """Sets the is_secure of this LbSslCipherInfo.

        Secure/insecure SSL cipher flag  # noqa: E501

        :param is_secure: The is_secure of this LbSslCipherInfo.  # noqa: E501
        :type: bool
        """
        if is_secure is None:
            raise ValueError("Invalid value for `is_secure`, must not be `None`")  # noqa: E501

        self._is_secure = is_secure

    @property
    def cipher_group_labels(self):
        """Gets the cipher_group_labels of this LbSslCipherInfo.  # noqa: E501

        Several cipher groups might contain the same cipher suite, each cipher suite could have multiple cipher group labels.   # noqa: E501

        :return: The cipher_group_labels of this LbSslCipherInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._cipher_group_labels

    @cipher_group_labels.setter
    def cipher_group_labels(self, cipher_group_labels):
        """Sets the cipher_group_labels of this LbSslCipherInfo.

        Several cipher groups might contain the same cipher suite, each cipher suite could have multiple cipher group labels.   # noqa: E501

        :param cipher_group_labels: The cipher_group_labels of this LbSslCipherInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["BALANCED", "HIGH_SECURITY", "HIGH_COMPATIBILITY", "CUSTOM"]  # noqa: E501
        if not set(cipher_group_labels).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `cipher_group_labels` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(cipher_group_labels) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._cipher_group_labels = cipher_group_labels

    @property
    def cipher(self):
        """Gets the cipher of this LbSslCipherInfo.  # noqa: E501

        SSL cipher  # noqa: E501

        :return: The cipher of this LbSslCipherInfo.  # noqa: E501
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this LbSslCipherInfo.

        SSL cipher  # noqa: E501

        :param cipher: The cipher of this LbSslCipherInfo.  # noqa: E501
        :type: str
        """
        if cipher is None:
            raise ValueError("Invalid value for `cipher`, must not be `None`")  # noqa: E501
        allowed_values = ["TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA", "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA", "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA", "TLS_RSA_WITH_AES_256_CBC_SHA", "TLS_RSA_WITH_AES_128_CBC_SHA", "TLS_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384", "TLS_RSA_WITH_AES_128_CBC_SHA256", "TLS_RSA_WITH_AES_128_GCM_SHA256", "TLS_RSA_WITH_AES_256_CBC_SHA256", "TLS_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA", "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384", "TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA", "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384", "TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384"]  # noqa: E501
        if cipher not in allowed_values:
            raise ValueError(
                "Invalid value for `cipher` ({0}), must be one of {1}"  # noqa: E501
                .format(cipher, allowed_values)
            )

        self._cipher = cipher

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
        if issubclass(LbSslCipherInfo, dict):
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
        if not isinstance(other, LbSslCipherInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
