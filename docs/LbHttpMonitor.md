# LbHttpMonitor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_port** | **str** | If the monitor port is specified, it would override pool member port setting for healthcheck. A port range is not supported. For ICMP monitor, monitor_port is not required.  | [optional] 
**fall_count** | **int** | num of consecutive checks must fail before marking it down | [optional] [default to 3]
**interval** | **int** | the frequency at which the system issues the monitor check (in second) | [optional] [default to 5]
**rise_count** | **int** | num of consecutive checks must pass before marking it up | [optional] [default to 3]
**timeout** | **int** | the number of seconds the target has in which to respond to the monitor request  | [optional] [default to 15]
**response_status_codes** | **list[int]** | The HTTP response status code should be a valid HTTP status code.  | [optional] 
**request_method** | **str** | the health check method for HTTP monitor type | [optional] [default to 'GET']
**request_body** | **str** | String to send as part of HTTP health check request body. Valid only for certain HTTP methods like POST.  | [optional] 
**response_body** | **str** | If HTTP response body match string (regular expressions not supported) is specified (using LbHttpMonitor.response_body) then the healthcheck HTTP response body is matched against the specified string and server is considered healthy only if there is a match. If the response body string is not specified, HTTP healthcheck is considered successful if the HTTP response status code is 2xx, but it can be configured to accept other status codes as successful.  | [optional] 
**request_url** | **str** | URL used for HTTP monitor | [optional] 
**request_version** | **str** | HTTP request version | [optional] [default to 'HTTP_VERSION_1_1']
**request_headers** | [**list[LbHttpRequestHeader]**](LbHttpRequestHeader.md) | Array of HTTP request headers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

