# LbUdpMonitor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_port** | **str** | If the monitor port is specified, it would override pool member port setting for healthcheck. A port range is not supported. For ICMP monitor, monitor_port is not required.  | [optional] 
**fall_count** | **int** | num of consecutive checks must fail before marking it down | [optional] [default to 3]
**interval** | **int** | the frequency at which the system issues the monitor check (in second) | [optional] [default to 5]
**rise_count** | **int** | num of consecutive checks must pass before marking it up | [optional] [default to 3]
**timeout** | **int** | the number of seconds the target has in which to respond to the monitor request  | [optional] [default to 15]
**receive** | **str** | Expected data, can be anywhere in the response and it has to be a string, regular expressions are not supported. UDP healthcheck is considered failed if there is no server response within the timeout period.  | 
**send** | **str** | The data to be sent to the monitored server.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

