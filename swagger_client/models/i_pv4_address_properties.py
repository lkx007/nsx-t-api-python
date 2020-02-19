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


class IPv4AddressProperties(object):
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
        'netmask': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'netmask': 'netmask',
        'ip_address': 'ip_address'
    }

    def __init__(self, netmask=None, ip_address=None):  # noqa: E501
        """IPv4AddressProperties - a model defined in Swagger"""  # noqa: E501
        self._netmask = None
        self._ip_address = None
        self.discriminator = None
        if netmask is not None:
            self.netmask = netmask
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def netmask(self):
        """Gets the netmask of this IPv4AddressProperties.  # noqa: E501

        Interface netmask  # noqa: E501

        :return: The netmask of this IPv4AddressProperties.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this IPv4AddressProperties.

        Interface netmask  # noqa: E501

        :param netmask: The netmask of this IPv4AddressProperties.  # noqa: E501
        :type: str
        """

        self._netmask = netmask

    @property
    def ip_address(self):
        """Gets the ip_address of this IPv4AddressProperties.  # noqa: E501

        Interface IPv4 address  # noqa: E501

        :return: The ip_address of this IPv4AddressProperties.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this IPv4AddressProperties.

        Interface IPv4 address  # noqa: E501

        :param ip_address: The ip_address of this IPv4AddressProperties.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

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
        if issubclass(IPv4AddressProperties, dict):
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
        if not isinstance(other, IPv4AddressProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
