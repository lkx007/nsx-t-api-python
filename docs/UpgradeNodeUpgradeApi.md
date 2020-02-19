# swagger_client.UpgradeNodeUpgradeApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_upgrade_task_**](UpgradeNodeUpgradeApi.md#execute_upgrade_task_) | **POST** /node/upgrade/performtask?action&#x3D;[^/]+ | Execute upgrade task
[**get_upgrade_progress_status**](UpgradeNodeUpgradeApi.md#get_upgrade_progress_status) | **GET** /node/upgrade/progress-status | Get upgrade progress status
[**get_upgrade_task_status**](UpgradeNodeUpgradeApi.md#get_upgrade_task_status) | **GET** /node/upgrade | Get upgrade task status

# **execute_upgrade_task_**
> UpgradeTaskProperties execute_upgrade_task_(body)

Execute upgrade task

Execute upgrade task. 

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
api_instance = swagger_client.UpgradeNodeUpgradeApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpgradeTaskProperties() # UpgradeTaskProperties | 

try:
    # Execute upgrade task
    api_response = api_instance.execute_upgrade_task_(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeNodeUpgradeApi->execute_upgrade_task_: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeTaskProperties**](UpgradeTaskProperties.md)|  | 

### Return type

[**UpgradeTaskProperties**](UpgradeTaskProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_progress_status**
> UpgradeProgressStatus get_upgrade_progress_status()

Get upgrade progress status

Get progress status of last upgrade step, if upgrade bundle is present. 

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
api_instance = swagger_client.UpgradeNodeUpgradeApi(swagger_client.ApiClient(configuration))

try:
    # Get upgrade progress status
    api_response = api_instance.get_upgrade_progress_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeNodeUpgradeApi->get_upgrade_progress_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeProgressStatus**](UpgradeProgressStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_task_status**
> UpgradeTaskProperties get_upgrade_task_status(bundle_name=bundle_name, upgrade_task_id=upgrade_task_id)

Get upgrade task status

Get upgrade task status for the given task of the given bundle. Both bundle_name and task_id must be provided, otherwise you will receive a 404 NOT FOUND response. 

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
api_instance = swagger_client.UpgradeNodeUpgradeApi(swagger_client.ApiClient(configuration))
bundle_name = 'bundle_name_example' # str | Bundle Name (optional)
upgrade_task_id = 'upgrade_task_id_example' # str | Upgrade Task ID (optional)

try:
    # Get upgrade task status
    api_response = api_instance.get_upgrade_task_status(bundle_name=bundle_name, upgrade_task_id=upgrade_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeNodeUpgradeApi->get_upgrade_task_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_name** | **str**| Bundle Name | [optional] 
 **upgrade_task_id** | **str**| Upgrade Task ID | [optional] 

### Return type

[**UpgradeTaskProperties**](UpgradeTaskProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

