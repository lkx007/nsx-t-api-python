# LogicalPort

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
**logical_switch_id** | **str** | Id of the Logical switch that this port belongs to. | 
**init_state** | **str** | Set initial state when a new logical port is created. &#x27;UNBLOCKED_VLAN&#x27; means new port will be unblocked on traffic in creation, also VLAN will be set with corresponding logical switch setting. This port setting can only be configured at port creation (POST), and cannot be modified.  | [optional] 
**switching_profile_ids** | [**list[SwitchingProfileTypeIdEntry]**](SwitchingProfileTypeIdEntry.md) |  | [optional] 
**attachment** | [**LogicalPortAttachment**](LogicalPortAttachment.md) |  | [optional] 
**admin_state** | **str** | Represents Desired state of the logical port | 
**extra_configs** | [**list[ExtraConfig]**](ExtraConfig.md) | This property could be used for vendor specific configuration in key value string pairs. Logical port setting will override logical switch setting if the same key was set on both logical switch and logical port.  | [optional] 
**address_bindings** | [**list[PacketAddressClassifier]**](PacketAddressClassifier.md) | Each address binding must contain both an IPElement and MAC address. VLAN ID is optional. This binding configuration can be used by features such as spoof-guard and overrides any discovered bindings. Any non unique entries are deduplicated to generate a unique set of address bindings and then stored. For IPv6 addresses, a subnet address cannot have host bits set. A maximum of 128 unique address bindings is allowed per port.  | [optional] 
**ignore_address_bindings** | [**list[PacketAddressClassifier]**](PacketAddressClassifier.md) | IP Discovery module uses various mechanisms to discover address bindings being used on each port. If a user would like to ignore any specific discovered address bindings or prevent the discovery of a particular set of discovered bindings, then those address bindings can be provided here. Currently IP range in CIDR format is not supported.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

