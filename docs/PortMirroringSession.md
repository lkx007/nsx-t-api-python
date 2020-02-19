# PortMirroringSession

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
**direction** | **str** | Port mirroring session direction | 
**mirror_sources** | [**list[MirrorSource]**](MirrorSource.md) | Mirror sources | 
**encapsulation_vlan_id** | **int** | Only for Remote SPAN Port Mirror. | [optional] 
**session_type** | **str** | If this property is unset, this session will be treated as LocalPortMirrorSession.  | [optional] [default to 'LocalPortMirrorSession']
**snap_length** | **int** | If this property is set, the packet will be truncated to the provided length. If this property is unset, entire packet will be mirrored.  | [optional] 
**port_mirroring_filters** | [**list[PortMirroringFilter]**](PortMirroringFilter.md) | An array of 5-tuples used to filter packets for the mirror session, if not provided, all the packets will be mirrored. | [optional] 
**preserve_original_vlan** | **bool** | Only for Remote SPAN Port Mirror. Whether to preserve original VLAN. | [optional] [default to False]
**mirror_destination** | [**MirrorDestination**](MirrorDestination.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

