# swagger_client.ManagementPlaneApiVpnStatisticsL2VpnSessionStatusApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_l2_vpn_session_status**](ManagementPlaneApiVpnStatisticsL2VpnSessionStatusApi.md#get_l2_vpn_session_status) | **GET** /vpn/l2vpn/sessions/{session-id}/status | Get L2VPN session status

# **get_l2_vpn_session_status**
> L2VPNSessionStatus get_l2_vpn_session_status(session_id, source=source)

Get L2VPN session status

Aggregated status of L2VPN session. Query parameter source=realtime|cached is supported.

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
api_instance = swagger_client.ManagementPlaneApiVpnStatisticsL2VpnSessionStatusApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get L2VPN session status
    api_response = api_instance.get_l2_vpn_session_status(session_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiVpnStatisticsL2VpnSessionStatusApi->get_l2_vpn_session_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**L2VPNSessionStatus**](L2VPNSessionStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

