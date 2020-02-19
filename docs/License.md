# License

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**features** | **str** | semicolon delimited feature list | [optional] 
**description** | **str** | license edition | [optional] 
**product_version** | **str** | product version | [optional] 
**expiry** | **int** | date that license expires | [optional] 
**is_eval** | **bool** | true for evalution license | [optional] 
**is_mh** | **bool** | multi-hypervisor support | [optional] 
**license_key** | **str** | license key | [optional] 
**is_expired** | **bool** | whether the license has expired | [optional] 
**product_name** | **str** | product name | [optional] 
**capacity_type** | **str** | License metrics specifying the capacity type of license key. Types are: - VM - CPU - USER(Concurrent User)  | [optional] 
**quantity** | **int** | license capacity; 0 for unlimited | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

