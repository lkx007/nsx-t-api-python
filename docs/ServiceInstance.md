# ServiceInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_failure_policy** | **str** | Failure policy of the service instance - if it has to be different from the service. By default the service instance inherits the FailurePolicy of the service it belongs to. | [optional] 
**transport_type** | **str** | Transport to be used by this service instance for deploying the Service-VM. This field is to be set Not Applicable(NA) if the service only caters to functionality EPP(Endpoint Protection). | 
**resource_type** | **str** | ServiceInstance is used when NSX handles the lifecyle of   appliance. Deployment and appliance related all the information is necessary. ByodServiceInstance is a custom instance to be used when NSX is not handling   the lifecycles of appliance/s. User will manage their own appliance (BYOD)   to connect with NSX. VirtualServiceInstance is a a custom instance to be used when NSX is not   handling the lifecycle of an appliance and when the user is not bringing   their own appliance.  | 
**service_id** | **str** | The Service to which the service instance is associated. | [optional] 
**deployment_spec_name** | **str** | Name of the deployment spec to be used by this service instance. | 
**instance_deployment_template** | [**DeploymentTemplate**](DeploymentTemplate.md) |  | 
**implementation_type** | **str** | Implementation to be used by this service instance for deploying the Service-VM. | 
**attachment_point** | **str** | Attachment point to be used by this service instance for deploying the Service-VM. | 
**instance_deployment_config** | [**InstanceDeploymentConfig**](InstanceDeploymentConfig.md) |  | [optional] 
**deployment_mode** | **str** | Deployment mode specifies where the partner appliance will be deployed in HA or non-HA i.e standalone mode. | [default to 'ACTIVE_STANDBY']
**deployed_to** | [**list[ResourceReference]**](ResourceReference.md) | List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion. | 
**service_deployment_id** | **str** | Id of the Service Deployment using which the instances were deployed. Its available only for instances that were deployed using service deployment API. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

