# AdvertisementConfig

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
**advertise_nsx_connected_routes** | **bool** | Flag to advertise all connected routes | [optional] [default to False]
**advertise_lb_vip** | **bool** | Flag to advertise lb vip ips | [optional] [default to False]
**advertise_static_routes** | **bool** | Flag to advertise all static routes | [optional] [default to False]
**logical_router_id** | **str** | TIER1 logical router id on which to enable this configuration | [optional] 
**advertise_dns_forwarder** | **bool** | Flag to advertise all routes of dns forwarder listener ips and source ips | [optional] [default to False]
**advertise_nat_routes** | **bool** | Flag to advertise all routes of nat | [optional] [default to False]
**advertise_ipsec_local_ip** | **bool** | Flag to advertise all IPSec VPN local endpoint ips to linked TIER0 logical router | [optional] [default to False]
**enabled** | **bool** | Flag to enable this configuration | [optional] [default to False]
**advertise_lb_snat_ip** | **bool** | Flag to advertise all lb SNAT ips | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

