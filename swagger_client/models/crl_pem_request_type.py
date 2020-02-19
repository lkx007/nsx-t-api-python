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


class CrlPemRequestType(object):
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
        'cdp_uri': 'str'
    }

    attribute_map = {
        'cdp_uri': 'cdp_uri'
    }

    def __init__(self, cdp_uri=None):  # noqa: E501
        """CrlPemRequestType - a model defined in Swagger"""  # noqa: E501
        self._cdp_uri = None
        self.discriminator = None
        if cdp_uri is not None:
            self.cdp_uri = cdp_uri

    @property
    def cdp_uri(self):
        """Gets the cdp_uri of this CrlPemRequestType.  # noqa: E501

        CRL Distribution Point URI where to fetch the CRL.  # noqa: E501

        :return: The cdp_uri of this CrlPemRequestType.  # noqa: E501
        :rtype: str
        """
        return self._cdp_uri

    @cdp_uri.setter
    def cdp_uri(self, cdp_uri):
        """Sets the cdp_uri of this CrlPemRequestType.

        CRL Distribution Point URI where to fetch the CRL.  # noqa: E501

        :param cdp_uri: The cdp_uri of this CrlPemRequestType.  # noqa: E501
        :type: str
        """

        self._cdp_uri = cdp_uri

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
        if issubclass(CrlPemRequestType, dict):
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
        if not isinstance(other, CrlPemRequestType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
