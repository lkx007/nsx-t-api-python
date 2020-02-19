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


class Dhcpv6Header(object):
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
        'msg_type': 'str'
    }

    attribute_map = {
        'msg_type': 'msg_type'
    }

    def __init__(self, msg_type='SOLICIT'):  # noqa: E501
        """Dhcpv6Header - a model defined in Swagger"""  # noqa: E501
        self._msg_type = None
        self.discriminator = None
        if msg_type is not None:
            self.msg_type = msg_type

    @property
    def msg_type(self):
        """Gets the msg_type of this Dhcpv6Header.  # noqa: E501

        This is used to specify the DHCP v6 message. To request the assignment of one or more IPv6 addresses, a client first locates a DHCP server and then requests the assignment of addresses and other configuration information from the server. The client sends a Solicit message to the All_DHCP_Relay_Agents_and_Servers address to find available DHCP servers. Any server that can meet the client's requirements responds with an Advertise message. The client then chooses one of the servers and sends a Request message to the server asking for confirmed assignment of addresses and other configuration information. The server responds with a Reply message that contains the confirmed addresses and configuration. SOLICIT - A client sends a Solicit message to locate servers. ADVERTISE - A server sends and Advertise message to indicate that it is available. REQUEST - A client sends a Request message to request configuration parameters. REPLY - A server sends a Reply message containing assigned addresses and configuration parameters.  # noqa: E501

        :return: The msg_type of this Dhcpv6Header.  # noqa: E501
        :rtype: str
        """
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        """Sets the msg_type of this Dhcpv6Header.

        This is used to specify the DHCP v6 message. To request the assignment of one or more IPv6 addresses, a client first locates a DHCP server and then requests the assignment of addresses and other configuration information from the server. The client sends a Solicit message to the All_DHCP_Relay_Agents_and_Servers address to find available DHCP servers. Any server that can meet the client's requirements responds with an Advertise message. The client then chooses one of the servers and sends a Request message to the server asking for confirmed assignment of addresses and other configuration information. The server responds with a Reply message that contains the confirmed addresses and configuration. SOLICIT - A client sends a Solicit message to locate servers. ADVERTISE - A server sends and Advertise message to indicate that it is available. REQUEST - A client sends a Request message to request configuration parameters. REPLY - A server sends a Reply message containing assigned addresses and configuration parameters.  # noqa: E501

        :param msg_type: The msg_type of this Dhcpv6Header.  # noqa: E501
        :type: str
        """
        allowed_values = ["SOLICIT", "ADVERTISE", "REQUEST", "REPLY"]  # noqa: E501
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
        if issubclass(Dhcpv6Header, dict):
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
        if not isinstance(other, Dhcpv6Header):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
