# LbPassiveMonitor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Load balancers monitor the health of backend servers to ensure traffic is not black holed. There are two types of healthchecks: active and passive. Passive healthchecks depend on failures in actual client traffic (e.g. RST from server in response to a client connection) to detect that the server or the application is down. In case of active healthchecks, load balancer itself initiates new connections (or sends ICMP ping) to the servers periodically to check their health, completely independent of any data traffic. Currently, active health monitors are supported for HTTP, HTTPS, TCP, UDP and ICMP protocols.  | 
**max_fails** | **int** | When the consecutive failures reach this value, then the member is considered temporarily unavailable for a configurable period  | [optional] [default to 5]
**timeout** | **int** | After this timeout period, the member is tried again for a new connection to see if it is available.  | [optional] [default to 5]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

