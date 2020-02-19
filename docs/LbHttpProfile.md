# LbHttpProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | An application profile can be bound to a virtual server to specify the application protocol characteristics. It is used to influence how load balancing is performed. Currently, three types of application profiles are supported: LbFastTCPProfile, LbFastUDPProfile and LbHttpProfile. LbFastTCPProfile or LbFastUDPProfile is typically used when the application is using a custom protocol or a standard protocol not supported by the load balancer. It is also used in cases where the user only wants L4 load balancing mainly because L4 load balancing has much higher performance and scalability, and/or supports connection mirroring. LbHttpProfile is used for both HTTP and HTTPS applications. Though application rules, if bound to the virtual server, can be used to accomplish the same goal, LbHttpProfile is intended to simplify enabling certain common use cases.  | 
**response_timeout** | **int** | If server doesn&#x27;t send any packet within this time, the connection is closed.  | [optional] [default to 60]
**idle_timeout** | **int** | It is used to specify the HTTP application idle timeout, it means that how long the load balancer will keep the connection idle to wait for the client to send the next keep-alive request. It is not a TCP socket setting.  | [optional] [default to 15]
**request_body_size** | **int** | If it is not specified, it means that request body size is unlimited.  | [optional] 
**response_header_size** | **int** | A response with header larger than response_header_size will be dropped.  | [optional] [default to 4096]
**ntlm** | **bool** | NTLM is an authentication protocol that can be used over HTTP. If the flag is set to true, LB will use NTLM challenge/response methodology.  | [optional] [default to False]
**request_header_size** | **int** | A request with header larger than request_header_size will be processed as best effort whereas a request with header below this specified size is guaranteed to be processed.  | [optional] [default to 1024]
**http_redirect_to** | **str** | If a website is temporarily down or has moved, incoming requests for that virtual server can be temporarily redirected to a URL  | [optional] 
**x_forwarded_for** | **str** | insert or replace x_forwarded_for | [optional] 
**http_redirect_to_https** | **bool** | Certain secure applications may want to force communication over SSL, but instead of rejecting non-SSL connections, they may choose to redirect the client automatically to use SSL.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

