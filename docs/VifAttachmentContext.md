# VifAttachmentContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocate_addresses** | **str** | A flag to indicate whether to allocate addresses from allocation     pools bound to the parent logical switch.  | [optional] 
**resource_type** | **str** | Used to identify which concrete class it is | 
**vif_type** | **str** | Type of the VIF attached to logical port | 
**parent_vif_id** | **str** | VIF ID of the parent VIF if vif_type is CHILD | [optional] 
**app_id** | **str** | An application ID used to identify / look up a child VIF behind a parent VIF. Only effective when vif_type is CHILD.  | [optional] 
**traffic_tag** | **int** | Current we use VLAN id as the traffic tag. Only effective when vif_type is CHILD. Each logical port inside a container must have a unique traffic tag. If the traffic_tag is not unique, no error is generated, but traffic will not be delivered to any port with a non-unique tag.  | [optional] 
**transport_node_uuid** | **str** | Only effective when vif_type is INDEPENDENT. Each logical port inside a bare metal server or container must have a transport node UUID. We use transport node ID as transport node UUID.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

