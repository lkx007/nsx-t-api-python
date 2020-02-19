# LbSessionCookieTime

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Both session cookie and persistence cookie are supported, Use LbSessionCookieTime for session cookie time setting, Use LbPersistenceCookieTime for persistence cookie time setting  | 
**cookie_max_idle** | **int** | Instead of using HTTP Cookie max-age and relying on client to expire the cookie, max idle time and/or max lifetime of the cookie can be used. Max idle time, if configured, specifies the maximum interval the cookie is valid for from the last time it was seen in a request. It is available for insert mode.  | [optional] 
**cookie_max_life** | **int** | Max life time, if configured, specifies the maximum interval the cookie is valid for from the first time the cookie was seen in a request. It is available for insert mode.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

