# VmToolsInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_sync_time** | **int** | Timestamp of last modification | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**source** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**vm_type** | **str** | Type of VM - Edge, Service or other. | [optional] 
**network_agent_version** | **str** | Version of network agent on the VM of a third party partner solution. | [optional] 
**host_local_id** | **str** | Id of the VM which is assigned locally by the host. It is the VM-moref on ESXi hosts, in other environments it is VM UUID. | [optional] 
**external_id** | **str** | Current external id of this virtual machine in the system. | [optional] 
**tools_version** | **str** | Version of VMTools installed on the VM. | [optional] 
**file_agent_version** | **str** | Version of file agent on the VM of a third party partner solution. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

