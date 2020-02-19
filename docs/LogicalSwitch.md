# LogicalSwitch

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
**switch_type** | **str** | This field indicates purpose of a LogicalSwitch. It is set by manager internally or user can provide this field. If not set, DEFAULT type is assigned. NSX components can use this field to create LogicalSwitch that provides component specific functionality. DEFAULT type LogicalSwitches are created for basic L2 connectivity by API users. SERVICE_PLANE type LogicalSwitches are system created service plane LogicalSwitches for Service Insertion service. User can not create SERVICE_PLANE type of LogicalSwitch. DHCP_RELAY type LogicalSwitches are created by external user like Policy with special permissions or by system and will be treated as internal LogicalSwitches. Such LogicalSwitch will not be exposed to vSphere user.  | [optional] 
**replication_mode** | **str** | Replication mode of the Logical Switch | [optional] 
**extra_configs** | [**list[ExtraConfig]**](ExtraConfig.md) | This property could be used for vendor specific configuration in key value string pairs, the setting in extra_configs will be automatically inheritted by logical ports in the logical switch.  | [optional] 
**uplink_teaming_policy_name** | **str** | This name has to be one of the switching uplink teaming policy names listed inside the logical switch&#x27;s TransportZone. If this field is not specified, the logical switch will not have a teaming policy associated with it and the host switch&#x27;s default teaming policy will be used. | [optional] 
**transport_zone_id** | **str** | Id of the TransportZone to which this LogicalSwitch is associated | 
**ip_pool_id** | **str** | IP pool id that associated with a LogicalSwitch. | [optional] 
**vlan** | **int** | This property is dedicated to VLAN based network, to set VLAN of logical network. It is mutually exclusive with &#x27;vlan_trunk_spec&#x27;.  | [optional] 
**hybrid** | **bool** | If this flag is set to true, then all the logical switch ports attached to this logical switch will behave in a hybrid fashion. The hybrid logical switch port indicates to NSX that the VM intends to operate in underlay mode, but retains the ability to forward egress traffic to the NSX overlay network. This flag can be enabled only for the logical switches in the overlay type transport zone which has host switch mode as STANDARD and also has either CrossCloud or CloudScope tag scopes. Only the NSX public cloud gateway (PCG) uses this flag, other host agents like ESX, KVM and Edge will ignore it. This property cannot be modified once the logical switch is created.  | [optional] [default to False]
**mac_pool_id** | **str** | Mac pool id that associated with a LogicalSwitch. | [optional] 
**vni** | **int** | Only for OVERLAY network. A VNI will be auto-allocated from the default VNI pool if not given; otherwise the given VNI has to be inside the default pool and not used by any other LogicalSwitch.  | [optional] 
**vlan_trunk_spec** | [**VlanTrunkSpec**](VlanTrunkSpec.md) |  | [optional] 
**admin_state** | **str** | Represents Desired state of the Logical Switch | 
**address_bindings** | [**list[PacketAddressClassifier]**](PacketAddressClassifier.md) | Address bindings for the Logical switch | [optional] 
**switching_profile_ids** | [**list[SwitchingProfileTypeIdEntry]**](SwitchingProfileTypeIdEntry.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

