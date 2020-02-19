# ManagementPlaneProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**account** | **object** | The account name to use when authenticating to the management plane&#x27;s message bus. | [optional] 
**secret** | **str** | The shared secret to use when autnenticating to the management plane&#x27;s message bus. Not returned in REST responses. | [optional] 
**brokers** | [**list[ManagementPlaneBrokerProperties]**](ManagementPlaneBrokerProperties.md) | The list of messaging brokers this controller is configured with. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

