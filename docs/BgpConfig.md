# BgpConfig

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
**inter_sr_ibgp** | [**InterSRRoutingConfig**](InterSRRoutingConfig.md) |  | [optional] 
**as_number** | **int** | This is a deprecated property, Please use &#x27;as_num&#x27; instead. | [optional] 
**route_aggregation** | [**list[BgpRouteAggregation]**](BgpRouteAggregation.md) | List of routes to be aggregated | [optional] 
**logical_router_id** | **str** | Logical router id | [optional] 
**graceful_restart** | **bool** | Flag to enable graceful restart. This field is deprecated, kindly use graceful_restart_config parameter for graceful restart configuration. If both parameters are set and consistent with each other [i.e. graceful_restart&#x3D;false and graceful_restart_mode&#x3D;HELPER_ONLY OR graceful_restart&#x3D;true and graceful_restart_mode&#x3D;GR_AND_HELPER] then this is allowed, but if inconsistent with each other then this is not allowed and validation error will be thrown.  | [optional] 
**as_num** | **str** | 4 Byte ASN in ASPLAIN/ASDOT Format | [optional] 
**enabled** | **bool** | While creation of BGP config this flag will be set to - true for Tier0 logical router with Active-Active high-availability mode - false for Tier0 logical router with Active-Standby high-availanility mode. User can change this value while updating the config. If this property is not specified in the payload, the default value will be considered as false irrespective of the high-availability mode.  | [optional] [default to False]
**graceful_restart_config** | [**GracefulRestartConfig**](GracefulRestartConfig.md) |  | [optional] 
**multipath_relax** | **bool** | Flag to enable BGP multipath relax option | [optional] [default to True]
**ecmp** | **bool** | While creation of BGP config this flag will be set to - true for Tier0 logical router with Active-Active high-availability mode - false for Tier0 logical router with Active-Standby high-availability mode. User can change this value while updating BGP config. If this property is not specified in the payload, the default value will be considered as true irrespective of the high-availability mode.  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

