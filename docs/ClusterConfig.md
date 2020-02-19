# ClusterConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **int** | The _revision property describes the current revision of the resource. To prevent clients from overwriting each other&#x27;s changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected. | [optional] 
**control_cluster_changes_allowed** | **bool** | True if control cluster nodes may be added or removed | [optional] 
**nodes** | [**list[ClusterNodeInfo]**](ClusterNodeInfo.md) | Configuration of each node in cluster | [optional] 
**mgmt_cluster_changes_allowed** | **bool** | True if management cluster nodes may be added or removed | [optional] 
**cluster_id** | **str** | Unique identifier of this cluster | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

