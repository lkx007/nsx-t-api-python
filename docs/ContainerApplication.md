# ContainerApplication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_sync_time** | **int** | Timestamp of last modification | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**status** | **str** | Status of the container application. | [optional] 
**container_cluster_id** | **str** | Identifier of the container cluster this container application belongs to. | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Array of additional specific properties of container application in key-value format.  | [optional] 
**external_id** | **str** | Identifier of the container application on container cluster e.g. PCF app id, k8s service id.  | 
**container_project_id** | **str** | Identifier of the project which this container application belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

