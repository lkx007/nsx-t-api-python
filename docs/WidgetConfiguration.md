# WidgetConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_owned** | **bool** | Indicates system owned resource | [optional] 
**display_name** | **str** | Title of the widget. If display_name is omitted, the widget will be shown without a title. | [optional] 
**description** | **str** | Description of this resource | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**create_user** | **str** | ID of the user who created this resource | [optional] 
**protection** | **str** | Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite&#x3D;true. UNKNOWN - the _protection field could not be determined for this           entity.  | [optional] 
**create_time** | **int** | Timestamp of resource creation | [optional] 
**last_modified_time** | **int** | Timestamp of last modification | [optional] 
**last_modified_user** | **str** | ID of the user who last modified this resource | [optional] 
**id** | **str** | Unique identifier of this resource | [optional] 
**resource_type** | **str** | Supported visualization types are LabelValueConfiguration, DonutConfiguration, GridConfiguration, StatsConfiguration, MultiWidgetConfiguration, GraphConfiguration and ContainerConfiguration. | 
**datasources** | [**list[Datasource]**](Datasource.md) | The &#x27;datasources&#x27; represent the sources from which data will be fetched. Currently, only NSX-API is supported as a &#x27;default&#x27; datasource. An example of specifying &#x27;default&#x27; datasource along with the urls to fetch data from is given at &#x27;example_request&#x27; section of &#x27;CreateWidgetConfiguration&#x27; API. | [optional] 
**weight** | **int** | Specify relavite weight in WidgetItem for placement in a view. Please see WidgetItem for details. | [optional] 
**icons** | [**list[Icon]**](Icon.md) | Icons to be applied at dashboard for widgets and UI elements. | [optional] 
**shared** | **bool** | Please use the property &#x27;shared&#x27; of View instead of this. The widgets of a shared view are visible to other users. | [optional] 
**footer** | [**Footer**](Footer.md) |  | [optional] 
**drilldown_id** | **str** | Id of drilldown widget, if any. Id should be a valid id of an existing widget. A widget is considered as drilldown widget when it is associated with any other widget and provides more detailed information about any data item from the parent widget. | [optional] 
**is_drilldown** | **bool** | Set to true if this widget should be used as a drilldown. | [optional] [default to False]
**legend** | [**Legend**](Legend.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

