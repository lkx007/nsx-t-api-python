# LogicalRouterRouteTable

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
**sort_ascending** | **bool** | If true, results are sorted in ascending order | [optional] 
**sort_by** | **str** | Field by which records are sorted | [optional] 
**result_count** | **int** | Count of results found (across all pages), set only on first page | [optional] 
**logical_router_name** | **str** | Name of the logical router | [optional] 
**last_update_timestamp** | **int** | Timestamp when the data was last updated; unset if data source has never updated the data. | [optional] 
**logical_router_id** | **str** | The id of the logical router | 
**results** | [**list[LogicalRouterRouteEntry]**](LogicalRouterRouteEntry.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

