# swagger_client.ManagementPlaneApiVpnIpsecLocalEndpointsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_sec_vpn_local_endpoint**](ManagementPlaneApiVpnIpsecLocalEndpointsApi.md#create_ip_sec_vpn_local_endpoint) | **POST** /vpn/ipsec/local-endpoints | Create custom local endpoint
[**delete_ip_sec_vpn_local_endpoint**](ManagementPlaneApiVpnIpsecLocalEndpointsApi.md#delete_ip_sec_vpn_local_endpoint) | **DELETE** /vpn/ipsec/local-endpoints/{ipsec-vpn-local-endpoint-id} | Delete custom IPSec local endpoint
[**get_ip_sec_vpn_local_endpoint**](ManagementPlaneApiVpnIpsecLocalEndpointsApi.md#get_ip_sec_vpn_local_endpoint) | **GET** /vpn/ipsec/local-endpoints/{ipsec-vpn-local-endpoint-id} | Get custom IPSec local endpoint
[**list_ip_sec_vpn_local_endpoints**](ManagementPlaneApiVpnIpsecLocalEndpointsApi.md#list_ip_sec_vpn_local_endpoints) | **GET** /vpn/ipsec/local-endpoints | Get IPSec local endpoint list result
[**update_ip_sec_vpn_local_endpoint**](ManagementPlaneApiVpnIpsecLocalEndpointsApi.md#update_ip_sec_vpn_local_endpoint) | **PUT** /vpn/ipsec/local-endpoints/{ipsec-vpn-local-endpoint-id} | Edit custom IPSec local endpoint

# **create_ip_sec_vpn_local_endpoint**
> IPSecVPNLocalEndpoint create_ip_sec_vpn_local_endpoint(body)

Create custom local endpoint

Create custom IPSec local endpoint.

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
api_instance = swagger_client.ManagementPlaneApiVpnIpsecLocalEndpointsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNLocalEndpoint() # IPSecVPNLocalEndpoint | 

try:
    # Create custom local endpoint
    api_response = api_instance.create_ip_sec_vpn_local_endpoint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiVpnIpsecLocalEndpointsApi->create_ip_sec_vpn_local_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)|  | 

### Return type

[**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_sec_vpn_local_endpoint**
> delete_ip_sec_vpn_local_endpoint(ipsec_vpn_local_endpoint_id, force=force)

Delete custom IPSec local endpoint

Delete custom IPSec local endpoint.

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
api_instance = swagger_client.ManagementPlaneApiVpnIpsecLocalEndpointsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_local_endpoint_id = 'ipsec_vpn_local_endpoint_id_example' # str | 
force = true # bool | Force delete the resource even if it is being used somewhere  (optional)

try:
    # Delete custom IPSec local endpoint
    api_instance.delete_ip_sec_vpn_local_endpoint(ipsec_vpn_local_endpoint_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiVpnIpsecLocalEndpointsApi->delete_ip_sec_vpn_local_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_local_endpoint_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpn_local_endpoint**
> IPSecVPNLocalEndpoint get_ip_sec_vpn_local_endpoint(ipsec_vpn_local_endpoint_id)

Get custom IPSec local endpoint

Get custom IPSec local endpoint.

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
api_instance = swagger_client.ManagementPlaneApiVpnIpsecLocalEndpointsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_local_endpoint_id = 'ipsec_vpn_local_endpoint_id_example' # str | 

try:
    # Get custom IPSec local endpoint
    api_response = api_instance.get_ip_sec_vpn_local_endpoint(ipsec_vpn_local_endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiVpnIpsecLocalEndpointsApi->get_ip_sec_vpn_local_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_local_endpoint_id** | **str**|  | 

### Return type

[**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_sec_vpn_local_endpoints**
> IPSecVPNLocalEndpointListResult list_ip_sec_vpn_local_endpoints(cursor=cursor, included_fields=included_fields, ipsec_vpn_service_id=ipsec_vpn_service_id, logical_router_id=logical_router_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get IPSec local endpoint list result

Get paginated list of all local endpoints.

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
api_instance = swagger_client.ManagementPlaneApiVpnIpsecLocalEndpointsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
ipsec_vpn_service_id = 'ipsec_vpn_service_id_example' # str | Id of the IPSec VPN service (optional)
logical_router_id = 'logical_router_id_example' # str | Id of logical router (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get IPSec local endpoint list result
    api_response = api_instance.list_ip_sec_vpn_local_endpoints(cursor=cursor, included_fields=included_fields, ipsec_vpn_service_id=ipsec_vpn_service_id, logical_router_id=logical_router_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiVpnIpsecLocalEndpointsApi->list_ip_sec_vpn_local_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **ipsec_vpn_service_id** | **str**| Id of the IPSec VPN service | [optional] 
 **logical_router_id** | **str**| Id of logical router | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IPSecVPNLocalEndpointListResult**](IPSecVPNLocalEndpointListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_sec_vpn_local_endpoint**
> IPSecVPNLocalEndpoint update_ip_sec_vpn_local_endpoint(body, ipsec_vpn_local_endpoint_id)

Edit custom IPSec local endpoint

Edit custom IPSec local endpoint.

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
api_instance = swagger_client.ManagementPlaneApiVpnIpsecLocalEndpointsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNLocalEndpoint() # IPSecVPNLocalEndpoint | 
ipsec_vpn_local_endpoint_id = 'ipsec_vpn_local_endpoint_id_example' # str | 

try:
    # Edit custom IPSec local endpoint
    api_response = api_instance.update_ip_sec_vpn_local_endpoint(body, ipsec_vpn_local_endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiVpnIpsecLocalEndpointsApi->update_ip_sec_vpn_local_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)|  | 
 **ipsec_vpn_local_endpoint_id** | **str**|  | 

### Return type

[**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

