# MetadataProxy

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
**secret** | **str** | secret to access metadata server | [optional] 
**metadata_server_ca_ids** | **list[str]** | The CAs referenced here must be uploaded to the truststore using the API POST /api/v1/trust-management/certificates?action&#x3D;import. User needs to ensure a correct CA for this metedata server is used. The REST API can not detect a wrong CA which was used to verify a different server. If the Metadata Proxy reports an ERROR or NO_BACKUP status, user can check the metadata proxy log at transport node for a possible CA issue.  | [optional] 
**edge_cluster_member_indexes** | **list[int]** | If none is provided, the NSX will auto-select two edge-nodes from the given edge cluster. If user provides only one edge node, there will be no HA support.  | [optional] 
**crypto_protocols** | **list[str]** | The cryptographic protocols listed here are supported by the metadata proxy. The TLSv1.1 and TLSv1.2 are supported by default.  | [optional] 
**metadata_server_url** | **str** | The URL in format scheme://host:port/path. Please note, the scheme supports only http and https as of now, port supports range 3000 - 9000, inclusive.  | 
**attached_logical_port_id** | **str** | id of attached logical port | [optional] 
**enable_standby_relocation** | **bool** | Flag to enable the auto-relocation of standby Metadata Proxy in case of edge node failure. Only tier 1 and auto placed Metadata Proxy are considered for the relocation.  | [optional] [default to False]
**edge_cluster_id** | **str** | edge cluster uuid | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

