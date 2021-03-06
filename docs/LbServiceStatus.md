# LbServiceStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pools** | [**list[LbPoolStatus]**](LbPoolStatus.md) | status of load balancer pools | [optional] 
**cpu_usage** | **int** | Cpu usage in percentage | [optional] 
**active_transport_nodes** | **list[str]** | Ids of load balancer service related active transport nodes | [optional] 
**memory_usage** | **int** | Memory usage in percentage | [optional] 
**service_id** | **str** | Load balancer service identifier | 
**last_update_timestamp** | **int** | Timestamp when the data was last updated | [optional] 
**standby_transport_nodes** | **list[str]** | Ids of load balancer service related standby transport nodes | [optional] 
**error_message** | **str** | Error message, if available | [optional] 
**virtual_servers** | [**list[LbVirtualServerStatus]**](LbVirtualServerStatus.md) | status of load balancer virtual servers | [optional] 
**service_status** | **str** | UP means the load balancer service is working fine on both transport-nodes(if have); DOWN means the load balancer service is down on both transport-nodes (if have), hence the load balancer will not respond to any requests; ERROR means error happens on transport-node(s) or no status is reported from transport-node(s). The load balancer service may be working (or not working); NO_STANDBY means load balancer service is working in one of the transport node while not in the other transport-node (if have). Hence if the load balancer service in the working transport-node goes down, the load balancer service will go down; DETACHED means that the load balancer service has no attachment setting and is not instantiated in any transport nodes; DISABLED means that admin state of load balancer service is DISABLED; UNKNOWN means that no status reported from transport-nodes.The load balancer service may be working(or not working).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

