# NodeStatusProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**load_average** | **list[float]** | One, five, and fifteen minute load averages for the system | [optional] 
**swap_used** | **int** | Amount of swap disk in use, in kilobytes | [optional] 
**cpu_usage** | [**CpuUsage**](CpuUsage.md) |  | [optional] 
**non_dpdk_cpu_cores** | **int** | Number of non-DPDK cores on Edge Node. | [optional] 
**swap_total** | **int** | Amount of disk available for swap, in kilobytes | [optional] 
**system_time** | **int** | Current time expressed in milliseconds since epoch | [optional] 
**cpu_cores** | **int** | Number of CPU cores on the system | [optional] 
**uptime** | **int** | Milliseconds since system start | [optional] 
**mem_cache** | **int** | Amount of RAM on the system that can be flushed out to disk, in kilobytes | [optional] 
**mem_total** | **int** | Amount of RAM allocated to the system, in kilobytes | [optional] 
**mem_used** | **int** | Amount of RAM in use on the system, in kilobytes | [optional] 
**dpdk_cpu_cores** | **int** | Number of DPDK cores on Edge Node which are used for packet IO processing. | [optional] 
**file_systems** | [**list[NodeFileSystemProperties]**](NodeFileSystemProperties.md) | File systems configured on the system | [optional] 
**source** | **str** | Source of status data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

