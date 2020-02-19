# InstanceRuntime

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
**service_vm_id** | **str** | Service-VM/SVM id of deployed virtual-machine. | [optional] 
**deployment_status** | **str** | Service-Instance Runtime deployment status of the Service-VM. It shows the latest status during the process of deployment, redeploy, upgrade, and un-deployment of VM. | [optional] 
**vm_nic_info** | [**VmNicInfo**](VmNicInfo.md) |  | [optional] 
**maintenance_mode** | **str** | The maintenance mode indicates whether the corresponding service VM is in maintenance mode. The service VM will not be used to service new requests if it is in maintenance mode.  | [optional] 
**runtime_status** | **str** | Service-Instance Runtime status of the deployed Service-VM. | [optional] 
**error_message** | **str** | Error message for the Service Instance Runtime if any. | [optional] 
**service_instance_id** | **str** | Id of an instantiation of a registered service. | [optional] 
**runtime_health_status_by_partner** | **str** | Service-Instance runtime health status set by partner to indicate whether the service is running properly or not.  | [optional] 
**unhealthy_reason** | **str** | Reason provided by partner for the service being unhealthy. This could be due to various reasons such as connectivity lost as an example.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

