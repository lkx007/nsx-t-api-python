# FirewallSessionTimerProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Resource type to use as profile type | 
**tcp_closed** | **int** | The timeout value of connection in seconds after one endpoint sends an RST. | [default to 20]
**tcp_opening** | **int** | The timeout value of connection in seconds after a second packet has been transferred. | [default to 30]
**udp_single** | **int** | The timeout value of connection in seconds if the source host sends more than one packet but the destination host has never sent one back. | [default to 30]
**tcp_finwait** | **int** | The timeout value of connection in seconds after both FINs have been exchanged and connection is closed. | [default to 45]
**tcp_first_packet** | **int** | The timeout value of connection in seconds after the first packet has been sent. | [default to 120]
**tcp_closing** | **int** | The timeout value of connection in seconds after the first FIN has been sent. | [default to 120]
**tcp_established** | **int** | The timeout value of connection in seconds once the connection has become fully established. | [default to 43200]
**udp_multiple** | **int** | The timeout value of connection in seconds if both hosts have sent packets. | [default to 60]
**icmp_error_reply** | **int** | The timeout value for the connection after an ICMP error came back in response to an ICMP packet. | [default to 10]
**udp_first_packet** | **int** | The timeout value of connection in seconds after the first packet. This will be the initial timeout for the new UDP flow. | [default to 60]
**icmp_first_packet** | **int** | The timeout value of connection in seconds after the first packet. This will be the initial timeout for the new ICMP flow. | [default to 20]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

