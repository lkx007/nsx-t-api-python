# swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_node**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#add_cluster_node) | **POST** /cluster/nodes | Add a controller to the cluster
[**clear_cluster_certificate_clear_cluster_certificate**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#clear_cluster_certificate_clear_cluster_certificate) | **POST** /cluster/api-certificate?action&#x3D;clear_cluster_certificate | Clear the cluster certificate
[**clear_cluster_virtual_ip_clear_virtual_ip**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#clear_cluster_virtual_ip_clear_virtual_ip) | **POST** /cluster/api-virtual-ip?action&#x3D;clear_virtual_ip | Clear cluster virtual IP address
[**delete_cluster_node_config**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#delete_cluster_node_config) | **DELETE** /cluster/nodes/{node-id} | Remove a controller from the cluster
[**detach_cluster_node_remove_node**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#detach_cluster_node_remove_node) | **POST** /cluster/{node-id}?action&#x3D;remove_node | Detach a node from the Cluster
[**get_api_service_config**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#get_api_service_config) | **GET** /cluster/api-service | Read API service properties
[**get_cluster_certificate_id**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#get_cluster_certificate_id) | **GET** /cluster/api-certificate | Read cluster certificate ID
[**get_cluster_node_config**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#get_cluster_node_config) | **GET** /cluster/{node-id} | Read cluster node configuration
[**get_cluster_virtual_ip**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#get_cluster_virtual_ip) | **GET** /cluster/api-virtual-ip | Read cluster virtual IP address
[**join_cluster_join_cluster**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#join_cluster_join_cluster) | **POST** /cluster?action&#x3D;join_cluster | Join this node to a NSX Cluster
[**list_cluster_node_configs**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#list_cluster_node_configs) | **GET** /cluster/nodes | List Cluster Node Configurations
[**list_cluster_node_interfaces**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#list_cluster_node_interfaces) | **GET** /cluster/nodes/{node-id}/network/interfaces | List the specified node&#x27;s Network Interfaces
[**read_cluster_config**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#read_cluster_config) | **GET** /cluster | Read Cluster Configuration
[**read_cluster_node_config**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#read_cluster_node_config) | **GET** /cluster/nodes/{node-id} | Read Cluster Node Configuration
[**read_cluster_node_interface**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#read_cluster_node_interface) | **GET** /cluster/nodes/{node-id}/network/interfaces/{interface-id} | Read the node&#x27;s Network Interface
[**read_cluster_node_interface_statistics**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#read_cluster_node_interface_statistics) | **GET** /cluster/nodes/{node-id}/network/interfaces/{interface-id}/stats | Read the NSX Manager/Controller&#x27;s Network Interface Statistics
[**read_cluster_node_status**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#read_cluster_node_status) | **GET** /cluster/nodes/{node-id}/status | Read cluster node runtime status
[**read_cluster_nodes_aggregate_status**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#read_cluster_nodes_aggregate_status) | **GET** /cluster/nodes/status | Read cluster runtime status
[**read_cluster_status**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#read_cluster_status) | **GET** /cluster/status | Read Cluster Status
[**set_cluster_certificate_set_cluster_certificate**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#set_cluster_certificate_set_cluster_certificate) | **POST** /cluster/api-certificate?action&#x3D;set_cluster_certificate | Set the cluster certificate
[**set_cluster_virtual_ip_set_virtual_ip**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#set_cluster_virtual_ip_set_virtual_ip) | **POST** /cluster/api-virtual-ip?action&#x3D;set_virtual_ip | Set cluster virtual IP address
[**update_api_service_config**](ManagementPlaneApiNsxComponentAdministrationClusterManagementApi.md#update_api_service_config) | **PUT** /cluster/api-service | Update API service properties

# **add_cluster_node**
> ClusterNodeConfig add_cluster_node(body, action)

Add a controller to the cluster

Add a new controller to the NSX cluster. Deprecated. Use POST /cluster?action=join_cluster to join a node to cluster. The controller comes with the new node. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddClusterNodeSpec() # AddClusterNodeSpec | 
action = 'action_example' # str | 

try:
    # Add a controller to the cluster
    api_response = api_instance.add_cluster_node(body, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->add_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddClusterNodeSpec**](AddClusterNodeSpec.md)|  | 
 **action** | **str**|  | 

### Return type

[**ClusterNodeConfig**](ClusterNodeConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_cluster_certificate_clear_cluster_certificate**
> ClusterCertificateId clear_cluster_certificate_clear_cluster_certificate(certificate_id)

Clear the cluster certificate

Clears the certificate used for the MP cluster. This does not affect the certificate itself. This API is deprecated. Instead use the  /api/v1/cluster/api-certificate?action=set_cluster_certificate API to set the cluster certificate to a different one. It just means that from now on, individual certificates will be used on each MP node. This affects all nodes in the cluster. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
certificate_id = 'certificate_id_example' # str | Certificate ID

try:
    # Clear the cluster certificate
    api_response = api_instance.clear_cluster_certificate_clear_cluster_certificate(certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->clear_cluster_certificate_clear_cluster_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| Certificate ID | 

### Return type

[**ClusterCertificateId**](ClusterCertificateId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_cluster_virtual_ip_clear_virtual_ip**
> ClusterVirtualIpProperties clear_cluster_virtual_ip_clear_virtual_ip()

Clear cluster virtual IP address

Clears the cluster virtual IP address. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))

try:
    # Clear cluster virtual IP address
    api_response = api_instance.clear_cluster_virtual_ip_clear_virtual_ip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->clear_cluster_virtual_ip_clear_virtual_ip: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterVirtualIpProperties**](ClusterVirtualIpProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_node_config**
> delete_cluster_node_config(node_id)

Remove a controller from the cluster

Removes the specified controller from the NSX cluster. Before you can remove a controller from the cluster, you must shut down the controller service with the \"stop service controller\" command. Deprecated. Use POST /cluster/<node-id>?action=remove_node to detach a node from cluster. The controller is removed with the node. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Remove a controller from the cluster
    api_instance.delete_cluster_node_config(node_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->delete_cluster_node_config: %s\n" % e)
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

# **detach_cluster_node_remove_node**
> ClusterConfiguration detach_cluster_node_remove_node(node_id, force=force, graceful_shutdown=graceful_shutdown, ignore_repository_ip_check=ignore_repository_ip_check)

Detach a node from the Cluster

Detach a node from the Cluster

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | UUID of the node
force = 'force_example' # str |  (optional)
graceful_shutdown = 'graceful_shutdown_example' # str |  (optional)
ignore_repository_ip_check = 'ignore_repository_ip_check_example' # str |  (optional)

try:
    # Detach a node from the Cluster
    api_response = api_instance.detach_cluster_node_remove_node(node_id, force=force, graceful_shutdown=graceful_shutdown, ignore_repository_ip_check=ignore_repository_ip_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->detach_cluster_node_remove_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| UUID of the node | 
 **force** | **str**|  | [optional] 
 **graceful_shutdown** | **str**|  | [optional] 
 **ignore_repository_ip_check** | **str**|  | [optional] 

### Return type

[**ClusterConfiguration**](ClusterConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_service_config**
> ApiServiceConfig get_api_service_config()

Read API service properties

Read the configuration of the NSX API service. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read API service properties
    api_response = api_instance.get_api_service_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->get_api_service_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiServiceConfig**](ApiServiceConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_certificate_id**
> ClusterCertificateId get_cluster_certificate_id()

Read cluster certificate ID

Returns the ID of the certificate that is used as the cluster certificate for MP 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster certificate ID
    api_response = api_instance.get_cluster_certificate_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->get_cluster_certificate_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterCertificateId**](ClusterCertificateId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node_config**
> ClusterNodeInfo get_cluster_node_config(node_id)

Read cluster node configuration

Returns information about the specified NSX cluster node.

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Read cluster node configuration
    api_response = api_instance.get_cluster_node_config(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->get_cluster_node_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**ClusterNodeInfo**](ClusterNodeInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_virtual_ip**
> ClusterVirtualIpProperties get_cluster_virtual_ip()

Read cluster virtual IP address

Returns the configured cluster virtual IP address or null if not configured. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster virtual IP address
    api_response = api_instance.get_cluster_virtual_ip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->get_cluster_virtual_ip: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterVirtualIpProperties**](ClusterVirtualIpProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_cluster_join_cluster**
> ClusterConfiguration join_cluster_join_cluster(body)

Join this node to a NSX Cluster

Join this node to a NSX Cluster

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.JoinClusterParameters() # JoinClusterParameters | 

try:
    # Join this node to a NSX Cluster
    api_response = api_instance.join_cluster_join_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->join_cluster_join_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JoinClusterParameters**](JoinClusterParameters.md)|  | 

### Return type

[**ClusterConfiguration**](ClusterConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_node_configs**
> ClusterNodeConfigListResult list_cluster_node_configs(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List Cluster Node Configurations

Returns information about all NSX cluster nodes. Deprecated. Use GET /cluster to get cluster configuration. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List Cluster Node Configurations
    api_response = api_instance.list_cluster_node_configs(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->list_cluster_node_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ClusterNodeConfigListResult**](ClusterNodeConfigListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_node_interfaces**
> NodeInterfacePropertiesListResult list_cluster_node_interfaces(node_id, source=source)

List the specified node's Network Interfaces

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # List the specified node's Network Interfaces
    api_response = api_instance.list_cluster_node_interfaces(node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->list_cluster_node_interfaces: %s\n" % e)
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

# **read_cluster_config**
> ClusterConfig read_cluster_config()

Read Cluster Configuration

Returns information about the NSX cluster configuration. An NSX cluster has two functions or purposes, commonly referred to as \"roles.\" These two roles are control and management. Each NSX installation has a single cluster. Separate NSX clusters do not share data. In other words, a given data-plane node is attached to only one cluster, not to multiple clusters. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read Cluster Configuration
    api_response = api_instance.read_cluster_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->read_cluster_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterConfig**](ClusterConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_node_config**
> ClusterNodeConfig read_cluster_node_config(node_id)

Read Cluster Node Configuration

Returns information about the specified NSX cluster node. Deprecated. Use GET /cluster/<node-id> to get cluster node configuration. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Read Cluster Node Configuration
    api_response = api_instance.read_cluster_node_config(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->read_cluster_node_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**ClusterNodeConfig**](ClusterNodeConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_node_interface**
> NodeInterfaceProperties read_cluster_node_interface(node_id, interface_id, source=source)

Read the node's Network Interface

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the node's Network Interface
    api_response = api_instance.read_cluster_node_interface(node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->read_cluster_node_interface: %s\n" % e)
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

# **read_cluster_node_interface_statistics**
> NodeInterfaceStatisticsProperties read_cluster_node_interface_statistics(node_id, interface_id, source=source)

Read the NSX Manager/Controller's Network Interface Statistics

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the NSX Manager/Controller's Network Interface Statistics
    api_response = api_instance.read_cluster_node_interface_statistics(node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->read_cluster_node_interface_statistics: %s\n" % e)
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

# **read_cluster_node_status**
> ClusterNodeStatus read_cluster_node_status(node_id, source=source)

Read cluster node runtime status

Read aggregated runtime status of cluster node. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read cluster node runtime status
    api_response = api_instance.read_cluster_node_status(node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->read_cluster_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**ClusterNodeStatus**](ClusterNodeStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_nodes_aggregate_status**
> ClustersAggregateInfo read_cluster_nodes_aggregate_status()

Read cluster runtime status

Read aggregated runtime status of all cluster nodes. Deprecated. Use GET /cluster/status instead. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster runtime status
    api_response = api_instance.read_cluster_nodes_aggregate_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->read_cluster_nodes_aggregate_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClustersAggregateInfo**](ClustersAggregateInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_status**
> ClusterStatus read_cluster_status()

Read Cluster Status

Returns status information for the NSX cluster control role and management role. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read Cluster Status
    api_response = api_instance.read_cluster_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->read_cluster_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStatus**](ClusterStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cluster_certificate_set_cluster_certificate**
> ClusterCertificateId set_cluster_certificate_set_cluster_certificate(certificate_id)

Set the cluster certificate

Sets the certificate used for the MP cluster. Issuing this request causes the http service to restart so that the service can begin using the new certificate. When the POST request succeeds, it doesn't return a valid response. The request times out because of the restart. This affects all nodes in the cluster. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
certificate_id = 'certificate_id_example' # str | Certificate ID

try:
    # Set the cluster certificate
    api_response = api_instance.set_cluster_certificate_set_cluster_certificate(certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->set_cluster_certificate_set_cluster_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| Certificate ID | 

### Return type

[**ClusterCertificateId**](ClusterCertificateId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cluster_virtual_ip_set_virtual_ip**
> ClusterVirtualIpProperties set_cluster_virtual_ip_set_virtual_ip(ip_address)

Set cluster virtual IP address

Sets the cluster virtual IP address. Note, all nodes in the management cluster must be in the same subnet. If not, a 409 CONFLICT status is returned. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
ip_address = 'ip_address_example' # str | Virtual IP address, 0.0.0.0 if not configured

try:
    # Set cluster virtual IP address
    api_response = api_instance.set_cluster_virtual_ip_set_virtual_ip(ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->set_cluster_virtual_ip_set_virtual_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| Virtual IP address, 0.0.0.0 if not configured | 

### Return type

[**ClusterVirtualIpProperties**](ClusterVirtualIpProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_service_config**
> ApiServiceConfig update_api_service_config(body)

Update API service properties

Read the configuration of the NSX API service. Changes are applied to all nodes in the cluster. The API service on each node will restart after it is updated using this API. There may be a delay of up to a minute or so between the time this API call completes and when the new configuration goes into effect.

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiServiceConfig() # ApiServiceConfig | 

try:
    # Update API service properties
    api_response = api_instance.update_api_service_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationClusterManagementApi->update_api_service_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiServiceConfig**](ApiServiceConfig.md)|  | 

### Return type

[**ApiServiceConfig**](ApiServiceConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

