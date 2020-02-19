# swagger_client.ManagementPlaneApiFabricNodesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_node**](ManagementPlaneApiFabricNodesApi.md#add_node) | **POST** /fabric/nodes | Register and Install NSX Components on a Node
[**delete_node**](ManagementPlaneApiFabricNodesApi.md#delete_node) | **DELETE** /fabric/nodes/{node-id} | Delete a Node
[**get_fabric_node_modules**](ManagementPlaneApiFabricNodesApi.md#get_fabric_node_modules) | **GET** /fabric/nodes/{node-id}/modules | Get the module details of a Fabric Node This api is deprecated, use Transport Node API GET /transport-nodes/&amp;lt;transportnode-id&amp;gt;/modules to get fabric node modules. 
[**get_fabric_node_state**](ManagementPlaneApiFabricNodesApi.md#get_fabric_node_state) | **GET** /fabric/nodes/{node-id}/state | Get the Realized State of a Fabric Node.
[**get_supported_host_os_types**](ManagementPlaneApiFabricNodesApi.md#get_supported_host_os_types) | **GET** /fabric/ostypes | Return list of supported host OS types
[**list_fabric_node_interfaces**](ManagementPlaneApiFabricNodesApi.md#list_fabric_node_interfaces) | **GET** /fabric/nodes/{node-id}/network/interfaces | List the specified node&#x27;s Network Interfaces
[**list_node_capabilities**](ManagementPlaneApiFabricNodesApi.md#list_node_capabilities) | **GET** /fabric/nodes/{node-id}/capabilities | Return the List of Capabilities of a Single Node
[**list_nodes**](ManagementPlaneApiFabricNodesApi.md#list_nodes) | **GET** /fabric/nodes | Return the List of Nodes
[**perform_host_node_upgrade_action_upgrade_infra**](ManagementPlaneApiFabricNodesApi.md#perform_host_node_upgrade_action_upgrade_infra) | **POST** /fabric/nodes/{node-id}?action&#x3D;upgrade_infra | Perform a service deployment upgrade on a host node
[**perform_node_action**](ManagementPlaneApiFabricNodesApi.md#perform_node_action) | **POST** /fabric/nodes/{node-id} | Perform an Action on Fabric Node
[**read_fabric_node_interface**](ManagementPlaneApiFabricNodesApi.md#read_fabric_node_interface) | **GET** /fabric/nodes/{node-id}/network/interfaces/{interface-id} | Read the node&#x27;s Network Interface
[**read_fabric_node_interface_statistics**](ManagementPlaneApiFabricNodesApi.md#read_fabric_node_interface_statistics) | **GET** /fabric/nodes/{node-id}/network/interfaces/{interface-id}/stats | Read the NSX Manager&#x27;s Network Interface Statistics
[**read_node**](ManagementPlaneApiFabricNodesApi.md#read_node) | **GET** /fabric/nodes/{node-id} | Return Node Information
[**read_node_status**](ManagementPlaneApiFabricNodesApi.md#read_node_status) | **GET** /fabric/nodes/{node-id}/status | Return Runtime Status Information for a Node
[**read_nodes_status**](ManagementPlaneApiFabricNodesApi.md#read_nodes_status) | **GET** /fabric/nodes/status | Return Runtime Status Information for given Nodes
[**restart_inventory_sync_restart_inventory_sync**](ManagementPlaneApiFabricNodesApi.md#restart_inventory_sync_restart_inventory_sync) | **POST** /fabric/nodes/{node-id}?action&#x3D;restart_inventory_sync | Restart the inventory sync for the node if it is paused currently.
[**update_node**](ManagementPlaneApiFabricNodesApi.md#update_node) | **PUT** /fabric/nodes/{node-id} | Update a Node

# **add_node**
> Node add_node(body)

Register and Install NSX Components on a Node

Creates a host node (hypervisor) or edge node (router) in the transport network.  When you run this command for a host, NSX Manager attempts to install the NSX kernel modules, which are packaged as VIB, RPM, or DEB files. For the installation to succeed, you must provide the host login credentials and the host thumbprint.  To get the ESXi host thumbprint, SSH to the host and run the <b>openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha256 -noout</b> command.  To generate host key thumbprint using SHA-256 algorithm please follow the steps below.  Log into the host, making sure that the connection is not vulnerable to a man in the middle attack. Check whether a public key already exists. Host public key is generally located at '/etc/ssh/ssh_host_rsa_key.pub'. If the key is not present then generate a new key by running the following command and follow the instructions.  <b>ssh-keygen -t rsa</b>  Now generate a SHA256 hash of the key using the following command. Please make sure to pass the appropriate file name if the public key is stored with a different file name other than the default 'id_rsa.pub'.  <b>awk '{print $2}' id_rsa.pub | base64 -d | sha256sum -b | sed 's/ .*$//' | xxd -r -p | base64</b> This api is deprecated as part of FN+TN unification. Please use Transport Node API POST /transport-nodes to install NSX components on a node. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Node() # Node | 

try:
    # Register and Install NSX Components on a Node
    api_response = api_instance.add_node(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->add_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Node**](Node.md)|  | 

### Return type

[**Node**](Node.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> delete_node(node_id, unprepare_host=unprepare_host)

Delete a Node

Removes a specified fabric node (host or edge). A fabric node may only be deleted when it is no longer referenced by a Transport Node. If unprepare_host option is set to false, the host will be deleted without uninstalling the NSX components from the host. This api is deprecated, use Transport Node API DELETE /transport-nodes/&lt;transport-node-id&gt; to delete FN. DELETE /transport-nodes/<transport-node-id> to delete FN. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
unprepare_host = true # bool | Delete a host and uninstall NSX components (optional)

try:
    # Delete a Node
    api_instance.delete_node(node_id, unprepare_host=unprepare_host)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->delete_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **unprepare_host** | **bool**| Delete a host and uninstall NSX components | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabric_node_modules**
> SoftwareModuleResult get_fabric_node_modules(node_id)

Get the module details of a Fabric Node This api is deprecated, use Transport Node API GET /transport-nodes/&lt;transportnode-id&gt;/modules to get fabric node modules. 

Get the module details of a Fabric Node This api is deprecated, use Transport Node API GET /transport-nodes/&lt;transportnode-id&gt;/modules to get fabric node modules. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Get the module details of a Fabric Node This api is deprecated, use Transport Node API GET /transport-nodes/&lt;transportnode-id&gt;/modules to get fabric node modules. 
    api_response = api_instance.get_fabric_node_modules(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->get_fabric_node_modules: %s\n" % e)
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

# **get_fabric_node_state**
> ConfigurationState get_fabric_node_state(node_id)

Get the Realized State of a Fabric Node.

For edge nodes, returns the current install state when deployment is in progress, NODE_READY when deployment is complete and the failure state when deployment has failed. This api is deprecated. Please use /transport-nodes/&lt;transportnode-id&gt;/state to get realized state of a Fabric Node. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Get the Realized State of a Fabric Node.
    api_response = api_instance.get_fabric_node_state(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->get_fabric_node_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**ConfigurationState**](ConfigurationState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_host_os_types**
> SupportedHostOSListResult get_supported_host_os_types()

Return list of supported host OS types

Returns names of all supported host OS.

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))

try:
    # Return list of supported host OS types
    api_response = api_instance.get_supported_host_os_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->get_supported_host_os_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportedHostOSListResult**](SupportedHostOSListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fabric_node_interfaces**
> NodeInterfacePropertiesListResult list_fabric_node_interfaces(node_id, source=source)

List the specified node's Network Interfaces

Returns the number of interfaces on the node and detailed information about each interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network mask, and the IP configuration method (static or DHCP). This api is deprecated. Please use Transport Node API GET /transport-nodes/<transport-node-id>/network/interfaces to list node network interfaces for the corresponding TN. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # List the specified node's Network Interfaces
    api_response = api_instance.list_fabric_node_interfaces(node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->list_fabric_node_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfacePropertiesListResult**](NodeInterfacePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_capabilities**
> NodeCapabilitiesResult list_node_capabilities(node_id)

Return the List of Capabilities of a Single Node

Returns information about capabilities of a single fabric host node. Edge nodes do not have capabilities. This api is deprecated, use GET /transport-nodes/&lt;transportnode-id&gt;/capabilities if FN is converted to TN.

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Return the List of Capabilities of a Single Node
    api_response = api_instance.list_node_capabilities(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->list_node_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**NodeCapabilitiesResult**](NodeCapabilitiesResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nodes**
> NodeListResult list_nodes(cursor=cursor, discovered_node_id=discovered_node_id, display_name=display_name, external_id=external_id, hardware_id=hardware_id, hypervisor_os_type=hypervisor_os_type, included_fields=included_fields, ip_address=ip_address, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by)

Return the List of Nodes

Returns information about all fabric nodes (hosts and edges). This api is deprecated as part of FN+TN unification. Please use Transport Node API GET /transport-nodes to list all fabric nodes. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
discovered_node_id = 'discovered_node_id_example' # str | Id of the discovered node which was converted to create this node (optional)
display_name = 'display_name_example' # str | HostNode display name (optional)
external_id = 'external_id_example' # str | HostNode external id (optional)
hardware_id = 'hardware_id_example' # str | Hardware Id of the host (optional)
hypervisor_os_type = 'hypervisor_os_type_example' # str | HostNode's Hypervisor type, for example ESXi, RHEL KVM or UBUNTU KVM. (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
ip_address = 'ip_address_example' # str | Management IP address of the node (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
resource_type = 'resource_type_example' # str | Node type from 'HostNode', 'EdgeNode', 'PublicCloudGatewayNode' (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the List of Nodes
    api_response = api_instance.list_nodes(cursor=cursor, discovered_node_id=discovered_node_id, display_name=display_name, external_id=external_id, hardware_id=hardware_id, hypervisor_os_type=hypervisor_os_type, included_fields=included_fields, ip_address=ip_address, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->list_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **discovered_node_id** | **str**| Id of the discovered node which was converted to create this node | [optional] 
 **display_name** | **str**| HostNode display name | [optional] 
 **external_id** | **str**| HostNode external id | [optional] 
 **hardware_id** | **str**| Hardware Id of the host | [optional] 
 **hypervisor_os_type** | **str**| HostNode&#x27;s Hypervisor type, for example ESXi, RHEL KVM or UBUNTU KVM. | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **ip_address** | **str**| Management IP address of the node | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **resource_type** | **str**| Node type from &#x27;HostNode&#x27;, &#x27;EdgeNode&#x27;, &#x27;PublicCloudGatewayNode&#x27; | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NodeListResult**](NodeListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_host_node_upgrade_action_upgrade_infra**
> Node perform_host_node_upgrade_action_upgrade_infra(node_id, disable_vm_migration=disable_vm_migration)

Perform a service deployment upgrade on a host node

Perform a service deployment upgrade on a host node

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
disable_vm_migration = true # bool | Should VM migration be disabled during upgrade (optional)

try:
    # Perform a service deployment upgrade on a host node
    api_response = api_instance.perform_host_node_upgrade_action_upgrade_infra(node_id, disable_vm_migration=disable_vm_migration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->perform_host_node_upgrade_action_upgrade_infra: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **disable_vm_migration** | **bool**| Should VM migration be disabled during upgrade | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_node_action**
> Node perform_node_action(node_id, action=action, evacuate_powered_off_vms=evacuate_powered_off_vms, vsan_mode=vsan_mode)

Perform an Action on Fabric Node

The supported fabric node actions are enter_maintenance_mode, exit_maintenance_mode for EdgeNode. This API is deprecated, please call TransportNode maintenance mode API to update maintenance mode, refer to \"Update transport node maintenance mode\". 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
action = 'action_example' # str | Supported fabric node actions (optional)
evacuate_powered_off_vms = true # bool | Evacuate powered-off vms (optional)
vsan_mode = 'vsan_mode_example' # str | Vsan decommission mode (optional)

try:
    # Perform an Action on Fabric Node
    api_response = api_instance.perform_node_action(node_id, action=action, evacuate_powered_off_vms=evacuate_powered_off_vms, vsan_mode=vsan_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->perform_node_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **action** | **str**| Supported fabric node actions | [optional] 
 **evacuate_powered_off_vms** | **bool**| Evacuate powered-off vms | [optional] 
 **vsan_mode** | **str**| Vsan decommission mode | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_fabric_node_interface**
> NodeInterfaceProperties read_fabric_node_interface(node_id, interface_id, source=source)

Read the node's Network Interface

Returns detailed information about the specified interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network  mask, and the IP configuration method (static or DHCP). This api is deprecated as part of FN+TN unification. Please use Transport Node API GET /transport-nodes/<transport-node-id>/network/interfaces/<interface-id> to get interface details of a node. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the node's Network Interface
    api_response = api_instance.read_fabric_node_interface(node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->read_fabric_node_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
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

# **read_fabric_node_interface_statistics**
> NodeInterfaceStatisticsProperties read_fabric_node_interface_statistics(node_id, interface_id, source=source)

Read the NSX Manager's Network Interface Statistics

On the specified interface, returns the number of received (rx), transmitted (tx), and dropped packets; the number of bytes and errors received and transmitted on the interface; and the number of detected collisions. This api is deprecated as part of FN+TN unification. Please use /transport-nodes/<transportnode-id>/network/interfaces/<interface-id>/stats to read network interface statistics with contraint FN is converted to TN. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the NSX Manager's Network Interface Statistics
    api_response = api_instance.read_fabric_node_interface_statistics(node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->read_fabric_node_interface_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
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

# **read_node**
> Node read_node(node_id)

Return Node Information

Returns information about a specific fabric node (host or edge). This api is deprecated, use Transport Node API GET /transport-nodes/&lt;transport-node-id&gt; to get fabric node information. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Return Node Information
    api_response = api_instance.read_node(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->read_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**Node**](Node.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_status**
> NodeStatus read_node_status(node_id, source=source)

Return Runtime Status Information for a Node

Returns connectivity, heartbeat, and version information about a fabric node (host or edge). Note that the LCP connectivity status remains down until after the fabric node has been added as a transpot node and the NSX host switch has been successfully installed. See POST /api/v1/transport-nodes. This api is deprecated, use GET /api/v1/transport-nodes/&lt;node-id&gt;/status to get status information of a node with constraint FN is converted to TN. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Return Runtime Status Information for a Node
    api_response = api_instance.read_node_status(node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->read_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeStatus**](NodeStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_nodes_status**
> NodeStatusListResult read_nodes_status(node_ids)

Return Runtime Status Information for given Nodes

Returns connectivity, heartbeat, and version information about all fabric nodes (host or edge). This api is deprecated as part of FN+TN unification. Please use Transport Node Status API /transport-nodes/&lt;node-id&gt;/status to get status information of a node and to get all transport nodes ids use GET /transport-nodes. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_ids = 'node_ids_example' # str | List of requested Nodes.

try:
    # Return Runtime Status Information for given Nodes
    api_response = api_instance.read_nodes_status(node_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->read_nodes_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_ids** | **str**| List of requested Nodes. | 

### Return type

[**NodeStatusListResult**](NodeStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_inventory_sync_restart_inventory_sync**
> restart_inventory_sync_restart_inventory_sync(node_id)

Restart the inventory sync for the node if it is paused currently.

Restart the inventory sync for the node if it is currently internally paused. After this action the next inventory sync coming from the node is processed. This api is deprecated as part of FN+TN unification. Please use Transport Node API POST /transport-nodes/&lt;transport-node-id&gt;?action=restart_inventory_sync to restart inventory sync of node. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Restart the inventory sync for the node if it is paused currently.
    api_instance.restart_inventory_sync_restart_inventory_sync(node_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->restart_inventory_sync_restart_inventory_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node**
> Node update_node(body, node_id)

Update a Node

Modifies attributes of a fabric node (host or edge). This api is deprecated as part of FN+TN unification. Please use Transport Node API PUT /transport-nodes/&lt;transport-node-id&gt; to update fabric node details. API PUT /transport-nodes/<transport-node-id> to update fabric node details. 

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
api_instance = swagger_client.ManagementPlaneApiFabricNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Node() # Node | 
node_id = 'node_id_example' # str | 

try:
    # Update a Node
    api_response = api_instance.update_node(body, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricNodesApi->update_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Node**](Node.md)|  | 
 **node_id** | **str**|  | 

### Return type

[**Node**](Node.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

