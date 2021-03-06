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


class IpfixCollector(object):
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
        'collector_ip_address': 'str',
        'collector_port': 'int'
    }

    attribute_map = {
        'collector_ip_address': 'collector_ip_address',
        'collector_port': 'collector_port'
    }

    def __init__(self, collector_ip_address=None, collector_port=4739):  # noqa: E501
        """IpfixCollector - a model defined in Swagger"""  # noqa: E501
        self._collector_ip_address = None
        self._collector_port = None
        self.discriminator = None
        self.collector_ip_address = collector_ip_address
        if collector_port is not None:
            self.collector_port = collector_port

    @property
    def collector_ip_address(self):
        """Gets the collector_ip_address of this IpfixCollector.  # noqa: E501

        IP address for the IPFIX collector  # noqa: E501

        :return: The collector_ip_address of this IpfixCollector.  # noqa: E501
        :rtype: str
        """
        return self._collector_ip_address

    @collector_ip_address.setter
    def collector_ip_address(self, collector_ip_address):
        """Sets the collector_ip_address of this IpfixCollector.

        IP address for the IPFIX collector  # noqa: E501

        :param collector_ip_address: The collector_ip_address of this IpfixCollector.  # noqa: E501
        :type: str
        """
        if collector_ip_address is None:
            raise ValueError("Invalid value for `collector_ip_address`, must not be `None`")  # noqa: E501

        self._collector_ip_address = collector_ip_address

    @property
    def collector_port(self):
        """Gets the collector_port of this IpfixCollector.  # noqa: E501

        Port for the IPFIX collector  # noqa: E501

        :return: The collector_port of this IpfixCollector.  # noqa: E501
        :rtype: int
        """
        return self._collector_port

    @collector_port.setter
    def collector_port(self, collector_port):
        """Sets the collector_port of this IpfixCollector.

        Port for the IPFIX collector  # noqa: E501

        :param collector_port: The collector_port of this IpfixCollector.  # noqa: E501
        :type: int
        """

        self._collector_port = collector_port

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
        if issubclass(IpfixCollector, dict):
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
        if not isinstance(other, IpfixCollector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
