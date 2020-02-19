# DirectoryLdapServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_owned** | **bool** | Indicates system owned resource | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**create_user** | **str** | ID of the user who created this resource | [optional] 
**protection** | **str** | Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite&#x3D;true. UNKNOWN - the _protection field could not be determined for this           entity.  | [optional] 
**create_time** | **int** | Timestamp of resource creation | [optional] 
**last_modified_time** | **int** | Timestamp of last modification | [optional] 
**last_modified_user** | **str** | ID of the user who last modified this resource | [optional] 
**id** | **str** | Unique identifier of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | [optional] 
**username** | **str** | Directory LDAP server connection user name. | [optional] 
**host** | **str** | Directory LDAP server DNS host name or ip address which is reachable by NSX manager to be connected and do object synchronization. | 
**protocol** | **str** | Directory LDAP server connection protocol which is either LDAP or LDAPS. | [optional] [default to 'LDAP']
**thumbprint** | **str** | Directory LDAP server certificate thumbprint used in secure LDAPS connection. | [optional] 
**password** | **str** | Directory LDAP server connection password. | [optional] 
**domain_name** | **str** | Directory domain name which best describes the domain. It could be unique fqdn name or it could also be descriptive. There is no unique contraint for domain name among different domains. | [optional] 
**port** | **int** | Directory LDAP server connection TCP/UDP port. | [optional] [default to 389]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

