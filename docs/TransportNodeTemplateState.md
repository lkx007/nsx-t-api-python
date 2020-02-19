# TransportNodeTemplateState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Transport node template state on individual hosts of ComputeCollection which enabled automated transport code creation. &#x27;FAILED_TO_CREATE&#x27; means transport node isn&#x27;t created. &#x27;IN_PROGRESS&#x27; means transport node is in progress of creation. &#x27;FAILED_TO_REALIZE&#x27; means transport node has been created, but failed on host realization, it will repush to host by NSX later. &#x27;SUCCESS&#x27; means transport node creation is succeeded.  | [optional] 
**node_id** | **str** | node id | 
**transport_node_id** | **str** | transport node id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

