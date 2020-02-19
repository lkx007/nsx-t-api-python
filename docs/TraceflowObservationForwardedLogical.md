# TraceflowObservationForwardedLogical

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_micro** | **int** | Timestamp when the observation was created by the transport node (microseconds epoch) | [optional] 
**component_sub_type** | **str** | The sub type of the component that issued the observation. | [optional] 
**resource_type** | **str** |  | 
**component_type** | **str** | The type of the component that issued the observation. | [optional] 
**transport_node_name** | **str** | name of the transport node that observed a traceflow packet | [optional] 
**timestamp** | **int** | Timestamp when the observation was created by the transport node (milliseconds epoch) | [optional] 
**transport_node_id** | **str** | id of the transport node that observed a traceflow packet | [optional] 
**sequence_no** | **int** | the hop count for observations on the transport node that a traceflow packet is injected in will be 0. The hop count is incremented each time a subsequent transport node receives the traceflow packet. The sequence number of 999 indicates that the hop count could not be determined for the containing observation. | [optional] 
**transport_node_type** | **str** | type of the transport node that observed a traceflow packet | [optional] 
**component_name** | **str** | The name of the component that issued the observation. | [optional] 
**service_path_index** | **int** | The path index of the service insertion component | [optional] 
**component_id** | **str** | The id of the component that forwarded the traceflow packet. | [optional] 
**resend_type** | **str** | ARP_UNKNOWN_FROM_CP - Unknown ARP query result emitted by control plane ND_NS_UNKNOWN_FROM_CP - Unknown neighbor solicitation query result emitted by control plane UNKNOWN - Unknown resend type | [optional] 
**lport_name** | **str** | The name of the logical port through which the traceflow packet was forwarded. | [optional] 
**acl_rule_id** | **int** | The id of the acl rule that was applied to forward the traceflow packet | [optional] 
**service_index** | **int** | The index of the service insertion component | [optional] 
**dst_component_type** | **str** | The type of the destination component to which the traceflow packet was forwarded. | [optional] 
**dst_component_name** | **str** | The name of the destination component to which the traceflow packet was forwarded. | [optional] 
**nat_rule_id** | **int** | The ID of the NAT rule that was applied to forward the traceflow packet | [optional] 
**translated_src_ip** | **str** | The translated source IP address of VPN/NAT | [optional] 
**translated_dst_ip** | **str** | The translated destination IP address of VNP/NAT | [optional] 
**vni** | **int** | VNI for the logical network on which the traceflow packet was forwarded. | [optional] 
**lport_id** | **str** | The id of the logical port through which the traceflow packet was forwarded. | [optional] 
**dst_component_id** | **str** | The id of the destination component to which the traceflow packet was forwarded. | [optional] 
**service_ttl** | **int** | The ttl of the service insertion component | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

