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


class FirewallFloodProtectionProfile(object):
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
        'resource_type': 'str',
        'icmp_active_flow_limit': 'int',
        'other_active_conn_limit': 'int',
        'enable_syncache': 'bool',
        'udp_active_flow_limit': 'int',
        'tcp_half_open_conn_limit': 'int',
        'enable_rst_spoofing': 'bool'
    }
    if hasattr(BaseFirewallProfile, "swagger_types"):
        swagger_types.update(BaseFirewallProfile.swagger_types)

    attribute_map = {
        'resource_type': 'resource_type',
        'icmp_active_flow_limit': 'icmp_active_flow_limit',
        'other_active_conn_limit': 'other_active_conn_limit',
        'enable_syncache': 'enable_syncache',
        'udp_active_flow_limit': 'udp_active_flow_limit',
        'tcp_half_open_conn_limit': 'tcp_half_open_conn_limit',
        'enable_rst_spoofing': 'enable_rst_spoofing'
    }
    if hasattr(BaseFirewallProfile, "attribute_map"):
        attribute_map.update(BaseFirewallProfile.attribute_map)

    def __init__(self, resource_type=None, icmp_active_flow_limit=None, other_active_conn_limit=None, enable_syncache=False, udp_active_flow_limit=None, tcp_half_open_conn_limit=None, enable_rst_spoofing=False, *args, **kwargs):  # noqa: E501
        """FirewallFloodProtectionProfile - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._icmp_active_flow_limit = None
        self._other_active_conn_limit = None
        self._enable_syncache = None
        self._udp_active_flow_limit = None
        self._tcp_half_open_conn_limit = None
        self._enable_rst_spoofing = None
        self.discriminator = None
        self.resource_type = resource_type
        if icmp_active_flow_limit is not None:
            self.icmp_active_flow_limit = icmp_active_flow_limit
        if other_active_conn_limit is not None:
            self.other_active_conn_limit = other_active_conn_limit
        if enable_syncache is not None:
            self.enable_syncache = enable_syncache
        if udp_active_flow_limit is not None:
            self.udp_active_flow_limit = udp_active_flow_limit
        if tcp_half_open_conn_limit is not None:
            self.tcp_half_open_conn_limit = tcp_half_open_conn_limit
        if enable_rst_spoofing is not None:
            self.enable_rst_spoofing = enable_rst_spoofing
        BaseFirewallProfile.__init__(self, *args, **kwargs)

    @property
    def resource_type(self):
        """Gets the resource_type of this FirewallFloodProtectionProfile.  # noqa: E501

        Resource type to use as profile type  # noqa: E501

        :return: The resource_type of this FirewallFloodProtectionProfile.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FirewallFloodProtectionProfile.

        Resource type to use as profile type  # noqa: E501

        :param resource_type: The resource_type of this FirewallFloodProtectionProfile.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FirewallSessionTimerProfile", "FirewallCpuMemThresholdsProfile", "FirewallFloodProtectionProfile", "FirewallDnsProfile"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def icmp_active_flow_limit(self):
        """Gets the icmp_active_flow_limit of this FirewallFloodProtectionProfile.  # noqa: E501

        The maximum limit of active icmp connections. If this property is omitted, or set to null, then there is no limit on active icmp connections for those components if it's applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it's applied to EDGE components (such as, gateway), it will be set to default limit (10,000) on the specific components.  # noqa: E501

        :return: The icmp_active_flow_limit of this FirewallFloodProtectionProfile.  # noqa: E501
        :rtype: int
        """
        return self._icmp_active_flow_limit

    @icmp_active_flow_limit.setter
    def icmp_active_flow_limit(self, icmp_active_flow_limit):
        """Sets the icmp_active_flow_limit of this FirewallFloodProtectionProfile.

        The maximum limit of active icmp connections. If this property is omitted, or set to null, then there is no limit on active icmp connections for those components if it's applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it's applied to EDGE components (such as, gateway), it will be set to default limit (10,000) on the specific components.  # noqa: E501

        :param icmp_active_flow_limit: The icmp_active_flow_limit of this FirewallFloodProtectionProfile.  # noqa: E501
        :type: int
        """

        self._icmp_active_flow_limit = icmp_active_flow_limit

    @property
    def other_active_conn_limit(self):
        """Gets the other_active_conn_limit of this FirewallFloodProtectionProfile.  # noqa: E501

        The maximum limit of other active connections besides udp, icmp and half open tcp connections. If this property is omitted, or set to null, then there is no limit on other active connections besides udp, icmp and tcp half open connections for those components if it's applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it's applied to EDGE components (such as, gateway), it will be set to default limit (10,000) on the specific components.  # noqa: E501

        :return: The other_active_conn_limit of this FirewallFloodProtectionProfile.  # noqa: E501
        :rtype: int
        """
        return self._other_active_conn_limit

    @other_active_conn_limit.setter
    def other_active_conn_limit(self, other_active_conn_limit):
        """Sets the other_active_conn_limit of this FirewallFloodProtectionProfile.

        The maximum limit of other active connections besides udp, icmp and half open tcp connections. If this property is omitted, or set to null, then there is no limit on other active connections besides udp, icmp and tcp half open connections for those components if it's applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it's applied to EDGE components (such as, gateway), it will be set to default limit (10,000) on the specific components.  # noqa: E501

        :param other_active_conn_limit: The other_active_conn_limit of this FirewallFloodProtectionProfile.  # noqa: E501
        :type: int
        """

        self._other_active_conn_limit = other_active_conn_limit

    @property
    def enable_syncache(self):
        """Gets the enable_syncache of this FirewallFloodProtectionProfile.  # noqa: E501

        The flag to indicate syncache is enabled or not. This option does not apply to EDGE components.  # noqa: E501

        :return: The enable_syncache of this FirewallFloodProtectionProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_syncache

    @enable_syncache.setter
    def enable_syncache(self, enable_syncache):
        """Sets the enable_syncache of this FirewallFloodProtectionProfile.

        The flag to indicate syncache is enabled or not. This option does not apply to EDGE components.  # noqa: E501

        :param enable_syncache: The enable_syncache of this FirewallFloodProtectionProfile.  # noqa: E501
        :type: bool
        """

        self._enable_syncache = enable_syncache

    @property
    def udp_active_flow_limit(self):
        """Gets the udp_active_flow_limit of this FirewallFloodProtectionProfile.  # noqa: E501

        The maximum limit of active udp connections. If this property is omitted, or set to null, then there is no limit on active udp connections for those components if it's applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it's applied to EDGE components (such as, gateway), it will be set to default limit (100,000) on the specific component.  # noqa: E501

        :return: The udp_active_flow_limit of this FirewallFloodProtectionProfile.  # noqa: E501
        :rtype: int
        """
        return self._udp_active_flow_limit

    @udp_active_flow_limit.setter
    def udp_active_flow_limit(self, udp_active_flow_limit):
        """Sets the udp_active_flow_limit of this FirewallFloodProtectionProfile.

        The maximum limit of active udp connections. If this property is omitted, or set to null, then there is no limit on active udp connections for those components if it's applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it's applied to EDGE components (such as, gateway), it will be set to default limit (100,000) on the specific component.  # noqa: E501

        :param udp_active_flow_limit: The udp_active_flow_limit of this FirewallFloodProtectionProfile.  # noqa: E501
        :type: int
        """

        self._udp_active_flow_limit = udp_active_flow_limit

    @property
    def tcp_half_open_conn_limit(self):
        """Gets the tcp_half_open_conn_limit of this FirewallFloodProtectionProfile.  # noqa: E501

        The maximum limit of tcp half open connections. If this property is omitted, or set to null, then there is no limit on active tcp half open connections for those components if it's applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it's applied to EDGE components (such as, gateway), it will be set to default limit (1,000,000) on the specific components.  # noqa: E501

        :return: The tcp_half_open_conn_limit of this FirewallFloodProtectionProfile.  # noqa: E501
        :rtype: int
        """
        return self._tcp_half_open_conn_limit

    @tcp_half_open_conn_limit.setter
    def tcp_half_open_conn_limit(self, tcp_half_open_conn_limit):
        """Sets the tcp_half_open_conn_limit of this FirewallFloodProtectionProfile.

        The maximum limit of tcp half open connections. If this property is omitted, or set to null, then there is no limit on active tcp half open connections for those components if it's applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it's applied to EDGE components (such as, gateway), it will be set to default limit (1,000,000) on the specific components.  # noqa: E501

        :param tcp_half_open_conn_limit: The tcp_half_open_conn_limit of this FirewallFloodProtectionProfile.  # noqa: E501
        :type: int
        """

        self._tcp_half_open_conn_limit = tcp_half_open_conn_limit

    @property
    def enable_rst_spoofing(self):
        """Gets the enable_rst_spoofing of this FirewallFloodProtectionProfile.  # noqa: E501

        The flag to indicate RST spoofing is enabled or not. This option does not apply to EDGE components. This can be enabled only if syncache is enabled.  # noqa: E501

        :return: The enable_rst_spoofing of this FirewallFloodProtectionProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_rst_spoofing

    @enable_rst_spoofing.setter
    def enable_rst_spoofing(self, enable_rst_spoofing):
        """Sets the enable_rst_spoofing of this FirewallFloodProtectionProfile.

        The flag to indicate RST spoofing is enabled or not. This option does not apply to EDGE components. This can be enabled only if syncache is enabled.  # noqa: E501

        :param enable_rst_spoofing: The enable_rst_spoofing of this FirewallFloodProtectionProfile.  # noqa: E501
        :type: bool
        """

        self._enable_rst_spoofing = enable_rst_spoofing

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
        if issubclass(FirewallFloodProtectionProfile, dict):
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
        if not isinstance(other, FirewallFloodProtectionProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
