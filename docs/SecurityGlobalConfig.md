# SecurityGlobalConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Valid Global configuration types | 
**ca_signed_only** | **bool** | When this flag is set to true (for NDcPP compliance) only ca-signed certificates will be allowed to be applied as server certificates. | [optional] [default to False]
**crl_checking_enabled** | **bool** | When this flag is set to true, during certificate checking the CRL is fetched and checked whether the certificate is revoked or not. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

