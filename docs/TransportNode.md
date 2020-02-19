# TransportNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_owned** | **bool** | Indicates system owned resource | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**create_user** | **str** | ID of the user who created this resource | [optional] 
**protection** | **str** | Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite&#x3D;true. UNKNOWN - the _protection field could not be determined for this           entity.  | [optional] 
**create_time** | **int** | Timestamp of resource creation | [optional] 
**last_modified_time** | **int** | Timestamp of last modification | [optional] 
**last_modified_user** | **str** | ID of the user who last modified this resource | [optional] 
**id** | **str** | Unique identifier of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | [optional] 
**host_switch_spec** | [**HostSwitchSpec**](HostSwitchSpec.md) |  | [optional] 
**node_id** | **str** | Unique Id of the fabric node | [optional] 
**node_deployment_info** | [**Node**](Node.md) |  | [optional] 
**host_switches** | [**list[HostSwitch]**](HostSwitch.md) | This property is deprecated in favor of &#x27;host_switch_spec&#x27;. Property &#x27;host_switches&#x27; can only be used for NSX managed transport nodes. &#x27;host_switch_spec&#x27; can be used for both NSX managed or manually preconfigured host switches. | [optional] 
**maintenance_mode** | **str** | The property is read-only, used for querying result. User could update transport node maintenance mode by UpdateTransportNodeMaintenanceMode call. | [optional] 
**failure_domain_id** | **str** | Set failure domain of edge transport node which will help in auto placement of TIER1 logical routers, DHCP Servers and MDProxies, if failure domain based allocation is enabled in edge cluster API. It is only supported for edge transport node and not for host transport node. In case failure domain is not set by user explicitly, it will be always assigned with default system created failure domain.  | [optional] 
**is_overridden** | **bool** | This flag is relevant to only those hosts which are part of a compute collection which has transport node profile (TNP) applied on it. If you change the transport node configuration and it is different than cluster level TNP then this flag will be set to true  | [optional] 
**transport_zone_endpoints** | [**list[TransportZoneEndPoint]**](TransportZoneEndPoint.md) | Transport zone endpoints. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

