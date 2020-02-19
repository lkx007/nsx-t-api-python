# swagger_client.ManagementPlaneApiUpgradeBundlesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_upgrade_bundle_upload_cancel_upload**](ManagementPlaneApiUpgradeBundlesApi.md#cancel_upgrade_bundle_upload_cancel_upload) | **POST** /upgrade/bundles/{bundle-id}?action&#x3D;cancel_upload | Cancel upgrade bundle upload
[**fetch_upgrade_bundle_from_url**](ManagementPlaneApiUpgradeBundlesApi.md#fetch_upgrade_bundle_from_url) | **POST** /upgrade/bundles | Fetch upgrade bundle from given url
[**get_upgrade_bundle_info**](ManagementPlaneApiUpgradeBundlesApi.md#get_upgrade_bundle_info) | **GET** /upgrade/bundles/{bundle-id} | Get uploaded upgrade bundle information
[**get_upgrade_bundle_upload_status**](ManagementPlaneApiUpgradeBundlesApi.md#get_upgrade_bundle_upload_status) | **GET** /upgrade/bundles/{bundle-id}/upload-status | Get uploaded upgrade bundle upload status
[**upload_upgrade_bundle_async_upload**](ManagementPlaneApiUpgradeBundlesApi.md#upload_upgrade_bundle_async_upload) | **POST** /upgrade/bundles?action&#x3D;upload | Upload upgrade bundle

# **cancel_upgrade_bundle_upload_cancel_upload**
> cancel_upgrade_bundle_upload_cancel_upload(bundle_id)

Cancel upgrade bundle upload

Cancel upload of upgrade bundle. This API works only when bundle upload is in-progress and will not work during post-processing of upgrade bundle. If bundle upload is in-progress, then the API call returns http OK response after cancelling the upload and deleting partially uploaded bundle. 

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
api_instance = swagger_client.ManagementPlaneApiUpgradeBundlesApi(swagger_client.ApiClient(configuration))
bundle_id = 'bundle_id_example' # str | 

try:
    # Cancel upgrade bundle upload
    api_instance.cancel_upgrade_bundle_upload_cancel_upload(bundle_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUpgradeBundlesApi->cancel_upgrade_bundle_upload_cancel_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_upgrade_bundle_from_url**
> UpgradeBundleId fetch_upgrade_bundle_from_url(body)

Fetch upgrade bundle from given url

Fetches the upgrade bundle from url. The call returns after fetch is initiated. Check status by periodically retrieving upgrade bundle upload status using GET /upgrade/bundles/<bundle-id>/upload-status. The upload is complete when the status is SUCCESS. 

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
api_instance = swagger_client.ManagementPlaneApiUpgradeBundlesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpgradeBundleFetchRequest() # UpgradeBundleFetchRequest | 

try:
    # Fetch upgrade bundle from given url
    api_response = api_instance.fetch_upgrade_bundle_from_url(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUpgradeBundlesApi->fetch_upgrade_bundle_from_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeBundleFetchRequest**](UpgradeBundleFetchRequest.md)|  | 

### Return type

[**UpgradeBundleId**](UpgradeBundleId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_bundle_info**
> UpgradeBundleInfo get_upgrade_bundle_info(bundle_id)

Get uploaded upgrade bundle information

Get uploaded upgrade bundle information 

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
api_instance = swagger_client.ManagementPlaneApiUpgradeBundlesApi(swagger_client.ApiClient(configuration))
bundle_id = 'bundle_id_example' # str | 

try:
    # Get uploaded upgrade bundle information
    api_response = api_instance.get_upgrade_bundle_info(bundle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUpgradeBundlesApi->get_upgrade_bundle_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  | 

### Return type

[**UpgradeBundleInfo**](UpgradeBundleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_bundle_upload_status**
> UpgradeBundleUploadStatus get_upgrade_bundle_upload_status(bundle_id)

Get uploaded upgrade bundle upload status

Get uploaded upgrade bundle upload status 

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
api_instance = swagger_client.ManagementPlaneApiUpgradeBundlesApi(swagger_client.ApiClient(configuration))
bundle_id = 'bundle_id_example' # str | 

try:
    # Get uploaded upgrade bundle upload status
    api_response = api_instance.get_upgrade_bundle_upload_status(bundle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUpgradeBundlesApi->get_upgrade_bundle_upload_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  | 

### Return type

[**UpgradeBundleUploadStatus**](UpgradeBundleUploadStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_upgrade_bundle_async_upload**
> UpgradeBundleId upload_upgrade_bundle_async_upload(file)

Upload upgrade bundle

Upload the upgrade bundle. This call returns after upload is completed. You can check bundle processing status periodically by retrieving upgrade bundle upload status to find out if the upload and processing is completed. 

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
api_instance = swagger_client.ManagementPlaneApiUpgradeBundlesApi(swagger_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # Upload upgrade bundle
    api_response = api_instance.upload_upgrade_bundle_async_upload(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiUpgradeBundlesApi->upload_upgrade_bundle_async_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

[**UpgradeBundleId**](UpgradeBundleId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

