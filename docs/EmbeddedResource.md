# EmbeddedResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **int** | The _revision property describes the current revision of the resource. To prevent clients from overwriting each other&#x27;s changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected. | [optional] 
**owner** | [**OwnerResourceLink**](OwnerResourceLink.md) |  | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**id** | **str** | Identifier of the resource | [optional] 
**resource_type** | **str** | The type of this resource. | [optional] 
**description** | **str** | Description of this resource | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

