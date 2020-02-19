# NodeInterfaceStatisticsProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**tx_dropped** | **int** | Number of packets dropped | [optional] 
**rx_packets** | **int** | Number of packets received | [optional] 
**tx_carrier** | **int** | Number of carrier losses detected | [optional] 
**rx_bytes** | **int** | Number of bytes received | [optional] 
**tx_errors** | **int** | Number of transmit errors | [optional] 
**interface_id** | **str** | Interface ID | [optional] 
**tx_colls** | **int** | Number of collisions detected | [optional] 
**rx_frame** | **int** | Number of framing errors | [optional] 
**rx_errors** | **int** | Number of receive errors | [optional] 
**tx_bytes** | **int** | Number of bytes transmitted | [optional] 
**rx_dropped** | **int** | Number of packets dropped | [optional] 
**tx_packets** | **int** | Number of packets transmitted | [optional] 
**source** | **str** | Source of status data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

