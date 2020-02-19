# LbRule

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
**phase** | **str** | Each load balancer rule is used at a specific phase of load balancer processing. Currently three phases are supported, HTTP_REQUEST_REWRITE, HTTP_FORWARDING and HTTP_RESPONSE_REWRITE. When an HTTP request message is received by load balancer, all HTTP_REQUEST_REWRITE rules, if present are executed in the order they are applied to virtual server. And then if HTTP_FORWARDING rules present, only first matching rule&#x27;s action is executed, remaining rules are not checked. HTTP_FORWARDING rules can have only one action. If the request is forwarded to a backend server and the response goes back to load balancer, all HTTP_RESPONSE_REWRITE rules, if present, are executed in the order they are applied to the virtual server.  | 
**match_conditions** | [**list[LbRuleCondition]**](LbRuleCondition.md) | A list of match conditions used to match application traffic. Multiple match conditions can be specified in one load balancer rule, each match condition defines a criterion to match application traffic. If no match conditions are specified, then the load balancer rule will always match and it is used typically to define default rules. If more than one match condition is specified, then match strategy determines if all conditions should match or any one condition should match for the load balancer rule to considered a match.  | [optional] 
**actions** | [**list[LbRuleAction]**](LbRuleAction.md) | A list of actions to be executed at specified phase when load balancer rule matches. The actions are used to manipulate application traffic, such as rewrite URI of HTTP messages, redirect HTTP messages, etc.  | 
**match_strategy** | **str** | Strategy to define how load balancer rule is considered a match when multiple match conditions are specified in one rule. If match_stragety is set to ALL, then load balancer rule is considered a match only if all the conditions match. If match_strategy is set to ANY, then load balancer rule is considered a match if any one of the conditions match.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

