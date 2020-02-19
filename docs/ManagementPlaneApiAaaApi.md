# swagger_client.ManagementPlaneApiAaaApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registration_token**](ManagementPlaneApiAaaApi.md#create_registration_token) | **POST** /aaa/registration-token | Create registration access token
[**create_role_binding**](ManagementPlaneApiAaaApi.md#create_role_binding) | **POST** /aaa/role-bindings | Assign roles to User or Group
[**delete_all_stale_role_bindings_delete_stale_bindings**](ManagementPlaneApiAaaApi.md#delete_all_stale_role_bindings_delete_stale_bindings) | **POST** /aaa/role-bindings?action&#x3D;delete_stale_bindings | Delete all stale role assignments
[**delete_registration_token**](ManagementPlaneApiAaaApi.md#delete_registration_token) | **DELETE** /aaa/registration-token/{token} | Delete registration access token
[**delete_role_binding**](ManagementPlaneApiAaaApi.md#delete_role_binding) | **DELETE** /aaa/role-bindings/{binding-id} | Delete user/group&#x27;s roles assignment
[**get_all_role_bindings**](ManagementPlaneApiAaaApi.md#get_all_role_bindings) | **GET** /aaa/role-bindings | Get all users and groups with their roles
[**get_all_roles_info**](ManagementPlaneApiAaaApi.md#get_all_roles_info) | **GET** /aaa/roles | Get information about all roles
[**get_current_user_info**](ManagementPlaneApiAaaApi.md#get_current_user_info) | **GET** /aaa/user-info | Get information about logged-in user. The permissions parameter of the NsxRole has been deprecated.
[**get_group_vidm_search_result**](ManagementPlaneApiAaaApi.md#get_group_vidm_search_result) | **GET** /aaa/vidm/groups | Get all the User Groups where vIDM display name matches the search key case insensitively. The search key is checked to be a substring of display name. This is a non paginated API.
[**get_registration_token**](ManagementPlaneApiAaaApi.md#get_registration_token) | **GET** /aaa/registration-token/{token} | Get registration access token
[**get_role_binding**](ManagementPlaneApiAaaApi.md#get_role_binding) | **GET** /aaa/role-bindings/{binding-id} | Get user/group&#x27;s role information
[**get_role_info**](ManagementPlaneApiAaaApi.md#get_role_info) | **GET** /aaa/roles/{role} | Get role information
[**get_user_vidm_search_result**](ManagementPlaneApiAaaApi.md#get_user_vidm_search_result) | **GET** /aaa/vidm/users | Get all the users from vIDM whose userName, givenName or familyName matches the search key case insensitively. The search key is checked to be a substring of name or given name or family name. This is a non paginated API.
[**get_vidm_search_result**](ManagementPlaneApiAaaApi.md#get_vidm_search_result) | **POST** /aaa/vidm/search | Get all the users and groups from vIDM matching the search key case insensitively. The search key is checked to be a substring of name or given name or family name of user and display name of group. This is a non paginated API.
[**update_role_binding**](ManagementPlaneApiAaaApi.md#update_role_binding) | **PUT** /aaa/role-bindings/{binding-id} | Update User or Group&#x27;s roles

# **create_registration_token**
> RegistrationToken create_registration_token()

Create registration access token

The privileges of the registration token will be the same as the caller.

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))

try:
    # Create registration access token
    api_response = api_instance.create_registration_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->create_registration_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistrationToken**](RegistrationToken.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_binding**
> RoleBinding create_role_binding(body)

Assign roles to User or Group

When assigning a user role, specify the user name with the same case as it appears in vIDM to access the NSX-T user interface. For example, if vIDM has the user name User1@example.com then the name attribute in the API call must be be User1@example.com and cannot be user1@example.com. 

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleBinding() # RoleBinding | 

try:
    # Assign roles to User or Group
    api_response = api_instance.create_role_binding(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->create_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleBinding**](RoleBinding.md)|  | 

### Return type

[**RoleBinding**](RoleBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_stale_role_bindings_delete_stale_bindings**
> delete_all_stale_role_bindings_delete_stale_bindings()

Delete all stale role assignments

Delete all stale role assignments

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))

try:
    # Delete all stale role assignments
    api_instance.delete_all_stale_role_bindings_delete_stale_bindings()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->delete_all_stale_role_bindings_delete_stale_bindings: %s\n" % e)
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

# **delete_registration_token**
> delete_registration_token(token)

Delete registration access token

Delete registration access token

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | Registration token

try:
    # Delete registration access token
    api_instance.delete_registration_token(token)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->delete_registration_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Registration token | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_binding**
> delete_role_binding(binding_id)

Delete user/group's roles assignment

Delete user/group's roles assignment

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
binding_id = 'binding_id_example' # str | User/Group's id

try:
    # Delete user/group's roles assignment
    api_instance.delete_role_binding(binding_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->delete_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binding_id** | **str**| User/Group&#x27;s id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_role_bindings**
> RoleBindingListResult get_all_role_bindings(cursor=cursor, included_fields=included_fields, name=name, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

Get all users and groups with their roles

Get all users and groups with their roles

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
name = 'name_example' # str | User/Group name (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | Type (optional)

try:
    # Get all users and groups with their roles
    api_response = api_instance.get_all_role_bindings(cursor=cursor, included_fields=included_fields, name=name, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->get_all_role_bindings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **name** | **str**| User/Group name | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **type** | **str**| Type | [optional] 

### Return type

[**RoleBindingListResult**](RoleBindingListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles_info**
> RoleListResult get_all_roles_info()

Get information about all roles

Get information about all roles

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))

try:
    # Get information about all roles
    api_response = api_instance.get_all_roles_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->get_all_roles_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleListResult**](RoleListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_info**
> UserInfo get_current_user_info()

Get information about logged-in user. The permissions parameter of the NsxRole has been deprecated.

Get information about logged-in user. The permissions parameter of the NsxRole has been deprecated.

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))

try:
    # Get information about logged-in user. The permissions parameter of the NsxRole has been deprecated.
    api_response = api_instance.get_current_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->get_current_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_vidm_search_result**
> VidmInfoListResult get_group_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get all the User Groups where vIDM display name matches the search key case insensitively. The search key is checked to be a substring of display name. This is a non paginated API.

Get all the User Groups where vIDM display name matches the search key case insensitively. The search key is checked to be a substring of display name. This is a non paginated API.

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
search_string = 'search_string_example' # str | Search string to search for. 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all the User Groups where vIDM display name matches the search key case insensitively. The search key is checked to be a substring of display name. This is a non paginated API.
    api_response = api_instance.get_group_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->get_group_vidm_search_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| Search string to search for.  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**VidmInfoListResult**](VidmInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_token**
> RegistrationToken get_registration_token(token)

Get registration access token

Get registration access token

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | Registration token

try:
    # Get registration access token
    api_response = api_instance.get_registration_token(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->get_registration_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Registration token | 

### Return type

[**RegistrationToken**](RegistrationToken.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_binding**
> RoleBinding get_role_binding(binding_id)

Get user/group's role information

Get user/group's role information

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
binding_id = 'binding_id_example' # str | User/Group's id

try:
    # Get user/group's role information
    api_response = api_instance.get_role_binding(binding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->get_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binding_id** | **str**| User/Group&#x27;s id | 

### Return type

[**RoleBinding**](RoleBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_info**
> RoleWithFeatures get_role_info(role)

Get role information

Get role information

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | Role Name

try:
    # Get role information
    api_response = api_instance.get_role_info(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->get_role_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Role Name | 

### Return type

[**RoleWithFeatures**](RoleWithFeatures.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_vidm_search_result**
> VidmInfoListResult get_user_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get all the users from vIDM whose userName, givenName or familyName matches the search key case insensitively. The search key is checked to be a substring of name or given name or family name. This is a non paginated API.

Get all the users from vIDM whose userName, givenName or familyName matches the search key case insensitively. The search key is checked to be a substring of name or given name or family name. This is a non paginated API.

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
search_string = 'search_string_example' # str | Search string to search for. 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all the users from vIDM whose userName, givenName or familyName matches the search key case insensitively. The search key is checked to be a substring of name or given name or family name. This is a non paginated API.
    api_response = api_instance.get_user_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->get_user_vidm_search_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| Search string to search for.  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**VidmInfoListResult**](VidmInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vidm_search_result**
> VidmInfoListResult get_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get all the users and groups from vIDM matching the search key case insensitively. The search key is checked to be a substring of name or given name or family name of user and display name of group. This is a non paginated API.

Get all the users and groups from vIDM matching the search key case insensitively. The search key is checked to be a substring of name or given name or family name of user and display name of group. This is a non paginated API.

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
search_string = 'search_string_example' # str | Search string to search for. 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all the users and groups from vIDM matching the search key case insensitively. The search key is checked to be a substring of name or given name or family name of user and display name of group. This is a non paginated API.
    api_response = api_instance.get_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->get_vidm_search_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| Search string to search for.  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**VidmInfoListResult**](VidmInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_binding**
> RoleBinding update_role_binding(body, binding_id)

Update User or Group's roles

Update User or Group's roles

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
api_instance = swagger_client.ManagementPlaneApiAaaApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleBinding() # RoleBinding | 
binding_id = 'binding_id_example' # str | User/Group's id

try:
    # Update User or Group's roles
    api_response = api_instance.update_role_binding(body, binding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiAaaApi->update_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleBinding**](RoleBinding.md)|  | 
 **binding_id** | **str**| User/Group&#x27;s id | 

### Return type

[**RoleBinding**](RoleBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

