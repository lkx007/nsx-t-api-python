# IntelligenceHostConfigurationInfo

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
**context_data_collection_interval** | **int** | Interval in minute of reporting VM guest context data to NSX-Intelligence.  | [optional] 
**broker_truststore** | **str** | A truststore to establish the trust between NSX and NSX-Intelligence brokers.  | [optional] 
**broker_certificate** | **str** | A broker certificate to verify the identity of brokers.  | [optional] 
**context_user_uids** | **list[str]** | List of linux user uid to collect context data. Empty implies all users.  | [optional] 
**context_process_hashes** | **list[str]** | List of hashes of processes to collect context data. Empty implies all processes.  | [optional] 
**enable_data_collection** | **bool** | Enable NSX-Intelligence data collection in host nodes.  | [optional] 
**context_process_names** | **list[str]** | List of processes to collect context data. Empty implies all processes.  | [optional] 
**private_ip_prefix** | [**list[IntelligenceFlowPrivateIpPrefixInfo]**](IntelligenceFlowPrivateIpPrefixInfo.md) | List of private IP prefix that NSX-Intelligence network flow is collected from.  | [optional] 
**broker_bootstrap_servers** | [**list[IntelligenceBrokerEndpointInfo]**](IntelligenceBrokerEndpointInfo.md) | List of NSX-Intelligence broker endpoints that host nodes contact initially.  | [optional] 
**max_inactive_flow_count** | **int** | Maximum inactive network flow to collect in collection interval.  | [optional] 
**context_user_sids** | **list[str]** | List of windows user sid to collect context data. Empty implies all users.  | [optional] 
**flow_data_collection_interval** | **int** | Interval in minute of reporting network flow data to NSX-Intelligence.  | [optional] 
**max_active_flow_count** | **int** | Maximum active network flow to collect in collection interval.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

