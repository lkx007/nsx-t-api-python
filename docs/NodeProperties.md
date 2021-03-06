# NodeProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**system_time** | **int** | Current time expressed in milliseconds since epoch | [optional] 
**node_uuid** | **str** | Node Unique Identifier | [optional] 
**motd** | **object** | Message of the day to display when users login to node using the NSX CLI | [optional] 
**cli_timeout** | **int** | NSX CLI inactivity timeout, set to 0 to configure no timeout | [optional] 
**kernel_version** | **str** | Kernel version | [optional] 
**export_type** | **str** | Export restrictions in effect, if any | [optional] 
**hostname** | **str** | Host name or fully qualified domain name of node | [optional] 
**product_version** | **str** | Product version | [optional] 
**node_version** | **str** | Node version | [optional] 
**system_datetime** | **str** | System date time in UTC | [optional] 
**fully_qualified_domain_name** | **str** | Fully qualified domain name | [optional] 
**timezone** | **str** | Timezone | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

