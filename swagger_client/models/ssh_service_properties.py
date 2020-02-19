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


class SshServiceProperties(object):
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
        'start_on_boot': 'bool'
    }

    attribute_map = {
        'start_on_boot': 'start_on_boot'
    }

    def __init__(self, start_on_boot=None):  # noqa: E501
        """SshServiceProperties - a model defined in Swagger"""  # noqa: E501
        self._start_on_boot = None
        self.discriminator = None
        self.start_on_boot = start_on_boot

    @property
    def start_on_boot(self):
        """Gets the start_on_boot of this SshServiceProperties.  # noqa: E501

        Start service when system boots  # noqa: E501

        :return: The start_on_boot of this SshServiceProperties.  # noqa: E501
        :rtype: bool
        """
        return self._start_on_boot

    @start_on_boot.setter
    def start_on_boot(self, start_on_boot):
        """Sets the start_on_boot of this SshServiceProperties.

        Start service when system boots  # noqa: E501

        :param start_on_boot: The start_on_boot of this SshServiceProperties.  # noqa: E501
        :type: bool
        """
        if start_on_boot is None:
            raise ValueError("Invalid value for `start_on_boot`, must not be `None`")  # noqa: E501

        self._start_on_boot = start_on_boot

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
        if issubclass(SshServiceProperties, dict):
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
        if not isinstance(other, SshServiceProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other