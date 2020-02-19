# IPSecVPNTunnelProfile

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
**encapsulation_mode** | **str** | Encapsulation Mode to be used for encryption of packet. Tunnel mode protects internal routing information by encrypting IP header of original packet. | [optional] [default to 'TUNNEL_MODE']
**transform_protocol** | **str** | IPSec transform specifies IPSec security protocol. | [optional] [default to 'ESP']
**digest_algorithms** | **list[str]** | Algorithm to be used for message digest. Default digest algorithm is implicitly covered by default encryption algorithm \&quot;AES_GCM_128\&quot;. | [optional] 
**encryption_algorithms** | **list[str]** | Encryption algorithm to encrypt/decrypt the messages exchanged between IPSec VPN initiator and responder during tunnel negotiation. Default is AES_GCM_128. | [optional] 
**enable_perfect_forward_secrecy** | **bool** | If true, perfect forward secrecy (PFS) is enabled. | [optional] [default to True]
**dh_groups** | **list[str]** | Diffie-Hellman group to be used if PFS is enabled. Default is GROUP14. | [optional] 
**df_policy** | **str** | Defragmentation policy helps to handle defragmentation bit present in the inner packet. COPY copies the defragmentation bit from the inner IP packet into the outer packet. CLEAR ignores the defragmentation bit present in the inner packet. | [optional] [default to 'COPY']
**sa_life_time** | **int** | SA life time specifies the expiry time of security association. Default is 3600 seconds.  | [optional] [default to 3600]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

