# AppDiscoverySessionResultSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the session | [optional] 
**end_timestamp** | **int** | End time of the session expressed in milliseconds since epoch | [optional] 
**start_timestamp** | **int** | Start time of the session expressed in milliseconds since epoch | [optional] 
**failed_reason** | **str** | The reason for the session status failure. | [optional] 
**reclassification** | **str** | Some App Profiles that were part of the discovery session could be modified or deleted | after the session has been completed. NOT_REQUIRED status denotes that there were no such modifications. | REQUIRED status denotes some App Profiles that were part of the session has been modified/deleted and some | and some applications might not have been classfifed correctly. Use /session/&lt;session-id&gt;/reclassify API to| re-classfy the applications discovered based on app profiles.  | [optional] 
**app_profile_summary_list** | [**list[AppDiscoveryAppProfileResultSummary]**](AppDiscoveryAppProfileResultSummary.md) | List of App Profiles summary discovered in this session | [optional] 
**ns_groups** | [**list[NSGroupMetaInfo]**](NSGroupMetaInfo.md) | List of NSGroups provided for discovery for this session | [optional] 
**app_profiles** | [**list[AppProfileMetaInfo]**](AppProfileMetaInfo.md) | List of app profiles targeted to be classified for this session | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

