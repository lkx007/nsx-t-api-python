# DonutPart

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | A numerical value that represents the portion or entity of the donut or stats chart. | 
**drilldown_id** | **str** | Id of drilldown widget, if any. Id should be a valid id of an existing widget. A widget is considered as drilldown widget when it is associated with any other widget and provides more detailed information about any data item from the parent widget. | [optional] 
**render_configuration** | [**list[RenderConfiguration]**](RenderConfiguration.md) | Additional rendering or conditional evaluation of the field values to be performed, if any. | [optional] 
**navigation** | **str** | Hyperlink of the specified UI page that provides details. If drilldown_id is provided, then navigation cannot be used. | [optional] 
**tooltip** | [**list[Tooltip]**](Tooltip.md) | Multi-line text to be shown on tooltip while hovering over the portion. | [optional] 
**label** | [**Label**](Label.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

