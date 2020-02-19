# swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_compute_collection_transport_node_template_and_tn_collection**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#create_compute_collection_transport_node_template_and_tn_collection) | **POST** /compute-collection-transport-node-templates | Create transport node template for compute collection.
[**create_network_migration_spec**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#create_network_migration_spec) | **POST** /network-migration-specs | Create a template of network migration specification.
[**create_transport_node_with_deployment_info**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#create_transport_node_with_deployment_info) | **POST** /transport-nodes | Create a Transport Node
[**delete_compute_collection_transport_node_template_and_tn_collection**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#delete_compute_collection_transport_node_template_and_tn_collection) | **DELETE** /compute-collection-transport-node-templates/{template-id} | Delete a compute collection transport node template
[**delete_network_migration_spec**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#delete_network_migration_spec) | **DELETE** /network-migration-specs/{template-id} | Delete a network migration specification template
[**delete_transport_node_with_deployment_info**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#delete_transport_node_with_deployment_info) | **DELETE** /transport-nodes/{transport-node-id} | Delete a Transport Node
[**disable_flow_cache_disable_flow_cache**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#disable_flow_cache_disable_flow_cache) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;disable_flow_cache | Disable flow cache for an edge transport node
[**enable_flow_cache_enable_flow_cache**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#enable_flow_cache_enable_flow_cache) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;enable_flow_cache | Enable flow cache for an edge transport node
[**get_all_transport_nodes_status**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_all_transport_nodes_status) | **GET** /transport-nodes/status | Get high-level summary of all transport nodes. The service layer does not support source &#x3D; realtime or cached.
[**get_all_transport_zone_status**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_all_transport_zone_status) | **GET** /transport-zones/status | Get high-level summary of a transport zone. The service layer does not support source &#x3D; realtime or cached.
[**get_compute_collection_transport_node_template**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_compute_collection_transport_node_template) | **GET** /compute-collection-transport-node-templates/{template-id} | Get compute collection transportnode template by id
[**get_compute_collection_transport_node_template_state**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_compute_collection_transport_node_template_state) | **GET** /compute-collection-transport-node-templates/{template-id}/state | Get compute collection transportnode template application states
[**get_fabric_node_modules_of_transport_node**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_fabric_node_modules_of_transport_node) | **GET** /transport-nodes/{node-id}/modules | Get the module details of a transport node 
[**get_heatmap_transport_zone_status**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_heatmap_transport_zone_status) | **GET** /transport-zones/{zone-id}/status | Get high-level summary of a transport zone
[**get_network_migration_spec**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_network_migration_spec) | **GET** /network-migration-specs/{template-id} | Get network migration specification template by id.
[**get_pnic_statuses_for_transport_node**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_pnic_statuses_for_transport_node) | **GET** /transport-nodes/{node-id}/pnic-bond-status | Get high-level summary of a transport node
[**get_transport_node_report**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_transport_node_report) | **GET** /transport-zones/transport-node-status-report | Creates a status report of transport nodes of all the transport zones
[**get_transport_node_report_for_a_transport_zone**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_transport_node_report_for_a_transport_zone) | **GET** /transport-zones/{zone-id}/transport-node-status-report | Creates a status report of transport nodes in a transport zone
[**get_transport_node_state_with_deployment_info**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_transport_node_state_with_deployment_info) | **GET** /transport-nodes/{transport-node-id}/state | Get a Transport Node&#x27;s State
[**get_transport_node_status**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_transport_node_status) | **GET** /transport-nodes/{node-id}/status | Read status of a transport node
[**get_transport_node_with_deployment_info**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_transport_node_with_deployment_info) | **GET** /transport-nodes/{transport-node-id} | Get a Transport Node
[**get_tunnel**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#get_tunnel) | **GET** /transport-nodes/{node-id}/tunnels/{tunnel-name} | Tunnel properties
[**list_compute_collection_transport_node_templates**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_compute_collection_transport_node_templates) | **GET** /compute-collection-transport-node-templates | List compute collection transportnode templates
[**list_neighbor_properties**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_neighbor_properties) | **GET** /lldp/transport-nodes/{node-id}/interfaces | List LLDP Neighbor Properties of Transport Node
[**list_network_migration_specs**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_network_migration_specs) | **GET** /network-migration-specs | List all network migration specification templates.
[**list_remote_transport_node_status**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_remote_transport_node_status) | **GET** /transport-nodes/{node-id}/remote-transport-node-status | Read status of all transport nodes with tunnel connections to transport node 
[**list_transport_node_capabilities**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_transport_node_capabilities) | **GET** /transport-nodes/{transport-node-id}/capabilities | Return the list of capabilities of transport node
[**list_transport_node_interfaces**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_transport_node_interfaces) | **GET** /transport-nodes/{transport-node-id}/network/interfaces | List the specified transport node&#x27;s network interfaces
[**list_transport_node_status**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_transport_node_status) | **GET** /transport-zones/transport-node-status | Read status of all the transport nodes
[**list_transport_node_status_for_transport_zone**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_transport_node_status_for_transport_zone) | **GET** /transport-zones/{zone-id}/transport-node-status | Read status of transport nodes in a transport zone
[**list_transport_nodes_by_state_with_deployment_info**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_transport_nodes_by_state_with_deployment_info) | **GET** /transport-nodes/state | List transport nodes by realized state
[**list_transport_nodes_with_deployment_info**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#list_transport_nodes_with_deployment_info) | **GET** /transport-nodes | List Transport Nodes
[**query_tunnels**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#query_tunnels) | **GET** /transport-nodes/{node-id}/tunnels | List of tunnels
[**read_neighbor_properties**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#read_neighbor_properties) | **GET** /lldp/transport-nodes/{node-id}/interfaces/{interface-name} | Read LLDP Neighbor Properties of Transport Node by Interface Name 
[**read_transport_node_interface**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#read_transport_node_interface) | **GET** /transport-nodes/{transport-node-id}/network/interfaces/{interface-id} | Read the transport node&#x27;s network interface
[**read_transport_node_interface_statistics**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#read_transport_node_interface_statistics) | **GET** /transport-nodes/{transport-node-id}/network/interfaces/{interface-id}/stats | Read the NSX Manager&#x27;s Network Interface Statistics
[**refresh_transport_node**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#refresh_transport_node) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;refresh_node_configuration&amp;resource_type&#x3D;EdgeNode | Refresh the node configuration for the Edge node.
[**restart_transport_node_inventory_sync_restart_inventory_sync**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#restart_transport_node_inventory_sync_restart_inventory_sync) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;restart_inventory_sync | Restart the inventory sync for the node if it is paused currently.
[**restore_parent_cluster_configuration_restore_cluster_config**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#restore_parent_cluster_configuration_restore_cluster_config) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;restore_cluster_config | Apply cluster level Transport Node Profile on overridden host
[**resync_transport_node_resync_host_config**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#resync_transport_node_resync_host_config) | **POST** /transport-nodes/{transportnode-id}?action&#x3D;resync_host_config | Resync a Transport Node
[**update_compute_collection_transport_node_template_and_tn_collection**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#update_compute_collection_transport_node_template_and_tn_collection) | **PUT** /compute-collection-transport-node-templates/{template-id} | Update compute collection transportnode template
[**update_network_migration_spec**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#update_network_migration_spec) | **PUT** /network-migration-specs/{template-id} | Update a template of network migration specification.
[**update_transport_node_maintenance_mode**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#update_transport_node_maintenance_mode) | **POST** /transport-nodes/{transportnode-id} | Update transport node maintenance mode
[**update_transport_node_with_deployment_info**](ManagementPlaneApiNetworkTransportTransportNodesApi.md#update_transport_node_with_deployment_info) | **PUT** /transport-nodes/{transport-node-id} | Update a Transport Node

# **create_compute_collection_transport_node_template_and_tn_collection**
> ComputeCollectionTransportNodeTemplate create_compute_collection_transport_node_template_and_tn_collection(body)

Create transport node template for compute collection.

If automated transport node creation is configured on compute collection, this template will serve as the default setting for transport node creation. Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComputeCollectionTransportNodeTemplate() # ComputeCollectionTransportNodeTemplate | 

try:
    # Create transport node template for compute collection.
    api_response = api_instance.create_compute_collection_transport_node_template_and_tn_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->create_compute_collection_transport_node_template_and_tn_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComputeCollectionTransportNodeTemplate**](ComputeCollectionTransportNodeTemplate.md)|  | 

### Return type

[**ComputeCollectionTransportNodeTemplate**](ComputeCollectionTransportNodeTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_migration_spec**
> NetworkMigrationSpec create_network_migration_spec(body)

Create a template of network migration specification.

Network migration specification once created and can be used as a template to indicate associated component which networks should be migrated and where. Currently migration template can be associated with compute collections which are managed by vCenter host profiles, to trigger automatic migration of networks for Stateless ESX hosts. Currently we only support creation of HostProfileNetworkMigrationSpec type of specification. Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NetworkMigrationSpec() # NetworkMigrationSpec | 

try:
    # Create a template of network migration specification.
    api_response = api_instance.create_network_migration_spec(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->create_network_migration_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkMigrationSpec**](NetworkMigrationSpec.md)|  | 

### Return type

[**NetworkMigrationSpec**](NetworkMigrationSpec.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transport_node_with_deployment_info**
> TransportNode create_transport_node_with_deployment_info(body)

Create a Transport Node

Transport nodes are hypervisor hosts and NSX Edges that will participate in an NSX-T overlay. For a hypervisor host, this means that it hosts VMs that will communicate over NSX-T logical switches. For NSX Edges, this means that it will have logical router uplinks and downlinks.  This API creates transport node for a host node (hypervisor) or edge node (router) in the transport network.  When you run this command for a host, NSX Manager attempts to install the NSX kernel modules, which are packaged as VIB, RPM, or DEB files. For the installation to succeed, you must provide the host login credentials and the host thumbprint.  To get the ESXi host thumbprint, SSH to the host and run the <b>openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha256 -noout</b> command.  To generate host key thumbprint using SHA-256 algorithm please follow the steps below.  Log into the host, making sure that the connection is not vulnerable to a man in the middle attack. Check whether a public key already exists. Host public key is generally located at '/etc/ssh/ssh_host_rsa_key.pub'. If the key is not present then generate a new key by running the following command and follow the instructions.  <b>ssh-keygen -t rsa</b>  Now generate a SHA256 hash of the key using the following command. Please make sure to pass the appropriate file name if the public key is stored with a different file name other than the default 'id_rsa.pub'.  <b>awk '{print $2}' id_rsa.pub | base64 -d | sha256sum -b | sed 's/ .*$//' | xxd -r -p | base64</b> This api is deprecated as part of FN+TN unification. Please use Transport Node API to install NSX components on a node.  Additional documentation on creating a transport node can be found in the NSX-T Installation Guide.  In order for the transport node to forward packets, the host_switch_spec property must be specified.  Host switches (called bridges in OVS on KVM hypervisors) are the individual switches within the host virtual switch. Virtual machines are connected to the host switches.  When creating a transport node, you need to specify if the host switches are already manually preconfigured on the node, or if NSX should create and manage the host switches. You specify this choice by the type of host switches you pass in the host_switch_spec property of the TransportNode request payload.  For a KVM host, you can preconfigure the host switch, or you can have NSX Manager perform the configuration. For an ESXi host or NSX Edge node, NSX Manager always configures the host switch.  To preconfigure the host switches on a KVM host, pass an array of PreconfiguredHostSwitchSpec objects that describes those host switches. In the current NSX-T release, only one prefonfigured host switch can be specified.  See the PreconfiguredHostSwitchSpec schema definition for documentation on the properties that must be provided. Preconfigured host switches are only supported on KVM hosts, not on ESXi hosts or NSX Edge nodes.  To allow NSX to manage the host switch configuration on KVM hosts, ESXi hosts, or NSX Edge nodes, pass an array of StandardHostSwitchSpec objects in the host_switch_spec property, and NSX will automatically create host switches with the properties you provide. In the current NSX-T release, up to 5 host switches can be automatically managed. See the StandardHostSwitchSpec schema definition for documentation on the properties that must be provided.  Note: previous versions of NSX-T used a property named host_switches to specify the host switch configuration on the transport node. That property is deprecated, but still functions. You should configure new host switches using the host_switch_spec property.  The request should either provide node_deployement_info or node_id.  If the host node (hypervisor) or edge node (router) is already added in system then it can be converted to transport node by providing node_id in request.  If host node (hypervisor) or edge node (router) is not already present in system then information should be provided under node_deployment_info. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNode() # TransportNode | 

try:
    # Create a Transport Node
    api_response = api_instance.create_transport_node_with_deployment_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->create_transport_node_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNode**](TransportNode.md)|  | 

### Return type

[**TransportNode**](TransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compute_collection_transport_node_template_and_tn_collection**
> delete_compute_collection_transport_node_template_and_tn_collection(template_id)

Delete a compute collection transport node template

Delete the specified compute collection transport node template. Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | 

try:
    # Delete a compute collection transport node template
    api_instance.delete_compute_collection_transport_node_template_and_tn_collection(template_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->delete_compute_collection_transport_node_template_and_tn_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_migration_spec**
> delete_network_migration_spec(template_id)

Delete a network migration specification template

Delete the specified network migration specification template. Delete will fail if this is a HostProfileNetworkMigrationSpec and is associated with certain compute collection. Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | 

try:
    # Delete a network migration specification template
    api_instance.delete_network_migration_spec(template_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->delete_network_migration_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transport_node_with_deployment_info**
> delete_transport_node_with_deployment_info(transport_node_id, force=force, unprepare_host=unprepare_host)

Delete a Transport Node

Deletes the specified transport node. Query param force can be used to force delete the host nodes. Force deletion of edge and public cloud gateway nodes is not supported.  It also removes the specified node (host or edge) from system. If unprepare_host option is set to false, then host will be deleted without uninstalling the NSX components from the host. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 
force = true # bool | Force delete the resource even if it is being used somewhere  (optional)
unprepare_host = true # bool | Uninstall NSX components from host while deleting (optional)

try:
    # Delete a Transport Node
    api_instance.delete_transport_node_with_deployment_info(transport_node_id, force=force, unprepare_host=unprepare_host)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->delete_transport_node_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] 
 **unprepare_host** | **bool**| Uninstall NSX components from host while deleting | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_flow_cache_disable_flow_cache**
> disable_flow_cache_disable_flow_cache(transport_node_id)

Disable flow cache for an edge transport node

Disable flow cache for edge transport node. Caution: This involves restart of the edge dataplane and hence may lead to network disruption. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Disable flow cache for an edge transport node
    api_instance.disable_flow_cache_disable_flow_cache(transport_node_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->disable_flow_cache_disable_flow_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_flow_cache_enable_flow_cache**
> enable_flow_cache_enable_flow_cache(transport_node_id)

Enable flow cache for an edge transport node

Enable flow cache for edge transport node. Caution: This involves restart of the edge dataplane and hence may lead to network disruption. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Enable flow cache for an edge transport node
    api_instance.enable_flow_cache_enable_flow_cache(transport_node_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->enable_flow_cache_enable_flow_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_transport_nodes_status**
> HeatMapTransportZoneStatus get_all_transport_nodes_status(node_type=node_type)

Get high-level summary of all transport nodes. The service layer does not support source = realtime or cached.

Get high-level summary of all transport nodes. The service layer does not support source = realtime or cached.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
node_type = 'node_type_example' # str | Transport node type (optional)

try:
    # Get high-level summary of all transport nodes. The service layer does not support source = realtime or cached.
    api_response = api_instance.get_all_transport_nodes_status(node_type=node_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_all_transport_nodes_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_type** | **str**| Transport node type | [optional] 

### Return type

[**HeatMapTransportZoneStatus**](HeatMapTransportZoneStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_transport_zone_status**
> HeatMapTransportNodesAggregateStatus get_all_transport_zone_status()

Get high-level summary of a transport zone. The service layer does not support source = realtime or cached.

Get high-level summary of a transport zone. The service layer does not support source = realtime or cached.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))

try:
    # Get high-level summary of a transport zone. The service layer does not support source = realtime or cached.
    api_response = api_instance.get_all_transport_zone_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_all_transport_zone_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HeatMapTransportNodesAggregateStatus**](HeatMapTransportNodesAggregateStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compute_collection_transport_node_template**
> ComputeCollectionTransportNodeTemplate get_compute_collection_transport_node_template(template_id)

Get compute collection transportnode template by id

Returns compute collection transportnode template by id Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | 

try:
    # Get compute collection transportnode template by id
    api_response = api_instance.get_compute_collection_transport_node_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_compute_collection_transport_node_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**ComputeCollectionTransportNodeTemplate**](ComputeCollectionTransportNodeTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compute_collection_transport_node_template_state**
> ComputeCollectionTransportNodeTemplateStateList get_compute_collection_transport_node_template_state(template_id, compute_collection_id=compute_collection_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get compute collection transportnode template application states

Returns detailed transport node states for this compute collection Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | 
compute_collection_id = 'compute_collection_id_example' # str | Compute collection id (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get compute collection transportnode template application states
    api_response = api_instance.get_compute_collection_transport_node_template_state(template_id, compute_collection_id=compute_collection_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_compute_collection_transport_node_template_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **compute_collection_id** | **str**| Compute collection id | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ComputeCollectionTransportNodeTemplateStateList**](ComputeCollectionTransportNodeTemplateStateList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabric_node_modules_of_transport_node**
> SoftwareModuleResult get_fabric_node_modules_of_transport_node(node_id)

Get the module details of a transport node 

Get the module details of a transport node 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Get the module details of a transport node 
    api_response = api_instance.get_fabric_node_modules_of_transport_node(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_fabric_node_modules_of_transport_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**SoftwareModuleResult**](SoftwareModuleResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap_transport_zone_status**
> HeatMapTransportZoneStatus get_heatmap_transport_zone_status(zone_id, source=source)

Get high-level summary of a transport zone

Get high-level summary of a transport zone

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | ID of transport zone
source = 'source_example' # str | Data source type. (optional)

try:
    # Get high-level summary of a transport zone
    api_response = api_instance.get_heatmap_transport_zone_status(zone_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_heatmap_transport_zone_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| ID of transport zone | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**HeatMapTransportZoneStatus**](HeatMapTransportZoneStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_migration_spec**
> NetworkMigrationSpec get_network_migration_spec(template_id)

Get network migration specification template by id.

Network migration specification once created and can be used as a template to indicate associated component which networks should be migrated and where. Currently migration template can be associated with compute collections which are managed by vCenter host profiles, to trigger automatic migration of networks for Stateless ESX hosts. Currently we only support creation of HostProfileNetworkMigrationSpec type of specification. Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | 

try:
    # Get network migration specification template by id.
    api_response = api_instance.get_network_migration_spec(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_network_migration_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**NetworkMigrationSpec**](NetworkMigrationSpec.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pnic_statuses_for_transport_node**
> PnicBondStatusListResult get_pnic_statuses_for_transport_node(node_id, status=status)

Get high-level summary of a transport node

Get high-level summary of a transport node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
status = 'status_example' # str | pNic/bond status (optional)

try:
    # Get high-level summary of a transport node
    api_response = api_instance.get_pnic_statuses_for_transport_node(node_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_pnic_statuses_for_transport_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **status** | **str**| pNic/bond status | [optional] 

### Return type

[**PnicBondStatusListResult**](PnicBondStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_report**
> get_transport_node_report(source=source, status=status)

Creates a status report of transport nodes of all the transport zones

You must provide the request header \"Accept:application/octet-stream\" when calling this API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Transport node (optional)

try:
    # Creates a status report of transport nodes of all the transport zones
    api_instance.get_transport_node_report(source=source, status=status)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_transport_node_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Transport node | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_report_for_a_transport_zone**
> get_transport_node_report_for_a_transport_zone(zone_id, source=source, status=status)

Creates a status report of transport nodes in a transport zone

You must provide the request header \"Accept:application/octet-stream\" when calling this API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | ID of transport zone
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Transport node (optional)

try:
    # Creates a status report of transport nodes in a transport zone
    api_instance.get_transport_node_report_for_a_transport_zone(zone_id, source=source, status=status)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_transport_node_report_for_a_transport_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| ID of transport zone | 
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Transport node | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_state_with_deployment_info**
> TransportNodeState get_transport_node_state_with_deployment_info(transport_node_id)

Get a Transport Node's State

Returns information about the current state of the transport node configuration and information about the associated hostswitch. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Get a Transport Node's State
    api_response = api_instance.get_transport_node_state_with_deployment_info(transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_transport_node_state_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

[**TransportNodeState**](TransportNodeState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_status**
> TransportNodeStatus get_transport_node_status(node_id, source=source)

Read status of a transport node

Read status of a transport node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
source = 'source_example' # str | Data source type. (optional)

try:
    # Read status of a transport node
    api_response = api_instance.get_transport_node_status(node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_transport_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**TransportNodeStatus**](TransportNodeStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_with_deployment_info**
> TransportNode get_transport_node_with_deployment_info(transport_node_id)

Get a Transport Node

Returns information about a specified transport node.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Get a Transport Node
    api_response = api_instance.get_transport_node_with_deployment_info(transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_transport_node_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

[**TransportNode**](TransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tunnel**
> TunnelProperties get_tunnel(node_id, tunnel_name, source=source)

Tunnel properties

Tunnel properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
tunnel_name = 'tunnel_name_example' # str | Tunnel name
source = 'source_example' # str | Data source type. (optional)

try:
    # Tunnel properties
    api_response = api_instance.get_tunnel(node_id, tunnel_name, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->get_tunnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **tunnel_name** | **str**| Tunnel name | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**TunnelProperties**](TunnelProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compute_collection_transport_node_templates**
> TransportNodeTemplateListResult list_compute_collection_transport_node_templates(compute_collection_id=compute_collection_id)

List compute collection transportnode templates

Returns all eligible compute collection transportnode templates Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
compute_collection_id = 'compute_collection_id_example' # str | Compute collection id (optional)

try:
    # List compute collection transportnode templates
    api_response = api_instance.list_compute_collection_transport_node_templates(compute_collection_id=compute_collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_compute_collection_transport_node_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_collection_id** | **str**| Compute collection id | [optional] 

### Return type

[**TransportNodeTemplateListResult**](TransportNodeTemplateListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_neighbor_properties**
> InterfaceNeighborPropertyListResult list_neighbor_properties(node_id)

List LLDP Neighbor Properties of Transport Node

List LLDP Neighbor Properties for all interfaces of Transport Node 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node

try:
    # List LLDP Neighbor Properties of Transport Node
    api_response = api_instance.list_neighbor_properties(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_neighbor_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 

### Return type

[**InterfaceNeighborPropertyListResult**](InterfaceNeighborPropertyListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_migration_specs**
> NetworkMigrationSpecListResult list_network_migration_specs(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

List all network migration specification templates.

Network migration specification once created and can be used as a template to indicate associated component which networks should be migrated and where. Currently migration template can be associated with compute collections which are managed by vCenter host profiles, to trigger automatic migration of networks for Stateless ESX hosts. Currently we only support creation of HostProfileNetworkMigrationSpec type of specification. Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
include_system_owned = true # bool | Whether the list result contains system resources (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | Supported network migration specification types. (optional)

try:
    # List all network migration specification templates.
    api_response = api_instance.list_network_migration_specs(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_network_migration_specs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **include_system_owned** | **bool**| Whether the list result contains system resources | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **type** | **str**| Supported network migration specification types. | [optional] 

### Return type

[**NetworkMigrationSpecListResult**](NetworkMigrationSpecListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_remote_transport_node_status**
> TransportNodeStatusListResult list_remote_transport_node_status(node_id, bfd_diagnostic_code=bfd_diagnostic_code, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, tunnel_status=tunnel_status)

Read status of all transport nodes with tunnel connections to transport node 

Read status of all transport nodes with tunnel connections to transport node 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
bfd_diagnostic_code = 'bfd_diagnostic_code_example' # str | BFD diagnostic code of Tunnel (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
tunnel_status = 'tunnel_status_example' # str | Tunnel Status (optional)

try:
    # Read status of all transport nodes with tunnel connections to transport node 
    api_response = api_instance.list_remote_transport_node_status(node_id, bfd_diagnostic_code=bfd_diagnostic_code, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, tunnel_status=tunnel_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_remote_transport_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **bfd_diagnostic_code** | **str**| BFD diagnostic code of Tunnel | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **tunnel_status** | **str**| Tunnel Status | [optional] 

### Return type

[**TransportNodeStatusListResult**](TransportNodeStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_capabilities**
> NodeCapabilitiesResult list_transport_node_capabilities(transport_node_id)

Return the list of capabilities of transport node

Returns information about capabilities of transport host node. Edge nodes do not have capabilities.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Return the list of capabilities of transport node
    api_response = api_instance.list_transport_node_capabilities(transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_transport_node_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

[**NodeCapabilitiesResult**](NodeCapabilitiesResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_interfaces**
> NodeInterfacePropertiesListResult list_transport_node_interfaces(transport_node_id, source=source)

List the specified transport node's network interfaces

Returns the number of interfaces on the node and detailed information about each interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network mask, and the IP configuration method (static or DHCP). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # List the specified transport node's network interfaces
    api_response = api_instance.list_transport_node_interfaces(transport_node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_transport_node_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfacePropertiesListResult**](NodeInterfacePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_status**
> TransportNodeStatusListResult list_transport_node_status(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)

Read status of all the transport nodes

Read status of all the transport nodes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Transport node (optional)

try:
    # Read status of all the transport nodes
    api_response = api_instance.list_transport_node_status(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_transport_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Transport node | [optional] 

### Return type

[**TransportNodeStatusListResult**](TransportNodeStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_status_for_transport_zone**
> TransportNodeStatusListResult list_transport_node_status_for_transport_zone(zone_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)

Read status of transport nodes in a transport zone

Read status of transport nodes in a transport zone

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | ID of transport zone
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Transport node (optional)

try:
    # Read status of transport nodes in a transport zone
    api_response = api_instance.list_transport_node_status_for_transport_zone(zone_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_transport_node_status_for_transport_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| ID of transport zone | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Transport node | [optional] 

### Return type

[**TransportNodeStatusListResult**](TransportNodeStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_nodes_by_state_with_deployment_info**
> TransportNodeStateListResult list_transport_nodes_by_state_with_deployment_info(mm_state=mm_state, status=status, vtep_ip=vtep_ip)

List transport nodes by realized state

Returns a list of transport node states that have realized state as provided as query parameter 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
mm_state = 'mm_state_example' # str | maintenance mode state (optional)
status = 'status_example' # str | Realized state of transport nodes (optional)
vtep_ip = 'vtep_ip_example' # str | Virtual tunnel endpoint ip address of transport node (optional)

try:
    # List transport nodes by realized state
    api_response = api_instance.list_transport_nodes_by_state_with_deployment_info(mm_state=mm_state, status=status, vtep_ip=vtep_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_transport_nodes_by_state_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mm_state** | **str**| maintenance mode state | [optional] 
 **status** | **str**| Realized state of transport nodes | [optional] 
 **vtep_ip** | **str**| Virtual tunnel endpoint ip address of transport node | [optional] 

### Return type

[**TransportNodeStateListResult**](TransportNodeStateListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_nodes_with_deployment_info**
> TransportNodeListResult list_transport_nodes_with_deployment_info(cursor=cursor, in_maintenance_mode=in_maintenance_mode, included_fields=included_fields, node_id=node_id, node_ip=node_ip, node_types=node_types, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, transport_zone_id=transport_zone_id)

List Transport Nodes

Returns information about all transport nodes along with underlying host or edge details. A transport node is a host or edge that contains hostswitches. A hostswitch can have virtual machines connected to them.  Because each transport node has hostswitches, transport nodes can also have virtual tunnel endpoints, which means that they can be part of the overlay. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
in_maintenance_mode = true # bool | maintenance mode flag (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
node_id = 'node_id_example' # str | node identifier (optional)
node_ip = 'node_ip_example' # str | Fabric node IP address (optional)
node_types = 'node_types_example' # str | a list of fabric node types separated by comma or a single type (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
transport_zone_id = 'transport_zone_id_example' # str | Transport zone identifier (optional)

try:
    # List Transport Nodes
    api_response = api_instance.list_transport_nodes_with_deployment_info(cursor=cursor, in_maintenance_mode=in_maintenance_mode, included_fields=included_fields, node_id=node_id, node_ip=node_ip, node_types=node_types, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, transport_zone_id=transport_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->list_transport_nodes_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **in_maintenance_mode** | **bool**| maintenance mode flag | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **node_id** | **str**| node identifier | [optional] 
 **node_ip** | **str**| Fabric node IP address | [optional] 
 **node_types** | **str**| a list of fabric node types separated by comma or a single type | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **transport_zone_id** | **str**| Transport zone identifier | [optional] 

### Return type

[**TransportNodeListResult**](TransportNodeListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_tunnels**
> TunnelList query_tunnels(node_id, bfd_diagnostic_code=bfd_diagnostic_code, cursor=cursor, included_fields=included_fields, page_size=page_size, remote_node_id=remote_node_id, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)

List of tunnels

List of tunnels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
bfd_diagnostic_code = 'bfd_diagnostic_code_example' # str | BFD diagnostic code of Tunnel as defined in RFC 5880 (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
remote_node_id = 'remote_node_id_example' # str |  (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Tunnel status (optional)

try:
    # List of tunnels
    api_response = api_instance.query_tunnels(node_id, bfd_diagnostic_code=bfd_diagnostic_code, cursor=cursor, included_fields=included_fields, page_size=page_size, remote_node_id=remote_node_id, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->query_tunnels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **bfd_diagnostic_code** | **str**| BFD diagnostic code of Tunnel as defined in RFC 5880 | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **remote_node_id** | **str**|  | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Tunnel status | [optional] 

### Return type

[**TunnelList**](TunnelList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_neighbor_properties**
> InterfaceNeighborProperties read_neighbor_properties(node_id, interface_name)

Read LLDP Neighbor Properties of Transport Node by Interface Name 

Read LLDP Neighbor Properties for a specific interface of Transport Node 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
interface_name = 'interface_name_example' # str | Interface name to read

try:
    # Read LLDP Neighbor Properties of Transport Node by Interface Name 
    api_response = api_instance.read_neighbor_properties(node_id, interface_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->read_neighbor_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **interface_name** | **str**| Interface name to read | 

### Return type

[**InterfaceNeighborProperties**](InterfaceNeighborProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_transport_node_interface**
> NodeInterfaceProperties read_transport_node_interface(transport_node_id, interface_id, source=source)

Read the transport node's network interface

Returns detailed information about the specified interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network  mask, and the IP configuration method (static or DHCP). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the transport node's network interface
    api_response = api_instance.read_transport_node_interface(transport_node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->read_transport_node_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 
 **interface_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfaceProperties**](NodeInterfaceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_transport_node_interface_statistics**
> NodeInterfaceStatisticsProperties read_transport_node_interface_statistics(transport_node_id, interface_id, source=source)

Read the NSX Manager's Network Interface Statistics

On the specified interface, returns the number of received (rx), transmitted (tx), and dropped packets; the number of bytes and errors received and transmitted on the interface; and the number of detected collisions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the NSX Manager's Network Interface Statistics
    api_response = api_instance.read_transport_node_interface_statistics(transport_node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->read_transport_node_interface_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 
 **interface_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfaceStatisticsProperties**](NodeInterfaceStatisticsProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_transport_node**
> refresh_transport_node(transport_node_id)

Refresh the node configuration for the Edge node.

The API is applicable for Edge transport nodes. If you update the VM configuration and find a discrepancy in VM configuration at NSX Manager, then use this API to refresh configuration at NSX Manager. It refreshes the VM configuration from sources external to MP. Sources include vSphere Server and the edge node. After this action, the API GET api/v1/transport-nodes will show refreshed data. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Refresh the node configuration for the Edge node.
    api_instance.refresh_transport_node(transport_node_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->refresh_transport_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_transport_node_inventory_sync_restart_inventory_sync**
> restart_transport_node_inventory_sync_restart_inventory_sync(transport_node_id)

Restart the inventory sync for the node if it is paused currently.

Restart the inventory sync for the node if it is currently internally paused. After this action the next inventory sync coming from the node is processed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Restart the inventory sync for the node if it is paused currently.
    api_instance.restart_transport_node_inventory_sync_restart_inventory_sync(transport_node_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->restart_transport_node_inventory_sync_restart_inventory_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_parent_cluster_configuration_restore_cluster_config**
> restore_parent_cluster_configuration_restore_cluster_config(transport_node_id)

Apply cluster level Transport Node Profile on overridden host

A host can be overridden to have different configuration than Transport Node Profile(TNP) on cluster. This action will restore such overridden host back to cluster level TNP.  This API can be used in other case. When TNP is applied to a cluster, if any validation fails (e.g. VMs running on host) then existing transport node (TN) is not updated. In that case after the issue is resolved manually (e.g. VMs powered off), you can call this API to update TN as per cluster level TNP. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Apply cluster level Transport Node Profile on overridden host
    api_instance.restore_parent_cluster_configuration_restore_cluster_config(transport_node_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->restore_parent_cluster_configuration_restore_cluster_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resync_transport_node_resync_host_config**
> resync_transport_node_resync_host_config(transportnode_id)

Resync a Transport Node

Resync the TransportNode configuration on a host. It is similar to updating the TransportNode with existing configuration, but force synce these configurations to the host (no backend optimizations). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transportnode_id = 'transportnode_id_example' # str | 

try:
    # Resync a Transport Node
    api_instance.resync_transport_node_resync_host_config(transportnode_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->resync_transport_node_resync_host_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transportnode_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_compute_collection_transport_node_template_and_tn_collection**
> ComputeCollectionTransportNodeTemplate update_compute_collection_transport_node_template_and_tn_collection(body, template_id)

Update compute collection transportnode template

Update configuration of compute collection transportnode template. Compute_collection_id isn't allowed to be changed since it represents the association between ComputeCollection and this template. This is determined when ComputeCollectionTransportNodeTemplate got created. Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComputeCollectionTransportNodeTemplate() # ComputeCollectionTransportNodeTemplate | 
template_id = 'template_id_example' # str | 

try:
    # Update compute collection transportnode template
    api_response = api_instance.update_compute_collection_transport_node_template_and_tn_collection(body, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->update_compute_collection_transport_node_template_and_tn_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComputeCollectionTransportNodeTemplate**](ComputeCollectionTransportNodeTemplate.md)|  | 
 **template_id** | **str**|  | 

### Return type

[**ComputeCollectionTransportNodeTemplate**](ComputeCollectionTransportNodeTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_migration_spec**
> NetworkMigrationSpec update_network_migration_spec(body, template_id)

Update a template of network migration specification.

Network migration specification once created and can be used as a template to indicate associated component which networks should be migrated and where. Currently migration template can be associated with compute collections which are managed by vCenter host profiles, to trigger automatic migration of networks for Stateless ESX hosts. Currently we only support creation of HostProfileNetworkMigrationSpec type of specification. For a HostProfileNetworkMigrationSpec which is already associated with a compute collection, updating it would mean next time the system needs to trigger migration for hosts managed by compute collection, it will use the updated migration specification. Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NetworkMigrationSpec() # NetworkMigrationSpec | 
template_id = 'template_id_example' # str | 

try:
    # Update a template of network migration specification.
    api_response = api_instance.update_network_migration_spec(body, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->update_network_migration_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkMigrationSpec**](NetworkMigrationSpec.md)|  | 
 **template_id** | **str**|  | 

### Return type

[**NetworkMigrationSpec**](NetworkMigrationSpec.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transport_node_maintenance_mode**
> update_transport_node_maintenance_mode(transportnode_id, action=action)

Update transport node maintenance mode

Put transport node into maintenance mode or exit from maintenance mode.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transportnode_id = 'transportnode_id_example' # str | 
action = 'action_example' # str |  (optional)

try:
    # Update transport node maintenance mode
    api_instance.update_transport_node_maintenance_mode(transportnode_id, action=action)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->update_transport_node_maintenance_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transportnode_id** | **str**|  | 
 **action** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transport_node_with_deployment_info**
> TransportNode update_transport_node_with_deployment_info(body, transport_node_id, esx_mgmt_if_migration_dest=esx_mgmt_if_migration_dest, if_id=if_id, ping_ip=ping_ip, vnic=vnic, vnic_migration_dest=vnic_migration_dest)

Update a Transport Node

Modifies the transport node information. The host_switch_name field must match the host_switch_name value specified in the transport zone (API: transport-zones). You must create the associated uplink profile (API: host-switch-profiles) before you can specify an uplink_name here. If the host is an ESX and has only one physical NIC being used by a vSphere standard switch, TransportNodeUpdateParameters should be used to migrate the management interface and the physical NIC into a logical switch that is in a transport zone this transport node will join or has already joined. If the migration is already done, TransportNodeUpdateParameters can also be used to migrate the management interface and the physical NIC back to a vSphere standard switch. In other cases, the TransportNodeUpdateParameters should NOT be used. When updating transport node you should follow pattern where you should fetch the existing transport node and then only modify the required properties keeping other properties as is. For API backward compatibility, property host_switches will be still returned in response and will contain the configuration matching the one in host_switch_spec. In update call you should only modify configuration in either host_switch_spec or host_switches, but not both. Property host_switch_spec should be preferred over deprecated host_switches property when creating or updating transport nodes.  It also modifies attributes of node (host or edge). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNode() # TransportNode | 
transport_node_id = 'transport_node_id_example' # str | 
esx_mgmt_if_migration_dest = 'esx_mgmt_if_migration_dest_example' # str | The network ids to which the ESX vmk interfaces will be migrated (optional)
if_id = 'if_id_example' # str | The ESX vmk interfaces to migrate (optional)
ping_ip = 'ping_ip_example' # str | IP Addresses to ping right after ESX vmk interfaces were migrated. (optional)
vnic = 'vnic_example' # str | The ESX vmk interfaces and/or VM NIC to migrate (optional)
vnic_migration_dest = 'vnic_migration_dest_example' # str | The migration destinations of ESX vmk interfaces and/or VM NIC (optional)

try:
    # Update a Transport Node
    api_response = api_instance.update_transport_node_with_deployment_info(body, transport_node_id, esx_mgmt_if_migration_dest=esx_mgmt_if_migration_dest, if_id=if_id, ping_ip=ping_ip, vnic=vnic, vnic_migration_dest=vnic_migration_dest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodesApi->update_transport_node_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNode**](TransportNode.md)|  | 
 **transport_node_id** | **str**|  | 
 **esx_mgmt_if_migration_dest** | **str**| The network ids to which the ESX vmk interfaces will be migrated | [optional] 
 **if_id** | **str**| The ESX vmk interfaces to migrate | [optional] 
 **ping_ip** | **str**| IP Addresses to ping right after ESX vmk interfaces were migrated. | [optional] 
 **vnic** | **str**| The ESX vmk interfaces and/or VM NIC to migrate | [optional] 
 **vnic_migration_dest** | **str**| The migration destinations of ESX vmk interfaces and/or VM NIC | [optional] 

### Return type

[**TransportNode**](TransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

