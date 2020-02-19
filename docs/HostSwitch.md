# HostSwitch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnics** | [**list[Pnic]**](Pnic.md) | Physical NICs connected to the host switch | [optional] 
**host_switch_name** | **str** | If this name is unset or empty then the default host switch name will be used. The name must be unique among all host switches specified in a given Transport Node; unset name, empty name and the default host switch name are considered the same in terms of uniqueness. | [optional] [default to 'nsxDefaultHostSwitch']
**static_ip_pool_id** | **str** | ID of configured Static IP Pool. If specified allocate IP for Endpoints from Pool. Else assume IP will be assigned for Endpoints from DHCP. This field is deprecated, use ip_assignment_spec field instead. | [optional] 
**host_switch_profile_ids** | [**list[HostSwitchProfileTypeIdEntry]**](HostSwitchProfileTypeIdEntry.md) | HostSwitch profiles bound to this HostSwitch. If a profile ID is not provided for any HostSwitchProfileType that is supported by the Transport Node, the corresponding default profile will be bound to the HostSwitch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

