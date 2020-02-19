# ContainerApplicationInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_sync_time** | **int** | Timestamp of last modification | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**status** | **str** | Status of the container application instance. | [optional] 
**container_cluster_id** | **str** | Identifier of the container cluster this application instance belongs to. | [optional] 
**cluster_node_id** | **str** | Cluster node id where application instance is running. | [optional] 
**external_id** | **str** | Identifier of the container application instance on container cluster. | 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Array of additional specific properties of container application instance in key-value format.  | [optional] 
**container_application_ids** | **list[str]** | List of identifiers of the container application. | [optional] 
**container_project_id** | **str** | Identifier of the container project which this container application instance belongs to.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

