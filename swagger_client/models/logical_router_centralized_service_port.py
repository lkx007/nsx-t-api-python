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


class LogicalRouterCentralizedServicePort(object):
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
        'linked_logical_switch_port_id': 'ResourceReference',
        'subnets': 'list[IPSubnet]',
        'enable_netx': 'bool',
        'urpf_mode': 'str',
        'ndra_profile_id': 'str',
        'mtu': 'int'
    }
    if hasattr(LogicalRouterPort, "swagger_types"):
        swagger_types.update(LogicalRouterPort.swagger_types)

    attribute_map = {
        'logical_router_id': 'logical_router_id',
        'service_bindings': 'service_bindings',
        'resource_type': 'resource_type',
        'linked_logical_switch_port_id': 'linked_logical_switch_port_id',
        'subnets': 'subnets',
        'enable_netx': 'enable_netx',
        'urpf_mode': 'urpf_mode',
        'ndra_profile_id': 'ndra_profile_id',
        'mtu': 'mtu'
    }
    if hasattr(LogicalRouterPort, "attribute_map"):
        attribute_map.update(LogicalRouterPort.attribute_map)

    def __init__(self, logical_router_id=None, service_bindings=None, resource_type=None, linked_logical_switch_port_id=None, subnets=None, enable_netx=False, urpf_mode='STRICT', ndra_profile_id=None, mtu=None, *args, **kwargs):  # noqa: E501
        """LogicalRouterCentralizedServicePort - a model defined in Swagger"""  # noqa: E501
        self._logical_router_id = None
        self._service_bindings = None
        self._resource_type = None
        self._linked_logical_switch_port_id = None
        self._subnets = None
        self._enable_netx = None
        self._urpf_mode = None
        self._ndra_profile_id = None
        self._mtu = None
        self.discriminator = None
        self.logical_router_id = logical_router_id
        if service_bindings is not None:
            self.service_bindings = service_bindings
        self.resource_type = resource_type
        if linked_logical_switch_port_id is not None:
            self.linked_logical_switch_port_id = linked_logical_switch_port_id
        self.subnets = subnets
        if enable_netx is not None:
            self.enable_netx = enable_netx
        if urpf_mode is not None:
            self.urpf_mode = urpf_mode
        if ndra_profile_id is not None:
            self.ndra_profile_id = ndra_profile_id
        if mtu is not None:
            self.mtu = mtu
        LogicalRouterPort.__init__(self, *args, **kwargs)

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Identifier for logical router on which this port is created  # noqa: E501

        :return: The logical_router_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this LogicalRouterCentralizedServicePort.

        Identifier for logical router on which this port is created  # noqa: E501

        :param logical_router_id: The logical_router_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: str
        """
        if logical_router_id is None:
            raise ValueError("Invalid value for `logical_router_id`, must not be `None`")  # noqa: E501

        self._logical_router_id = logical_router_id

    @property
    def service_bindings(self):
        """Gets the service_bindings of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Service Bindings  # noqa: E501

        :return: The service_bindings of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: list[ServiceBinding]
        """
        return self._service_bindings

    @service_bindings.setter
    def service_bindings(self, service_bindings):
        """Sets the service_bindings of this LogicalRouterCentralizedServicePort.

        Service Bindings  # noqa: E501

        :param service_bindings: The service_bindings of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: list[ServiceBinding]
        """

        self._service_bindings = service_bindings

    @property
    def resource_type(self):
        """Gets the resource_type of this LogicalRouterCentralizedServicePort.  # noqa: E501

        LogicalRouterUpLinkPort is allowed only on TIER0 logical router.   It is the north facing port of the logical router. LogicalRouterLinkPortOnTIER0 is allowed only on TIER0 logical router.   This is the port where the LogicalRouterLinkPortOnTIER1 of TIER1 logical router connects to. LogicalRouterLinkPortOnTIER1 is allowed only on TIER1 logical router.   This is the port using which the user connected to TIER1 logical router for upwards connectivity via TIER0 logical router.   Connect this port to the LogicalRouterLinkPortOnTIER0 of the TIER0 logical router. LogicalRouterDownLinkPort is for the connected subnets on the logical router. LogicalRouterLoopbackPort is a loopback port for logical router component   which is placed on chosen edge cluster member. LogicalRouterIPTunnelPort is a IPSec VPN tunnel port created on   logical router when route based VPN session configured. LogicalRouterCentralizedServicePort is allowed only on Active/Standby TIER0 and TIER1   logical router. Port can be connected to VLAN or overlay logical switch.   Unlike downlink port it does not participate in distributed routing and hosted   on all edge cluster members associated with logical router.   Stateful services can be applied on this port.   # noqa: E501

        :return: The resource_type of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this LogicalRouterCentralizedServicePort.

        LogicalRouterUpLinkPort is allowed only on TIER0 logical router.   It is the north facing port of the logical router. LogicalRouterLinkPortOnTIER0 is allowed only on TIER0 logical router.   This is the port where the LogicalRouterLinkPortOnTIER1 of TIER1 logical router connects to. LogicalRouterLinkPortOnTIER1 is allowed only on TIER1 logical router.   This is the port using which the user connected to TIER1 logical router for upwards connectivity via TIER0 logical router.   Connect this port to the LogicalRouterLinkPortOnTIER0 of the TIER0 logical router. LogicalRouterDownLinkPort is for the connected subnets on the logical router. LogicalRouterLoopbackPort is a loopback port for logical router component   which is placed on chosen edge cluster member. LogicalRouterIPTunnelPort is a IPSec VPN tunnel port created on   logical router when route based VPN session configured. LogicalRouterCentralizedServicePort is allowed only on Active/Standby TIER0 and TIER1   logical router. Port can be connected to VLAN or overlay logical switch.   Unlike downlink port it does not participate in distributed routing and hosted   on all edge cluster members associated with logical router.   Stateful services can be applied on this port.   # noqa: E501

        :param resource_type: The resource_type of this LogicalRouterCentralizedServicePort.  # noqa: E501
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
    def linked_logical_switch_port_id(self):
        """Gets the linked_logical_switch_port_id of this LogicalRouterCentralizedServicePort.  # noqa: E501


        :return: The linked_logical_switch_port_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._linked_logical_switch_port_id

    @linked_logical_switch_port_id.setter
    def linked_logical_switch_port_id(self, linked_logical_switch_port_id):
        """Sets the linked_logical_switch_port_id of this LogicalRouterCentralizedServicePort.


        :param linked_logical_switch_port_id: The linked_logical_switch_port_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: ResourceReference
        """

        self._linked_logical_switch_port_id = linked_logical_switch_port_id

    @property
    def subnets(self):
        """Gets the subnets of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Logical router port subnets  # noqa: E501

        :return: The subnets of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: list[IPSubnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this LogicalRouterCentralizedServicePort.

        Logical router port subnets  # noqa: E501

        :param subnets: The subnets of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: list[IPSubnet]
        """
        if subnets is None:
            raise ValueError("Invalid value for `subnets`, must not be `None`")  # noqa: E501

        self._subnets = subnets

    @property
    def enable_netx(self):
        """Gets the enable_netx of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Port is exclusively used for N-S service insertion  # noqa: E501

        :return: The enable_netx of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: bool
        """
        return self._enable_netx

    @enable_netx.setter
    def enable_netx(self, enable_netx):
        """Sets the enable_netx of this LogicalRouterCentralizedServicePort.

        Port is exclusively used for N-S service insertion  # noqa: E501

        :param enable_netx: The enable_netx of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: bool
        """

        self._enable_netx = enable_netx

    @property
    def urpf_mode(self):
        """Gets the urpf_mode of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Unicast Reverse Path Forwarding mode  # noqa: E501

        :return: The urpf_mode of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: str
        """
        return self._urpf_mode

    @urpf_mode.setter
    def urpf_mode(self, urpf_mode):
        """Sets the urpf_mode of this LogicalRouterCentralizedServicePort.

        Unicast Reverse Path Forwarding mode  # noqa: E501

        :param urpf_mode: The urpf_mode of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "STRICT"]  # noqa: E501
        if urpf_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `urpf_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(urpf_mode, allowed_values)
            )

        self._urpf_mode = urpf_mode

    @property
    def ndra_profile_id(self):
        """Gets the ndra_profile_id of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Identifier of Neighbor Discovery Router Advertisement profile associated with port. When NDRA profile id is associated at both the port level and logical router level, the profile id specified at port level takes the precedence.   # noqa: E501

        :return: The ndra_profile_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: str
        """
        return self._ndra_profile_id

    @ndra_profile_id.setter
    def ndra_profile_id(self, ndra_profile_id):
        """Sets the ndra_profile_id of this LogicalRouterCentralizedServicePort.

        Identifier of Neighbor Discovery Router Advertisement profile associated with port. When NDRA profile id is associated at both the port level and logical router level, the profile id specified at port level takes the precedence.   # noqa: E501

        :param ndra_profile_id: The ndra_profile_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: str
        """

        self._ndra_profile_id = ndra_profile_id

    @property
    def mtu(self):
        """Gets the mtu of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Maximum transmission unit specifies the size of the largest packet that a network protocol can transmit. If not specified, the global logical MTU set in the /api/v1/global-configs/RoutingGlobalConfig API will be used.   # noqa: E501

        :return: The mtu of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this LogicalRouterCentralizedServicePort.

        Maximum transmission unit specifies the size of the largest packet that a network protocol can transmit. If not specified, the global logical MTU set in the /api/v1/global-configs/RoutingGlobalConfig API will be used.   # noqa: E501

        :param mtu: The mtu of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

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
        if issubclass(LogicalRouterCentralizedServicePort, dict):
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
        if not isinstance(other, LogicalRouterCentralizedServicePort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
