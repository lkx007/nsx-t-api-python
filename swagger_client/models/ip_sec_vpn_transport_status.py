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


class IPSecVPNTransportStatus(object):
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
        'tunnel_id': 'ResourceReference',
        'status': 'IPSecVPNSessionStatus'
    }
    if hasattr(L2VPNTransportTunnelStatus, "swagger_types"):
        swagger_types.update(L2VPNTransportTunnelStatus.swagger_types)

    attribute_map = {
        'resource_type': 'resource_type',
        'tunnel_id': 'tunnel_id',
        'status': 'status'
    }
    if hasattr(L2VPNTransportTunnelStatus, "attribute_map"):
        attribute_map.update(L2VPNTransportTunnelStatus.attribute_map)

    def __init__(self, resource_type=None, tunnel_id=None, status=None, *args, **kwargs):  # noqa: E501
        """IPSecVPNTransportStatus - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._tunnel_id = None
        self._status = None
        self.discriminator = None
        self.resource_type = resource_type
        if tunnel_id is not None:
            self.tunnel_id = tunnel_id
        if status is not None:
            self.status = status
        L2VPNTransportTunnelStatus.__init__(self, *args, **kwargs)

    @property
    def resource_type(self):
        """Gets the resource_type of this IPSecVPNTransportStatus.  # noqa: E501

        Resource types of L2VPN Transport tunnels  # noqa: E501

        :return: The resource_type of this IPSecVPNTransportStatus.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this IPSecVPNTransportStatus.

        Resource types of L2VPN Transport tunnels  # noqa: E501

        :param resource_type: The resource_type of this IPSecVPNTransportStatus.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["IPSecVPNTransportStatus"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def tunnel_id(self):
        """Gets the tunnel_id of this IPSecVPNTransportStatus.  # noqa: E501


        :return: The tunnel_id of this IPSecVPNTransportStatus.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._tunnel_id

    @tunnel_id.setter
    def tunnel_id(self, tunnel_id):
        """Sets the tunnel_id of this IPSecVPNTransportStatus.


        :param tunnel_id: The tunnel_id of this IPSecVPNTransportStatus.  # noqa: E501
        :type: ResourceReference
        """

        self._tunnel_id = tunnel_id

    @property
    def status(self):
        """Gets the status of this IPSecVPNTransportStatus.  # noqa: E501


        :return: The status of this IPSecVPNTransportStatus.  # noqa: E501
        :rtype: IPSecVPNSessionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IPSecVPNTransportStatus.


        :param status: The status of this IPSecVPNTransportStatus.  # noqa: E501
        :type: IPSecVPNSessionStatus
        """

        self._status = status

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
        if issubclass(IPSecVPNTransportStatus, dict):
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
        if not isinstance(other, IPSecVPNTransportStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
