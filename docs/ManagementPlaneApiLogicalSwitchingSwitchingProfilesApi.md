# swagger_client.ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_switching_profile**](ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi.md#create_switching_profile) | **POST** /switching-profiles | Create a Switching Profile
[**delete_switching_profile**](ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi.md#delete_switching_profile) | **DELETE** /switching-profiles/{switching-profile-id} | Delete a Switching Profile
[**get_switching_profile**](ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi.md#get_switching_profile) | **GET** /switching-profiles/{switching-profile-id} | Get Switching Profile by ID
[**get_switching_profile_status**](ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi.md#get_switching_profile_status) | **GET** /switching-profiles/{switching-profile-id}/summary | Get Counts of Ports and Switches Using This Switching Profile
[**list_switching_profiles**](ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi.md#list_switching_profiles) | **GET** /switching-profiles | List Switching Profiles
[**update_switching_profile**](ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi.md#update_switching_profile) | **PUT** /switching-profiles/{switching-profile-id} | Update a Switching Profile

# **create_switching_profile**
> BaseSwitchingProfile create_switching_profile(body)

Create a Switching Profile

Creates a new, custom qos, port-mirroring, spoof-guard or port-security switching profile. You can override their default switching profile assignments by creating a new switching profile and assigning it to one or more logical switches. You cannot override the default ipfix or ip_discovery switching profiles. 

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
api_instance = swagger_client.ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseSwitchingProfile() # BaseSwitchingProfile | 

try:
    # Create a Switching Profile
    api_response = api_instance.create_switching_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi->create_switching_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseSwitchingProfile**](BaseSwitchingProfile.md)|  | 

### Return type

[**BaseSwitchingProfile**](BaseSwitchingProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_switching_profile**
> delete_switching_profile(switching_profile_id, unbind=unbind)

Delete a Switching Profile

Deletes the specified switching profile.

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
api_instance = swagger_client.ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi(swagger_client.ApiClient(configuration))
switching_profile_id = 'switching_profile_id_example' # str | 
unbind = true # bool | force unbinding of logical switches and ports from a switching profile (optional)

try:
    # Delete a Switching Profile
    api_instance.delete_switching_profile(switching_profile_id, unbind=unbind)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi->delete_switching_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switching_profile_id** | **str**|  | 
 **unbind** | **bool**| force unbinding of logical switches and ports from a switching profile | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_switching_profile**
> BaseSwitchingProfile get_switching_profile(switching_profile_id)

Get Switching Profile by ID

Returns information about a specified switching profile.

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
api_instance = swagger_client.ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi(swagger_client.ApiClient(configuration))
switching_profile_id = 'switching_profile_id_example' # str | 

try:
    # Get Switching Profile by ID
    api_response = api_instance.get_switching_profile(switching_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi->get_switching_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switching_profile_id** | **str**|  | 

### Return type

[**BaseSwitchingProfile**](BaseSwitchingProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_switching_profile_status**
> SwitchingProfileStatus get_switching_profile_status(switching_profile_id)

Get Counts of Ports and Switches Using This Switching Profile

Get Counts of Ports and Switches Using This Switching Profile

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
api_instance = swagger_client.ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi(swagger_client.ApiClient(configuration))
switching_profile_id = 'switching_profile_id_example' # str | 

try:
    # Get Counts of Ports and Switches Using This Switching Profile
    api_response = api_instance.get_switching_profile_status(switching_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi->get_switching_profile_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switching_profile_id** | **str**|  | 

### Return type

[**SwitchingProfileStatus**](SwitchingProfileStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_switching_profiles**
> SwitchingProfilesListResult list_switching_profiles(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, switching_profile_type=switching_profile_type)

List Switching Profiles

Returns information about the system-default and user-configured switching profiles. Each switching profile has a unique ID, a display name, and various other read-only and configurable properties. The default switching profiles are assigned automatically to each switch. 

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
api_instance = swagger_client.ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
include_system_owned = true # bool | Whether the list result contains system resources (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
switching_profile_type = 'switching_profile_type_example' # str | comma-separated list of switching profile types, e.g. ?switching_profile_type=QosSwitchingProfile,IpDiscoverySwitchingProfile (optional)

try:
    # List Switching Profiles
    api_response = api_instance.list_switching_profiles(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, switching_profile_type=switching_profile_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi->list_switching_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **include_system_owned** | **bool**| Whether the list result contains system resources | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **switching_profile_type** | **str**| comma-separated list of switching profile types, e.g. ?switching_profile_type&#x3D;QosSwitchingProfile,IpDiscoverySwitchingProfile | [optional] 

### Return type

[**SwitchingProfilesListResult**](SwitchingProfilesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_switching_profile**
> BaseSwitchingProfile update_switching_profile(body, switching_profile_id)

Update a Switching Profile

Updates the user-configurable parameters of a switching profile. Only the qos, port-mirroring, spoof-guard and port-security switching profiles can be modified. You cannot modify the ipfix or ip-discovery switching profiles. 

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
api_instance = swagger_client.ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseSwitchingProfile() # BaseSwitchingProfile | 
switching_profile_id = 'switching_profile_id_example' # str | 

try:
    # Update a Switching Profile
    api_response = api_instance.update_switching_profile(body, switching_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi->update_switching_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseSwitchingProfile**](BaseSwitchingProfile.md)|  | 
 **switching_profile_id** | **str**|  | 

### Return type

[**BaseSwitchingProfile**](BaseSwitchingProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

