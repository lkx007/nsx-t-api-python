# RouteMapSequenceSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_preference** | **int** | Local preference indicates the degree of preference for one BGP route over other BGP routes. The path/route with highest local preference value is preferred/selected. If local preference value is not specified then it will be considered as 100 by default.  | [optional] 
**weight** | **int** | Weight used to select certain path | [optional] 
**large_community** | **str** | Set large BGP community, community value shoud be in aa:bb:nn format where aa, bb, nn are unsigned integers with range [1-4294967295]. | [optional] 
**as_path_prepend** | **str** | As Path Prepending to influence path selection | [optional] 
**community** | **str** | Set normal BGP community either well-known community name or community value in aa:nn(2byte:2byte) format.  | [optional] 
**multi_exit_discriminator** | **int** | Multi Exit Discriminator (MED) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

