# TelemetryProxy

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
**username** | **str** | Specify the user name used to authenticate with the proxy server, if required.  | [optional] 
**password** | **str** | Specify the password used to authenticate with the proxy server, if required. A GET call on /telemetry/config returns a non-meaningful password to maintain security. To change the password to a new value, issue a PUT call after updating this field. To remove the password, issue a PUT call after emptying this field. To retain a previously set password, issue a PUT call keeping the non-meaningful value obtained from the GET call.  | [optional] 
**scheme** | **str** | The scheme accepted by the proxy server. Specify one of HTTP and HTTPS.  | 
**hostname** | **str** | Specify the fully qualified domain name, or ip address, of the proxy server.  | 
**port** | **int** | Specify the port of the proxy server. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

