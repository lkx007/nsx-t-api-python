# swagger_client.ManagementPlaneApiConfigsInventoryApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inventory_config**](ManagementPlaneApiConfigsInventoryApi.md#get_inventory_config) | **GET** /configs/inventory | Return inventory configuration

# **get_inventory_config**
> InventoryConfig get_inventory_config()

Return inventory configuration

Supports retrieving following configuration of inventory module 1. Soft limit on number of compute managers that can be registered. 

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
api_instance = swagger_client.ManagementPlaneApiConfigsInventoryApi(swagger_client.ApiClient(configuration))

try:
    # Return inventory configuration
    api_response = api_instance.get_inventory_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiConfigsInventoryApi->get_inventory_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InventoryConfig**](InventoryConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

