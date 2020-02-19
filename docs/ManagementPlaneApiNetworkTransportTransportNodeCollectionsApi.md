# swagger_client.ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transport_node_collection**](ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi.md#create_transport_node_collection) | **POST** /transport-node-collections | Create transport node collection by attaching Transport Node Profile to cluster.
[**delete_transport_node_collection**](ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi.md#delete_transport_node_collection) | **DELETE** /transport-node-collections/{transport-node-collection-id} | Detach transport node profile from compute collection.
[**get_transport_node_collection**](ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi.md#get_transport_node_collection) | **GET** /transport-node-collections/{transport-node-collection-id} | Get Transport Node collection by id
[**get_transport_node_collection_state**](ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi.md#get_transport_node_collection_state) | **GET** /transport-node-collections/{transport-node-collection-id}/state | Get Transport Node collection application state
[**list_transport_node_collections**](ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi.md#list_transport_node_collections) | **GET** /transport-node-collections | List Transport Node collections
[**update_transport_node_collection**](ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi.md#update_transport_node_collection) | **PUT** /transport-node-collections/{transport-node-collection-id} | Update Transport Node collection

# **create_transport_node_collection**
> TransportNodeCollection create_transport_node_collection(body)

Create transport node collection by attaching Transport Node Profile to cluster.

When transport node collection is created the hosts which are part of compute collection will be prepared automatically i.e. NSX Manager attempts to install the NSX components on hosts. Transport nodes for these hosts are created using the configuration specified in transport node profile. 

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
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNodeCollection() # TransportNodeCollection | 

try:
    # Create transport node collection by attaching Transport Node Profile to cluster.
    api_response = api_instance.create_transport_node_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi->create_transport_node_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNodeCollection**](TransportNodeCollection.md)|  | 

### Return type

[**TransportNodeCollection**](TransportNodeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transport_node_collection**
> delete_transport_node_collection(transport_node_collection_id)

Detach transport node profile from compute collection.

By deleting transport node collection, we are detaching the transport node profile(TNP) from the compute collection. It has no effect on existing transport nodes. However, new hosts added to the compute collection will no longer be automatically converted to NSX transport node. Detaching TNP from compute collection does not delete TNP. 

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
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi(swagger_client.ApiClient(configuration))
transport_node_collection_id = 'transport_node_collection_id_example' # str | 

try:
    # Detach transport node profile from compute collection.
    api_instance.delete_transport_node_collection(transport_node_collection_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi->delete_transport_node_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_collection_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_collection**
> TransportNodeCollection get_transport_node_collection(transport_node_collection_id)

Get Transport Node collection by id

Returns transport node collection by id

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
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi(swagger_client.ApiClient(configuration))
transport_node_collection_id = 'transport_node_collection_id_example' # str | 

try:
    # Get Transport Node collection by id
    api_response = api_instance.get_transport_node_collection(transport_node_collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi->get_transport_node_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_collection_id** | **str**|  | 

### Return type

[**TransportNodeCollection**](TransportNodeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_collection_state**
> TransportNodeCollectionState get_transport_node_collection_state(transport_node_collection_id)

Get Transport Node collection application state

Returns the state of transport node collection based on the states of transport nodes of the hosts which are part of compute collection. 

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
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi(swagger_client.ApiClient(configuration))
transport_node_collection_id = 'transport_node_collection_id_example' # str | 

try:
    # Get Transport Node collection application state
    api_response = api_instance.get_transport_node_collection_state(transport_node_collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi->get_transport_node_collection_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_collection_id** | **str**|  | 

### Return type

[**TransportNodeCollectionState**](TransportNodeCollectionState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_collections**
> TransportNodeCollectionListResult list_transport_node_collections()

List Transport Node collections

Returns all Transport Node collections

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
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi(swagger_client.ApiClient(configuration))

try:
    # List Transport Node collections
    api_response = api_instance.list_transport_node_collections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi->list_transport_node_collections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransportNodeCollectionListResult**](TransportNodeCollectionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transport_node_collection**
> TransportNodeCollection update_transport_node_collection(body, transport_node_collection_id)

Update Transport Node collection

Attach different transport node profile to compute collection by updating transport node collection. 

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
api_instance = swagger_client.ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNodeCollection() # TransportNodeCollection | 
transport_node_collection_id = 'transport_node_collection_id_example' # str | 

try:
    # Update Transport Node collection
    api_response = api_instance.update_transport_node_collection(body, transport_node_collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNetworkTransportTransportNodeCollectionsApi->update_transport_node_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNodeCollection**](TransportNodeCollection.md)|  | 
 **transport_node_collection_id** | **str**|  | 

### Return type

[**TransportNodeCollection**](TransportNodeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

