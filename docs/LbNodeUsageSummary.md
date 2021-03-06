# LbNodeUsageSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_percentage** | **float** | The overall usage percentage of all nodes for the load balancer services.  | [optional] 
**current_credit_number** | **int** | The current credit number reflects the overall credit usage for all nodes.  | [optional] 
**node_usages** | [**list[LbNodeUsage]**](LbNodeUsage.md) | The property contains lb node usages for each node.  | [optional] 
**severity** | **str** | The severity calculation is based on current credit usage percentage of load balancer for all nodes.  | [optional] 
**node_counts** | [**list[LbNodeCountPerSeverity]**](LbNodeCountPerSeverity.md) | The property identifies array of node count for each severity (RED, ORANGE and GREEN).  | [optional] 
**remaining_credit_number** | **int** | The remaining credit number is the overall remaining credits that can be used for load balancer service configuration for all nodes.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

