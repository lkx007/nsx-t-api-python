# MACAddressElement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **int** | The _revision property describes the current revision of the resource. To prevent clients from overwriting each other&#x27;s changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected. | [optional] 
**mac_address** | **str** | A MAC address. Must be 6 pairs of hexadecimal digits, upper or lower case, separated by colons or dashes. Examples: 01:23:45:67:89:ab, 01-23-45-67-89-AB.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

