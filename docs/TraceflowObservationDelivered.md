# TraceflowObservationDelivered

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
**resolution_type** | **str** | This field specifies the resolution type of ARP ARP_SUPPRESSION_PORT_CACHE - ARP request is suppressed by port DB ARP_SUPPRESSION_TABLE - ARP request is suppressed by ARP table ARP_SUPPRESSION_CP_QUERY - ARP request is suppressed by info derived from CP ARP_VM - No suppression and the ARP request is resolved. | [optional] 
**lport_name** | **str** | The name of the logical port into which the traceflow packet was delivered | [optional] 
**target_mac** | **str** | The source MAC address of form: \&quot;^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$\&quot;. For example: 00:00:00:00:00:00.  | [optional] 
**vlan_id** | **int** | VLAN on bridged network | [optional] 
**lport_id** | **str** | The id of the logical port into which the traceflow packet was delivered | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

