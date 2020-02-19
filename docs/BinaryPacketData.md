# BinaryPacketData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routed** | **bool** | A flag, when set true, indicates that the traceflow packet is of L3 routing. | [optional] 
**transport_type** | **str** | transport type of the traceflow packet | [optional] [default to 'UNICAST']
**resource_type** | **str** | Packet configuration | 
**frame_size** | **int** | If the requested frame_size is too small (given the payload and traceflow metadata requirement of 16 bytes), the traceflow request will fail with an appropriate message.  The frame will be zero padded to the requested size. | [optional] [default to 128]
**payload** | **str** | Up to 1000 bytes of payload may be supplied (with a base64-encoded length of 1336 bytes.) Additional bytes of traceflow metadata will be appended to the payload. The payload must contain all headers (Ethernet, IP, etc). Note that VLAN is not supported in the logical space. Hence, payload must not contain 802.1Q headers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

