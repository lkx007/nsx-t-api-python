# FieldsPacketData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routed** | **bool** | A flag, when set true, indicates that the traceflow packet is of L3 routing. | [optional] 
**transport_type** | **str** | transport type of the traceflow packet | [optional] [default to 'UNICAST']
**resource_type** | **str** | Packet configuration | 
**frame_size** | **int** | If the requested frame_size is too small (given the payload and traceflow metadata requirement of 16 bytes), the traceflow request will fail with an appropriate message.  The frame will be zero padded to the requested size. | [optional] [default to 128]
**ipv6_header** | [**Ipv6Header**](Ipv6Header.md) |  | [optional] 
**arp_header** | [**ArpHeader**](ArpHeader.md) |  | [optional] 
**transport_header** | [**TransportProtocolHeader**](TransportProtocolHeader.md) |  | [optional] 
**ip_header** | [**Ipv4Header**](Ipv4Header.md) |  | [optional] 
**eth_header** | [**EthernetHeader**](EthernetHeader.md) |  | [optional] 
**payload** | **str** | Up to 1000 bytes of payload may be supplied (with a base64-encoded length of 1336 bytes.) Additional bytes of traceflow metadata will be appended to the payload. The payload contains any data the user wants to put after the transport header. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

