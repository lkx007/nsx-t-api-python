# NamedTeamingPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | Teaming policy | 
**standby_list** | [**list[Uplink]**](Uplink.md) | List of Uplinks used in standby list | [optional] 
**active_list** | [**list[Uplink]**](Uplink.md) | List of Uplinks used in active list | 
**name** | **str** | An uplink teaming policy of a given name defined in UplinkHostSwitchProfile. The names of all NamedTeamingPolicies in an UplinkHostSwitchProfile must be different, but a name can be shared by different UplinkHostSwitchProfiles. Different TransportNodes can use different NamedTeamingPolicies having the same name in different UplinkHostSwitchProfiles to realize an uplink teaming policy on a logical switch. An uplink teaming policy on a logical switch can be any policy defined by a user; it does not have to be a single type of FAILOVER or LOADBALANCE. It can be a combination of types, for instance, a user can define a policy with name \&quot;MyHybridTeamingPolicy\&quot; as \&quot;FAILOVER on all ESX TransportNodes and LOADBALANCE on all KVM TransportNodes\&quot;. The name is the key of the teaming policy and can not be changed once assigned. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

