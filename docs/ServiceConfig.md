# ServiceConfig

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
**applied_to** | [**list[ResourceReference]**](ResourceReference.md) | The list of entities that the configurations should be applied to. This can either be a NSGroup or any other entity like TransportNode, LogicalPorts etc.  | [optional] 
**precedence** | **int** | Every ServiceConfig has a priority based upon its precedence value. Lower the value of precedence, higher will be its priority. If user doesnt specify the precedence, it is generated automatically by system. The precedence is generated based upon the type of profile used in ServiceConfig. Precedence are auto-generated in decreasing order with difference of 100. Automatically generated precedence value will be 100 less than the current minimum value of precedence of ServiceConfig of a given profile type in system.There cannot be duplicate precedence for ServiceConfig of same profile type.  | [optional] 
**profiles** | [**list[NSXProfileReference]**](NSXProfileReference.md) | These are the NSX Profiles which will be added to service config, which will be applied to entities/groups provided to applied_to field of service config.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

