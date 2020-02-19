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


class NdpHeader(object):
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
        'dst_ip': 'str',
        'msg_type': 'str'
    }

    attribute_map = {
        'dst_ip': 'dst_ip',
        'msg_type': 'msg_type'
    }

    def __init__(self, dst_ip=None, msg_type='NEIGHBOR_SOLICITATION'):  # noqa: E501
        """NdpHeader - a model defined in Swagger"""  # noqa: E501
        self._dst_ip = None
        self._msg_type = None
        self.discriminator = None
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if msg_type is not None:
            self.msg_type = msg_type

    @property
    def dst_ip(self):
        """Gets the dst_ip of this NdpHeader.  # noqa: E501

        The IP address of the destination of the solicitation. It MUST NOT be a multicast address.  # noqa: E501

        :return: The dst_ip of this NdpHeader.  # noqa: E501
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        """Sets the dst_ip of this NdpHeader.

        The IP address of the destination of the solicitation. It MUST NOT be a multicast address.  # noqa: E501

        :param dst_ip: The dst_ip of this NdpHeader.  # noqa: E501
        :type: str
        """

        self._dst_ip = dst_ip

    @property
    def msg_type(self):
        """Gets the msg_type of this NdpHeader.  # noqa: E501

        This field specifies the type of the Neighbor discover message being sent. NEIGHBOR_SOLICITATION - Neighbor Solicitation message to discover the link-layer address of an on-link IPv6 node or to confirm a previously determined link-layer address. NEIGHBOR_ADVERTISEMENT - Neighbor Advertisement message in response to a Neighbor Solicitation message.  # noqa: E501

        :return: The msg_type of this NdpHeader.  # noqa: E501
        :rtype: str
        """
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        """Sets the msg_type of this NdpHeader.

        This field specifies the type of the Neighbor discover message being sent. NEIGHBOR_SOLICITATION - Neighbor Solicitation message to discover the link-layer address of an on-link IPv6 node or to confirm a previously determined link-layer address. NEIGHBOR_ADVERTISEMENT - Neighbor Advertisement message in response to a Neighbor Solicitation message.  # noqa: E501

        :param msg_type: The msg_type of this NdpHeader.  # noqa: E501
        :type: str
        """
        allowed_values = ["NEIGHBOR_SOLICITATION", "NEIGHBOR_ADVERTISEMENT"]  # noqa: E501
        if msg_type not in allowed_values:
            raise ValueError(
                "Invalid value for `msg_type` ({0}), must be one of {1}"  # noqa: E501
                .format(msg_type, allowed_values)
            )

        self._msg_type = msg_type

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
        if issubclass(NdpHeader, dict):
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
        if not isinstance(other, NdpHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
