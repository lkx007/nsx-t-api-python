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


class LbHttpRequestHeader(object):
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
        'header_value': 'str',
        'header_name': 'str'
    }

    attribute_map = {
        'header_value': 'header_value',
        'header_name': 'header_name'
    }

    def __init__(self, header_value=None, header_name=None):  # noqa: E501
        """LbHttpRequestHeader - a model defined in Swagger"""  # noqa: E501
        self._header_value = None
        self._header_name = None
        self.discriminator = None
        self.header_value = header_value
        self.header_name = header_name

    @property
    def header_value(self):
        """Gets the header_value of this LbHttpRequestHeader.  # noqa: E501

        Value of HTTP request header  # noqa: E501

        :return: The header_value of this LbHttpRequestHeader.  # noqa: E501
        :rtype: str
        """
        return self._header_value

    @header_value.setter
    def header_value(self, header_value):
        """Sets the header_value of this LbHttpRequestHeader.

        Value of HTTP request header  # noqa: E501

        :param header_value: The header_value of this LbHttpRequestHeader.  # noqa: E501
        :type: str
        """
        if header_value is None:
            raise ValueError("Invalid value for `header_value`, must not be `None`")  # noqa: E501

        self._header_value = header_value

    @property
    def header_name(self):
        """Gets the header_name of this LbHttpRequestHeader.  # noqa: E501

        Name of HTTP request header  # noqa: E501

        :return: The header_name of this LbHttpRequestHeader.  # noqa: E501
        :rtype: str
        """
        return self._header_name

    @header_name.setter
    def header_name(self, header_name):
        """Sets the header_name of this LbHttpRequestHeader.

        Name of HTTP request header  # noqa: E501

        :param header_name: The header_name of this LbHttpRequestHeader.  # noqa: E501
        :type: str
        """
        if header_name is None:
            raise ValueError("Invalid value for `header_name`, must not be `None`")  # noqa: E501

        self._header_name = header_name

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
        if issubclass(LbHttpRequestHeader, dict):
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
        if not isinstance(other, LbHttpRequestHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
