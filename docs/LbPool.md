# LbPool

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
**member_group** | [**PoolMemberGroup**](PoolMemberGroup.md) |  | [optional] 
**snat_translation** | [**LbSnatTranslation**](LbSnatTranslation.md) |  | [optional] 
**algorithm** | **str** | Load balancing algorithm, configurable per pool controls how the incoming connections are distributed among the members.  | [optional] [default to 'ROUND_ROBIN']
**members** | [**list[PoolMember]**](PoolMember.md) | Server pool consists of one or more pool members. Each pool member is identified, typically, by an IP address and a port.  | [optional] 
**passive_monitor_id** | **str** | Passive healthchecks are disabled by default and can be enabled by attaching a passive health monitor to a server pool. Each time a client connection to a pool member fails, its failed count is incremented. For pools bound to L7 virtual servers, a connection is considered to be failed and failed count is incremented if any TCP connection errors (e.g. TCP RST or failure to send data) or SSL handshake failures occur. For pools bound to L4 virtual servers, if no response is received to a TCP SYN sent to the pool member or if a TCP RST is received in response to a TCP SYN, then the pool member is considered to have failed and the failed count is incremented.  | [optional] 
**tcp_multiplexing_number** | **int** | The maximum number of TCP connections per pool that are idly kept alive for sending future client requests.  | [optional] [default to 6]
**active_monitor_ids** | **list[str]** | In case of active healthchecks, load balancer itself initiates new connections (or sends ICMP ping) to the servers periodically to check their health, completely independent of any data traffic. Active healthchecks are disabled by default and can be enabled for a server pool by binding a health monitor to the pool. Currently, only one active health monitor can be configured per server pool.  | [optional] 
**tcp_multiplexing_enabled** | **bool** | TCP multiplexing allows the same TCP connection between load balancer and the backend server to be used for sending multiple client requests from different client TCP connections.  | [optional] [default to False]
**min_active_members** | **int** | A pool is considered active if there are at least certain minimum number of members.  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

