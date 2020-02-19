# AppDiscoverySession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_owned** | **bool** | Indicates system owned resource | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**create_user** | **str** | ID of the user who created this resource | [optional] 
**protection** | **str** | Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite&#x3D;true. UNKNOWN - the _protection field could not be determined for this           entity.  | [optional] 
**create_time** | **int** | Timestamp of resource creation | [optional] 
**last_modified_time** | **int** | Timestamp of last modification | [optional] 
**last_modified_user** | **str** | ID of the user who last modified this resource | [optional] 
**id** | **str** | Unique identifier of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | [optional] 
**status** | **str** | The status of the session | [optional] 
**end_timestamp** | **int** | End time of the session expressed in milliseconds since epoch | [optional] 
**start_timestamp** | **int** | Start time of the session expressed in milliseconds since epoch | [optional] 
**failed_reason** | **str** | The reason for the session status failure. | [optional] 
**reclassification** | **str** | Some App Profiles that were part of the discovery session could be modified or deleted | after the session has been completed. NOT_REQUIRED status denotes that there were no such modifications. | REQUIRED status denotes some App Profiles that were part of the session has been modified/deleted and some | and some applications might not have been classfifed correctly. Use /session/&lt;session-id&gt;/reclassify API to| re-classfy the applications discovered based on app profiles.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

