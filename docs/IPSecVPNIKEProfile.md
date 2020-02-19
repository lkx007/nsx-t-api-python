# IPSecVPNIKEProfile

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
**digest_algorithms** | **list[str]** | Algorithm to be used for message digest during Internet Key Exchange(IKE) negotiation. Default is SHA2_256. | [optional] 
**encryption_algorithms** | **list[str]** | Encryption algorithm is used during Internet Key Exchange(IKE) negotiation. Default is AES_128. | [optional] 
**dh_groups** | **list[str]** | Diffie-Hellman group to be used if PFS is enabled. Default is GROUP14. | [optional] 
**sa_life_time** | **int** | Life time for security association. Default is 86400 seconds (1 day). | [optional] [default to 86400]
**ike_version** | **str** | IKE protocol version to be used. IKE-Flex will initiate IKE-V2 and responds to both IKE-V1 and IKE-V2. | [optional] [default to 'IKE_V2']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

