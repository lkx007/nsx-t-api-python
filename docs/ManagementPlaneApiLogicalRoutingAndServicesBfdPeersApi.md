# swagger_client.ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_static_hop_bfd_peer**](ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi.md#create_static_hop_bfd_peer) | **POST** /logical-routers/{logical-router-id}/routing/static-routes/bfd-peers | Create a static hop BFD peer
[**delete_static_hop_bfd_peer**](ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi.md#delete_static_hop_bfd_peer) | **DELETE** /logical-routers/{logical-router-id}/routing/static-routes/bfd-peers/{bfd-peer-id} | Delete a specified static route BFD peer cofigured on a specified logical router
[**list_static_hop_bfd_peers**](ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi.md#list_static_hop_bfd_peers) | **GET** /logical-routers/{logical-router-id}/routing/static-routes/bfd-peers | List static routes BFD Peers
[**read_static_hop_bfd_peer**](ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi.md#read_static_hop_bfd_peer) | **GET** /logical-routers/{logical-router-id}/routing/static-routes/bfd-peers/{bfd-peer-id} | Read a static route BFD peer
[**update_static_hop_bfd_peer**](ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi.md#update_static_hop_bfd_peer) | **PUT** /logical-routers/{logical-router-id}/routing/static-routes/bfd-peers/{bfd-peer-id} | Update a static route BFD peer

# **create_static_hop_bfd_peer**
> StaticHopBfdPeer create_static_hop_bfd_peer(body, logical_router_id)

Create a static hop BFD peer

Creates a BFD peer for static route. The required parameters includes peer IP address. 

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
api_instance = swagger_client.ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi(swagger_client.ApiClient(configuration))
body = swagger_client.StaticHopBfdPeer() # StaticHopBfdPeer | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Create a static hop BFD peer
    api_response = api_instance.create_static_hop_bfd_peer(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi->create_static_hop_bfd_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StaticHopBfdPeer**](StaticHopBfdPeer.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**StaticHopBfdPeer**](StaticHopBfdPeer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_static_hop_bfd_peer**
> delete_static_hop_bfd_peer(logical_router_id, bfd_peer_id, force=force)

Delete a specified static route BFD peer cofigured on a specified logical router

Deletes the specified BFD peer present on specified logical router. 

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
api_instance = swagger_client.ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
bfd_peer_id = 'bfd_peer_id_example' # str | 
force = true # bool | Force delete the resource even if it is being used somewhere  (optional)

try:
    # Delete a specified static route BFD peer cofigured on a specified logical router
    api_instance.delete_static_hop_bfd_peer(logical_router_id, bfd_peer_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi->delete_static_hop_bfd_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **bfd_peer_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_static_hop_bfd_peers**
> StaticHopBfdPeerListResult list_static_hop_bfd_peers(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List static routes BFD Peers

Returns information about all BFD peers created on specified logical router for static routes. 

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
api_instance = swagger_client.ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List static routes BFD Peers
    api_response = api_instance.list_static_hop_bfd_peers(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi->list_static_hop_bfd_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**StaticHopBfdPeerListResult**](StaticHopBfdPeerListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_static_hop_bfd_peer**
> StaticHopBfdPeer read_static_hop_bfd_peer(logical_router_id, bfd_peer_id)

Read a static route BFD peer

Read the BFD peer having specified ID. 

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
api_instance = swagger_client.ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
bfd_peer_id = 'bfd_peer_id_example' # str | 

try:
    # Read a static route BFD peer
    api_response = api_instance.read_static_hop_bfd_peer(logical_router_id, bfd_peer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi->read_static_hop_bfd_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **bfd_peer_id** | **str**|  | 

### Return type

[**StaticHopBfdPeer**](StaticHopBfdPeer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_static_hop_bfd_peer**
> StaticHopBfdPeer update_static_hop_bfd_peer(body, logical_router_id, bfd_peer_id)

Update a static route BFD peer

Modifies the static route BFD peer. Modifiable parameters includes peer IP, enable flag and configuration of the BFD peer. 

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
api_instance = swagger_client.ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi(swagger_client.ApiClient(configuration))
body = swagger_client.StaticHopBfdPeer() # StaticHopBfdPeer | 
logical_router_id = 'logical_router_id_example' # str | 
bfd_peer_id = 'bfd_peer_id_example' # str | 

try:
    # Update a static route BFD peer
    api_response = api_instance.update_static_hop_bfd_peer(body, logical_router_id, bfd_peer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi->update_static_hop_bfd_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StaticHopBfdPeer**](StaticHopBfdPeer.md)|  | 
 **logical_router_id** | **str**|  | 
 **bfd_peer_id** | **str**|  | 

### Return type

[**StaticHopBfdPeer**](StaticHopBfdPeer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

