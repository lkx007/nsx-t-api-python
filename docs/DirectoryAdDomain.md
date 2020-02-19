# DirectoryAdDomain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldap_servers** | [**list[DirectoryLdapServer]**](DirectoryLdapServer.md) | Directory domain LDAP servers&#x27; information including host, name, port, protocol and so on. | 
**name** | **str** | Directory domain name which best describes the domain. It could be unique fqdn name or it could also be descriptive. There is no unique contraint for domain name among different domains. | 
**resource_type** | **str** | Domain resource type comes from multiple sub-classes extending this base class. For example, DirectoryAdDomain is one accepted resource_type. If there are more sub-classes defined, they will also be accepted resource_type. | 
**base_distinguished_name** | **str** | Each active directory domain has a domain naming context (NC), which contains domain-specific data. The root of this naming context is represented by a domain&#x27;s distinguished name (DN) and is typically referred to as the NC head. | 
**sync_settings** | [**DirectoryDomainSyncSettings**](DirectoryDomainSyncSettings.md) |  | [optional] 
**netbios_name** | **str** | NetBIOS names can contain all alphanumeric characters except for the certain disallowed characters. Names can contain a period, but names cannot start with a period. NetBIOS is similar to DNS in that it can serve as a directory service, but more limited as it has no provisions for a name hierarchy and names are limited to 15 characters. The netbios name is case insensitive and is stored in upper case regardless of input case. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

