# ServiceDefinition

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
**service_deployment_spec** | [**ServiceDeploymentSpec**](ServiceDeploymentSpec.md) |  | [optional] 
**service_capability** | [**ServiceCapability**](ServiceCapability.md) |  | [optional] 
**functionalities** | **list[str]** | The capabilities provided by the services. Needs to be one or more of the following | NG_FW - Next Generation Firewall | IDS_IPS - Intrusion detection System / Intrusion Prevention System | NET_MON - Network Monitoring | HCX - Hybrid Cloud Exchange | BYOD - Bring Your Own Device | EPP - Endpoint Protection.(Third party AntiVirus partners using NXGI should use this functionality for the service) | 
**attachment_point** | **list[str]** | The point at which the service is deployed/attached for redirecting the traffic to the the partner appliance. Attachment Point is required if Service caters to any functionality other than EPP. | [optional] 
**service_manager_id** | **str** | ID of the service manager to which this service is attached with. This field is not set during creation of service. This field will be set explicitly when Service Manager is created successfully using this service.  | [optional] 
**vendor_id** | **str** | Id which is unique to a vendor or partner for which the service is created. | 
**on_failure_policy** | **str** | Failure policy for the service tells datapath, the action to take i.e to Allow or Block traffic during failure scenarios. For north-south ServiceInsertion, failure policy in the service instance takes precedence. For east-west ServiceInsertion, failure policy in the service chain takes precedence. BLOCK is not supported for Endpoint protection (EPP) functionality. | [optional] [default to 'ALLOW']
**transports** | **list[str]** | Transport Type of the service, which is the mechanism of redirecting the traffic to the the partner appliance. Transport type is required if Service caters to any functionality other than EPP. | [optional] 
**implementations** | **list[str]** | This indicates the insertion point of the service i.e whether the service will be used to protect North-South or East-West traffic in the datacenter. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

