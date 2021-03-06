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


class DnsHeader(object):
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
        'address_type': 'str',
        'message_type': 'str',
        'address': 'str'
    }

    attribute_map = {
        'address_type': 'address_type',
        'message_type': 'message_type',
        'address': 'address'
    }

    def __init__(self, address_type='V4', message_type='QUERY', address=None):  # noqa: E501
        """DnsHeader - a model defined in Swagger"""  # noqa: E501
        self._address_type = None
        self._message_type = None
        self._address = None
        self.discriminator = None
        if address_type is not None:
            self.address_type = address_type
        if message_type is not None:
            self.message_type = message_type
        if address is not None:
            self.address = address

    @property
    def address_type(self):
        """Gets the address_type of this DnsHeader.  # noqa: E501

        This is used to specify the type of the address. V4 - The address provided is an IPv4 domain name/IP address, the Type in query or response will be A V6 - The address provided is an IPv6 domain name/IP address, the Type in query or response will be AAAA  # noqa: E501

        :return: The address_type of this DnsHeader.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this DnsHeader.

        This is used to specify the type of the address. V4 - The address provided is an IPv4 domain name/IP address, the Type in query or response will be A V6 - The address provided is an IPv6 domain name/IP address, the Type in query or response will be AAAA  # noqa: E501

        :param address_type: The address_type of this DnsHeader.  # noqa: E501
        :type: str
        """
        allowed_values = ["V4", "V6"]  # noqa: E501
        if address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `address_type` ({0}), must be one of {1}"  # noqa: E501
                .format(address_type, allowed_values)
            )

        self._address_type = address_type

    @property
    def message_type(self):
        """Gets the message_type of this DnsHeader.  # noqa: E501

        Specifies the message type whether it is a query or a response.  # noqa: E501

        :return: The message_type of this DnsHeader.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this DnsHeader.

        Specifies the message type whether it is a query or a response.  # noqa: E501

        :param message_type: The message_type of this DnsHeader.  # noqa: E501
        :type: str
        """
        allowed_values = ["QUERY", "RESPONSE"]  # noqa: E501
        if message_type not in allowed_values:
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"  # noqa: E501
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def address(self):
        """Gets the address of this DnsHeader.  # noqa: E501

        This is used to define what is being asked or responded.  # noqa: E501

        :return: The address of this DnsHeader.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DnsHeader.

        This is used to define what is being asked or responded.  # noqa: E501

        :param address: The address of this DnsHeader.  # noqa: E501
        :type: str
        """

        self._address = address

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
        if issubclass(DnsHeader, dict):
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
        if not isinstance(other, DnsHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
