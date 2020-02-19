# LbHttpSslCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverse** | **bool** | A flag to indicate whether reverse the match result of this condition | [optional] [default to False]
**type** | **str** | Type of load balancer rule condition | 
**client_supported_ssl_ciphers** | **list[str]** | Cipher list which supported by client | [optional] 
**client_certificate_issuer_dn** | [**LbClientCertificateIssuerDnCondition**](LbClientCertificateIssuerDnCondition.md) |  | [optional] 
**client_certificate_subject_dn** | [**LbClientCertificateSubjectDnCondition**](LbClientCertificateSubjectDnCondition.md) |  | [optional] 
**used_ssl_cipher** | **str** | Cipher used for an established SSL connection | [optional] 
**session_reused** | **str** | The type of SSL session reused | [optional] [default to 'IGNORE']
**used_protocol** | **str** | Protocol of an established SSL connection | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

