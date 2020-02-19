# IPSecVPNSession

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
**resource_type** | **str** | A Policy Based VPN requires to define protect rules that match   local and peer subnets. IPSec security associations is   negotiated for each pair of local and peer subnet. A Route Based VPN is more flexible, more powerful and recommended over   policy based VPN. IP Tunnel port is created and all traffic routed via   tunnel port is protected. Routes can be configured statically   or can be learned through BGP. A route based VPN is must for establishing   redundant VPN session to remote site.  | 
**peer_endpoint_id** | **str** | Peer endpoint identifier. | 
**ipsec_vpn_service_id** | **str** | Identifier of VPN Service linked with local endpoint. | [optional] 
**local_endpoint_id** | **str** | Local endpoint identifier. | 
**tcp_mss_clamping** | [**TcpMssClamping**](TcpMssClamping.md) |  | [optional] 
**enabled** | **bool** | Enable/Disable IPSec VPN session. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

