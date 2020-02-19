# RoutingGlobalConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Valid Global configuration types | 
**logical_uplink_mtu** | **int** | This is the global default MTU for all the logical uplinks in a NSX domain. Currently logical uplink MTU can only be set globally and applies to the entire NSX domain. There is no option to override this value at transport zone level or transport node level. If this value is not set, the default value of 1500 will be used. | [optional] [default to 1500]
**l3_forwarding_mode** | **str** | This setting does not restrict configuration as per other modes. But the forwarding will only work as per the mode set here. | [default to 'IPV4_ONLY']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

