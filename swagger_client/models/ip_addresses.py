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


class IPAddresses(object):
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
        'ip_addresses': 'list[str]'
    }

    attribute_map = {
        'ip_addresses': 'ip_addresses'
    }

    def __init__(self, ip_addresses=None):  # noqa: E501
        """IPAddresses - a model defined in Swagger"""  # noqa: E501
        self._ip_addresses = None
        self.discriminator = None
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this IPAddresses.  # noqa: E501

        The IP addresses in the form of IP Address, IP Range, CIDR, used as source IPs or destination IPs of filters.  # noqa: E501

        :return: The ip_addresses of this IPAddresses.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this IPAddresses.

        The IP addresses in the form of IP Address, IP Range, CIDR, used as source IPs or destination IPs of filters.  # noqa: E501

        :param ip_addresses: The ip_addresses of this IPAddresses.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

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
        if issubclass(IPAddresses, dict):
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
        if not isinstance(other, IPAddresses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
