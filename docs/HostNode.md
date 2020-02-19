# HostNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovered_ip_addresses** | **list[str]** | Discovered IP Addresses of the fabric node, version 4 or 6 | [optional] 
**ip_addresses** | **list[str]** | IP Addresses of the Node, version 4 or 6. This property is mandatory for all nodes except for automatic deployment of edge virtual machine node. For automatic deployment, the ip address from management_port_subnets property will be considered.  | [optional] 
**external_id** | **str** | ID of the Node maintained on the Node and used to recognize the Node | [optional] 
**fqdn** | **str** | Fully qualified domain name of the fabric node | [optional] 
**resource_type** | **str** | Fabric node type, for example &#x27;HostNode&#x27;, &#x27;EdgeNode&#x27; or &#x27;PublicCloudGatewayNode&#x27; | 
**discovered_node_id** | **str** | Id of discovered node which was converted to create this node | [optional] 
**managed_by_server** | **str** | The id of the vCenter server managing the ESXi type HostNode | [optional] 
**host_credential** | [**HostNodeLoginCredential**](HostNodeLoginCredential.md) |  | [optional] 
**os_version** | **str** | Version of the hypervisor operating system | [optional] 
**os_type** | **str** | Hypervisor type, for example ESXi or RHEL KVM | 
**maintenance_mode_state** | **str** | Indicates host node&#x27;s maintenance mode state. The state is ENTERING when a task to put the host in maintenance-mode is in progress.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

