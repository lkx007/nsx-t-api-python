# PortConnectionLogicalSwitch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**ManagedResource**](ManagedResource.md) |  | [optional] 
**id** | **str** | Resource ID is mapped to this. (ID is Generated for Edge node groups, since resource will be null) | [optional] 
**vm_ports_states** | [**list[LogicalPortState]**](LogicalPortState.md) | States of Logical Ports that are attached to a VIF/VM | [optional] 
**vm_ports** | [**list[LogicalPort]**](LogicalPort.md) | Logical Ports that are attached to a VIF/VM | [optional] 
**vm_vnics** | [**list[VirtualNetworkInterface]**](VirtualNetworkInterface.md) | Virutal Network Interfaces that are attached to the Logical Ports | [optional] 
**router_ports** | [**list[LogicalPort]**](LogicalPort.md) | Logical Ports that are attached to a router | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

