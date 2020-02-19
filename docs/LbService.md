# LbService

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
**access_log_enabled** | **bool** | whether access log is enabled | [optional] [default to False]
**attachment** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**error_log_level** | **str** | Load balancer engine writes information about encountered issues of different severity levels to the error log. This setting is used to define the severity level of the error log.  | [optional] [default to 'INFO']
**enabled** | **bool** | whether the load balancer service is enabled | [optional] [default to True]
**virtual_server_ids** | **list[str]** | virtual servers can be associated to LbService(which is similar to physical/virtual load balancer), Lb virtual servers, pools and other entities could be defined independently, the virtual server identifier list here would be used to maintain the relationship of LbService and other Lb entities.  | [optional] 
**size** | **str** | the size of load balancer service | [optional] [default to 'SMALL']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

