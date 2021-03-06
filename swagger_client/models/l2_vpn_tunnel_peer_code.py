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


class L2VpnTunnelPeerCode(object):
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
        'transport_tunnel': 'ResourceReference',
        'peer_code': 'str'
    }

    attribute_map = {
        'transport_tunnel': 'transport_tunnel',
        'peer_code': 'peer_code'
    }

    def __init__(self, transport_tunnel=None, peer_code=None):  # noqa: E501
        """L2VpnTunnelPeerCode - a model defined in Swagger"""  # noqa: E501
        self._transport_tunnel = None
        self._peer_code = None
        self.discriminator = None
        self.transport_tunnel = transport_tunnel
        self.peer_code = peer_code

    @property
    def transport_tunnel(self):
        """Gets the transport_tunnel of this L2VpnTunnelPeerCode.  # noqa: E501


        :return: The transport_tunnel of this L2VpnTunnelPeerCode.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._transport_tunnel

    @transport_tunnel.setter
    def transport_tunnel(self, transport_tunnel):
        """Sets the transport_tunnel of this L2VpnTunnelPeerCode.


        :param transport_tunnel: The transport_tunnel of this L2VpnTunnelPeerCode.  # noqa: E501
        :type: ResourceReference
        """
        if transport_tunnel is None:
            raise ValueError("Invalid value for `transport_tunnel`, must not be `None`")  # noqa: E501

        self._transport_tunnel = transport_tunnel

    @property
    def peer_code(self):
        """Gets the peer_code of this L2VpnTunnelPeerCode.  # noqa: E501

        Copy this code to paste on the remote end of the tunnel. This is a base64 encoded string which has all the configuration for tunnel. E.g tap device local/peer ips and protocol, encryption algorithm, etc. The peer code also contains a pre-shared key; be careful when sharing or storing it.  # noqa: E501

        :return: The peer_code of this L2VpnTunnelPeerCode.  # noqa: E501
        :rtype: str
        """
        return self._peer_code

    @peer_code.setter
    def peer_code(self, peer_code):
        """Sets the peer_code of this L2VpnTunnelPeerCode.

        Copy this code to paste on the remote end of the tunnel. This is a base64 encoded string which has all the configuration for tunnel. E.g tap device local/peer ips and protocol, encryption algorithm, etc. The peer code also contains a pre-shared key; be careful when sharing or storing it.  # noqa: E501

        :param peer_code: The peer_code of this L2VpnTunnelPeerCode.  # noqa: E501
        :type: str
        """
        if peer_code is None:
            raise ValueError("Invalid value for `peer_code`, must not be `None`")  # noqa: E501

        self._peer_code = peer_code

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
        if issubclass(L2VpnTunnelPeerCode, dict):
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
        if not isinstance(other, L2VpnTunnelPeerCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
