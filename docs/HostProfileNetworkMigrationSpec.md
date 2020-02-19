# HostProfileNetworkMigrationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead. | 
**network_mappings** | [**list[VmkToLogicalSwitchMapping]**](VmkToLogicalSwitchMapping.md) | Based on provided mappings, VMkernal adapters will be migrated to mentioned logical switch. Without mappings specification doesn&#x27;t make any sense, hence minium one mapping should be specified. Assuming some sane value of 10 maximum migrations which will be supported by any single specification.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

