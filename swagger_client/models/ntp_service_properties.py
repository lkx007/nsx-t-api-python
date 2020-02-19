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


class NtpServiceProperties(object):
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
        'start_on_boot': 'bool',
        'servers': 'list[str]'
    }

    attribute_map = {
        'start_on_boot': 'start_on_boot',
        'servers': 'servers'
    }

    def __init__(self, start_on_boot=True, servers=None):  # noqa: E501
        """NtpServiceProperties - a model defined in Swagger"""  # noqa: E501
        self._start_on_boot = None
        self._servers = None
        self.discriminator = None
        if start_on_boot is not None:
            self.start_on_boot = start_on_boot
        self.servers = servers

    @property
    def start_on_boot(self):
        """Gets the start_on_boot of this NtpServiceProperties.  # noqa: E501

        Start NTP service when system boots  # noqa: E501

        :return: The start_on_boot of this NtpServiceProperties.  # noqa: E501
        :rtype: bool
        """
        return self._start_on_boot

    @start_on_boot.setter
    def start_on_boot(self, start_on_boot):
        """Sets the start_on_boot of this NtpServiceProperties.

        Start NTP service when system boots  # noqa: E501

        :param start_on_boot: The start_on_boot of this NtpServiceProperties.  # noqa: E501
        :type: bool
        """

        self._start_on_boot = start_on_boot

    @property
    def servers(self):
        """Gets the servers of this NtpServiceProperties.  # noqa: E501

        NTP servers  # noqa: E501

        :return: The servers of this NtpServiceProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this NtpServiceProperties.

        NTP servers  # noqa: E501

        :param servers: The servers of this NtpServiceProperties.  # noqa: E501
        :type: list[str]
        """
        if servers is None:
            raise ValueError("Invalid value for `servers`, must not be `None`")  # noqa: E501

        self._servers = servers

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
        if issubclass(NtpServiceProperties, dict):
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
        if not isinstance(other, NtpServiceProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
