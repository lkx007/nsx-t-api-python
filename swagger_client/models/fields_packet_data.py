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


class FieldsPacketData(object):
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
        'routed': 'bool',
        'transport_type': 'str',
        'resource_type': 'str',
        'frame_size': 'int',
        'ipv6_header': 'Ipv6Header',
        'arp_header': 'ArpHeader',
        'transport_header': 'TransportProtocolHeader',
        'ip_header': 'Ipv4Header',
        'eth_header': 'EthernetHeader',
        'payload': 'str'
    }
    if hasattr(PacketData, "swagger_types"):
        swagger_types.update(PacketData.swagger_types)

    attribute_map = {
        'routed': 'routed',
        'transport_type': 'transport_type',
        'resource_type': 'resource_type',
        'frame_size': 'frame_size',
        'ipv6_header': 'ipv6_header',
        'arp_header': 'arp_header',
        'transport_header': 'transport_header',
        'ip_header': 'ip_header',
        'eth_header': 'eth_header',
        'payload': 'payload'
    }
    if hasattr(PacketData, "attribute_map"):
        attribute_map.update(PacketData.attribute_map)

    def __init__(self, routed=None, transport_type='UNICAST', resource_type=None, frame_size=128, ipv6_header=None, arp_header=None, transport_header=None, ip_header=None, eth_header=None, payload=None, *args, **kwargs):  # noqa: E501
        """FieldsPacketData - a model defined in Swagger"""  # noqa: E501
        self._routed = None
        self._transport_type = None
        self._resource_type = None
        self._frame_size = None
        self._ipv6_header = None
        self._arp_header = None
        self._transport_header = None
        self._ip_header = None
        self._eth_header = None
        self._payload = None
        self.discriminator = None
        if routed is not None:
            self.routed = routed
        if transport_type is not None:
            self.transport_type = transport_type
        self.resource_type = resource_type
        if frame_size is not None:
            self.frame_size = frame_size
        if ipv6_header is not None:
            self.ipv6_header = ipv6_header
        if arp_header is not None:
            self.arp_header = arp_header
        if transport_header is not None:
            self.transport_header = transport_header
        if ip_header is not None:
            self.ip_header = ip_header
        if eth_header is not None:
            self.eth_header = eth_header
        if payload is not None:
            self.payload = payload
        PacketData.__init__(self, *args, **kwargs)

    @property
    def routed(self):
        """Gets the routed of this FieldsPacketData.  # noqa: E501

        A flag, when set true, indicates that the traceflow packet is of L3 routing.  # noqa: E501

        :return: The routed of this FieldsPacketData.  # noqa: E501
        :rtype: bool
        """
        return self._routed

    @routed.setter
    def routed(self, routed):
        """Sets the routed of this FieldsPacketData.

        A flag, when set true, indicates that the traceflow packet is of L3 routing.  # noqa: E501

        :param routed: The routed of this FieldsPacketData.  # noqa: E501
        :type: bool
        """

        self._routed = routed

    @property
    def transport_type(self):
        """Gets the transport_type of this FieldsPacketData.  # noqa: E501

        transport type of the traceflow packet  # noqa: E501

        :return: The transport_type of this FieldsPacketData.  # noqa: E501
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """Sets the transport_type of this FieldsPacketData.

        transport type of the traceflow packet  # noqa: E501

        :param transport_type: The transport_type of this FieldsPacketData.  # noqa: E501
        :type: str
        """
        allowed_values = ["BROADCAST", "UNICAST", "MULTICAST", "UNKNOWN"]  # noqa: E501
        if transport_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transport_type, allowed_values)
            )

        self._transport_type = transport_type

    @property
    def resource_type(self):
        """Gets the resource_type of this FieldsPacketData.  # noqa: E501

        Packet configuration  # noqa: E501

        :return: The resource_type of this FieldsPacketData.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FieldsPacketData.

        Packet configuration  # noqa: E501

        :param resource_type: The resource_type of this FieldsPacketData.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["BinaryPacketData", "FieldsPacketData"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def frame_size(self):
        """Gets the frame_size of this FieldsPacketData.  # noqa: E501

        If the requested frame_size is too small (given the payload and traceflow metadata requirement of 16 bytes), the traceflow request will fail with an appropriate message.  The frame will be zero padded to the requested size.  # noqa: E501

        :return: The frame_size of this FieldsPacketData.  # noqa: E501
        :rtype: int
        """
        return self._frame_size

    @frame_size.setter
    def frame_size(self, frame_size):
        """Sets the frame_size of this FieldsPacketData.

        If the requested frame_size is too small (given the payload and traceflow metadata requirement of 16 bytes), the traceflow request will fail with an appropriate message.  The frame will be zero padded to the requested size.  # noqa: E501

        :param frame_size: The frame_size of this FieldsPacketData.  # noqa: E501
        :type: int
        """

        self._frame_size = frame_size

    @property
    def ipv6_header(self):
        """Gets the ipv6_header of this FieldsPacketData.  # noqa: E501


        :return: The ipv6_header of this FieldsPacketData.  # noqa: E501
        :rtype: Ipv6Header
        """
        return self._ipv6_header

    @ipv6_header.setter
    def ipv6_header(self, ipv6_header):
        """Sets the ipv6_header of this FieldsPacketData.


        :param ipv6_header: The ipv6_header of this FieldsPacketData.  # noqa: E501
        :type: Ipv6Header
        """

        self._ipv6_header = ipv6_header

    @property
    def arp_header(self):
        """Gets the arp_header of this FieldsPacketData.  # noqa: E501


        :return: The arp_header of this FieldsPacketData.  # noqa: E501
        :rtype: ArpHeader
        """
        return self._arp_header

    @arp_header.setter
    def arp_header(self, arp_header):
        """Sets the arp_header of this FieldsPacketData.


        :param arp_header: The arp_header of this FieldsPacketData.  # noqa: E501
        :type: ArpHeader
        """

        self._arp_header = arp_header

    @property
    def transport_header(self):
        """Gets the transport_header of this FieldsPacketData.  # noqa: E501


        :return: The transport_header of this FieldsPacketData.  # noqa: E501
        :rtype: TransportProtocolHeader
        """
        return self._transport_header

    @transport_header.setter
    def transport_header(self, transport_header):
        """Sets the transport_header of this FieldsPacketData.


        :param transport_header: The transport_header of this FieldsPacketData.  # noqa: E501
        :type: TransportProtocolHeader
        """

        self._transport_header = transport_header

    @property
    def ip_header(self):
        """Gets the ip_header of this FieldsPacketData.  # noqa: E501


        :return: The ip_header of this FieldsPacketData.  # noqa: E501
        :rtype: Ipv4Header
        """
        return self._ip_header

    @ip_header.setter
    def ip_header(self, ip_header):
        """Sets the ip_header of this FieldsPacketData.


        :param ip_header: The ip_header of this FieldsPacketData.  # noqa: E501
        :type: Ipv4Header
        """

        self._ip_header = ip_header

    @property
    def eth_header(self):
        """Gets the eth_header of this FieldsPacketData.  # noqa: E501


        :return: The eth_header of this FieldsPacketData.  # noqa: E501
        :rtype: EthernetHeader
        """
        return self._eth_header

    @eth_header.setter
    def eth_header(self, eth_header):
        """Sets the eth_header of this FieldsPacketData.


        :param eth_header: The eth_header of this FieldsPacketData.  # noqa: E501
        :type: EthernetHeader
        """

        self._eth_header = eth_header

    @property
    def payload(self):
        """Gets the payload of this FieldsPacketData.  # noqa: E501

        Up to 1000 bytes of payload may be supplied (with a base64-encoded length of 1336 bytes.) Additional bytes of traceflow metadata will be appended to the payload. The payload contains any data the user wants to put after the transport header.  # noqa: E501

        :return: The payload of this FieldsPacketData.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this FieldsPacketData.

        Up to 1000 bytes of payload may be supplied (with a base64-encoded length of 1336 bytes.) Additional bytes of traceflow metadata will be appended to the payload. The payload contains any data the user wants to put after the transport header.  # noqa: E501

        :param payload: The payload of this FieldsPacketData.  # noqa: E501
        :type: str
        """

        self._payload = payload

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
        if issubclass(FieldsPacketData, dict):
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
        if not isinstance(other, FieldsPacketData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
