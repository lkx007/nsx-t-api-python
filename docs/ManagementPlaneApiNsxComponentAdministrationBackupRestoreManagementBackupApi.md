# swagger_client.ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_backup_config**](ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi.md#configure_backup_config) | **PUT** /cluster/backups/config | Configure backup
[**get_backup_config**](ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi.md#get_backup_config) | **GET** /cluster/backups/config | Get backup configuration
[**get_backup_history**](ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi.md#get_backup_history) | **GET** /cluster/backups/history | Get backup history
[**get_backup_status**](ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi.md#get_backup_status) | **GET** /cluster/backups/status | Get backup status
[**get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint**](ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi.md#get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint) | **POST** /cluster/backups?action&#x3D;retrieve_ssh_fingerprint | Get ssh fingerprint of remote(backup) server
[**request_onetime_backup_backup_to_remote**](ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi.md#request_onetime_backup_backup_to_remote) | **POST** /cluster?action&#x3D;backup_to_remote | Request one-time backup
[**request_onetime_inventory_summary_summarize_inventory_to_remote**](ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi.md#request_onetime_inventory_summary_summarize_inventory_to_remote) | **POST** /cluster?action&#x3D;summarize_inventory_to_remote | Request one-time inventory summary.

# **configure_backup_config**
> BackupConfiguration configure_backup_config(body)

Configure backup

Configure file server and timers for automated backup. If secret fields are omitted (password, passphrase) then use the previously set value. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))
body = swagger_client.BackupConfiguration() # BackupConfiguration | 

try:
    # Configure backup
    api_response = api_instance.configure_backup_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi->configure_backup_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupConfiguration**](BackupConfiguration.md)|  | 

### Return type

[**BackupConfiguration**](BackupConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_config**
> BackupConfiguration get_backup_config()

Get backup configuration

Get a configuration of a file server and timers for automated backup. Fields that contain secrets (password, passphrase) are not returned. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))

try:
    # Get backup configuration
    api_response = api_instance.get_backup_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi->get_backup_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupConfiguration**](BackupConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_history**
> BackupOperationHistory get_backup_history()

Get backup history

Get history of previous backup operations 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))

try:
    # Get backup history
    api_response = api_instance.get_backup_history()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi->get_backup_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupOperationHistory**](BackupOperationHistory.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_status**
> CurrentBackupOperationStatus get_backup_status()

Get backup status

Get status of active backup operations 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))

try:
    # Get backup status
    api_response = api_instance.get_backup_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi->get_backup_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentBackupOperationStatus**](CurrentBackupOperationStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint**
> RemoteServerFingerprint get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint(body)

Get ssh fingerprint of remote(backup) server

Get SHA256 fingerprint of ECDSA key of remote server. The caller should independently verify that the key is trusted. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))
body = swagger_client.RemoteServerFingerprintRequest() # RemoteServerFingerprintRequest | 

try:
    # Get ssh fingerprint of remote(backup) server
    api_response = api_instance.get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi->get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteServerFingerprintRequest**](RemoteServerFingerprintRequest.md)|  | 

### Return type

[**RemoteServerFingerprint**](RemoteServerFingerprint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_onetime_backup_backup_to_remote**
> request_onetime_backup_backup_to_remote()

Request one-time backup

Request one-time backup. The backup will be uploaded using the same server configuration as for automatic backup. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))

try:
    # Request one-time backup
    api_instance.request_onetime_backup_backup_to_remote()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi->request_onetime_backup_backup_to_remote: %s\n" % e)
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

# **request_onetime_inventory_summary_summarize_inventory_to_remote**
> request_onetime_inventory_summary_summarize_inventory_to_remote()

Request one-time inventory summary.

Request one-time inventory summary. The backup will be uploaded using the same server configuration as for an automatic backup. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))

try:
    # Request one-time inventory summary.
    api_instance.request_onetime_inventory_summary_summarize_inventory_to_remote()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementBackupApi->request_onetime_inventory_summary_summarize_inventory_to_remote: %s\n" % e)
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

