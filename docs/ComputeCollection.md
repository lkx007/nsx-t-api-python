# ComputeCollection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_sync_time** | **int** | Timestamp of last modification | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**origin_id** | **str** | Id of the compute manager from where this Compute Collection was discovered | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Key-Value map of additional specific properties of compute collection in the Compute Manager  | [optional] 
**external_id** | **str** | External ID of the ComputeCollection in the source Compute manager, e.g. mo-ref in VC  | [optional] 
**owner_id** | **str** | Id of the owner of compute collection in the Compute Manager | [optional] 
**origin_type** | **str** | ComputeCollection type like VC_Cluster. Here the Compute Manager type prefix would help in differentiating similar named Compute Collection types from different Compute Managers  | [optional] 
**cm_local_id** | **str** | Local Id of the compute collection in the Compute Manager | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

