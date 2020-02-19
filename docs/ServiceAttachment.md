# ServiceAttachment

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
**attachment_status** | **str** | UP - A Service Attachment will have its Service Port - UP and with a configured IP address. DOWN - An Inactive ServiceAttachment has its Service Port - DOWN. It can be used to connect set of appliances that do not need to exchange traffic to/from/through the Edge node. | [optional] [default to 'UP']
**service_port** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**deployed_to** | [**ResourceReference**](ResourceReference.md) |  | 
**logical_switch** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**local_ips** | [**list[IPInfo]**](IPInfo.md) | Local IPs associated with this Service Attachment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

