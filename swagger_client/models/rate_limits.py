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


class RateLimits(object):
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
        'rx_multicast': 'int',
        'tx_multicast': 'int',
        'enabled': 'bool',
        'tx_broadcast': 'int',
        'rx_broadcast': 'int'
    }

    attribute_map = {
        'rx_multicast': 'rx_multicast',
        'tx_multicast': 'tx_multicast',
        'enabled': 'enabled',
        'tx_broadcast': 'tx_broadcast',
        'rx_broadcast': 'rx_broadcast'
    }

    def __init__(self, rx_multicast=0, tx_multicast=0, enabled=False, tx_broadcast=0, rx_broadcast=0):  # noqa: E501
        """RateLimits - a model defined in Swagger"""  # noqa: E501
        self._rx_multicast = None
        self._tx_multicast = None
        self._enabled = None
        self._tx_broadcast = None
        self._rx_broadcast = None
        self.discriminator = None
        if rx_multicast is not None:
            self.rx_multicast = rx_multicast
        if tx_multicast is not None:
            self.tx_multicast = tx_multicast
        if enabled is not None:
            self.enabled = enabled
        if tx_broadcast is not None:
            self.tx_broadcast = tx_broadcast
        if rx_broadcast is not None:
            self.rx_broadcast = rx_broadcast

    @property
    def rx_multicast(self):
        """Gets the rx_multicast of this RateLimits.  # noqa: E501

        Incoming multicast traffic limit in packets per second  # noqa: E501

        :return: The rx_multicast of this RateLimits.  # noqa: E501
        :rtype: int
        """
        return self._rx_multicast

    @rx_multicast.setter
    def rx_multicast(self, rx_multicast):
        """Sets the rx_multicast of this RateLimits.

        Incoming multicast traffic limit in packets per second  # noqa: E501

        :param rx_multicast: The rx_multicast of this RateLimits.  # noqa: E501
        :type: int
        """

        self._rx_multicast = rx_multicast

    @property
    def tx_multicast(self):
        """Gets the tx_multicast of this RateLimits.  # noqa: E501

        Outgoing multicast traffic limit in packets per second  # noqa: E501

        :return: The tx_multicast of this RateLimits.  # noqa: E501
        :rtype: int
        """
        return self._tx_multicast

    @tx_multicast.setter
    def tx_multicast(self, tx_multicast):
        """Sets the tx_multicast of this RateLimits.

        Outgoing multicast traffic limit in packets per second  # noqa: E501

        :param tx_multicast: The tx_multicast of this RateLimits.  # noqa: E501
        :type: int
        """

        self._tx_multicast = tx_multicast

    @property
    def enabled(self):
        """Gets the enabled of this RateLimits.  # noqa: E501

        Whether rate limiting is enabled  # noqa: E501

        :return: The enabled of this RateLimits.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this RateLimits.

        Whether rate limiting is enabled  # noqa: E501

        :param enabled: The enabled of this RateLimits.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def tx_broadcast(self):
        """Gets the tx_broadcast of this RateLimits.  # noqa: E501

        Outgoing broadcast traffic limit in packets per second  # noqa: E501

        :return: The tx_broadcast of this RateLimits.  # noqa: E501
        :rtype: int
        """
        return self._tx_broadcast

    @tx_broadcast.setter
    def tx_broadcast(self, tx_broadcast):
        """Sets the tx_broadcast of this RateLimits.

        Outgoing broadcast traffic limit in packets per second  # noqa: E501

        :param tx_broadcast: The tx_broadcast of this RateLimits.  # noqa: E501
        :type: int
        """

        self._tx_broadcast = tx_broadcast

    @property
    def rx_broadcast(self):
        """Gets the rx_broadcast of this RateLimits.  # noqa: E501

        Incoming broadcast traffic limit in packets per second  # noqa: E501

        :return: The rx_broadcast of this RateLimits.  # noqa: E501
        :rtype: int
        """
        return self._rx_broadcast

    @rx_broadcast.setter
    def rx_broadcast(self, rx_broadcast):
        """Sets the rx_broadcast of this RateLimits.

        Incoming broadcast traffic limit in packets per second  # noqa: E501

        :param rx_broadcast: The rx_broadcast of this RateLimits.  # noqa: E501
        :type: int
        """

        self._rx_broadcast = rx_broadcast

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
        if issubclass(RateLimits, dict):
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
        if not isinstance(other, RateLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
