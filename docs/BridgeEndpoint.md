# BridgeEndpoint

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
**ha_enable** | **bool** | This field will not be used if an edge cluster is being used for the bridge endpoint  | [optional] [default to True]
**bridge_cluster_id** | **str** | This field will not be used if an edge cluster is being used for the bridge endpoint  | [optional] 
**vlan_transport_zone_id** | **str** | This field will not be used if a bridge cluster is being used for the bridge endpoint  | [optional] 
**bridge_endpoint_profile_id** | **str** | This field will not be used if a bridge cluster is being used for the bridge endpoint  | [optional] 
**uplink_teaming_policy_name** | **str** | This name has to be one of the switching uplink teaming policy names listed inside the TransportZone. If this field is not specified, bridge will use the first pnic in host-switch config. This field will not be used if a bridge cluster is being used for the bridge endpoint | [optional] 
**vlan_trunk_spec** | [**VlanTrunkSpec**](VlanTrunkSpec.md) |  | [optional] 
**vlan** | **int** | This property is used for VLAN specification of bridge endpoint. It&#x27;s mutually exclusive with &#x27;vlan_trunk_spec&#x27;, either &#x27;vlan&#x27; or &#x27;vlan_trunk_spec&#x27; should be specified.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

