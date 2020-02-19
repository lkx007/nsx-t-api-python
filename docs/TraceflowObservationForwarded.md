# TraceflowObservationForwarded

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
**uplink_name** | **str** | The name of the uplink the traceflow packet is forwarded on | [optional] 
**vtep_label** | **int** | The virtual tunnel endpoint label | [optional] 
**remote_ip_address** | **str** | IP address of the destination end of the tunnel | [optional] 
**context** | **int** | The 64bit tunnel context carried on the wire | [optional] 
**local_ip_address** | **str** | IP address of the source end of the tunnel | [optional] 
**dst_transport_node_id** | **str** | This field will not be always available. Use remote_ip_address when this field is not set. | [optional] 
**dst_transport_node_name** | **str** | The name of the transport node to which the traceflow packet is forwarded | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

