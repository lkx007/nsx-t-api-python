# swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_principal_identity**](ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi.md#delete_principal_identity) | **DELETE** /trust-management/principal-identities/{principal-identity-id} | Delete a principal identity
[**get_principal_identities**](ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi.md#get_principal_identities) | **GET** /trust-management/principal-identities | Return the list of principal identities
[**get_principal_identity**](ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi.md#get_principal_identity) | **GET** /trust-management/principal-identities/{principal-identity-id} | Get a Principal Identity
[**register_principal_identity**](ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi.md#register_principal_identity) | **POST** /trust-management/principal-identities | Register a name-certificate combination.
[**register_principal_identity_with_certificate**](ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi.md#register_principal_identity_with_certificate) | **POST** /trust-management/principal-identities/with-certificate | Register a name-certificate combination.
[**update_principal_identity_certificate_update_certificate**](ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi.md#update_principal_identity_certificate_update_certificate) | **POST** /trust-management/principal-identities?action&#x3D;update_certificate | Update a Principal Identity&#x27;s certificate

# **delete_principal_identity**
> delete_principal_identity(principal_identity_id)

Delete a principal identity

Delete a principal identity. It does not delete the certificate. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
principal_identity_id = 'principal_identity_id_example' # str | Unique id of the principal identity to delete

try:
    # Delete a principal identity
    api_instance.delete_principal_identity(principal_identity_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi->delete_principal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_identity_id** | **str**| Unique id of the principal identity to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_principal_identities**
> PrincipalIdentityList get_principal_identities()

Return the list of principal identities

Returns the list of principals registered with a certificate.

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))

try:
    # Return the list of principal identities
    api_response = api_instance.get_principal_identities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi->get_principal_identities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrincipalIdentityList**](PrincipalIdentityList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_principal_identity**
> PrincipalIdentity get_principal_identity(principal_identity_id)

Get a Principal Identity

Get a stored principal identity 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
principal_identity_id = 'principal_identity_id_example' # str | ID of Principal Identity to get

try:
    # Get a Principal Identity
    api_response = api_instance.get_principal_identity(principal_identity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi->get_principal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_identity_id** | **str**| ID of Principal Identity to get | 

### Return type

[**PrincipalIdentity**](PrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_principal_identity**
> PrincipalIdentity register_principal_identity(body)

Register a name-certificate combination.

Associates a principal's name with a certificate that is used to authenticate. Deprecated, use POST /trust-management/principal-identities/with-certificate instead. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
body = swagger_client.PrincipalIdentity() # PrincipalIdentity | 

try:
    # Register a name-certificate combination.
    api_response = api_instance.register_principal_identity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi->register_principal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrincipalIdentity**](PrincipalIdentity.md)|  | 

### Return type

[**PrincipalIdentity**](PrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_principal_identity_with_certificate**
> PrincipalIdentity register_principal_identity_with_certificate(body)

Register a name-certificate combination.

Create a Principal Identity with a new, unused, certificate. 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
body = swagger_client.PrincipalIdentityWithCertificate() # PrincipalIdentityWithCertificate | 

try:
    # Register a name-certificate combination.
    api_response = api_instance.register_principal_identity_with_certificate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi->register_principal_identity_with_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrincipalIdentityWithCertificate**](PrincipalIdentityWithCertificate.md)|  | 

### Return type

[**PrincipalIdentity**](PrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_principal_identity_certificate_update_certificate**
> PrincipalIdentity update_principal_identity_certificate_update_certificate(body)

Update a Principal Identity's certificate

Update a principal identity's certificate 

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
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePrincipalIdentityCertificateRequest() # UpdatePrincipalIdentityCertificateRequest | 

try:
    # Update a Principal Identity's certificate
    api_response = api_instance.update_principal_identity_certificate_update_certificate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationTrustManagementPrincipalIdentityApi->update_principal_identity_certificate_update_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePrincipalIdentityCertificateRequest**](UpdatePrincipalIdentityCertificateRequest.md)|  | 

### Return type

[**PrincipalIdentity**](PrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

