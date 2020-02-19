# coding: utf-8

"""
    NSX-T Manager API

    VMware NSX-T Manager REST API  # noqa: E501

    OpenAPI spec version: 2.5.1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ManagementPlaneApiNetworkTransportTransportProfilesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_transport_zone_profile(self, body, **kwargs):  # noqa: E501
        """Create a transport zone Profile  # noqa: E501

        Creates a transport zone profile. The resource_type is required.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_transport_zone_profile(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TransportZoneProfile body: (required)
        :return: TransportZoneProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_transport_zone_profile_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_transport_zone_profile_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_transport_zone_profile_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a transport zone Profile  # noqa: E501

        Creates a transport zone profile. The resource_type is required.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_transport_zone_profile_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TransportZoneProfile body: (required)
        :return: TransportZoneProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_transport_zone_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_transport_zone_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/transportzone-profiles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransportZoneProfile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_transport_zone_profile(self, transportzone_profile_id, **kwargs):  # noqa: E501
        """Delete a transport zone Profile  # noqa: E501

        Deletes a specified transport zone profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_transport_zone_profile(transportzone_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transportzone_profile_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_transport_zone_profile_with_http_info(transportzone_profile_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_transport_zone_profile_with_http_info(transportzone_profile_id, **kwargs)  # noqa: E501
            return data

    def delete_transport_zone_profile_with_http_info(self, transportzone_profile_id, **kwargs):  # noqa: E501
        """Delete a transport zone Profile  # noqa: E501

        Deletes a specified transport zone profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_transport_zone_profile_with_http_info(transportzone_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transportzone_profile_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transportzone_profile_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_transport_zone_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transportzone_profile_id' is set
        if ('transportzone_profile_id' not in params or
                params['transportzone_profile_id'] is None):
            raise ValueError("Missing the required parameter `transportzone_profile_id` when calling `delete_transport_zone_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transportzone_profile_id' in params:
            path_params['transportzone-profile-id'] = params['transportzone_profile_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/transportzone-profiles/{transportzone-profile-id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transport_zone_profile(self, transportzone_profile_id, **kwargs):  # noqa: E501
        """Get transport zone profile by identifier  # noqa: E501

        Returns information about a specified transport zone profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transport_zone_profile(transportzone_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transportzone_profile_id: (required)
        :return: TransportZoneProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transport_zone_profile_with_http_info(transportzone_profile_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transport_zone_profile_with_http_info(transportzone_profile_id, **kwargs)  # noqa: E501
            return data

    def get_transport_zone_profile_with_http_info(self, transportzone_profile_id, **kwargs):  # noqa: E501
        """Get transport zone profile by identifier  # noqa: E501

        Returns information about a specified transport zone profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transport_zone_profile_with_http_info(transportzone_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transportzone_profile_id: (required)
        :return: TransportZoneProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transportzone_profile_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transport_zone_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transportzone_profile_id' is set
        if ('transportzone_profile_id' not in params or
                params['transportzone_profile_id'] is None):
            raise ValueError("Missing the required parameter `transportzone_profile_id` when calling `get_transport_zone_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transportzone_profile_id' in params:
            path_params['transportzone-profile-id'] = params['transportzone_profile_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/transportzone-profiles/{transportzone-profile-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransportZoneProfile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_transport_zone_profiles(self, **kwargs):  # noqa: E501
        """List transport zone profiles  # noqa: E501

        Returns information about the configured transport zone profiles. Transport zone profiles define networking policies for transport zones and transport zone endpoints.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_transport_zone_profiles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param bool include_system_owned: Whether the list result contains system resources
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param str resource_type: comma-separated list of transport zone profile types, e.g. ?resource_type=BfdHealthMonitoringProfile
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: TransportZoneProfileListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_transport_zone_profiles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_transport_zone_profiles_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_transport_zone_profiles_with_http_info(self, **kwargs):  # noqa: E501
        """List transport zone profiles  # noqa: E501

        Returns information about the configured transport zone profiles. Transport zone profiles define networking policies for transport zones and transport zone endpoints.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_transport_zone_profiles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param bool include_system_owned: Whether the list result contains system resources
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param str resource_type: comma-separated list of transport zone profile types, e.g. ?resource_type=BfdHealthMonitoringProfile
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: TransportZoneProfileListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor', 'include_system_owned', 'included_fields', 'page_size', 'resource_type', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_transport_zone_profiles" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'include_system_owned' in params:
            query_params.append(('include_system_owned', params['include_system_owned']))  # noqa: E501
        if 'included_fields' in params:
            query_params.append(('included_fields', params['included_fields']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'resource_type' in params:
            query_params.append(('resource_type', params['resource_type']))  # noqa: E501
        if 'sort_ascending' in params:
            query_params.append(('sort_ascending', params['sort_ascending']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/transportzone-profiles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransportZoneProfileListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_transport_zone_profile(self, body, transportzone_profile_id, **kwargs):  # noqa: E501
        """Update a transport zone profile  # noqa: E501

        Modifies a specified transport zone profile. The body of the PUT request must include the resource_type.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_transport_zone_profile(body, transportzone_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TransportZoneProfile body: (required)
        :param str transportzone_profile_id: (required)
        :return: TransportZoneProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_transport_zone_profile_with_http_info(body, transportzone_profile_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_transport_zone_profile_with_http_info(body, transportzone_profile_id, **kwargs)  # noqa: E501
            return data

    def update_transport_zone_profile_with_http_info(self, body, transportzone_profile_id, **kwargs):  # noqa: E501
        """Update a transport zone profile  # noqa: E501

        Modifies a specified transport zone profile. The body of the PUT request must include the resource_type.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_transport_zone_profile_with_http_info(body, transportzone_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TransportZoneProfile body: (required)
        :param str transportzone_profile_id: (required)
        :return: TransportZoneProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'transportzone_profile_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_transport_zone_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_transport_zone_profile`")  # noqa: E501
        # verify the required parameter 'transportzone_profile_id' is set
        if ('transportzone_profile_id' not in params or
                params['transportzone_profile_id'] is None):
            raise ValueError("Missing the required parameter `transportzone_profile_id` when calling `update_transport_zone_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transportzone_profile_id' in params:
            path_params['transportzone-profile-id'] = params['transportzone_profile_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/transportzone-profiles/{transportzone-profile-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransportZoneProfile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
