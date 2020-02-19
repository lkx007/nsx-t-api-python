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


class IngressRateShaper(object):
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
        'enabled': 'bool',
        'resource_type': 'str',
        'average_bandwidth_mbps': 'int',
        'peak_bandwidth_mbps': 'int',
        'burst_size_bytes': 'int'
    }
    if hasattr(QosBaseRateShaper, "swagger_types"):
        swagger_types.update(QosBaseRateShaper.swagger_types)

    attribute_map = {
        'enabled': 'enabled',
        'resource_type': 'resource_type',
        'average_bandwidth_mbps': 'average_bandwidth_mbps',
        'peak_bandwidth_mbps': 'peak_bandwidth_mbps',
        'burst_size_bytes': 'burst_size_bytes'
    }
    if hasattr(QosBaseRateShaper, "attribute_map"):
        attribute_map.update(QosBaseRateShaper.attribute_map)

    def __init__(self, enabled=None, resource_type=None, average_bandwidth_mbps=0, peak_bandwidth_mbps=0, burst_size_bytes=0, *args, **kwargs):  # noqa: E501
        """IngressRateShaper - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._resource_type = None
        self._average_bandwidth_mbps = None
        self._peak_bandwidth_mbps = None
        self._burst_size_bytes = None
        self.discriminator = None
        self.enabled = enabled
        self.resource_type = resource_type
        if average_bandwidth_mbps is not None:
            self.average_bandwidth_mbps = average_bandwidth_mbps
        if peak_bandwidth_mbps is not None:
            self.peak_bandwidth_mbps = peak_bandwidth_mbps
        if burst_size_bytes is not None:
            self.burst_size_bytes = burst_size_bytes
        QosBaseRateShaper.__init__(self, *args, **kwargs)

    @property
    def enabled(self):
        """Gets the enabled of this IngressRateShaper.  # noqa: E501


        :return: The enabled of this IngressRateShaper.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IngressRateShaper.


        :param enabled: The enabled of this IngressRateShaper.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def resource_type(self):
        """Gets the resource_type of this IngressRateShaper.  # noqa: E501


        :return: The resource_type of this IngressRateShaper.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this IngressRateShaper.


        :param resource_type: The resource_type of this IngressRateShaper.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["IngressRateShaper", "IngressBroadcastRateShaper", "EgressRateShaper"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def average_bandwidth_mbps(self):
        """Gets the average_bandwidth_mbps of this IngressRateShaper.  # noqa: E501

        Average bandwidth in Mb/s  # noqa: E501

        :return: The average_bandwidth_mbps of this IngressRateShaper.  # noqa: E501
        :rtype: int
        """
        return self._average_bandwidth_mbps

    @average_bandwidth_mbps.setter
    def average_bandwidth_mbps(self, average_bandwidth_mbps):
        """Sets the average_bandwidth_mbps of this IngressRateShaper.

        Average bandwidth in Mb/s  # noqa: E501

        :param average_bandwidth_mbps: The average_bandwidth_mbps of this IngressRateShaper.  # noqa: E501
        :type: int
        """

        self._average_bandwidth_mbps = average_bandwidth_mbps

    @property
    def peak_bandwidth_mbps(self):
        """Gets the peak_bandwidth_mbps of this IngressRateShaper.  # noqa: E501

        Peak bandwidth in Mb/s  # noqa: E501

        :return: The peak_bandwidth_mbps of this IngressRateShaper.  # noqa: E501
        :rtype: int
        """
        return self._peak_bandwidth_mbps

    @peak_bandwidth_mbps.setter
    def peak_bandwidth_mbps(self, peak_bandwidth_mbps):
        """Sets the peak_bandwidth_mbps of this IngressRateShaper.

        Peak bandwidth in Mb/s  # noqa: E501

        :param peak_bandwidth_mbps: The peak_bandwidth_mbps of this IngressRateShaper.  # noqa: E501
        :type: int
        """

        self._peak_bandwidth_mbps = peak_bandwidth_mbps

    @property
    def burst_size_bytes(self):
        """Gets the burst_size_bytes of this IngressRateShaper.  # noqa: E501

        Burst size in bytes  # noqa: E501

        :return: The burst_size_bytes of this IngressRateShaper.  # noqa: E501
        :rtype: int
        """
        return self._burst_size_bytes

    @burst_size_bytes.setter
    def burst_size_bytes(self, burst_size_bytes):
        """Sets the burst_size_bytes of this IngressRateShaper.

        Burst size in bytes  # noqa: E501

        :param burst_size_bytes: The burst_size_bytes of this IngressRateShaper.  # noqa: E501
        :type: int
        """

        self._burst_size_bytes = burst_size_bytes

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
        if issubclass(IngressRateShaper, dict):
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
        if not isinstance(other, IngressRateShaper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
