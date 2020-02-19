# LbVirtualServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_owned** | **bool** | Indicates system owned resource | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Description of this resource | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**create_user** | **str** | ID of the user who created this resource | [optional] 
**protection** | **str** | Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite&#x3D;true. UNKNOWN - the _protection field could not be determined for this           entity.  | [optional] 
**create_time** | **int** | Timestamp of resource creation | [optional] 
**last_modified_time** | **int** | Timestamp of last modification | [optional] 
**last_modified_user** | **str** | ID of the user who last modified this resource | [optional] 
**id** | **str** | Unique identifier of this resource | [optional] 
**resource_type** | **str** | The type of this resource. | [optional] 
**ip_protocol** | **str** | Assigned Internet Protocol in IP header, TCP, UDP are supported.  | [optional] [default to 'TCP']
**server_tcp_profile_id** | **str** | Only L7 virtual server could be configured with customized server side TCP profile.  | [optional] 
**sorry_pool_id** | **str** | When load balancer can not select a backend server to serve the request in default pool or pool in rules, the request would be served by sorry server pool.  | [optional] 
**port** | **str** | This is a deprecated property, please use &#x27;ports&#x27; instead. Port setting could be single port for both L7 mode and L4 mode. For L4 mode, a single port range is also supported. The port setting could be a single port or port range such as \&quot;80\&quot;, \&quot;1234-1236\&quot;. If port is configured and ports are not specified, both port and ports in response payload would return the same port value. If both port and ports are configured, ports setting would take effect with higher priority.  | [optional] 
**server_ssl_profile_binding** | [**ServerSslProfileBinding**](ServerSslProfileBinding.md) |  | [optional] 
**pool_id** | **str** | The server pool(LbPool) contains backend servers. Server pool consists of one or more servers, also referred to as pool members, that are similarly configured and are running the same application.  | [optional] 
**client_tcp_profile_id** | **str** | Only L7 virtual server could be configured with customized client side TCP profile.  | [optional] 
**default_pool_member_port** | **str** | This is a deprecated property, please use &#x27;default_pool_member_ports&#x27; instead. If default_pool_member_port is configured and default_pool_member_ports are not specified, both default_pool_member_port and default_pool_member_ports in response payload would return the same port value. If both are specified, default_pool_member_ports setting would take effect with higher priority.  | [optional] 
**access_log_enabled** | **bool** | Whether access log is enabled | [optional] [default to False]
**application_profile_id** | **str** | The application profile defines the application protocol characteristics. It is used to influence how load balancing is performed. Currently, LbFastTCPProfile, LbFastUDPProfile and LbHttpProfile, etc are supported.  | 
**max_concurrent_connections** | **int** | To ensure one virtual server does not over consume resources, affecting other applications hosted on the same LBS, connections to a virtual server can be capped. If it is not specified, it means that connections are unlimited.  | [optional] 
**rule_ids** | **list[str]** | Load balancer rules allow customization of load balancing behavior using match/action rules. Currently, load balancer rules are supported for only layer 7 virtual servers with LbHttpProfile.  | [optional] 
**max_new_connection_rate** | **int** | To ensure one virtual server does not over consume resources, connections to a member can be rate limited. If it is not specified, it means that connection rate is unlimited.  | [optional] 
**persistence_profile_id** | **str** | Persistence profile is used to allow related client connections to be sent to the same backend server.  | [optional] 
**client_ssl_profile_binding** | [**ClientSslProfileBinding**](ClientSslProfileBinding.md) |  | [optional] 
**default_pool_member_ports** | **list[str]** | If default_pool_member_ports are configured, both default_pool_member_port and default_pool_member_ports in the response payload would include port settings, notice that the value of default_pool_member_port is the first element of default_pool_member_ports.  | [optional] 
**ip_address** | **str** | virtual server IP address | 
**ports** | **list[str]** | Port setting could be a single port for both L7 mode and L4 mode. For L4 mode, multiple ports or port ranges are also supported such as \&quot;80\&quot;, \&quot;443\&quot;, \&quot;1234-1236\&quot;. If ports is configured, both port and ports in the response payload would include port settings, notice that the port field value is the first element of ports.  | [optional] 
**enabled** | **bool** | whether the virtual server is enabled | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

