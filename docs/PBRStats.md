# PBRStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**packet_count** | **int** | Aggregated number of packets processed by the rule. | [optional] 
**byte_count** | **int** | Aggregated number of bytes processed by the rule. | [optional] 
**rule_id** | **str** | Rule Identifier of the PBR rule. This is a globally unique number. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

