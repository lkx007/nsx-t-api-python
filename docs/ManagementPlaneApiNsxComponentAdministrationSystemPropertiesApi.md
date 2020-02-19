# swagger_client.ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_management_plane_configuration**](ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi.md#delete_management_plane_configuration) | **DELETE** /node/management-plane | Delete the management_plane config
[**delete_mpa_configuration**](ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi.md#delete_mpa_configuration) | **DELETE** /node/mpa-config | Delete the MPA config file
[**read_management_plane_configuration**](ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi.md#read_management_plane_configuration) | **GET** /node/management-plane | Management plane this controller is communicating with
[**read_mpa_configuration**](ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi.md#read_mpa_configuration) | **GET** /node/mpa-config | MPA config for the management plane this node is communicating with
[**update_management_plane_configuration**](ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi.md#update_management_plane_configuration) | **PUT** /node/management-plane | Update management plane configuration
[**update_mpa_configuration**](ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi.md#update_mpa_configuration) | **PUT** /node/mpa-config | Update management plane agent configuration

# **delete_management_plane_configuration**
> delete_management_plane_configuration()

Delete the management_plane config

Delete the management_plane config

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi(swagger_client.ApiClient(configuration))

try:
    # Delete the management_plane config
    api_instance.delete_management_plane_configuration()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi->delete_management_plane_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mpa_configuration**
> delete_mpa_configuration()

Delete the MPA config file

Delete the MPA config file

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi(swagger_client.ApiClient(configuration))

try:
    # Delete the MPA config file
    api_instance.delete_mpa_configuration()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi->delete_mpa_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_management_plane_configuration**
> ManagementPlaneProperties read_management_plane_configuration()

Management plane this controller is communicating with

Management plane this controller is communicating with

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi(swagger_client.ApiClient(configuration))

try:
    # Management plane this controller is communicating with
    api_response = api_instance.read_management_plane_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi->read_management_plane_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManagementPlaneProperties**](ManagementPlaneProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_mpa_configuration**
> MPAConfigProperties read_mpa_configuration()

MPA config for the management plane this node is communicating with

MPA config for the management plane this node is communicating with

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi(swagger_client.ApiClient(configuration))

try:
    # MPA config for the management plane this node is communicating with
    api_response = api_instance.read_mpa_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi->read_mpa_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MPAConfigProperties**](MPAConfigProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_management_plane_configuration**
> ManagementPlaneProperties update_management_plane_configuration(body)

Update management plane configuration

Update management plane configuration

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ManagementPlaneProperties() # ManagementPlaneProperties | 

try:
    # Update management plane configuration
    api_response = api_instance.update_management_plane_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi->update_management_plane_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManagementPlaneProperties**](ManagementPlaneProperties.md)|  | 

### Return type

[**ManagementPlaneProperties**](ManagementPlaneProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mpa_configuration**
> MPAConfigProperties update_mpa_configuration(body)

Update management plane agent configuration

Update management plane agent configuration

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.MPAConfigProperties() # MPAConfigProperties | 

try:
    # Update management plane agent configuration
    api_response = api_instance.update_mpa_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi->update_mpa_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MPAConfigProperties**](MPAConfigProperties.md)|  | 

### Return type

[**MPAConfigProperties**](MPAConfigProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

