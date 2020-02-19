# DirectoryDomainSyncSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_sync_cron_expr** | **str** | Directory domain full synchronization schedule using cron expression. For example, cron expression \&quot;0 0 12 ? * SUN *\&quot; means full sync is scheduled every Sunday midnight. If this object is null, it means there is no background cron job running for full sync. | [optional] 
**delta_sync_interval** | **int** | Directory domain delta synchronization interval time between two delta sync in minutes. | [optional] [default to 180]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

