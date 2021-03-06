# NodeProcessProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**mem_used** | **int** | Virtual memory used by process in bytes | [optional] 
**cpu_time** | **int** | CPU time (user and system) consumed by process in milliseconds | [optional] 
**ppid** | **int** | Parent process id | [optional] 
**start_time** | **int** | Process start time expressed in milliseconds since epoch | [optional] 
**process_name** | **str** | Process name | [optional] 
**pid** | **int** | Process id | [optional] 
**uptime** | **int** | Milliseconds since process started | [optional] 
**mem_resident** | **int** | Resident set size of process in bytes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

