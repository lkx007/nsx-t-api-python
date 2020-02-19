# HealthCheckResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_mtu_status** | **str** | Status of VLAN-MTU health check result; TRUNKED - all specified VLAN IDs are allowed by VLAN and MTU settings; UNTRUNKED - some/all specified VLAN IDs may be disallowed by VLAN or MTU settings; UNKNOWN - some/all health check result are unknown due to infrastructure issues.  | [optional] 
**results_per_transport_node** | [**list[HealthCheckResultPerTransportNode]**](HealthCheckResultPerTransportNode.md) | List of health check results on specific transport node  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

