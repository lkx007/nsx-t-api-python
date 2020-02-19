# ServiceManager

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
**port** | **int** | Integer port value to specify a standard/non-standard HTTPS port. | 
**service_ids** | [**list[ResourceReference]**](ResourceReference.md) | The IDs of services, provided by partner. | 
**authentication_scheme** | [**CallbackAuthenticationScheme**](CallbackAuthenticationScheme.md) |  | 
**thumbprint** | **str** | Thumbprint (SHA-256 hash represented in lower case hex) for the certificate on the partner console. This will be required to establish secure communication with the console and to avoid man-in-the-middle attacks. | [optional] 
**vendor_id** | **str** | Id which is unique to a vendor or partner for which the service is created. | [optional] 
**uri** | **str** | URI on which notification requests should be made on the specified server. | 
**server** | **str** | IP address or fully qualified domain name of the partner REST server. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

