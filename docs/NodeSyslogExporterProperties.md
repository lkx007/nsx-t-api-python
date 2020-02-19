# NodeSyslogExporterProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | [**SelfResourceLink**](SelfResourceLink.md) |  | [optional] 
**links** | [**list[ResourceLink]**](ResourceLink.md) | The server will populate this field when returing the resource. Ignored on PUT and POST. | [optional] 
**schema** | **str** | Schema for this resource | [optional] 
**tls_ca_pem** | **str** | CA certificate PEM of TLS server to export to | [optional] 
**protocol** | **str** | Export protocol | 
**exporter_name** | **str** | Syslog exporter name | 
**level** | **str** | Logging level to export | 
**tls_client_ca_pem** | **str** | CA certificate PEM of the rsyslog client | [optional] 
**tls_cert_pem** | **str** | Certificate PEM of the rsyslog client | [optional] 
**server** | **str** | IP address or hostname of server to export to | 
**facilities** | **list[str]** | Facilities to export | [optional] 
**msgids** | **list[str]** | MSGIDs to export | [optional] 
**structured_data** | **list[str]** | Structured data to export | [optional] 
**port** | **int** | Port to export to | [optional] [default to 514]
**tls_key_pem** | **str** | Private key PEM of the rsyslog client | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

