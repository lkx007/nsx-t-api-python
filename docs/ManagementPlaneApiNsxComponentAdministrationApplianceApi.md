# swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_node_mode**](ManagementPlaneApiNsxComponentAdministrationApplianceApi.md#change_node_mode) | **POST** /configs/node/mode | NodeMode
[**get_node_mode**](ManagementPlaneApiNsxComponentAdministrationApplianceApi.md#get_node_mode) | **GET** /node/mode | NodeMode
[**set_node_time_set_system_time**](ManagementPlaneApiNsxComponentAdministrationApplianceApi.md#set_node_time_set_system_time) | **POST** /node?action&#x3D;set_system_time | Set the node system time

# **change_node_mode**
> NodeMode change_node_mode(body)

NodeMode

Currently only a switch from \"VMC_LOCAL\" to \"VMC\" is supported. Returns a new Node Mode, if the request successfuly changed it. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceApi(swagger_client.ApiClient(configuration))
body = swagger_client.SwitchingToVmcModeParameters() # SwitchingToVmcModeParameters | 

try:
    # NodeMode
    api_response = api_instance.change_node_mode(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceApi->change_node_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SwitchingToVmcModeParameters**](SwitchingToVmcModeParameters.md)|  | 

### Return type

[**NodeMode**](NodeMode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_mode**
> NodeMode get_node_mode()

NodeMode

Returns current Node Mode. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceApi(swagger_client.ApiClient(configuration))

try:
    # NodeMode
    api_response = api_instance.get_node_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceApi->get_node_mode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeMode**](NodeMode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_node_time_set_system_time**
> set_node_time_set_system_time(body)

Set the node system time

Set the node system time to the given time in UTC in the RFC3339 format 'yyyy-mm-ddThh:mm:ssZ'. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeTime() # NodeTime | 

try:
    # Set the node system time
    api_instance.set_node_time_set_system_time(body)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceApi->set_node_time_set_system_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeTime**](NodeTime.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

