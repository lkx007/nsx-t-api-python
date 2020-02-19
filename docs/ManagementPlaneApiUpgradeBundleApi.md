# swagger_client.ManagementPlaneApiUpgradeBundleApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_uc_upgrade_upgrade_uc**](ManagementPlaneApiUpgradeBundleApi.md#trigger_uc_upgrade_upgrade_uc) | **POST** /upgrade?action&#x3D;upgrade_uc | Upgrade the upgrade coordinator.

# **trigger_uc_upgrade_upgrade_uc**
> trigger_uc_upgrade_upgrade_uc()

Upgrade the upgrade coordinator.

Upgrade the upgrade coordinator module itself. This call is invoked after user uploads an upgrade bundle. Once this call is invoked, upgrade coordinator stops and gets restarted and target version upgrade coordinator module comes up after restart. 

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
api_instance = swagger_client.ManagementPlaneApiUpgradeBundleApi(swagger_client.ApiClient(configuration))

try:
    # Upgrade the upgrade coordinator.
    api_instance.trigger_uc_upgrade_upgrade_uc()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUpgradeBundleApi->trigger_uc_upgrade_upgrade_uc: %s\n" % e)
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

