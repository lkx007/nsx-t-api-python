# DhcpStaticBinding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease_time** | **int** | Lease time, in seconds, [60-(2^32-1)]. Default is 86400. | [optional] [default to 86400]
**gateway_ip** | **str** | Gateway ip address of the allocation. | [optional] 
**options** | [**DhcpOptions**](DhcpOptions.md) |  | [optional] 
**ip_address** | **str** | The ip address to be assigned to the host. | 
**host_name** | **str** | The host name to be assigned to the host. | [optional] 
**mac_address** | **str** | The MAC address of the host. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

