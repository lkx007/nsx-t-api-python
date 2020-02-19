# ServiceChain

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
**reverse_path_service_profiles** | [**list[ResourceReference]**](ResourceReference.md) | List of ServiceInsertionServiceProfiles id. Reverse path service profiles are applied to egress traffic and is optional. 2 different set of profiles can be defined for forward and reverse path. If not defined, the reverse of the forward path service profile is applied. | [optional] 
**service_attachments** | [**list[ResourceReference]**](ResourceReference.md) | Service attachment specifies the scope i.e Service plane at which the SVMs are deployed. | 
**forward_path_service_profiles** | [**list[ResourceReference]**](ResourceReference.md) | List of ServiceInsertionServiceProfiles that constitutes the the service chain. The forward path service profiles are applied to ingress traffic. | 
**service_chain_id** | **str** | A unique id generated for every service chain. This is not a uuid. | [optional] 
**path_selection_policy** | **str** | Path selection policy can be - ANY - Service Insertion is free to redirect to any service path regardless of any load balancing considerations or flow pinning. LOCAL - means to prefer local service insances. REMOTE - preference is to redirect to the SVM co-located on the same host. | [optional] [default to 'ANY']
**on_failure_policy** | **str** | Failure policy for the service tells datapath, the action to take i.e to allow or block traffic during failure scenarios. | [optional] [default to 'ALLOW']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

