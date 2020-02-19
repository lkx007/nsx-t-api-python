# DSSection

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
**stateful** | **bool** | Stateful or Stateless nature of distributed service section is enforced on all rules inside the section. Layer3 sections can be stateful or stateless. Layer2 sections can only be stateless. | 
**is_default** | **bool** | It is a boolean flag which reflects whether a distributed service section is default section or not. Each Layer 3 and Layer 2 section will have at least and at most one default section. | [optional] 
**applied_tos** | [**list[ResourceReference]**](ResourceReference.md) | List of objects where the rules in this section will be enforced. This will take precedence over rule level appliedTo. | [optional] 
**rule_count** | **int** | Number of rules in this section. | [optional] 
**section_type** | **str** | Type of the rules which a section can contain. Only homogeneous sections are supported. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

