# swagger_client.ManagementPlaneApiDirectoryServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_directory_domain**](ManagementPlaneApiDirectoryServiceApi.md#create_directory_domain) | **POST** /directory/domains | Create a directory domain
[**create_directory_ldap_server**](ManagementPlaneApiDirectoryServiceApi.md#create_directory_ldap_server) | **POST** /directory/domains/{domain-id}/ldap-servers | Create a LDAP server for directory domain
[**delete_directory_domain**](ManagementPlaneApiDirectoryServiceApi.md#delete_directory_domain) | **DELETE** /directory/domains/{domain-id} | Delete a specific domain with given identifier
[**delete_directory_ldap_server**](ManagementPlaneApiDirectoryServiceApi.md#delete_directory_ldap_server) | **DELETE** /directory/domains/{domain-id}/ldap-servers/{server-id} | Delete a LDAP server for directory domain
[**get_directory_domain**](ManagementPlaneApiDirectoryServiceApi.md#get_directory_domain) | **GET** /directory/domains/{domain-id} | Get a specific domain with given identifier
[**get_directory_domain_sync_stats**](ManagementPlaneApiDirectoryServiceApi.md#get_directory_domain_sync_stats) | **GET** /directory/domains/{domain-id}/sync-stats | Get domain sync statistics for the given identifier
[**get_directory_ldap_server**](ManagementPlaneApiDirectoryServiceApi.md#get_directory_ldap_server) | **GET** /directory/domains/{domain-id}/ldap-servers/{server-id} | Get a specific LDAP server for a given directory domain
[**list_directory_domains**](ManagementPlaneApiDirectoryServiceApi.md#list_directory_domains) | **GET** /directory/domains | List all configured domains
[**list_directory_group_member_groups**](ManagementPlaneApiDirectoryServiceApi.md#list_directory_group_member_groups) | **GET** /directory/domains/{domain-id}/groups/{group-id}/member-groups | List members of a directory group
[**list_directory_ldap_servers**](ManagementPlaneApiDirectoryServiceApi.md#list_directory_ldap_servers) | **GET** /directory/domains/{domain-id}/ldap-servers | List all configured domain LDAP servers
[**request_directory_domain_sync**](ManagementPlaneApiDirectoryServiceApi.md#request_directory_domain_sync) | **POST** /directory/domains/{domain-id} | Invoke full sync or delta sync for a specific domain, with additional delay in seconds if needed.  Stop sync will try to stop any pending sync if any to return to idle state.
[**search_directory_groups**](ManagementPlaneApiDirectoryServiceApi.md#search_directory_groups) | **GET** /directory/domains/{domain-id}/groups | Search for directory groups within a domain based on the substring of a distinguished name. (e.g. CN&#x3D;User,DC&#x3D;acme,DC&#x3D;com) The search filter pattern can optionally support multiple (up to 100 maximum) search pattern separated by &#x27;|&#x27; (url encoded %7C). In this case, the search results will be returned as the union of all matching criteria. (e.g. CN&#x3D;Ann,CN&#x3D;Users,DC&#x3D;acme,DC&#x3D;com|CN&#x3D;Bob,CN&#x3D;Users,DC&#x3D;acme,DC&#x3D;com)
[**test_directory_ldap_server**](ManagementPlaneApiDirectoryServiceApi.md#test_directory_ldap_server) | **POST** /directory/domains/{domain-id}/ldap-servers/{server-id} | Test a LDAP server connection for directory domain
[**update_directory_domain**](ManagementPlaneApiDirectoryServiceApi.md#update_directory_domain) | **PUT** /directory/domains/{domain-id} | Update a directory domain
[**update_directory_ldap_server**](ManagementPlaneApiDirectoryServiceApi.md#update_directory_ldap_server) | **PUT** /directory/domains/{domain-id}/ldap-servers/{server-id} | Update a LDAP server for directory domain
[**verify_directory_ldap_server**](ManagementPlaneApiDirectoryServiceApi.md#verify_directory_ldap_server) | **POST** /directory/ldap-server | Test a directory domain LDAP server connectivity

# **create_directory_domain**
> DirectoryDomain create_directory_domain(body)

Create a directory domain

Create a directory domain

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryDomain() # DirectoryDomain | 

try:
    # Create a directory domain
    api_response = api_instance.create_directory_domain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->create_directory_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryDomain**](DirectoryDomain.md)|  | 

### Return type

[**DirectoryDomain**](DirectoryDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_directory_ldap_server**
> DirectoryLdapServer create_directory_ldap_server(body, domain_id)

Create a LDAP server for directory domain

More than one LDAP server can be created and only one LDAP server is used to synchronize directory objects. If more than one LDAP server is configured, NSX will try all the servers until it is able to successfully connect to one.

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryLdapServer() # DirectoryLdapServer | 
domain_id = 'domain_id_example' # str | Directory domain identifier

try:
    # Create a LDAP server for directory domain
    api_response = api_instance.create_directory_ldap_server(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->create_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryLdapServer**](DirectoryLdapServer.md)|  | 
 **domain_id** | **str**| Directory domain identifier | 

### Return type

[**DirectoryLdapServer**](DirectoryLdapServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_directory_domain**
> delete_directory_domain(domain_id, force=force)

Delete a specific domain with given identifier

Delete a specific domain with given identifier

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
force = true # bool | Force delete the resource even if it is being used somewhere  (optional)

try:
    # Delete a specific domain with given identifier
    api_instance.delete_directory_domain(domain_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->delete_directory_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_directory_ldap_server**
> delete_directory_ldap_server(domain_id, server_id)

Delete a LDAP server for directory domain

Delete a LDAP server for directory domain

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
server_id = 'server_id_example' # str | LDAP server identifier

try:
    # Delete a LDAP server for directory domain
    api_instance.delete_directory_ldap_server(domain_id, server_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->delete_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **server_id** | **str**| LDAP server identifier | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_domain**
> DirectoryDomain get_directory_domain(domain_id)

Get a specific domain with given identifier

Get a specific domain with given identifier

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier

try:
    # Get a specific domain with given identifier
    api_response = api_instance.get_directory_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->get_directory_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 

### Return type

[**DirectoryDomain**](DirectoryDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_domain_sync_stats**
> DirectoryDomainSyncStats get_directory_domain_sync_stats(domain_id)

Get domain sync statistics for the given identifier

Get domain sync statistics for the given identifier

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier

try:
    # Get domain sync statistics for the given identifier
    api_response = api_instance.get_directory_domain_sync_stats(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->get_directory_domain_sync_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 

### Return type

[**DirectoryDomainSyncStats**](DirectoryDomainSyncStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_ldap_server**
> DirectoryLdapServer get_directory_ldap_server(domain_id, server_id)

Get a specific LDAP server for a given directory domain

Get a specific LDAP server for a given directory domain

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
server_id = 'server_id_example' # str | LDAP server identifier

try:
    # Get a specific LDAP server for a given directory domain
    api_response = api_instance.get_directory_ldap_server(domain_id, server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->get_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **server_id** | **str**| LDAP server identifier | 

### Return type

[**DirectoryLdapServer**](DirectoryLdapServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_directory_domains**
> DirectoryDomainListResults list_directory_domains(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all configured domains

List all configured domains

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all configured domains
    api_response = api_instance.list_directory_domains(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->list_directory_domains: %s\n" % e)
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

[**DirectoryDomainListResults**](DirectoryDomainListResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_directory_group_member_groups**
> DirectoryGroupMemberListResults list_directory_group_member_groups(domain_id, group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List members of a directory group

A member group could be either direct member of the group specified by group_id or nested member of it. Both direct member groups and nested member groups are returned.

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
group_id = 'group_id_example' # str | Directory group identifier
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List members of a directory group
    api_response = api_instance.list_directory_group_member_groups(domain_id, group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->list_directory_group_member_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **group_id** | **str**| Directory group identifier | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DirectoryGroupMemberListResults**](DirectoryGroupMemberListResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_directory_ldap_servers**
> DirectoryLdapServerListResults list_directory_ldap_servers(domain_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all configured domain LDAP servers

List all configured domain LDAP servers

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all configured domain LDAP servers
    api_response = api_instance.list_directory_ldap_servers(domain_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->list_directory_ldap_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DirectoryLdapServerListResults**](DirectoryLdapServerListResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_directory_domain_sync**
> request_directory_domain_sync(domain_id, action, delay=delay)

Invoke full sync or delta sync for a specific domain, with additional delay in seconds if needed.  Stop sync will try to stop any pending sync if any to return to idle state.

Invoke full sync or delta sync for a specific domain, with additional delay in seconds if needed.  Stop sync will try to stop any pending sync if any to return to idle state.

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
action = 'action_example' # str | Sync type requested
delay = 789 # int | Request to execute the sync with some delay in seconds (optional)

try:
    # Invoke full sync or delta sync for a specific domain, with additional delay in seconds if needed.  Stop sync will try to stop any pending sync if any to return to idle state.
    api_instance.request_directory_domain_sync(domain_id, action, delay=delay)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->request_directory_domain_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **action** | **str**| Sync type requested | 
 **delay** | **int**| Request to execute the sync with some delay in seconds | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_directory_groups**
> DirectoryGroupListResults search_directory_groups(domain_id, filter_value, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Search for directory groups within a domain based on the substring of a distinguished name. (e.g. CN=User,DC=acme,DC=com) The search filter pattern can optionally support multiple (up to 100 maximum) search pattern separated by '|' (url encoded %7C). In this case, the search results will be returned as the union of all matching criteria. (e.g. CN=Ann,CN=Users,DC=acme,DC=com|CN=Bob,CN=Users,DC=acme,DC=com)

Search for directory groups within a domain based on the substring of a distinguished name. (e.g. CN=User,DC=acme,DC=com) The search filter pattern can optionally support multiple (up to 100 maximum) search pattern separated by '|' (url encoded %7C). In this case, the search results will be returned as the union of all matching criteria. (e.g. CN=Ann,CN=Users,DC=acme,DC=com|CN=Bob,CN=Users,DC=acme,DC=com)

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
filter_value = 'filter_value_example' # str | Name search filter value
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Search for directory groups within a domain based on the substring of a distinguished name. (e.g. CN=User,DC=acme,DC=com) The search filter pattern can optionally support multiple (up to 100 maximum) search pattern separated by '|' (url encoded %7C). In this case, the search results will be returned as the union of all matching criteria. (e.g. CN=Ann,CN=Users,DC=acme,DC=com|CN=Bob,CN=Users,DC=acme,DC=com)
    api_response = api_instance.search_directory_groups(domain_id, filter_value, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->search_directory_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **filter_value** | **str**| Name search filter value | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DirectoryGroupListResults**](DirectoryGroupListResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_directory_ldap_server**
> test_directory_ldap_server(domain_id, server_id, action)

Test a LDAP server connection for directory domain

The API tests a LDAP server connection for an already configured domain. If the connection is successful, the response will be HTTP status 200. Otherwise the response will be HTTP status 500 and corresponding error message will be returned.

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
server_id = 'server_id_example' # str | LDAP server identifier
action = 'action_example' # str | LDAP server test requested

try:
    # Test a LDAP server connection for directory domain
    api_instance.test_directory_ldap_server(domain_id, server_id, action)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->test_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **server_id** | **str**| LDAP server identifier | 
 **action** | **str**| LDAP server test requested | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_directory_domain**
> DirectoryDomain update_directory_domain(body, domain_id)

Update a directory domain

Update to any field in the directory domain will trigger a full sync

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryDomain() # DirectoryDomain | 
domain_id = 'domain_id_example' # str | Directory domain identifier

try:
    # Update a directory domain
    api_response = api_instance.update_directory_domain(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->update_directory_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryDomain**](DirectoryDomain.md)|  | 
 **domain_id** | **str**| Directory domain identifier | 

### Return type

[**DirectoryDomain**](DirectoryDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_directory_ldap_server**
> DirectoryLdapServer update_directory_ldap_server(body, domain_id, server_id)

Update a LDAP server for directory domain

Update a LDAP server for directory domain

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryLdapServer() # DirectoryLdapServer | 
domain_id = 'domain_id_example' # str | Directory domain identifier
server_id = 'server_id_example' # str | LDAP server identifier

try:
    # Update a LDAP server for directory domain
    api_response = api_instance.update_directory_ldap_server(body, domain_id, server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->update_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryLdapServer**](DirectoryLdapServer.md)|  | 
 **domain_id** | **str**| Directory domain identifier | 
 **server_id** | **str**| LDAP server identifier | 

### Return type

[**DirectoryLdapServer**](DirectoryLdapServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_directory_ldap_server**
> DirectoryLdapServerStatus verify_directory_ldap_server(body, action)

Test a directory domain LDAP server connectivity

This API tests a LDAP server connectivity before the actual domain or LDAP server is configured. If the connectivity is good, the response will be HTTP status 200. Otherwise the response will be HTTP status 500 and corresponding error message will be returned.

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
api_instance = swagger_client.ManagementPlaneApiDirectoryServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryLdapServer() # DirectoryLdapServer | 
action = 'action_example' # str | LDAP server test requested

try:
    # Test a directory domain LDAP server connectivity
    api_response = api_instance.verify_directory_ldap_server(body, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiDirectoryServiceApi->verify_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryLdapServer**](DirectoryLdapServer.md)|  | 
 **action** | **str**| LDAP server test requested | 

### Return type

[**DirectoryLdapServerStatus**](DirectoryLdapServerStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

