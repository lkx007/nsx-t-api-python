# NodeServiceStatusProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**health** | **str** | Service health in addition to runtime_state | [optional] 
**pids** | **list[int]** | Service process ids | [optional] 
**runtime_state** | **str** | Service runtime state | [optional] 
**monitor_runtime_state** | **str** | Service monitor runtime state | [optional] 
**monitor_pid** | **int** | Service monitor process id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

