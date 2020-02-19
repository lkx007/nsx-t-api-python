# LbHttpResponseHeaderCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverse** | **bool** | A flag to indicate whether reverse the match result of this condition | [optional] [default to False]
**type** | **str** | Type of load balancer rule condition | 
**header_value** | **str** | Value of HTTP header field | 
**case_sensitive** | **bool** | If true, case is significant when comparing HTTP header value.  | [optional] [default to True]
**match_type** | **str** | Match type of HTTP header value | [optional] [default to 'REGEX']
**header_name** | **str** | Name of HTTP header field | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

