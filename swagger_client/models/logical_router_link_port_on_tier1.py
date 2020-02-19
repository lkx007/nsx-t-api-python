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


class LogicalRouterLinkPortOnTIER1(object):
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
        'logical_router_id': 'str',
        'service_bindings': 'list[ServiceBinding]',
        'resource_type': 'str',
        'subnets': 'list[IPSubnet]',
        'mac_address': 'str',
        'linked_logical_router_port_id': 'ResourceReference',
        'edge_cluster_member_index': 'list[int]'
    }
    if hasattr(LogicalRouterPort, "swagger_types"):
        swagger_types.update(LogicalRouterPort.swagger_types)

    attribute_map = {
        'logical_router_id': 'logical_router_id',
        'service_bindings': 'service_bindings',
        'resource_type': 'resource_type',
        'subnets': 'subnets',
        'mac_address': 'mac_address',
        'linked_logical_router_port_id': 'linked_logical_router_port_id',
        'edge_cluster_member_index': 'edge_cluster_member_index'
    }
    if hasattr(LogicalRouterPort, "attribute_map"):
        attribute_map.update(LogicalRouterPort.attribute_map)

    def __init__(self, logical_router_id=None, service_bindings=None, resource_type=None, subnets=None, mac_address=None, linked_logical_router_port_id=None, edge_cluster_member_index=None, *args, **kwargs):  # noqa: E501
        """LogicalRouterLinkPortOnTIER1 - a model defined in Swagger"""  # noqa: E501
        self._logical_router_id = None
        self._service_bindings = None
        self._resource_type = None
        self._subnets = None
        self._mac_address = None
        self._linked_logical_router_port_id = None
        self._edge_cluster_member_index = None
        self.discriminator = None
        self.logical_router_id = logical_router_id
        if service_bindings is not None:
            self.service_bindings = service_bindings
        self.resource_type = resource_type
        if subnets is not None:
            self.subnets = subnets
        if mac_address is not None:
            self.mac_address = mac_address
        if linked_logical_router_port_id is not None:
            self.linked_logical_router_port_id = linked_logical_router_port_id
        if edge_cluster_member_index is not None:
            self.edge_cluster_member_index = edge_cluster_member_index
        LogicalRouterPort.__init__(self, *args, **kwargs)

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this LogicalRouterLinkPortOnTIER1.  # noqa: E501

        Identifier for logical router on which this port is created  # noqa: E501

        :return: The logical_router_id of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this LogicalRouterLinkPortOnTIER1.

        Identifier for logical router on which this port is created  # noqa: E501

        :param logical_router_id: The logical_router_id of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :type: str
        """
        if logical_router_id is None:
            raise ValueError("Invalid value for `logical_router_id`, must not be `None`")  # noqa: E501

        self._logical_router_id = logical_router_id

    @property
    def service_bindings(self):
        """Gets the service_bindings of this LogicalRouterLinkPortOnTIER1.  # noqa: E501

        Service Bindings  # noqa: E501

        :return: The service_bindings of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :rtype: list[ServiceBinding]
        """
        return self._service_bindings

    @service_bindings.setter
    def service_bindings(self, service_bindings):
        """Sets the service_bindings of this LogicalRouterLinkPortOnTIER1.

        Service Bindings  # noqa: E501

        :param service_bindings: The service_bindings of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :type: list[ServiceBinding]
        """

        self._service_bindings = service_bindings

    @property
    def resource_type(self):
        """Gets the resource_type of this LogicalRouterLinkPortOnTIER1.  # noqa: E501

        LogicalRouterUpLinkPort is allowed only on TIER0 logical router.   It is the north facing port of the logical router. LogicalRouterLinkPortOnTIER0 is allowed only on TIER0 logical router.   This is the port where the LogicalRouterLinkPortOnTIER1 of TIER1 logical router connects to. LogicalRouterLinkPortOnTIER1 is allowed only on TIER1 logical router.   This is the port using which the user connected to TIER1 logical router for upwards connectivity via TIER0 logical router.   Connect this port to the LogicalRouterLinkPortOnTIER0 of the TIER0 logical router. LogicalRouterDownLinkPort is for the connected subnets on the logical router. LogicalRouterLoopbackPort is a loopback port for logical router component   which is placed on chosen edge cluster member. LogicalRouterIPTunnelPort is a IPSec VPN tunnel port created on   logical router when route based VPN session configured. LogicalRouterCentralizedServicePort is allowed only on Active/Standby TIER0 and TIER1   logical router. Port can be connected to VLAN or overlay logical switch.   Unlike downlink port it does not participate in distributed routing and hosted   on all edge cluster members associated with logical router.   Stateful services can be applied on this port.   # noqa: E501

        :return: The resource_type of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this LogicalRouterLinkPortOnTIER1.

        LogicalRouterUpLinkPort is allowed only on TIER0 logical router.   It is the north facing port of the logical router. LogicalRouterLinkPortOnTIER0 is allowed only on TIER0 logical router.   This is the port where the LogicalRouterLinkPortOnTIER1 of TIER1 logical router connects to. LogicalRouterLinkPortOnTIER1 is allowed only on TIER1 logical router.   This is the port using which the user connected to TIER1 logical router for upwards connectivity via TIER0 logical router.   Connect this port to the LogicalRouterLinkPortOnTIER0 of the TIER0 logical router. LogicalRouterDownLinkPort is for the connected subnets on the logical router. LogicalRouterLoopbackPort is a loopback port for logical router component   which is placed on chosen edge cluster member. LogicalRouterIPTunnelPort is a IPSec VPN tunnel port created on   logical router when route based VPN session configured. LogicalRouterCentralizedServicePort is allowed only on Active/Standby TIER0 and TIER1   logical router. Port can be connected to VLAN or overlay logical switch.   Unlike downlink port it does not participate in distributed routing and hosted   on all edge cluster members associated with logical router.   Stateful services can be applied on this port.   # noqa: E501

        :param resource_type: The resource_type of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LogicalRouterUpLinkPort", "LogicalRouterDownLinkPort", "LogicalRouterLinkPortOnTIER0", "LogicalRouterLinkPortOnTIER1", "LogicalRouterLoopbackPort", "LogicalRouterIPTunnelPort", "LogicalRouterCentralizedServicePort"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def subnets(self):
        """Gets the subnets of this LogicalRouterLinkPortOnTIER1.  # noqa: E501

        Logical router port subnets  # noqa: E501

        :return: The subnets of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :rtype: list[IPSubnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this LogicalRouterLinkPortOnTIER1.

        Logical router port subnets  # noqa: E501

        :param subnets: The subnets of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :type: list[IPSubnet]
        """

        self._subnets = subnets

    @property
    def mac_address(self):
        """Gets the mac_address of this LogicalRouterLinkPortOnTIER1.  # noqa: E501

        MAC address  # noqa: E501

        :return: The mac_address of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this LogicalRouterLinkPortOnTIER1.

        MAC address  # noqa: E501

        :param mac_address: The mac_address of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def linked_logical_router_port_id(self):
        """Gets the linked_logical_router_port_id of this LogicalRouterLinkPortOnTIER1.  # noqa: E501


        :return: The linked_logical_router_port_id of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._linked_logical_router_port_id

    @linked_logical_router_port_id.setter
    def linked_logical_router_port_id(self, linked_logical_router_port_id):
        """Sets the linked_logical_router_port_id of this LogicalRouterLinkPortOnTIER1.


        :param linked_logical_router_port_id: The linked_logical_router_port_id of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :type: ResourceReference
        """

        self._linked_logical_router_port_id = linked_logical_router_port_id

    @property
    def edge_cluster_member_index(self):
        """Gets the edge_cluster_member_index of this LogicalRouterLinkPortOnTIER1.  # noqa: E501

        Please use logical router API to pass edge cluster members indexes manually.   # noqa: E501

        :return: The edge_cluster_member_index of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :rtype: list[int]
        """
        return self._edge_cluster_member_index

    @edge_cluster_member_index.setter
    def edge_cluster_member_index(self, edge_cluster_member_index):
        """Sets the edge_cluster_member_index of this LogicalRouterLinkPortOnTIER1.

        Please use logical router API to pass edge cluster members indexes manually.   # noqa: E501

        :param edge_cluster_member_index: The edge_cluster_member_index of this LogicalRouterLinkPortOnTIER1.  # noqa: E501
        :type: list[int]
        """

        self._edge_cluster_member_index = edge_cluster_member_index

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
        if issubclass(LogicalRouterLinkPortOnTIER1, dict):
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
        if not isinstance(other, LogicalRouterLinkPortOnTIER1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other