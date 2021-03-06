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


class NatCounters(object):
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
        'total_packets': 'int',
        'total_bytes': 'int',
        'active_sessions': 'int'
    }

    attribute_map = {
        'total_packets': 'total_packets',
        'total_bytes': 'total_bytes',
        'active_sessions': 'active_sessions'
    }

    def __init__(self, total_packets=None, total_bytes=None, active_sessions=None):  # noqa: E501
        """NatCounters - a model defined in Swagger"""  # noqa: E501
        self._total_packets = None
        self._total_bytes = None
        self._active_sessions = None
        self.discriminator = None
        if total_packets is not None:
            self.total_packets = total_packets
        if total_bytes is not None:
            self.total_bytes = total_bytes
        if active_sessions is not None:
            self.active_sessions = active_sessions

    @property
    def total_packets(self):
        """Gets the total_packets of this NatCounters.  # noqa: E501

        The number of packets  # noqa: E501

        :return: The total_packets of this NatCounters.  # noqa: E501
        :rtype: int
        """
        return self._total_packets

    @total_packets.setter
    def total_packets(self, total_packets):
        """Sets the total_packets of this NatCounters.

        The number of packets  # noqa: E501

        :param total_packets: The total_packets of this NatCounters.  # noqa: E501
        :type: int
        """

        self._total_packets = total_packets

    @property
    def total_bytes(self):
        """Gets the total_bytes of this NatCounters.  # noqa: E501

        The number of bytes  # noqa: E501

        :return: The total_bytes of this NatCounters.  # noqa: E501
        :rtype: int
        """
        return self._total_bytes

    @total_bytes.setter
    def total_bytes(self, total_bytes):
        """Sets the total_bytes of this NatCounters.

        The number of bytes  # noqa: E501

        :param total_bytes: The total_bytes of this NatCounters.  # noqa: E501
        :type: int
        """

        self._total_bytes = total_bytes

    @property
    def active_sessions(self):
        """Gets the active_sessions of this NatCounters.  # noqa: E501

        The number of active sessions  # noqa: E501

        :return: The active_sessions of this NatCounters.  # noqa: E501
        :rtype: int
        """
        return self._active_sessions

    @active_sessions.setter
    def active_sessions(self, active_sessions):
        """Sets the active_sessions of this NatCounters.

        The number of active sessions  # noqa: E501

        :param active_sessions: The active_sessions of this NatCounters.  # noqa: E501
        :type: int
        """

        self._active_sessions = active_sessions

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
        if issubclass(NatCounters, dict):
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
        if not isinstance(other, NatCounters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
