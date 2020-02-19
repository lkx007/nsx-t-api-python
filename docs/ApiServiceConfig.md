# ApiServiceConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_api_concurrency_limit** | **int** | The maximum number of concurrent API requests that will be serviced. If the number of API requests being processed exceeds this limit, new API requests will be refused and a 503 Service Unavailable response will be returned to the client.  To disable API concurrency limiting, set this value to 0. | [optional] [default to 199]
**lockout_immune_addresses** | **list[str]** | The list of IP addresses which are not subjected to a lockout on failed login attempts. | [optional] 
**client_api_concurrency_limit** | **int** | The maximum number of concurrent API requests that will be serviced for a given authenticated client.  If the number of API requests being processed exceeds this limit, new API requests will be refused and a 503 Service Unavailable response will be returned to the client. To disable API concurrency limiting, set this value to 0. | [optional] [default to 40]
**session_timeout** | **int** | NSX session inactivity timeout | [optional] [default to 1800]
**client_api_rate_limit** | **int** | The maximum number of API requests that will be serviced per second for a given authenticated client.  If more API requests are received than can be serviced, a 429 Too Many Requests HTTP response will be returned. To disable API rate limiting, set this value to 0. | [optional] [default to 100]
**redirect_host** | **str** | Host name or IP address to use for redirect location headers, or empty string to derive from current request. To disable, set redirect_host to the empty string (\&quot;\&quot;). | [optional] [default to '']
**protocol_versions** | [**list[ProtocolVersion]**](ProtocolVersion.md) | The TLS protocol versions that the API service will negotiate. | [optional] 
**cipher_suites** | [**list[CipherSuite]**](CipherSuite.md) | The TLS cipher suites that the API service will negotiate. | [optional] 
**connection_timeout** | **int** | NSX connection timeout, in seconds. To disable timeout, set to 0. | [optional] [default to 30]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

