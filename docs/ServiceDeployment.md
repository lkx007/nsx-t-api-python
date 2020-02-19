# ServiceDeployment

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
**perimeter** | **str** | This indicates the deployment perimeter, such as a VC cluster or a host. | [optional] [default to 'HOST']
**deployment_spec_name** | **str** | Name of the deployment spec to be used for deployment, which specifies the OVF provided by the partner and the form factor. | 
**deployment_mode** | **str** | Mode of deployment. Currently, only stand alone deployment is supported. It is a single VM deployed through this deployment spec. In future, HA configurations will be supported here. | [optional] [default to 'STAND_ALONE']
**instance_deployment_template** | [**DeploymentTemplate**](DeploymentTemplate.md) |  | 
**service_deployment_config** | [**ServiceDeploymentConfig**](ServiceDeploymentConfig.md) |  | 
**service_id** | **str** | The Service to which the service deployment is associated. | [optional] 
**clustered_deployment_count** | **int** | Number of instances in case of clustered deployment. | [optional] [default to 1]
**deployed_to** | [**list[ResourceReference]**](ResourceReference.md) | List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion. Service Attachment in case of E-W ServiceInsertion. | [optional] 
**deployment_type** | **str** | Specifies whether the service VM should be deployed on each host such that it provides partner service locally on the host, or whether the service VMs can be deployed as a cluster. If deployment_type is CLUSTERED, then the clustered_deployment_count should be provided. | [optional] [default to 'CLUSTERED']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

