# swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ipfix_collector_upm_profile**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#create_ipfix_collector_upm_profile) | **POST** /ipfix-collector-profiles | Create a new IPFIX collector profile
[**create_ipfix_upm_profile**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#create_ipfix_upm_profile) | **POST** /ipfix-profiles | Create a new IPFIX profile
[**delete_ipfix_collector_upm_profile**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#delete_ipfix_collector_upm_profile) | **DELETE** /ipfix-collector-profiles/{ipfix-collector-profile-id} | Delete an existing IPFIX collector profile
[**delete_ipfix_upm_profile**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#delete_ipfix_upm_profile) | **DELETE** /ipfix-profiles/{ipfix-profile-id} | Delete an existing IPFIX profile
[**get_ipfix_collector_upm_profile**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#get_ipfix_collector_upm_profile) | **GET** /ipfix-collector-profiles/{ipfix-collector-profile-id} | Get an existing IPFIX collector profile
[**get_ipfix_upm_profile**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#get_ipfix_upm_profile) | **GET** /ipfix-profiles/{ipfix-profile-id} | Get an existing IPFIX profile
[**list_ipfix_collector_upm_profiles**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#list_ipfix_collector_upm_profiles) | **GET** /ipfix-collector-profiles | List IPFIX Collector Profies
[**list_ipfix_upm_profiles**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#list_ipfix_upm_profiles) | **GET** /ipfix-profiles | List IPFIX Profies
[**update_ipfix_collector_upm_profile**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#update_ipfix_collector_upm_profile) | **PUT** /ipfix-collector-profiles/{ipfix-collector-profile-id} | Update an existing IPFIX collector profile
[**update_ipfix_upm_profile**](ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi.md#update_ipfix_upm_profile) | **PUT** /ipfix-profiles/{ipfix-profile-id} | Update an existing IPFIX profile

# **create_ipfix_collector_upm_profile**
> IpfixCollectorUpmProfile create_ipfix_collector_upm_profile(body)

Create a new IPFIX collector profile

Create a new IPFIX collector profile with essential properties.

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixCollectorUpmProfile() # IpfixCollectorUpmProfile | 

try:
    # Create a new IPFIX collector profile
    api_response = api_instance.create_ipfix_collector_upm_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->create_ipfix_collector_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)|  | 

### Return type

[**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ipfix_upm_profile**
> IpfixUpmProfile create_ipfix_upm_profile(body)

Create a new IPFIX profile

Create a new IPFIX profile with essential properties.

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixUpmProfile() # IpfixUpmProfile | 

try:
    # Create a new IPFIX profile
    api_response = api_instance.create_ipfix_upm_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->create_ipfix_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixUpmProfile**](IpfixUpmProfile.md)|  | 

### Return type

[**IpfixUpmProfile**](IpfixUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipfix_collector_upm_profile**
> delete_ipfix_collector_upm_profile(ipfix_collector_profile_id)

Delete an existing IPFIX collector profile

Delete an existing IPFIX collector profile by ID.

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
ipfix_collector_profile_id = 'ipfix_collector_profile_id_example' # str | 

try:
    # Delete an existing IPFIX collector profile
    api_instance.delete_ipfix_collector_upm_profile(ipfix_collector_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->delete_ipfix_collector_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipfix_collector_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipfix_upm_profile**
> delete_ipfix_upm_profile(ipfix_profile_id)

Delete an existing IPFIX profile

Delete an existing IPFIX profile by ID.

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
ipfix_profile_id = 'ipfix_profile_id_example' # str | 

try:
    # Delete an existing IPFIX profile
    api_instance.delete_ipfix_upm_profile(ipfix_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->delete_ipfix_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipfix_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipfix_collector_upm_profile**
> IpfixCollectorUpmProfile get_ipfix_collector_upm_profile(ipfix_collector_profile_id)

Get an existing IPFIX collector profile

Get an existing IPFIX collector profile by profile ID.

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
ipfix_collector_profile_id = 'ipfix_collector_profile_id_example' # str | 

try:
    # Get an existing IPFIX collector profile
    api_response = api_instance.get_ipfix_collector_upm_profile(ipfix_collector_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->get_ipfix_collector_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipfix_collector_profile_id** | **str**|  | 

### Return type

[**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipfix_upm_profile**
> IpfixUpmProfile get_ipfix_upm_profile(ipfix_profile_id)

Get an existing IPFIX profile

Get an existing IPFIX profile by profile ID.

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
ipfix_profile_id = 'ipfix_profile_id_example' # str | 

try:
    # Get an existing IPFIX profile
    api_response = api_instance.get_ipfix_upm_profile(ipfix_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->get_ipfix_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipfix_profile_id** | **str**|  | 

### Return type

[**IpfixUpmProfile**](IpfixUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ipfix_collector_upm_profiles**
> IpfixCollectorUpmProfileListResult list_ipfix_collector_upm_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, profile_types=profile_types, sort_ascending=sort_ascending, sort_by=sort_by)

List IPFIX Collector Profies

Query IPFIX collector profiles with list parameters. List result can be filtered by profile type defined by IpfixCollectorUpmProfileType. 

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
profile_types = 'profile_types_example' # str | IPFIX Collector Profile Type List (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IPFIX Collector Profies
    api_response = api_instance.list_ipfix_collector_upm_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, profile_types=profile_types, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->list_ipfix_collector_upm_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **profile_types** | **str**| IPFIX Collector Profile Type List | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IpfixCollectorUpmProfileListResult**](IpfixCollectorUpmProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ipfix_upm_profiles**
> IpfixUpmProfileListResult list_ipfix_upm_profiles(applied_to_entity_id=applied_to_entity_id, applied_to_entity_type=applied_to_entity_type, cursor=cursor, included_fields=included_fields, page_size=page_size, profile_types=profile_types, sort_ascending=sort_ascending, sort_by=sort_by)

List IPFIX Profies

Query IPFIX profiles with list parameters. List result can be filtered by profile type defined by IpfixUpmProfileType. 

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
applied_to_entity_id = 'applied_to_entity_id_example' # str | ID of Entity Applied with Profile (optional)
applied_to_entity_type = 'applied_to_entity_type_example' # str | Supported Entity Types (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
profile_types = 'profile_types_example' # str | IPFIX Profile Type List (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IPFIX Profies
    api_response = api_instance.list_ipfix_upm_profiles(applied_to_entity_id=applied_to_entity_id, applied_to_entity_type=applied_to_entity_type, cursor=cursor, included_fields=included_fields, page_size=page_size, profile_types=profile_types, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->list_ipfix_upm_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applied_to_entity_id** | **str**| ID of Entity Applied with Profile | [optional] 
 **applied_to_entity_type** | **str**| Supported Entity Types | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **profile_types** | **str**| IPFIX Profile Type List | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IpfixUpmProfileListResult**](IpfixUpmProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ipfix_collector_upm_profile**
> IpfixCollectorUpmProfile update_ipfix_collector_upm_profile(body, ipfix_collector_profile_id)

Update an existing IPFIX collector profile

Update an existing IPFIX collector profile with profile ID and modified properties. 

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixCollectorUpmProfile() # IpfixCollectorUpmProfile | 
ipfix_collector_profile_id = 'ipfix_collector_profile_id_example' # str | 

try:
    # Update an existing IPFIX collector profile
    api_response = api_instance.update_ipfix_collector_upm_profile(body, ipfix_collector_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->update_ipfix_collector_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)|  | 
 **ipfix_collector_profile_id** | **str**|  | 

### Return type

[**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ipfix_upm_profile**
> IpfixUpmProfile update_ipfix_upm_profile(body, ipfix_profile_id)

Update an existing IPFIX profile

Update an existing IPFIX profile with profile ID and modified properties. 

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
api_instance = swagger_client.ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixUpmProfile() # IpfixUpmProfile | 
ipfix_profile_id = 'ipfix_profile_id_example' # str | 

try:
    # Update an existing IPFIX profile
    api_response = api_instance.update_ipfix_upm_profile(body, ipfix_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUnifiedNsgroupProfileManagementProfilesApi->update_ipfix_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixUpmProfile**](IpfixUpmProfile.md)|  | 
 **ipfix_profile_id** | **str**|  | 

### Return type

[**IpfixUpmProfile**](IpfixUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

