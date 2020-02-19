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


class DhcpStaticBinding(object):
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
        'lease_time': 'int',
        'gateway_ip': 'str',
        'options': 'DhcpOptions',
        'ip_address': 'str',
        'host_name': 'str',
        'mac_address': 'str'
    }
    if hasattr(IpAllocationBase, "swagger_types"):
        swagger_types.update(IpAllocationBase.swagger_types)

    attribute_map = {
        'lease_time': 'lease_time',
        'gateway_ip': 'gateway_ip',
        'options': 'options',
        'ip_address': 'ip_address',
        'host_name': 'host_name',
        'mac_address': 'mac_address'
    }
    if hasattr(IpAllocationBase, "attribute_map"):
        attribute_map.update(IpAllocationBase.attribute_map)

    def __init__(self, lease_time=86400, gateway_ip=None, options=None, ip_address=None, host_name=None, mac_address=None, *args, **kwargs):  # noqa: E501
        """DhcpStaticBinding - a model defined in Swagger"""  # noqa: E501
        self._lease_time = None
        self._gateway_ip = None
        self._options = None
        self._ip_address = None
        self._host_name = None
        self._mac_address = None
        self.discriminator = None
        if lease_time is not None:
            self.lease_time = lease_time
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if options is not None:
            self.options = options
        self.ip_address = ip_address
        if host_name is not None:
            self.host_name = host_name
        self.mac_address = mac_address
        IpAllocationBase.__init__(self, *args, **kwargs)

    @property
    def lease_time(self):
        """Gets the lease_time of this DhcpStaticBinding.  # noqa: E501

        Lease time, in seconds, [60-(2^32-1)]. Default is 86400.  # noqa: E501

        :return: The lease_time of this DhcpStaticBinding.  # noqa: E501
        :rtype: int
        """
        return self._lease_time

    @lease_time.setter
    def lease_time(self, lease_time):
        """Sets the lease_time of this DhcpStaticBinding.

        Lease time, in seconds, [60-(2^32-1)]. Default is 86400.  # noqa: E501

        :param lease_time: The lease_time of this DhcpStaticBinding.  # noqa: E501
        :type: int
        """

        self._lease_time = lease_time

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this DhcpStaticBinding.  # noqa: E501

        Gateway ip address of the allocation.  # noqa: E501

        :return: The gateway_ip of this DhcpStaticBinding.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this DhcpStaticBinding.

        Gateway ip address of the allocation.  # noqa: E501

        :param gateway_ip: The gateway_ip of this DhcpStaticBinding.  # noqa: E501
        :type: str
        """

        self._gateway_ip = gateway_ip

    @property
    def options(self):
        """Gets the options of this DhcpStaticBinding.  # noqa: E501


        :return: The options of this DhcpStaticBinding.  # noqa: E501
        :rtype: DhcpOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DhcpStaticBinding.


        :param options: The options of this DhcpStaticBinding.  # noqa: E501
        :type: DhcpOptions
        """

        self._options = options

    @property
    def ip_address(self):
        """Gets the ip_address of this DhcpStaticBinding.  # noqa: E501

        The ip address to be assigned to the host.  # noqa: E501

        :return: The ip_address of this DhcpStaticBinding.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DhcpStaticBinding.

        The ip address to be assigned to the host.  # noqa: E501

        :param ip_address: The ip_address of this DhcpStaticBinding.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def host_name(self):
        """Gets the host_name of this DhcpStaticBinding.  # noqa: E501

        The host name to be assigned to the host.  # noqa: E501

        :return: The host_name of this DhcpStaticBinding.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this DhcpStaticBinding.

        The host name to be assigned to the host.  # noqa: E501

        :param host_name: The host_name of this DhcpStaticBinding.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def mac_address(self):
        """Gets the mac_address of this DhcpStaticBinding.  # noqa: E501

        The MAC address of the host.  # noqa: E501

        :return: The mac_address of this DhcpStaticBinding.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this DhcpStaticBinding.

        The MAC address of the host.  # noqa: E501

        :param mac_address: The mac_address of this DhcpStaticBinding.  # noqa: E501
        :type: str
        """
        if mac_address is None:
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

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
        if issubclass(DhcpStaticBinding, dict):
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
        if not isinstance(other, DhcpStaticBinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
