# MigrationUnitAggregateInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**status** | **str** | Status of migration unit | [optional] 
**percent_complete** | **float** | Indicator of migration progress in percentage | [optional] 
**errors** | **list[str]** | List of errors occurred during migration of this migration unit | [optional] 
**unit** | [**MigrationUnit**](MigrationUnit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

