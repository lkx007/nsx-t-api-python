# EdgeCluster

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
**member_node_type** | **str** | Edge cluster is homogenous collection of transport nodes. Hence all transport nodes of the cluster must be of same type. This readonly field shows the type of transport nodes.  | [optional] 
**cluster_profile_bindings** | [**list[ClusterProfileTypeIdEntry]**](ClusterProfileTypeIdEntry.md) | Edge cluster profile bindings | [optional] 
**allocation_rules** | [**list[AllocationRule]**](AllocationRule.md) | Set of allocation rules and respected action for auto placement of logical router, DHCP and MDProxy on edge cluster members.  | [optional] 
**members** | [**list[EdgeClusterMember]**](EdgeClusterMember.md) | EdgeCluster only supports homogeneous members. These member should be backed by either EdgeNode or PublicCloudGatewayNode. TransportNode type of these nodes should be the same. DeploymentType (VIRTUAL_MACHINE|PHYSICAL_MACHINE) of these EdgeNodes is recommended to be the same. EdgeCluster supports members of different deployment types.  | [optional] 
**deployment_type** | **str** | This field is a readonly field which shows the deployment_type of members. It returns UNKNOWN if there are no members, and returns VIRTUAL_MACHINE| PHYSICAL_MACHINE if all edge members are VIRTUAL_MACHINE|PHYSICAL_MACHINE. It returns HYBRID if the cluster contains edge members of both types VIRTUAL_MACHINE and PHYSICAL_MACHINE.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

