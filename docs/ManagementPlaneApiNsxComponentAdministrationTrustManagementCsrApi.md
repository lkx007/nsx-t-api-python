# swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_csr**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi.md#delete_csr) | **DELETE** /trust-management/csrs/{csr-id} | Delete a CSR
[**generate_csr**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi.md#generate_csr) | **POST** /trust-management/csrs | Generate a New Certificate Signing Request
[**get_csr**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi.md#get_csr) | **GET** /trust-management/csrs/{csr-id} | Show CSR Data for the Given CSR ID
[**get_csr_pem**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi.md#get_csr_pem) | **GET** /trust-management/csrs/{csr-id}/pem-file | Get CSR PEM File for the Given CSR ID
[**get_csrs**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi.md#get_csrs) | **GET** /trust-management/csrs | Return All the Generated CSRs
[**import_certificate_import**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi.md#import_certificate_import) | **POST** /trust-management/csrs/{csr-id}?action&#x3D;import | Import a Certificate Associated with an Approved CSR
[**self_sign_certificate_self_sign**](ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi.md#self_sign_certificate_self_sign) | **POST** /trust-management/csrs/{csr-id}?action&#x3D;self_sign | Self-Sign the CSR

# **delete_csr**
> delete_csr(csr_id)

Delete a CSR

Removes a specified CSR. If a CSR is not used for verification, you can delete it. Note that the CSR import and upload POST actions automatically delete the associated CSR. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi(swagger_client.ApiClient(configuration))
csr_id = 'csr_id_example' # str | ID of CSR to delete

try:
    # Delete a CSR
    api_instance.delete_csr(csr_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi->delete_csr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| ID of CSR to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_csr**
> Csr generate_csr(body)

Generate a New Certificate Signing Request

Creates a new certificate signing request (CSR). A CSR is encrypted text that contains information about your organization (organization name, country, and so on) and your Web server's public key, which is a public certificate the is generated on the server that can be used to forward this request to a certificate authority (CA). A private key is also usually created at the same time as the CSR. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi(swagger_client.ApiClient(configuration))
body = swagger_client.Csr() # Csr | 

try:
    # Generate a New Certificate Signing Request
    api_response = api_instance.generate_csr(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi->generate_csr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Csr**](Csr.md)|  | 

### Return type

[**Csr**](Csr.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr**
> Csr get_csr(csr_id)

Show CSR Data for the Given CSR ID

Returns information about the specified CSR.

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi(swagger_client.ApiClient(configuration))
csr_id = 'csr_id_example' # str | ID of CSR to read

try:
    # Show CSR Data for the Given CSR ID
    api_response = api_instance.get_csr(csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi->get_csr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| ID of CSR to read | 

### Return type

[**Csr**](Csr.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr_pem**
> str get_csr_pem(csr_id)

Get CSR PEM File for the Given CSR ID

Downloads the CSR PEM file for a specified CSR. Clients must include an Accept: text/plain request header.

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi(swagger_client.ApiClient(configuration))
csr_id = 'csr_id_example' # str | ID of CSR to read

try:
    # Get CSR PEM File for the Given CSR ID
    api_response = api_instance.get_csr_pem(csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi->get_csr_pem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| ID of CSR to read | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csrs**
> CsrList get_csrs(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return All the Generated CSRs

Returns information about all of the CSRs that have been created.

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return All the Generated CSRs
    api_response = api_instance.get_csrs(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi->get_csrs: %s\n" % e)
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

[**CsrList**](CsrList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_certificate_import**
> CertificateList import_certificate_import(body, csr_id)

Import a Certificate Associated with an Approved CSR

Imports a certificate authority (CA)-signed certificate for a CSR. This action links the certificate to the private key created by the CSR. The pem_encoded string in the request body is the signed certificate provided by your CA in response to the CSR that you provide to them. The import POST action automatically deletes the associated CSR. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrustObjectData() # TrustObjectData | 
csr_id = 'csr_id_example' # str | CSR this certificate is associated with

try:
    # Import a Certificate Associated with an Approved CSR
    api_response = api_instance.import_certificate_import(body, csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi->import_certificate_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrustObjectData**](TrustObjectData.md)|  | 
 **csr_id** | **str**| CSR this certificate is associated with | 

### Return type

[**CertificateList**](CertificateList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_sign_certificate_self_sign**
> Certificate self_sign_certificate_self_sign(csr_id, days_valid)

Self-Sign the CSR

Self-signs the previously generated CSR. This action is similar to the import certificate action, but instead of using a public certificate signed by a CA, the self_sign POST action uses a certificate that is signed with NSX's own private key. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi(swagger_client.ApiClient(configuration))
csr_id = 'csr_id_example' # str | CSR this certificate is associated with
days_valid = 789 # int | Number of days the certificate will be valid, default 10 years

try:
    # Self-Sign the CSR
    api_response = api_instance.self_sign_certificate_self_sign(csr_id, days_valid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementCsrApi->self_sign_certificate_self_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| CSR this certificate is associated with | 
 **days_valid** | **int**| Number of days the certificate will be valid, default 10 years | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

