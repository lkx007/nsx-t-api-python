# swagger_client.ManagementPlaneApiGroupingObjectsNsServiceGroupsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ns_service_group**](ManagementPlaneApiGroupingObjectsNsServiceGroupsApi.md#create_ns_service_group) | **POST** /ns-service-groups | Create NSServiceGroup
[**delete_ns_service_group**](ManagementPlaneApiGroupingObjectsNsServiceGroupsApi.md#delete_ns_service_group) | **DELETE** /ns-service-groups/{ns-service-group-id} | Delete NSServiceGroup
[**list_ns_service_groups**](ManagementPlaneApiGroupingObjectsNsServiceGroupsApi.md#list_ns_service_groups) | **GET** /ns-service-groups | List all NSServiceGroups
[**read_ns_service_group**](ManagementPlaneApiGroupingObjectsNsServiceGroupsApi.md#read_ns_service_group) | **GET** /ns-service-groups/{ns-service-group-id} | Read NSServiceGroup
[**update_ns_service_group**](ManagementPlaneApiGroupingObjectsNsServiceGroupsApi.md#update_ns_service_group) | **PUT** /ns-service-groups/{ns-service-group-id} | Update NSServiceGroup

# **create_ns_service_group**
> NSServiceGroup create_ns_service_group(body)

Create NSServiceGroup

Creates a new NSServiceGroup which can contain NSServices. A given NSServiceGroup can contain either only ether type of NSServices or only non-ether type of NSServices, i.e. an NSServiceGroup cannot contain a mix of both ether and non-ether types of NSServices. 

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
api_instance = swagger_client.ManagementPlaneApiGroupingObjectsNsServiceGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSServiceGroup() # NSServiceGroup | 

try:
    # Create NSServiceGroup
    api_response = api_instance.create_ns_service_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiGroupingObjectsNsServiceGroupsApi->create_ns_service_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSServiceGroup**](NSServiceGroup.md)|  | 

### Return type

[**NSServiceGroup**](NSServiceGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ns_service_group**
> delete_ns_service_group(ns_service_group_id, force=force)

Delete NSServiceGroup

Deletes the specified NSServiceGroup. By default, if the NSServiceGroup is consumed in a Firewall rule, it won't get deleted. In such situations, pass \"force=true\" as query param to force delete the NSServiceGroup. 

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
api_instance = swagger_client.ManagementPlaneApiGroupingObjectsNsServiceGroupsApi(swagger_client.ApiClient(configuration))
ns_service_group_id = 'ns_service_group_id_example' # str | NSServiceGroup Id
force = true # bool | Force delete the resource even if it is being used somewhere  (optional)

try:
    # Delete NSServiceGroup
    api_instance.delete_ns_service_group(ns_service_group_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiGroupingObjectsNsServiceGroupsApi->delete_ns_service_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_service_group_id** | **str**| NSServiceGroup Id | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ns_service_groups**
> NSServiceGroupListResult list_ns_service_groups(cursor=cursor, default_service=default_service, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all NSServiceGroups

Returns paginated list of NSServiceGroups 

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
api_instance = swagger_client.ManagementPlaneApiGroupingObjectsNsServiceGroupsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
default_service = true # bool | Fetch all default NSServiceGroups (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all NSServiceGroups
    api_response = api_instance.list_ns_service_groups(cursor=cursor, default_service=default_service, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiGroupingObjectsNsServiceGroupsApi->list_ns_service_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **default_service** | **bool**| Fetch all default NSServiceGroups | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NSServiceGroupListResult**](NSServiceGroupListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ns_service_group**
> NSServiceGroup read_ns_service_group(ns_service_group_id)

Read NSServiceGroup

Returns information about the specified NSServiceGroup 

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
api_instance = swagger_client.ManagementPlaneApiGroupingObjectsNsServiceGroupsApi(swagger_client.ApiClient(configuration))
ns_service_group_id = 'ns_service_group_id_example' # str | NSServiceGroup Id

try:
    # Read NSServiceGroup
    api_response = api_instance.read_ns_service_group(ns_service_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiGroupingObjectsNsServiceGroupsApi->read_ns_service_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_service_group_id** | **str**| NSServiceGroup Id | 

### Return type

[**NSServiceGroup**](NSServiceGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ns_service_group**
> NSServiceGroup update_ns_service_group(body, ns_service_group_id)

Update NSServiceGroup

Updates the specified NSService. Modifiable parameters include the description, display_name and members. 

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
api_instance = swagger_client.ManagementPlaneApiGroupingObjectsNsServiceGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSServiceGroup() # NSServiceGroup | 
ns_service_group_id = 'ns_service_group_id_example' # str | NSServiceGroup Id

try:
    # Update NSServiceGroup
    api_response = api_instance.update_ns_service_group(body, ns_service_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiGroupingObjectsNsServiceGroupsApi->update_ns_service_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSServiceGroup**](NSServiceGroup.md)|  | 
 **ns_service_group_id** | **str**| NSServiceGroup Id | 

### Return type

[**NSServiceGroup**](NSServiceGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

