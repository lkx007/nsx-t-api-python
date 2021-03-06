# MultiWidgetConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Supported visualization types are LabelValueConfiguration, DonutConfiguration, GridConfiguration, StatsConfiguration, MultiWidgetConfiguration, GraphConfiguration and ContainerConfiguration. | 
**display_name** | **str** | Title of the widget. If display_name is omitted, the widget will be shown without a title. | [optional] 
**datasources** | [**list[Datasource]**](Datasource.md) | The &#x27;datasources&#x27; represent the sources from which data will be fetched. Currently, only NSX-API is supported as a &#x27;default&#x27; datasource. An example of specifying &#x27;default&#x27; datasource along with the urls to fetch data from is given at &#x27;example_request&#x27; section of &#x27;CreateWidgetConfiguration&#x27; API. | [optional] 
**weight** | **int** | Specify relavite weight in WidgetItem for placement in a view. Please see WidgetItem for details. | [optional] 
**icons** | [**list[Icon]**](Icon.md) | Icons to be applied at dashboard for widgets and UI elements. | [optional] 
**shared** | **bool** | Please use the property &#x27;shared&#x27; of View instead of this. The widgets of a shared view are visible to other users. | [optional] 
**footer** | [**Footer**](Footer.md) |  | [optional] 
**drilldown_id** | **str** | Id of drilldown widget, if any. Id should be a valid id of an existing widget. A widget is considered as drilldown widget when it is associated with any other widget and provides more detailed information about any data item from the parent widget. | [optional] 
**is_drilldown** | **bool** | Set to true if this widget should be used as a drilldown. | [optional] [default to False]
**legend** | [**Legend**](Legend.md) |  | [optional] 
**widgets** | [**list[WidgetItem]**](WidgetItem.md) | Array of widgets that are part of the multi-widget. | 
**navigation** | **str** | Hyperlink of the specified UI page that provides details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

