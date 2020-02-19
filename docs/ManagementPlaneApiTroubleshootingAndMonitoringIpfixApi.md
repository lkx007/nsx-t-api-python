# swagger_client.ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ipfix_obs_points**](ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi.md#get_ipfix_obs_points) | **GET** /ipfix-obs-points | Get the list of IPFIX observation points
[**get_switch_ipfix_config**](ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi.md#get_switch_ipfix_config) | **GET** /ipfix-obs-points/switch-global | Read global switch IPFIX export configuration
[**update_switch_ipfix_config**](ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi.md#update_switch_ipfix_config) | **PUT** /ipfix-obs-points/switch-global | Update global switch IPFIX export configuration

# **get_ipfix_obs_points**
> IpfixObsPointsListResult get_ipfix_obs_points()

Get the list of IPFIX observation points

Deprecated - Please use /ipfix-profiles for switch IPFIX profile and /ipfix-collector-profiles for IPFIX collector profile. 

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
api_instance = swagger_client.ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi(swagger_client.ApiClient(configuration))

try:
    # Get the list of IPFIX observation points
    api_response = api_instance.get_ipfix_obs_points()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi->get_ipfix_obs_points: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IpfixObsPointsListResult**](IpfixObsPointsListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_switch_ipfix_config**
> IpfixObsPointConfig get_switch_ipfix_config()

Read global switch IPFIX export configuration

Deprecated - Please use /ipfix-profiles/<ipfix-profile-id> for switch IPFIX profile and /ipfix-collector-profiles/<ipfix-collector-profile-id> for IPFIX collector profile. 

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
api_instance = swagger_client.ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi(swagger_client.ApiClient(configuration))

try:
    # Read global switch IPFIX export configuration
    api_response = api_instance.get_switch_ipfix_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi->get_switch_ipfix_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IpfixObsPointConfig**](IpfixObsPointConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_switch_ipfix_config**
> IpfixObsPointConfig update_switch_ipfix_config(body)

Update global switch IPFIX export configuration

Deprecated - Please use /ipfix-profiles/<ipfix-profile-id> for switch IPFIX profile and /ipfix-collector-profiles/<ipfix-collector-profile-id> for IPFIX collector profile. 

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
api_instance = swagger_client.ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixObsPointConfig() # IpfixObsPointConfig | 

try:
    # Update global switch IPFIX export configuration
    api_response = api_instance.update_switch_ipfix_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiTroubleshootingAndMonitoringIpfixApi->update_switch_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixObsPointConfig**](IpfixObsPointConfig.md)|  | 

### Return type

[**IpfixObsPointConfig**](IpfixObsPointConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

