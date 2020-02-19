# swagger_client.ManagementPlaneApiAppDiscoveryApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_app_profile**](ManagementPlaneApiAppDiscoveryApi.md#add_app_profile) | **POST** /app-discovery/app-profiles | Adds a new app profile
[**delete_app_discovery_session**](ManagementPlaneApiAppDiscoveryApi.md#delete_app_discovery_session) | **DELETE** /app-discovery/sessions/{session-id} | Cancel and delete the application discovery session
[**delete_app_profile**](ManagementPlaneApiAppDiscoveryApi.md#delete_app_profile) | **DELETE** /app-discovery/app-profiles/{app-profile-id} | Delete App Profile
[**get_app_discovery_session**](ManagementPlaneApiAppDiscoveryApi.md#get_app_discovery_session) | **GET** /app-discovery/sessions/{session-id} | Returns the status of the application discovery session and other details
[**get_app_discovery_session_app_profiles**](ManagementPlaneApiAppDiscoveryApi.md#get_app_discovery_session_app_profiles) | **GET** /app-discovery/sessions/{session-id}/app-profiles | application profiles in this application discovery session
[**get_app_discovery_session_installed_apps**](ManagementPlaneApiAppDiscoveryApi.md#get_app_discovery_session_installed_apps) | **GET** /app-discovery/sessions/{session-id}/installed-apps | Returns the details of the installed apps for the app profile ID in that session
[**get_app_discovery_session_ns_group_members**](ManagementPlaneApiAppDiscoveryApi.md#get_app_discovery_session_ns_group_members) | **GET** /app-discovery/sessions/{session-id}/ns-groups/{ns-group-id}/members | vms in the ns-group of the application discovery session
[**get_app_discovery_session_ns_groups**](ManagementPlaneApiAppDiscoveryApi.md#get_app_discovery_session_ns_groups) | **GET** /app-discovery/sessions/{session-id}/ns-groups | ns-groups in this application discovery session
[**get_app_discovery_session_summary**](ManagementPlaneApiAppDiscoveryApi.md#get_app_discovery_session_summary) | **GET** /app-discovery/sessions/{session-id}/summary | Returns the summary of the application discovery session
[**get_app_discovery_sessions**](ManagementPlaneApiAppDiscoveryApi.md#get_app_discovery_sessions) | **GET** /app-discovery/sessions | Returns the list of the application discovery sessions available
[**get_app_profile_details**](ManagementPlaneApiAppDiscoveryApi.md#get_app_profile_details) | **GET** /app-discovery/app-profiles/{app-profile-id} | Returns detail of the app profile
[**get_app_profiles**](ManagementPlaneApiAppDiscoveryApi.md#get_app_profiles) | **GET** /app-discovery/app-profiles | Returns list of app profile IDs created
[**get_appdiscovery_result_app_info_and_host_vm_in_csv_format_csv**](ManagementPlaneApiAppDiscoveryApi.md#get_appdiscovery_result_app_info_and_host_vm_in_csv_format_csv) | **POST** /app-discovery/sessions/{session-id}/report/app-info-and-vm?format&#x3D;csv | Export app discovery results in CSV format
[**get_appdiscovery_session_app_profile_member_apps_in_csv_format_csv**](ManagementPlaneApiAppDiscoveryApi.md#get_appdiscovery_session_app_profile_member_apps_in_csv_format_csv) | **GET** /app-discovery/sessions/{session-id}/report/app-profile-and-app-info?format&#x3D;csv | Export app profiles in CSV format for a given sessiom
[**reclassify_app_discovery_session**](ManagementPlaneApiAppDiscoveryApi.md#reclassify_app_discovery_session) | **POST** /app-discovery/sessions/{session-id}/re-classify | Re-classify a completed application discovery session.
[**start_app_discovery_session**](ManagementPlaneApiAppDiscoveryApi.md#start_app_discovery_session) | **POST** /app-discovery/sessions | Starts the discovery of application discovery session
[**update_app_profile**](ManagementPlaneApiAppDiscoveryApi.md#update_app_profile) | **PUT** /app-discovery/app-profiles/{app-profile-id} | Update AppProfile

# **add_app_profile**
> AppProfile add_app_profile(body)

Adds a new app profile

Adds a new app profile 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppProfile() # AppProfile | 

try:
    # Adds a new app profile
    api_response = api_instance.add_app_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->add_app_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppProfile**](AppProfile.md)|  | 

### Return type

[**AppProfile**](AppProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_discovery_session**
> delete_app_discovery_session(session_id)

Cancel and delete the application discovery session

Cancel and delete the application discovery session 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 

try:
    # Cancel and delete the application discovery session
    api_instance.delete_app_discovery_session(session_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->delete_app_discovery_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_profile**
> delete_app_profile(app_profile_id, force=force)

Delete App Profile

Deletes the specified AppProfile. 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
app_profile_id = 'app_profile_id_example' # str | 
force = true # bool | Force delete the resource even if it is being used somewhere  (optional)

try:
    # Delete App Profile
    api_instance.delete_app_profile(app_profile_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->delete_app_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_profile_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_discovery_session**
> AppDiscoverySession get_app_discovery_session(session_id)

Returns the status of the application discovery session and other details

Returns the status of the application discovery session and other details 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 

try:
    # Returns the status of the application discovery session and other details
    api_response = api_instance.get_app_discovery_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_app_discovery_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**AppDiscoverySession**](AppDiscoverySession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_discovery_session_app_profiles**
> AppProfileListResult get_app_discovery_session_app_profiles(session_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

application profiles in this application discovery session

Returns the application profiles that was part of the application discovery session | while it was started. 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # application profiles in this application discovery session
    api_response = api_instance.get_app_discovery_session_app_profiles(session_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_app_discovery_session_app_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**AppProfileListResult**](AppProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_discovery_session_installed_apps**
> AppInfoListResult get_app_discovery_session_installed_apps(session_id, app_profile_id=app_profile_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, vm_id=vm_id)

Returns the details of the installed apps for the app profile ID in that session

Returns the details of the installed apps for the app profile ID in that session 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 
app_profile_id = 'app_profile_id_example' # str |  (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
vm_id = 'vm_id_example' # str |  (optional)

try:
    # Returns the details of the installed apps for the app profile ID in that session
    api_response = api_instance.get_app_discovery_session_installed_apps(session_id, app_profile_id=app_profile_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_app_discovery_session_installed_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **app_profile_id** | **str**|  | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **vm_id** | **str**|  | [optional] 

### Return type

[**AppInfoListResult**](AppInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_discovery_session_ns_group_members**
> AppDiscoveryVmInfoListResult get_app_discovery_session_ns_group_members(session_id, ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

vms in the ns-group of the application discovery session

Returns the vms in the ns-group of the application discovery session 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 
ns_group_id = 'ns_group_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # vms in the ns-group of the application discovery session
    api_response = api_instance.get_app_discovery_session_ns_group_members(session_id, ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_app_discovery_session_ns_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **ns_group_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**AppDiscoveryVmInfoListResult**](AppDiscoveryVmInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_discovery_session_ns_groups**
> NSGroupMetaInfoListResult get_app_discovery_session_ns_groups(session_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

ns-groups in this application discovery session

Returns the ns groups that was part of the application discovery session | while it was started 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # ns-groups in this application discovery session
    api_response = api_instance.get_app_discovery_session_ns_groups(session_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_app_discovery_session_ns_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NSGroupMetaInfoListResult**](NSGroupMetaInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_discovery_session_summary**
> AppDiscoverySessionResultSummary get_app_discovery_session_summary(session_id)

Returns the summary of the application discovery session

Returns the summary of the application discovery session 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 

try:
    # Returns the summary of the application discovery session
    api_response = api_instance.get_app_discovery_session_summary(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_app_discovery_session_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**AppDiscoverySessionResultSummary**](AppDiscoverySessionResultSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_discovery_sessions**
> AppDiscoverySessionsListResult get_app_discovery_sessions(cursor=cursor, group_id=group_id, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, status=status)

Returns the list of the application discovery sessions available

Returns the list of the application discovery sessions available 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
group_id = 'group_id_example' # str | NSGroup id, helps user query sessions related to one nsgroup (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
status = 'status_example' # str | Session Status, e.g. get all running sessions (optional)

try:
    # Returns the list of the application discovery sessions available
    api_response = api_instance.get_app_discovery_sessions(cursor=cursor, group_id=group_id, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_app_discovery_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **group_id** | **str**| NSGroup id, helps user query sessions related to one nsgroup | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **status** | **str**| Session Status, e.g. get all running sessions | [optional] 

### Return type

[**AppDiscoverySessionsListResult**](AppDiscoverySessionsListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_profile_details**
> AppProfile get_app_profile_details(app_profile_id)

Returns detail of the app profile

Returns detail of the app profile 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
app_profile_id = 'app_profile_id_example' # str | 

try:
    # Returns detail of the app profile
    api_response = api_instance.get_app_profile_details(app_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_app_profile_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_profile_id** | **str**|  | 

### Return type

[**AppProfile**](AppProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_profiles**
> AppProfileListResult get_app_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Returns list of app profile IDs created

Returns list of app profile IDs created 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Returns list of app profile IDs created
    api_response = api_instance.get_app_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_app_profiles: %s\n" % e)
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

[**AppProfileListResult**](AppProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appdiscovery_result_app_info_and_host_vm_in_csv_format_csv**
> AppInfoHostVmListInCsvFormat get_appdiscovery_result_app_info_and_host_vm_in_csv_format_csv(body, session_id)

Export app discovery results in CSV format

Returns app discovery results in CSV format, each row contains discovered app information and the id of the vms this app is discovered from for a given set of vms (or for all vms belong to this session when no vm id is passed in) 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReportAppResultsForVmsRequestParameters() # ReportAppResultsForVmsRequestParameters | 
session_id = 'session_id_example' # str | 

try:
    # Export app discovery results in CSV format
    api_response = api_instance.get_appdiscovery_result_app_info_and_host_vm_in_csv_format_csv(body, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_appdiscovery_result_app_info_and_host_vm_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportAppResultsForVmsRequestParameters**](ReportAppResultsForVmsRequestParameters.md)|  | 
 **session_id** | **str**|  | 

### Return type

[**AppInfoHostVmListInCsvFormat**](AppInfoHostVmListInCsvFormat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appdiscovery_session_app_profile_member_apps_in_csv_format_csv**
> AppProfileMemberAppsListInCsvFormat get_appdiscovery_session_app_profile_member_apps_in_csv_format_csv(session_id)

Export app profiles in CSV format for a given sessiom

Returns app profiles information for a given session in CSV format Each row will contain detailed info of an app profile, and the id of apps which is member of this app profile in this session 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 

try:
    # Export app profiles in CSV format for a given sessiom
    api_response = api_instance.get_appdiscovery_session_app_profile_member_apps_in_csv_format_csv(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->get_appdiscovery_session_app_profile_member_apps_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**AppProfileMemberAppsListInCsvFormat**](AppProfileMemberAppsListInCsvFormat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reclassify_app_discovery_session**
> AppDiscoverySessionResultSummary reclassify_app_discovery_session(body, session_id)

Re-classify a completed application discovery session.

Re-classify completed application discovery session against input  AppProfiles. If no AppProfiles are specified then we use the previous  AppProfiles of that session. 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
body = swagger_client.SessionReclassificationParameter() # SessionReclassificationParameter | 
session_id = 'session_id_example' # str | 

try:
    # Re-classify a completed application discovery session.
    api_response = api_instance.reclassify_app_discovery_session(body, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->reclassify_app_discovery_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionReclassificationParameter**](SessionReclassificationParameter.md)|  | 
 **session_id** | **str**|  | 

### Return type

[**AppDiscoverySessionResultSummary**](AppDiscoverySessionResultSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_app_discovery_session**
> AppDiscoverySession start_app_discovery_session(body)

Starts the discovery of application discovery session

Starts the discovery of application discovery session 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
body = swagger_client.StartAppDiscoverySessionParameters() # StartAppDiscoverySessionParameters | 

try:
    # Starts the discovery of application discovery session
    api_response = api_instance.start_app_discovery_session(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->start_app_discovery_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StartAppDiscoverySessionParameters**](StartAppDiscoverySessionParameters.md)|  | 

### Return type

[**AppDiscoverySession**](AppDiscoverySession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_profile**
> AppProfile update_app_profile(body, app_profile_id)

Update AppProfile

Update AppProfile 

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
api_instance = swagger_client.ManagementPlaneApiAppDiscoveryApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppProfile() # AppProfile | 
app_profile_id = 'app_profile_id_example' # str | 

try:
    # Update AppProfile
    api_response = api_instance.update_app_profile(body, app_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAppDiscoveryApi->update_app_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppProfile**](AppProfile.md)|  | 
 **app_profile_id** | **str**|  | 

### Return type

[**AppProfile**](AppProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

