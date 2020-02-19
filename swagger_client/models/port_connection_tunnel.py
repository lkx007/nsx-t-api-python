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


class PortConnectionTunnel(object):
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
        'src_node_id': 'str',
        'tunnel_properties': 'TunnelProperties'
    }

    attribute_map = {
        'src_node_id': 'src_node_id',
        'tunnel_properties': 'tunnel_properties'
    }

    def __init__(self, src_node_id=None, tunnel_properties=None):  # noqa: E501
        """PortConnectionTunnel - a model defined in Swagger"""  # noqa: E501
        self._src_node_id = None
        self._tunnel_properties = None
        self.discriminator = None
        self.src_node_id = src_node_id
        self.tunnel_properties = tunnel_properties

    @property
    def src_node_id(self):
        """Gets the src_node_id of this PortConnectionTunnel.  # noqa: E501

        Id of the source transport node  # noqa: E501

        :return: The src_node_id of this PortConnectionTunnel.  # noqa: E501
        :rtype: str
        """
        return self._src_node_id

    @src_node_id.setter
    def src_node_id(self, src_node_id):
        """Sets the src_node_id of this PortConnectionTunnel.

        Id of the source transport node  # noqa: E501

        :param src_node_id: The src_node_id of this PortConnectionTunnel.  # noqa: E501
        :type: str
        """
        if src_node_id is None:
            raise ValueError("Invalid value for `src_node_id`, must not be `None`")  # noqa: E501

        self._src_node_id = src_node_id

    @property
    def tunnel_properties(self):
        """Gets the tunnel_properties of this PortConnectionTunnel.  # noqa: E501


        :return: The tunnel_properties of this PortConnectionTunnel.  # noqa: E501
        :rtype: TunnelProperties
        """
        return self._tunnel_properties

    @tunnel_properties.setter
    def tunnel_properties(self, tunnel_properties):
        """Sets the tunnel_properties of this PortConnectionTunnel.


        :param tunnel_properties: The tunnel_properties of this PortConnectionTunnel.  # noqa: E501
        :type: TunnelProperties
        """
        if tunnel_properties is None:
            raise ValueError("Invalid value for `tunnel_properties`, must not be `None`")  # noqa: E501

        self._tunnel_properties = tunnel_properties

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
        if issubclass(PortConnectionTunnel, dict):
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
        if not isinstance(other, PortConnectionTunnel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other