# MacLearningSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The maximum number of MAC addresses that can be learned on this port | [optional] [default to 4096]
**aging_time** | **int** | Aging time in sec for learned MAC address | [optional] [default to 600]
**enabled** | **bool** | Allowing source MAC address learning | 
**limit_policy** | **str** | The policy after MAC Limit is exceeded | [optional] [default to 'ALLOW']
**unicast_flooding_allowed** | **bool** | Allowing flooding for unlearned MAC for ingress traffic | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

