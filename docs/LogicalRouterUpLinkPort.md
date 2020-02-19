# LogicalRouterUpLinkPort

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_router_id** | **str** | Identifier for logical router on which this port is created | 
**service_bindings** | [**list[ServiceBinding]**](ServiceBinding.md) | Service Bindings | [optional] 
**resource_type** | **str** | LogicalRouterUpLinkPort is allowed only on TIER0 logical router.   It is the north facing port of the logical router. LogicalRouterLinkPortOnTIER0 is allowed only on TIER0 logical router.   This is the port where the LogicalRouterLinkPortOnTIER1 of TIER1 logical router connects to. LogicalRouterLinkPortOnTIER1 is allowed only on TIER1 logical router.   This is the port using which the user connected to TIER1 logical router for upwards connectivity via TIER0 logical router.   Connect this port to the LogicalRouterLinkPortOnTIER0 of the TIER0 logical router. LogicalRouterDownLinkPort is for the connected subnets on the logical router. LogicalRouterLoopbackPort is a loopback port for logical router component   which is placed on chosen edge cluster member. LogicalRouterIPTunnelPort is a IPSec VPN tunnel port created on   logical router when route based VPN session configured. LogicalRouterCentralizedServicePort is allowed only on Active/Standby TIER0 and TIER1   logical router. Port can be connected to VLAN or overlay logical switch.   Unlike downlink port it does not participate in distributed routing and hosted   on all edge cluster members associated with logical router.   Stateful services can be applied on this port.  | 
**subnets** | [**list[IPSubnet]**](IPSubnet.md) | Logical router port subnets | 
**linked_logical_switch_port_id** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**edge_cluster_member_index** | **list[int]** | Member index of the edge node on the cluster | 
**urpf_mode** | **str** | Unicast Reverse Path Forwarding mode | [optional] [default to 'STRICT']
**mac_address** | **str** | MAC address | [optional] 
**ndra_prefix_config** | [**list[NDRAPrefixConfig]**](NDRAPrefixConfig.md) | Configuration to override the neighbor discovery router advertisement prefix time parameters at the subnet level. Note that users are allowed to override the prefix time only for IPv6 subnets which are configured on the port.  | [optional] 
**ndra_profile_id** | **str** | Identifier of Neighbor Discovery Router Advertisement profile associated with port. When NDRA profile id is associated at both the port level and logical router level, the profile id specified at port level takes the precedence.  | [optional] 
**mtu** | **int** | Maximum transmission unit specifies the size of the largest packet that a network protocol can transmit. If not specified, the global logical MTU set in the /api/v1/global-configs/RoutingGlobalConfig API will be used.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

