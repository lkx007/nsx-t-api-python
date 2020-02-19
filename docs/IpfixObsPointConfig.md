# IpfixObsPointConfig

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
**idle_timeout** | **int** | The time in seconds after a Flow is expired if no more packets matching this Flow are received by the cache.  | [optional] [default to 300]
**observation_domain_id** | **int** | An identifier that is unique to the exporting process and used to meter the Flows.  | [optional] [default to 0]
**collectors** | [**list[IpfixCollector]**](IpfixCollector.md) | List of IPFIX collectors | [optional] 
**active_timeout** | **int** | The time in seconds after a Flow is expired even if more packets matching this Flow are received by the cache.  | [optional] [default to 300]
**packet_sample_probability** | **float** | The probability in percentage that a packet is sampled. The value should be  in range (0,100] and can only have three decimal places at most. The probability  is equal for every packet.  | [optional] 
**enabled** | **bool** | Enabled status of IPFIX export | 
**max_flows** | **int** | The maximum number of flow entries in each exporter flow cache.  | [optional] [default to 16384]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

