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


class PortMirroringFilter(object):
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
        'filter_action': 'str',
        'ip_protocol': 'str',
        'src_ips': 'IPAddresses',
        'dst_ips': 'IPAddresses',
        'dst_ports': 'str',
        'src_ports': 'str'
    }

    attribute_map = {
        'filter_action': 'filter_action',
        'ip_protocol': 'ip_protocol',
        'src_ips': 'src_ips',
        'dst_ips': 'dst_ips',
        'dst_ports': 'dst_ports',
        'src_ports': 'src_ports'
    }

    def __init__(self, filter_action='MIRROR', ip_protocol=None, src_ips=None, dst_ips=None, dst_ports=None, src_ports=None):  # noqa: E501
        """PortMirroringFilter - a model defined in Swagger"""  # noqa: E501
        self._filter_action = None
        self._ip_protocol = None
        self._src_ips = None
        self._dst_ips = None
        self._dst_ports = None
        self._src_ports = None
        self.discriminator = None
        if filter_action is not None:
            self.filter_action = filter_action
        if ip_protocol is not None:
            self.ip_protocol = ip_protocol
        if src_ips is not None:
            self.src_ips = src_ips
        if dst_ips is not None:
            self.dst_ips = dst_ips
        if dst_ports is not None:
            self.dst_ports = dst_ports
        if src_ports is not None:
            self.src_ports = src_ports

    @property
    def filter_action(self):
        """Gets the filter_action of this PortMirroringFilter.  # noqa: E501

        If set to MIRROR, packets will be mirrored. If set to DO_NOT_MIRROR, packets will not be mirrored.  # noqa: E501

        :return: The filter_action of this PortMirroringFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_action

    @filter_action.setter
    def filter_action(self, filter_action):
        """Sets the filter_action of this PortMirroringFilter.

        If set to MIRROR, packets will be mirrored. If set to DO_NOT_MIRROR, packets will not be mirrored.  # noqa: E501

        :param filter_action: The filter_action of this PortMirroringFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["MIRROR", "DO_NOT_MIRROR"]  # noqa: E501
        if filter_action not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_action` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_action, allowed_values)
            )

        self._filter_action = filter_action

    @property
    def ip_protocol(self):
        """Gets the ip_protocol of this PortMirroringFilter.  # noqa: E501

        The transport protocols of TCP or UDP, used to match the transport protocol of a packet. If not provided, no filtering by IP protocols is performed.  # noqa: E501

        :return: The ip_protocol of this PortMirroringFilter.  # noqa: E501
        :rtype: str
        """
        return self._ip_protocol

    @ip_protocol.setter
    def ip_protocol(self, ip_protocol):
        """Sets the ip_protocol of this PortMirroringFilter.

        The transport protocols of TCP or UDP, used to match the transport protocol of a packet. If not provided, no filtering by IP protocols is performed.  # noqa: E501

        :param ip_protocol: The ip_protocol of this PortMirroringFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["TCP", "UDP"]  # noqa: E501
        if ip_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `ip_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(ip_protocol, allowed_values)
            )

        self._ip_protocol = ip_protocol

    @property
    def src_ips(self):
        """Gets the src_ips of this PortMirroringFilter.  # noqa: E501


        :return: The src_ips of this PortMirroringFilter.  # noqa: E501
        :rtype: IPAddresses
        """
        return self._src_ips

    @src_ips.setter
    def src_ips(self, src_ips):
        """Sets the src_ips of this PortMirroringFilter.


        :param src_ips: The src_ips of this PortMirroringFilter.  # noqa: E501
        :type: IPAddresses
        """

        self._src_ips = src_ips

    @property
    def dst_ips(self):
        """Gets the dst_ips of this PortMirroringFilter.  # noqa: E501


        :return: The dst_ips of this PortMirroringFilter.  # noqa: E501
        :rtype: IPAddresses
        """
        return self._dst_ips

    @dst_ips.setter
    def dst_ips(self, dst_ips):
        """Sets the dst_ips of this PortMirroringFilter.


        :param dst_ips: The dst_ips of this PortMirroringFilter.  # noqa: E501
        :type: IPAddresses
        """

        self._dst_ips = dst_ips

    @property
    def dst_ports(self):
        """Gets the dst_ports of this PortMirroringFilter.  # noqa: E501

        Destination port in the form of a port or port range, used to match the destination port of a packet. If not provided, no filtering by destination port is performed.  # noqa: E501

        :return: The dst_ports of this PortMirroringFilter.  # noqa: E501
        :rtype: str
        """
        return self._dst_ports

    @dst_ports.setter
    def dst_ports(self, dst_ports):
        """Sets the dst_ports of this PortMirroringFilter.

        Destination port in the form of a port or port range, used to match the destination port of a packet. If not provided, no filtering by destination port is performed.  # noqa: E501

        :param dst_ports: The dst_ports of this PortMirroringFilter.  # noqa: E501
        :type: str
        """

        self._dst_ports = dst_ports

    @property
    def src_ports(self):
        """Gets the src_ports of this PortMirroringFilter.  # noqa: E501

        Source port in the form of a port or port range, used to match the source port of a packet. If not provided, no filtering by source port is performed.  # noqa: E501

        :return: The src_ports of this PortMirroringFilter.  # noqa: E501
        :rtype: str
        """
        return self._src_ports

    @src_ports.setter
    def src_ports(self, src_ports):
        """Sets the src_ports of this PortMirroringFilter.

        Source port in the form of a port or port range, used to match the source port of a packet. If not provided, no filtering by source port is performed.  # noqa: E501

        :param src_ports: The src_ports of this PortMirroringFilter.  # noqa: E501
        :type: str
        """

        self._src_ports = src_ports

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
        if issubclass(PortMirroringFilter, dict):
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
        if not isinstance(other, PortMirroringFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
