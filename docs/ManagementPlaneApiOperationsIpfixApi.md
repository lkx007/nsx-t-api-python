# swagger_client.ManagementPlaneApiOperationsIpfixApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ipfix_collector_config**](ManagementPlaneApiOperationsIpfixApi.md#create_ipfix_collector_config) | **POST** /ipfix/collectorconfigs | Create a new IPFIX collector configuration
[**create_ipfix_config**](ManagementPlaneApiOperationsIpfixApi.md#create_ipfix_config) | **POST** /ipfix/configs | Create a new IPFIX configuration
[**delete_ipfix_collector_config**](ManagementPlaneApiOperationsIpfixApi.md#delete_ipfix_collector_config) | **DELETE** /ipfix/collectorconfigs/{collector-config-id} | Delete an existing IPFIX collector configuration
[**delete_ipfix_config**](ManagementPlaneApiOperationsIpfixApi.md#delete_ipfix_config) | **DELETE** /ipfix/configs/{config-id} | Delete an existing IPFIX configuration
[**get_ipfix_collector_config**](ManagementPlaneApiOperationsIpfixApi.md#get_ipfix_collector_config) | **GET** /ipfix/collectorconfigs/{collector-config-id} | Get an existing IPFIX collector configuration
[**get_ipfix_config**](ManagementPlaneApiOperationsIpfixApi.md#get_ipfix_config) | **GET** /ipfix/configs/{config-id} | Get an existing IPFIX configuration
[**list_ipfix_collector_config**](ManagementPlaneApiOperationsIpfixApi.md#list_ipfix_collector_config) | **GET** /ipfix/collectorconfigs | List IPFIX collector configurations
[**list_ipfix_config**](ManagementPlaneApiOperationsIpfixApi.md#list_ipfix_config) | **GET** /ipfix/configs | List IPFIX configuration
[**update_ipfix_collector_config**](ManagementPlaneApiOperationsIpfixApi.md#update_ipfix_collector_config) | **PUT** /ipfix/collectorconfigs/{collector-config-id} | Update an existing IPFIX collector configuration
[**update_ipfix_config**](ManagementPlaneApiOperationsIpfixApi.md#update_ipfix_config) | **PUT** /ipfix/configs/{config-id} | Update an existing IPFIX configuration

# **create_ipfix_collector_config**
> IpfixCollectorConfig create_ipfix_collector_config(body)

Create a new IPFIX collector configuration

Create a new IPFIX collector configuration

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixCollectorConfig() # IpfixCollectorConfig | 

try:
    # Create a new IPFIX collector configuration
    api_response = api_instance.create_ipfix_collector_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->create_ipfix_collector_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixCollectorConfig**](IpfixCollectorConfig.md)|  | 

### Return type

[**IpfixCollectorConfig**](IpfixCollectorConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ipfix_config**
> IpfixConfig create_ipfix_config(body)

Create a new IPFIX configuration

Create a new IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixConfig() # IpfixConfig | 

try:
    # Create a new IPFIX configuration
    api_response = api_instance.create_ipfix_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->create_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixConfig**](IpfixConfig.md)|  | 

### Return type

[**IpfixConfig**](IpfixConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipfix_collector_config**
> delete_ipfix_collector_config(collector_config_id)

Delete an existing IPFIX collector configuration

Delete an existing IPFIX collector configuration

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
collector_config_id = 'collector_config_id_example' # str | 

try:
    # Delete an existing IPFIX collector configuration
    api_instance.delete_ipfix_collector_config(collector_config_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->delete_ipfix_collector_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_config_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipfix_config**
> delete_ipfix_config(config_id)

Delete an existing IPFIX configuration

Delete an existing IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
config_id = 'config_id_example' # str | 

try:
    # Delete an existing IPFIX configuration
    api_instance.delete_ipfix_config(config_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->delete_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipfix_collector_config**
> IpfixCollectorConfig get_ipfix_collector_config(collector_config_id)

Get an existing IPFIX collector configuration

Get an existing IPFIX collector configuration

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
collector_config_id = 'collector_config_id_example' # str | 

try:
    # Get an existing IPFIX collector configuration
    api_response = api_instance.get_ipfix_collector_config(collector_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->get_ipfix_collector_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_config_id** | **str**|  | 

### Return type

[**IpfixCollectorConfig**](IpfixCollectorConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipfix_config**
> IpfixConfig get_ipfix_config(config_id)

Get an existing IPFIX configuration

Get an existing IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
config_id = 'config_id_example' # str | 

try:
    # Get an existing IPFIX configuration
    api_response = api_instance.get_ipfix_config(config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->get_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  | 

### Return type

[**IpfixConfig**](IpfixConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ipfix_collector_config**
> IpfixCollectorConfigListResult list_ipfix_collector_config(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List IPFIX collector configurations

List IPFIX collector configurations

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IPFIX collector configurations
    api_response = api_instance.list_ipfix_collector_config(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->list_ipfix_collector_config: %s\n" % e)
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

[**IpfixCollectorConfigListResult**](IpfixCollectorConfigListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ipfix_config**
> IpfixConfigListResult list_ipfix_config(applied_to=applied_to, cursor=cursor, included_fields=included_fields, ipfix_config_type=ipfix_config_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List IPFIX configuration

List IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
applied_to = 'applied_to_example' # str | Applied To (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
ipfix_config_type = 'ipfix_config_type_example' # str | Supported IPFIX Config Types. (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IPFIX configuration
    api_response = api_instance.list_ipfix_config(applied_to=applied_to, cursor=cursor, included_fields=included_fields, ipfix_config_type=ipfix_config_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->list_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applied_to** | **str**| Applied To | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **ipfix_config_type** | **str**| Supported IPFIX Config Types. | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IpfixConfigListResult**](IpfixConfigListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ipfix_collector_config**
> IpfixCollectorConfig update_ipfix_collector_config(body, collector_config_id)

Update an existing IPFIX collector configuration

Update an existing IPFIX collector configuration

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixCollectorConfig() # IpfixCollectorConfig | 
collector_config_id = 'collector_config_id_example' # str | 

try:
    # Update an existing IPFIX collector configuration
    api_response = api_instance.update_ipfix_collector_config(body, collector_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->update_ipfix_collector_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixCollectorConfig**](IpfixCollectorConfig.md)|  | 
 **collector_config_id** | **str**|  | 

### Return type

[**IpfixCollectorConfig**](IpfixCollectorConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ipfix_config**
> IpfixConfig update_ipfix_config(body, config_id)

Update an existing IPFIX configuration

Update an existing IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneApiOperationsIpfixApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixConfig() # IpfixConfig | 
config_id = 'config_id_example' # str | 

try:
    # Update an existing IPFIX configuration
    api_response = api_instance.update_ipfix_config(body, config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiOperationsIpfixApi->update_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixConfig**](IpfixConfig.md)|  | 
 **config_id** | **str**|  | 

### Return type

[**IpfixConfig**](IpfixConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

