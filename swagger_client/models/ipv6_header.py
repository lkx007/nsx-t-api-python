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


class Ipv6Header(object):
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
        'src_ip': 'str',
        'dst_ip': 'str',
        'next_header': 'int',
        'hop_limit': 'int'
    }

    attribute_map = {
        'src_ip': 'src_ip',
        'dst_ip': 'dst_ip',
        'next_header': 'next_header',
        'hop_limit': 'hop_limit'
    }

    def __init__(self, src_ip=None, dst_ip=None, next_header=58, hop_limit=64):  # noqa: E501
        """Ipv6Header - a model defined in Swagger"""  # noqa: E501
        self._src_ip = None
        self._dst_ip = None
        self._next_header = None
        self._hop_limit = None
        self.discriminator = None
        if src_ip is not None:
            self.src_ip = src_ip
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if next_header is not None:
            self.next_header = next_header
        if hop_limit is not None:
            self.hop_limit = hop_limit

    @property
    def src_ip(self):
        """Gets the src_ip of this Ipv6Header.  # noqa: E501

        The source ip address.  # noqa: E501

        :return: The src_ip of this Ipv6Header.  # noqa: E501
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """Sets the src_ip of this Ipv6Header.

        The source ip address.  # noqa: E501

        :param src_ip: The src_ip of this Ipv6Header.  # noqa: E501
        :type: str
        """

        self._src_ip = src_ip

    @property
    def dst_ip(self):
        """Gets the dst_ip of this Ipv6Header.  # noqa: E501

        The destination ip address.  # noqa: E501

        :return: The dst_ip of this Ipv6Header.  # noqa: E501
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        """Sets the dst_ip of this Ipv6Header.

        The destination ip address.  # noqa: E501

        :param dst_ip: The dst_ip of this Ipv6Header.  # noqa: E501
        :type: str
        """

        self._dst_ip = dst_ip

    @property
    def next_header(self):
        """Gets the next_header of this Ipv6Header.  # noqa: E501

        Identifies the type of header immediately following the IPv6 header.  # noqa: E501

        :return: The next_header of this Ipv6Header.  # noqa: E501
        :rtype: int
        """
        return self._next_header

    @next_header.setter
    def next_header(self, next_header):
        """Sets the next_header of this Ipv6Header.

        Identifies the type of header immediately following the IPv6 header.  # noqa: E501

        :param next_header: The next_header of this Ipv6Header.  # noqa: E501
        :type: int
        """

        self._next_header = next_header

    @property
    def hop_limit(self):
        """Gets the hop_limit of this Ipv6Header.  # noqa: E501

        Decremented by 1 by each node that forwards the packets. The packet is discarded if Hop Limit is decremented to zero.  # noqa: E501

        :return: The hop_limit of this Ipv6Header.  # noqa: E501
        :rtype: int
        """
        return self._hop_limit

    @hop_limit.setter
    def hop_limit(self, hop_limit):
        """Sets the hop_limit of this Ipv6Header.

        Decremented by 1 by each node that forwards the packets. The packet is discarded if Hop Limit is decremented to zero.  # noqa: E501

        :param hop_limit: The hop_limit of this Ipv6Header.  # noqa: E501
        :type: int
        """

        self._hop_limit = hop_limit

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
        if issubclass(Ipv6Header, dict):
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
        if not isinstance(other, Ipv6Header):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other