# MPAConfigProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**rmq_client_type** | **object** | The nodes client type. | [optional] 
**rmq_broker_cluster** | [**list[BrokerProperties]**](BrokerProperties.md) | The list of messaging brokers this controller is configured with. | [optional] 
**shared_secret** | **str** | The shared secret to use when autnenticating to the management plane&#x27;s message bus. Not returned in REST responses. | [optional] 
**account_name** | **object** | The account name to use when authenticating to the management plane&#x27;s message bus. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

