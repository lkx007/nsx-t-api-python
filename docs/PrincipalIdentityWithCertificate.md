# PrincipalIdentityWithCertificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_protected** | **bool** | Indicator whether the entities created by this principal should be protected | [optional] 
**role** | **str** | Role | [optional] 
**name** | **str** | Name of the principal | 
**permission_group** | **str** | Use the &#x27;role&#x27; field instead and pass in &#x27;auditor&#x27; for read_only_api_users or &#x27;enterprise_admin&#x27; for the others. | [optional] 
**certificate_id** | **str** | Id of the stored certificate. When used with the deprecated POST /trust-management/principal-identities API this field is required. | [optional] 
**node_id** | **str** | Unique node-id of a principal | 
**certificate_pem** | **str** | PEM encoding of the new certificate | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

