# ContainerNetworkPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_sync_time** | **int** | Timestamp of last modification | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**container_cluster_id** | **str** | Identifier of the container cluster this network policy belongs to. | [optional] 
**policy_type** | **str** | Type e.g. Network Policy, ASG. | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Array of additional specific properties of container network policy in key-value format.  | [optional] 
**external_id** | **str** | Identifier of the container network policy. | 
**spec** | **str** | Container network policy specification. | [optional] 
**container_project_id** | **str** | Identifier of the project which this network policy belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

