# swagger_client.ManagementPlaneApiFabricVirtualMachinesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_virtual_machines**](ManagementPlaneApiFabricVirtualMachinesApi.md#list_virtual_machines) | **GET** /fabric/virtual-machines | Return the List of Virtual Machines
[**list_vm_tools_info**](ManagementPlaneApiFabricVirtualMachinesApi.md#list_vm_tools_info) | **GET** /fabric/virtual-machines/tools-info | Return the list of tools and agents installed in VMs.
[**update_virtual_machine_tags_update_tags**](ManagementPlaneApiFabricVirtualMachinesApi.md#update_virtual_machine_tags_update_tags) | **POST** /fabric/virtual-machines?action&#x3D;update_tags | Update tags applied to a virtual machine

# **list_virtual_machines**
> VirtualMachineListResult list_virtual_machines(cursor=cursor, display_name=display_name, external_id=external_id, host_id=host_id, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the List of Virtual Machines

Returns information about all virtual machines.

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
api_instance = swagger_client.ManagementPlaneApiFabricVirtualMachinesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
display_name = 'display_name_example' # str | Display Name of the virtual machine (optional)
external_id = 'external_id_example' # str | External id of the virtual machine (optional)
host_id = 'host_id_example' # str | Id of the host where this vif is located (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the List of Virtual Machines
    api_response = api_instance.list_virtual_machines(cursor=cursor, display_name=display_name, external_id=external_id, host_id=host_id, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricVirtualMachinesApi->list_virtual_machines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **display_name** | **str**| Display Name of the virtual machine | [optional] 
 **external_id** | **str**| External id of the virtual machine | [optional] 
 **host_id** | **str**| Id of the host where this vif is located | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**VirtualMachineListResult**](VirtualMachineListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vm_tools_info**
> VmToolsInfoListResult list_vm_tools_info(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the list of tools and agents installed in VMs.

This API returns the list of tools and agents installed in VMs.

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
api_instance = swagger_client.ManagementPlaneApiFabricVirtualMachinesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the list of tools and agents installed in VMs.
    api_response = api_instance.list_vm_tools_info(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricVirtualMachinesApi->list_vm_tools_info: %s\n" % e)
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

[**VmToolsInfoListResult**](VmToolsInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_machine_tags_update_tags**
> update_virtual_machine_tags_update_tags(body)

Update tags applied to a virtual machine

Update tags applied to the virtual machine. External id of the virtual machine will be specified in the request body. Request body should contain all the tags to be applied. To clear all tags, provide an empty list. User can apply maximum 25 tags on a virtual machine. The remaining 5 are reserved for system defined tags.

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
api_instance = swagger_client.ManagementPlaneApiFabricVirtualMachinesApi(swagger_client.ApiClient(configuration))
body = swagger_client.VirtualMachineTagUpdate() # VirtualMachineTagUpdate | 

try:
    # Update tags applied to a virtual machine
    api_instance.update_virtual_machine_tags_update_tags(body)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiFabricVirtualMachinesApi->update_virtual_machine_tags_update_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VirtualMachineTagUpdate**](VirtualMachineTagUpdate.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

