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


class LogicalRouterIPTunnelPort(object):
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
        'admin_state': 'str',
        'vpn_session_id': 'str'
    }
    if hasattr(LogicalRouterPort, "swagger_types"):
        swagger_types.update(LogicalRouterPort.swagger_types)

    attribute_map = {
        'logical_router_id': 'logical_router_id',
        'service_bindings': 'service_bindings',
        'resource_type': 'resource_type',
        'subnets': 'subnets',
        'admin_state': 'admin_state',
        'vpn_session_id': 'vpn_session_id'
    }
    if hasattr(LogicalRouterPort, "attribute_map"):
        attribute_map.update(LogicalRouterPort.attribute_map)

    def __init__(self, logical_router_id=None, service_bindings=None, resource_type=None, subnets=None, admin_state=None, vpn_session_id=None, *args, **kwargs):  # noqa: E501
        """LogicalRouterIPTunnelPort - a model defined in Swagger"""  # noqa: E501
        self._logical_router_id = None
        self._service_bindings = None
        self._resource_type = None
        self._subnets = None
        self._admin_state = None
        self._vpn_session_id = None
        self.discriminator = None
        self.logical_router_id = logical_router_id
        if service_bindings is not None:
            self.service_bindings = service_bindings
        self.resource_type = resource_type
        if subnets is not None:
            self.subnets = subnets
        if admin_state is not None:
            self.admin_state = admin_state
        if vpn_session_id is not None:
            self.vpn_session_id = vpn_session_id
        LogicalRouterPort.__init__(self, *args, **kwargs)

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this LogicalRouterIPTunnelPort.  # noqa: E501

        Identifier for logical router on which this port is created  # noqa: E501

        :return: The logical_router_id of this LogicalRouterIPTunnelPort.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this LogicalRouterIPTunnelPort.

        Identifier for logical router on which this port is created  # noqa: E501

        :param logical_router_id: The logical_router_id of this LogicalRouterIPTunnelPort.  # noqa: E501
        :type: str
        """
        if logical_router_id is None:
            raise ValueError("Invalid value for `logical_router_id`, must not be `None`")  # noqa: E501

        self._logical_router_id = logical_router_id

    @property
    def service_bindings(self):
        """Gets the service_bindings of this LogicalRouterIPTunnelPort.  # noqa: E501

        Service Bindings  # noqa: E501

        :return: The service_bindings of this LogicalRouterIPTunnelPort.  # noqa: E501
        :rtype: list[ServiceBinding]
        """
        return self._service_bindings

    @service_bindings.setter
    def service_bindings(self, service_bindings):
        """Sets the service_bindings of this LogicalRouterIPTunnelPort.

        Service Bindings  # noqa: E501

        :param service_bindings: The service_bindings of this LogicalRouterIPTunnelPort.  # noqa: E501
        :type: list[ServiceBinding]
        """

        self._service_bindings = service_bindings

    @property
    def resource_type(self):
        """Gets the resource_type of this LogicalRouterIPTunnelPort.  # noqa: E501

        LogicalRouterUpLinkPort is allowed only on TIER0 logical router.   It is the north facing port of the logical router. LogicalRouterLinkPortOnTIER0 is allowed only on TIER0 logical router.   This is the port where the LogicalRouterLinkPortOnTIER1 of TIER1 logical router connects to. LogicalRouterLinkPortOnTIER1 is allowed only on TIER1 logical router.   This is the port using which the user connected to TIER1 logical router for upwards connectivity via TIER0 logical router.   Connect this port to the LogicalRouterLinkPortOnTIER0 of the TIER0 logical router. LogicalRouterDownLinkPort is for the connected subnets on the logical router. LogicalRouterLoopbackPort is a loopback port for logical router component   which is placed on chosen edge cluster member. LogicalRouterIPTunnelPort is a IPSec VPN tunnel port created on   logical router when route based VPN session configured. LogicalRouterCentralizedServicePort is allowed only on Active/Standby TIER0 and TIER1   logical router. Port can be connected to VLAN or overlay logical switch.   Unlike downlink port it does not participate in distributed routing and hosted   on all edge cluster members associated with logical router.   Stateful services can be applied on this port.   # noqa: E501

        :return: The resource_type of this LogicalRouterIPTunnelPort.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this LogicalRouterIPTunnelPort.

        LogicalRouterUpLinkPort is allowed only on TIER0 logical router.   It is the north facing port of the logical router. LogicalRouterLinkPortOnTIER0 is allowed only on TIER0 logical router.   This is the port where the LogicalRouterLinkPortOnTIER1 of TIER1 logical router connects to. LogicalRouterLinkPortOnTIER1 is allowed only on TIER1 logical router.   This is the port using which the user connected to TIER1 logical router for upwards connectivity via TIER0 logical router.   Connect this port to the LogicalRouterLinkPortOnTIER0 of the TIER0 logical router. LogicalRouterDownLinkPort is for the connected subnets on the logical router. LogicalRouterLoopbackPort is a loopback port for logical router component   which is placed on chosen edge cluster member. LogicalRouterIPTunnelPort is a IPSec VPN tunnel port created on   logical router when route based VPN session configured. LogicalRouterCentralizedServicePort is allowed only on Active/Standby TIER0 and TIER1   logical router. Port can be connected to VLAN or overlay logical switch.   Unlike downlink port it does not participate in distributed routing and hosted   on all edge cluster members associated with logical router.   Stateful services can be applied on this port.   # noqa: E501

        :param resource_type: The resource_type of this LogicalRouterIPTunnelPort.  # noqa: E501
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
        """Gets the subnets of this LogicalRouterIPTunnelPort.  # noqa: E501

        Tunnel port subnets.  # noqa: E501

        :return: The subnets of this LogicalRouterIPTunnelPort.  # noqa: E501
        :rtype: list[IPSubnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this LogicalRouterIPTunnelPort.

        Tunnel port subnets.  # noqa: E501

        :param subnets: The subnets of this LogicalRouterIPTunnelPort.  # noqa: E501
        :type: list[IPSubnet]
        """

        self._subnets = subnets

    @property
    def admin_state(self):
        """Gets the admin_state of this LogicalRouterIPTunnelPort.  # noqa: E501

        Admin state of port.  # noqa: E501

        :return: The admin_state of this LogicalRouterIPTunnelPort.  # noqa: E501
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this LogicalRouterIPTunnelPort.

        Admin state of port.  # noqa: E501

        :param admin_state: The admin_state of this LogicalRouterIPTunnelPort.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN"]  # noqa: E501
        if admin_state not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_state` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_state, allowed_values)
            )

        self._admin_state = admin_state

    @property
    def vpn_session_id(self):
        """Gets the vpn_session_id of this LogicalRouterIPTunnelPort.  # noqa: E501

        Associated VPN session identifier.  # noqa: E501

        :return: The vpn_session_id of this LogicalRouterIPTunnelPort.  # noqa: E501
        :rtype: str
        """
        return self._vpn_session_id

    @vpn_session_id.setter
    def vpn_session_id(self, vpn_session_id):
        """Sets the vpn_session_id of this LogicalRouterIPTunnelPort.

        Associated VPN session identifier.  # noqa: E501

        :param vpn_session_id: The vpn_session_id of this LogicalRouterIPTunnelPort.  # noqa: E501
        :type: str
        """

        self._vpn_session_id = vpn_session_id

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
        if issubclass(LogicalRouterIPTunnelPort, dict):
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
        if not isinstance(other, LogicalRouterIPTunnelPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
