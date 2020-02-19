# swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_crl_import**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#add_crl_import) | **POST** /trust-management/crls?action&#x3D;import | Add a New Certificate Revocation List
[**create_crl_distribution_point**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#create_crl_distribution_point) | **POST** /trust-management/crl-distribution-points | Create a Crl Distribution Point
[**delete_crl**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#delete_crl) | **DELETE** /trust-management/crls/{crl-id} | Delete a CRL
[**delete_crl_distribution_point**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#delete_crl_distribution_point) | **DELETE** /trust-management/crl-distribution-points/{crl-distribution-point-id} | Delete a CrlDistributionPoint
[**get_crl**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#get_crl) | **GET** /trust-management/crls/{crl-id} | Show CRL Data for the Given CRL ID
[**get_crl_distribution_point**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#get_crl_distribution_point) | **GET** /trust-management/crl-distribution-points/{crl-distribution-point-id} | Return the CrlDistributionPoint with &lt;crl-distribution-point-id&gt;
[**get_crl_distribution_point_pem**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#get_crl_distribution_point_pem) | **POST** /trust-management/crl-distribution-points/pem-file | Return stored CRL in PEM format
[**get_crl_distribution_point_status**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#get_crl_distribution_point_status) | **GET** /trust-management/crl-distribution-points/{crl-distribution-point-id}/status | Return the status of the CrlDistributionPoint
[**get_crls**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#get_crls) | **GET** /trust-management/crls | Return All Added CRLs
[**get_trust_objects**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#get_trust_objects) | **GET** /trust-management | Return the Properties of a Trust Manager
[**list_crl_distribution_points**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#list_crl_distribution_points) | **GET** /trust-management/crl-distribution-points | Return the list of CrlDistributionPoints
[**update_crl**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#update_crl) | **PUT** /trust-management/crls/{crl-id} | Update CRL for the Given CRL ID
[**update_crl_distribution_point**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi.md#update_crl_distribution_point) | **PUT** /trust-management/crl-distribution-points/{crl-distribution-point-id} | Update CrlDistributionPoint with &lt;crl-distribution-point-id&gt; This allows updating the ManagedResource fields. 

# **add_crl_import**
> CrlList add_crl_import(body)

Add a New Certificate Revocation List

Adds a new certificate revocation list (CRL). The CRL is used to verify the client certificate status against the revocation lists published by the CA. For this reason, the administrator needs to add the CRL in certificate repository as well. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
body = swagger_client.CrlObjectData() # CrlObjectData | 

try:
    # Add a New Certificate Revocation List
    api_response = api_instance.add_crl_import(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->add_crl_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrlObjectData**](CrlObjectData.md)|  | 

### Return type

[**CrlList**](CrlList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_crl_distribution_point**
> CrlDistributionPoint create_crl_distribution_point(body)

Create a Crl Distribution Point

Create an entity that will represent a Crl Distribution Point 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
body = swagger_client.CrlDistributionPoint() # CrlDistributionPoint | 

try:
    # Create a Crl Distribution Point
    api_response = api_instance.create_crl_distribution_point(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->create_crl_distribution_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrlDistributionPoint**](CrlDistributionPoint.md)|  | 

### Return type

[**CrlDistributionPoint**](CrlDistributionPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_crl**
> delete_crl(crl_id)

Delete a CRL

Deletes an existing CRL.

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
crl_id = 'crl_id_example' # str | ID of CRL to delete

try:
    # Delete a CRL
    api_instance.delete_crl(crl_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->delete_crl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_id** | **str**| ID of CRL to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_crl_distribution_point**
> delete_crl_distribution_point(crl_distribution_point_id)

Delete a CrlDistributionPoint

Delete a CrlDistributionPoint. It does not delete the actual CRL. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
crl_distribution_point_id = 'crl_distribution_point_id_example' # str | Unique id of the CrlDistributionPoint to delete

try:
    # Delete a CrlDistributionPoint
    api_instance.delete_crl_distribution_point(crl_distribution_point_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->delete_crl_distribution_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_distribution_point_id** | **str**| Unique id of the CrlDistributionPoint to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crl**
> Crl get_crl(crl_id, details=details)

Show CRL Data for the Given CRL ID

Returns information about the specified CRL. For additional information, include the ?details=true modifier at the end of the request URI. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
crl_id = 'crl_id_example' # str | ID of CRL to read
details = true # bool | whether to expand the pem data and show all its details (optional)

try:
    # Show CRL Data for the Given CRL ID
    api_response = api_instance.get_crl(crl_id, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->get_crl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_id** | **str**| ID of CRL to read | 
 **details** | **bool**| whether to expand the pem data and show all its details | [optional] 

### Return type

[**Crl**](Crl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crl_distribution_point**
> CrlDistributionPoint get_crl_distribution_point(crl_distribution_point_id)

Return the CrlDistributionPoint with <crl-distribution-point-id>

Return the CrlDistributionPoint with <crl-distribution-point-id>

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
crl_distribution_point_id = 'crl_distribution_point_id_example' # str | 

try:
    # Return the CrlDistributionPoint with <crl-distribution-point-id>
    api_response = api_instance.get_crl_distribution_point(crl_distribution_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->get_crl_distribution_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_distribution_point_id** | **str**|  | 

### Return type

[**CrlDistributionPoint**](CrlDistributionPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crl_distribution_point_pem**
> str get_crl_distribution_point_pem(body)

Return stored CRL in PEM format

Return stored CRL in PEM format

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
body = swagger_client.CrlPemRequestType() # CrlPemRequestType | 

try:
    # Return stored CRL in PEM format
    api_response = api_instance.get_crl_distribution_point_pem(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->get_crl_distribution_point_pem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrlPemRequestType**](CrlPemRequestType.md)|  | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crl_distribution_point_status**
> CrlDistributionPointStatus get_crl_distribution_point_status(crl_distribution_point_id)

Return the status of the CrlDistributionPoint

Return the status of the CrlDistributionPoint

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
crl_distribution_point_id = 'crl_distribution_point_id_example' # str | 

try:
    # Return the status of the CrlDistributionPoint
    api_response = api_instance.get_crl_distribution_point_status(crl_distribution_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->get_crl_distribution_point_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_distribution_point_id** | **str**|  | 

### Return type

[**CrlDistributionPointStatus**](CrlDistributionPointStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crls**
> CrlList get_crls(cursor=cursor, details=details, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

Return All Added CRLs

Returns information about all CRLs. For additional information, include the ?details=true modifier at the end of the request URI. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
details = true # bool | whether to expand the pem data and show all its details (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | Type of certificate to return (optional)

try:
    # Return All Added CRLs
    api_response = api_instance.get_crls(cursor=cursor, details=details, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->get_crls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **details** | **bool**| whether to expand the pem data and show all its details | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **type** | **str**| Type of certificate to return | [optional] 

### Return type

[**CrlList**](CrlList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trust_objects**
> TrustManagementData get_trust_objects()

Return the Properties of a Trust Manager

Returns information about the supported algorithms and key sizes.

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))

try:
    # Return the Properties of a Trust Manager
    api_response = api_instance.get_trust_objects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->get_trust_objects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TrustManagementData**](TrustManagementData.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crl_distribution_points**
> CrlDistributionPointList list_crl_distribution_points(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the list of CrlDistributionPoints

Return the list of CrlDistributionPoints

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the list of CrlDistributionPoints
    api_response = api_instance.list_crl_distribution_points(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->list_crl_distribution_points: %s\n" % e)
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

[**CrlDistributionPointList**](CrlDistributionPointList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crl**
> Crl update_crl(body, crl_id)

Update CRL for the Given CRL ID

Updates an existing CRL.

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
body = swagger_client.Crl() # Crl | 
crl_id = 'crl_id_example' # str | ID of CRL to update

try:
    # Update CRL for the Given CRL ID
    api_response = api_instance.update_crl(body, crl_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->update_crl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Crl**](Crl.md)|  | 
 **crl_id** | **str**| ID of CRL to update | 

### Return type

[**Crl**](Crl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crl_distribution_point**
> CrlDistributionPoint update_crl_distribution_point(body, crl_distribution_point_id)

Update CrlDistributionPoint with <crl-distribution-point-id> This allows updating the ManagedResource fields. 

Update CrlDistributionPoint with <crl-distribution-point-id> This allows updating the ManagedResource fields. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi(swagger_client.ApiClient(configuration))
body = swagger_client.CrlDistributionPoint() # CrlDistributionPoint | 
crl_distribution_point_id = 'crl_distribution_point_id_example' # str | 

try:
    # Update CrlDistributionPoint with <crl-distribution-point-id> This allows updating the ManagedResource fields. 
    api_response = api_instance.update_crl_distribution_point(body, crl_distribution_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCrlApi->update_crl_distribution_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrlDistributionPoint**](CrlDistributionPoint.md)|  | 
 **crl_distribution_point_id** | **str**|  | 

### Return type

[**CrlDistributionPoint**](CrlDistributionPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

