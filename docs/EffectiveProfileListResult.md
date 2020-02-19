# EffectiveProfileListResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
**sort_ascending** | **bool** | If true, results are sorted in ascending order | [optional] 
**sort_by** | **str** | Field by which records are sorted | [optional] 
**result_count** | **int** | Count of results found (across all pages), set only on first page | [optional] 
**results** | [**list[NSXProfileReference]**](NSXProfileReference.md) | Paged Collection of profiles which are applied to an Entity | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

