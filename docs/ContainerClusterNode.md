# ContainerClusterNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_sync_time** | **int** | Timestamp of last modification | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**container_cluster_id** | **str** | External identifier of the container cluster. | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Array of additional specific properties of container cluster node in key-value format.  | [optional] 
**external_id** | **str** | External identifier of the container cluster node in K8S/PAS.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

