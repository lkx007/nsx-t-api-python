# NotificationWatcher

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_owned** | **bool** | Indicates system owned resource | [optional] 
**display_name** | **str** | Defaults to ID if not set | [optional] 
**description** | **str** | Optional description that can be associated with this NotificationWatcher. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Opaque identifiers meaningful to the API user | [optional] 
**create_user** | **str** | ID of the user who created this resource | [optional] 
**protection** | **str** | Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite&#x3D;true. UNKNOWN - the _protection field could not be determined for this           entity.  | [optional] 
**create_time** | **int** | Timestamp of resource creation | [optional] 
**last_modified_time** | **int** | Timestamp of last modification | [optional] 
**last_modified_user** | **str** | ID of the user who last modified this resource | [optional] 
**id** | **str** | System generated identifier to identify a notification watcher uniquely.  | [optional] 
**resource_type** | **str** | The type of this resource. | [optional] 
**send_timeout** | **int** | Optional time duration (in seconds) to specify request timeout to notification watcher. If the send reaches the timeout, will try to send refresh_needed as true in the next time interval. The default value is 30 seconds. | [optional] [default to 30]
**uri** | **str** | URI notification requests should be made on the specified server. | 
**certificate_sha256_thumbprint** | **str** | Contains the hex-encoded SHA256 thumbprint of the HTTPS certificate. It must be specified if use_https is set to true. | [optional] 
**method** | **str** | Type of method notification requests should be made on the specified server. The value must be set to POST. | 
**send_interval** | **int** | Optional time interval (in seconds) for which notification URIs will be accumulated. At the end of the time interval the accumulated notification URIs will be sent to this NotificationWatcher in the form of zero (nothing accumulated) or more notification requests as soon as possible. If it is not specified, the NotificationWatcher should expected to receive notifications at any time. | [optional] 
**max_send_uri_count** | **int** | If the number of notification URIs accumulated in specified send_interval exceeds max_send_uri_count, then multiple notification requests (each with max_send_uri_count or less number of notification URIs) will be sent to this NotificationWatcher. The default value is 5000. | [optional] [default to 5000]
**authentication_scheme** | [**NotificationAuthenticationScheme**](NotificationAuthenticationScheme.md) |  | 
**server** | **str** | IP address or fully qualified domain name of the partner/customer watcher. | 
**port** | **int** | Optional integer port value to specify a non-standard HTTP or HTTPS port. | [optional] 
**use_https** | **bool** | Optional field, when set to true indicates REST API server should use HTTPS. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

