# StandardHostSwitch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnics_uninstall_migration** | [**list[Pnic]**](Pnic.md) | The pnics to be migrated out to a non N-VDS switch during transport node deletion. | [optional] 
**ip_assignment_spec** | [**IpAssignmentSpec**](IpAssignmentSpec.md) |  | [optional] 
**cpu_config** | [**list[CpuCoreConfigForEnhancedNetworkingStackSwitch]**](CpuCoreConfigForEnhancedNetworkingStackSwitch.md) | CPU configuration specifies number of Logical cpu cores (Lcores) per Non Uniform Memory Access (NUMA) node dedicated to Enhanced Networking Stack enabled HostSwitch to get the best performance. | [optional] 
**is_migrate_pnics** | **bool** | If the pnics specified in the pnics field are used by a single Vsphere Standard Switch or DVS, then migrate the pnics to N-VDS. If any two pnics are not used by the same Vsphere Standard Switch or DVS, it is not supported. In such cases, please migrate them in multiple steps, one Vsphere Standard Switch or DVS at a time. | [optional] [default to False]
**vmk_uninstall_migration** | [**list[VmknicNetwork]**](VmknicNetwork.md) | The vmk interfaces and the associated portgroups on the VSS/DVS. This field is realized on the host during transport node deletion or NSX uninstallation to specify the destination for all vmks on N-VDS switches. | [optional] 
**pnics** | [**list[Pnic]**](Pnic.md) | Physical NICs connected to the host switch | [optional] 
**host_switch_name** | **str** | If this name is unset or empty then the default host switch name will be used. The name must be unique among all host switches specified in a given transport node; unset name, empty name and the default host switch name are considered the same in terms of uniqueness. | [optional] [default to 'nsxDefaultHostSwitch']
**vmk_install_migration** | [**list[VmknicNetwork]**](VmknicNetwork.md) | The vmk interfaces and the associated logical switches on the host switch. The state of this field is realized on the transport node during creation and update. | [optional] 
**host_switch_profile_ids** | [**list[HostSwitchProfileTypeIdEntry]**](HostSwitchProfileTypeIdEntry.md) | host switch profiles bound to this host switch. If a profile ID is not provided for any HostSwitchProfileType that is supported by the transport node, the corresponding default profile will be bound to the host switch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

