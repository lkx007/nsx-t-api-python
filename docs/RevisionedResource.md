# RevisionedResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**revision** | **int** | The _revision property describes the current revision of the resource. To prevent clients from overwriting each other&#x27;s changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

