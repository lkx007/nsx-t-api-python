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


class L2VpnSessionPeerCodes(object):
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
        'peer_codes': 'list[L2VpnTunnelPeerCode]'
    }

    attribute_map = {
        'peer_codes': 'peer_codes'
    }

    def __init__(self, peer_codes=None):  # noqa: E501
        """L2VpnSessionPeerCodes - a model defined in Swagger"""  # noqa: E501
        self._peer_codes = None
        self.discriminator = None
        self.peer_codes = peer_codes

    @property
    def peer_codes(self):
        """Gets the peer_codes of this L2VpnSessionPeerCodes.  # noqa: E501

        List of peer codes per transport tunnel.  # noqa: E501

        :return: The peer_codes of this L2VpnSessionPeerCodes.  # noqa: E501
        :rtype: list[L2VpnTunnelPeerCode]
        """
        return self._peer_codes

    @peer_codes.setter
    def peer_codes(self, peer_codes):
        """Sets the peer_codes of this L2VpnSessionPeerCodes.

        List of peer codes per transport tunnel.  # noqa: E501

        :param peer_codes: The peer_codes of this L2VpnSessionPeerCodes.  # noqa: E501
        :type: list[L2VpnTunnelPeerCode]
        """
        if peer_codes is None:
            raise ValueError("Invalid value for `peer_codes`, must not be `None`")  # noqa: E501

        self._peer_codes = peer_codes

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
        if issubclass(L2VpnSessionPeerCodes, dict):
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
        if not isinstance(other, L2VpnSessionPeerCodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other