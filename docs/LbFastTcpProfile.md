# LbFastTcpProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | An application profile can be bound to a virtual server to specify the application protocol characteristics. It is used to influence how load balancing is performed. Currently, three types of application profiles are supported: LbFastTCPProfile, LbFastUDPProfile and LbHttpProfile. LbFastTCPProfile or LbFastUDPProfile is typically used when the application is using a custom protocol or a standard protocol not supported by the load balancer. It is also used in cases where the user only wants L4 load balancing mainly because L4 load balancing has much higher performance and scalability, and/or supports connection mirroring. LbHttpProfile is used for both HTTP and HTTPS applications. Though application rules, if bound to the virtual server, can be used to accomplish the same goal, LbHttpProfile is intended to simplify enabling certain common use cases.  | 
**close_timeout** | **int** | It is used to specify how long a closing TCP connection (both FINs received or a RST is received) should be kept for this application before cleaning up the connection.  | [optional] [default to 8]
**idle_timeout** | **int** | It is used to configure how long an idle TCP connection in ESTABLISHED state should be kept for this application before cleaning up.  | [optional] [default to 1800]
**ha_flow_mirroring_enabled** | **bool** | If flow mirroring is enabled, all the flows to the bounded virtual server are mirrored to the standby node.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

