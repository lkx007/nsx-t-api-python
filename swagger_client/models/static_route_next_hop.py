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


class StaticRouteNextHop(object):
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
        'blackhole_action': 'str',
        'administrative_distance': 'int',
        'ip_address': 'str',
        'bfd_enabled': 'bool',
        'logical_router_port_id': 'ResourceReference'
    }

    attribute_map = {
        'blackhole_action': 'blackhole_action',
        'administrative_distance': 'administrative_distance',
        'ip_address': 'ip_address',
        'bfd_enabled': 'bfd_enabled',
        'logical_router_port_id': 'logical_router_port_id'
    }

    def __init__(self, blackhole_action=None, administrative_distance=1, ip_address=None, bfd_enabled=False, logical_router_port_id=None):  # noqa: E501
        """StaticRouteNextHop - a model defined in Swagger"""  # noqa: E501
        self._blackhole_action = None
        self._administrative_distance = None
        self._ip_address = None
        self._bfd_enabled = None
        self._logical_router_port_id = None
        self.discriminator = None
        if blackhole_action is not None:
            self.blackhole_action = blackhole_action
        if administrative_distance is not None:
            self.administrative_distance = administrative_distance
        if ip_address is not None:
            self.ip_address = ip_address
        if bfd_enabled is not None:
            self.bfd_enabled = bfd_enabled
        if logical_router_port_id is not None:
            self.logical_router_port_id = logical_router_port_id

    @property
    def blackhole_action(self):
        """Gets the blackhole_action of this StaticRouteNextHop.  # noqa: E501

        Action to be taken on matching packets for NULL routes.  # noqa: E501

        :return: The blackhole_action of this StaticRouteNextHop.  # noqa: E501
        :rtype: str
        """
        return self._blackhole_action

    @blackhole_action.setter
    def blackhole_action(self, blackhole_action):
        """Sets the blackhole_action of this StaticRouteNextHop.

        Action to be taken on matching packets for NULL routes.  # noqa: E501

        :param blackhole_action: The blackhole_action of this StaticRouteNextHop.  # noqa: E501
        :type: str
        """
        allowed_values = ["DISCARD"]  # noqa: E501
        if blackhole_action not in allowed_values:
            raise ValueError(
                "Invalid value for `blackhole_action` ({0}), must be one of {1}"  # noqa: E501
                .format(blackhole_action, allowed_values)
            )

        self._blackhole_action = blackhole_action

    @property
    def administrative_distance(self):
        """Gets the administrative_distance of this StaticRouteNextHop.  # noqa: E501

        Administrative Distance for the next hop IP  # noqa: E501

        :return: The administrative_distance of this StaticRouteNextHop.  # noqa: E501
        :rtype: int
        """
        return self._administrative_distance

    @administrative_distance.setter
    def administrative_distance(self, administrative_distance):
        """Sets the administrative_distance of this StaticRouteNextHop.

        Administrative Distance for the next hop IP  # noqa: E501

        :param administrative_distance: The administrative_distance of this StaticRouteNextHop.  # noqa: E501
        :type: int
        """

        self._administrative_distance = administrative_distance

    @property
    def ip_address(self):
        """Gets the ip_address of this StaticRouteNextHop.  # noqa: E501

        Next Hop IP  # noqa: E501

        :return: The ip_address of this StaticRouteNextHop.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this StaticRouteNextHop.

        Next Hop IP  # noqa: E501

        :param ip_address: The ip_address of this StaticRouteNextHop.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def bfd_enabled(self):
        """Gets the bfd_enabled of this StaticRouteNextHop.  # noqa: E501

        Status of bfd for this next hop where bfd_enabled = true indicate bfd is enabled for this next hop and bfd_enabled = false indicate bfd peer is disabled or not configured for this next hop.  # noqa: E501

        :return: The bfd_enabled of this StaticRouteNextHop.  # noqa: E501
        :rtype: bool
        """
        return self._bfd_enabled

    @bfd_enabled.setter
    def bfd_enabled(self, bfd_enabled):
        """Sets the bfd_enabled of this StaticRouteNextHop.

        Status of bfd for this next hop where bfd_enabled = true indicate bfd is enabled for this next hop and bfd_enabled = false indicate bfd peer is disabled or not configured for this next hop.  # noqa: E501

        :param bfd_enabled: The bfd_enabled of this StaticRouteNextHop.  # noqa: E501
        :type: bool
        """

        self._bfd_enabled = bfd_enabled

    @property
    def logical_router_port_id(self):
        """Gets the logical_router_port_id of this StaticRouteNextHop.  # noqa: E501


        :return: The logical_router_port_id of this StaticRouteNextHop.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._logical_router_port_id

    @logical_router_port_id.setter
    def logical_router_port_id(self, logical_router_port_id):
        """Sets the logical_router_port_id of this StaticRouteNextHop.


        :param logical_router_port_id: The logical_router_port_id of this StaticRouteNextHop.  # noqa: E501
        :type: ResourceReference
        """

        self._logical_router_port_id = logical_router_port_id

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
        if issubclass(StaticRouteNextHop, dict):
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
        if not isinstance(other, StaticRouteNextHop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
