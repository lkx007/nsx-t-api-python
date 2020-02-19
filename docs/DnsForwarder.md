# DnsForwarder

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
**conditional_forwarders** | [**list[ConditionalForwarderZone]**](ConditionalForwarderZone.md) | The conditional zone forwarders. During matching a zone forwarder, the DNS forwarder will use the conditional fowarder with the longest domain name that matches the query.  | [optional] 
**logical_router_id** | **str** | Specify the LogicalRouter where the DnsForwarder runs. The HA mode of the hosting LogicalRouter must be Active/Standby.  | 
**cache_size** | **int** | One DNS answer cache entry will consume ~120 bytes. Hence 1 KB cache size can cache ~8 DNS answer entries, and the default 1024 KB cache size can hold ~8k DNS answer entries.  | [optional] [default to 1024]
**default_forwarder** | [**ForwarderZone**](ForwarderZone.md) |  | 
**log_level** | **str** | Log level of the DNS forwarder | [optional] [default to 'INFO']
**enabled** | **bool** | Flag to enable/disable the forwarder | [optional] [default to True]
**listener_ip** | **str** | The ip address the DNS forwarder listens on. It can be an ip address already owned by the logical-router uplink port or router-link, or a loopback port ip address. But it can not be a downlink port address. User needs to ensure the address is reachable via router or NAT from both client VMs and upstream servers. User will need to create Firewall rules if needed to allow such traffic on a Tier-1 or Tier-0.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

