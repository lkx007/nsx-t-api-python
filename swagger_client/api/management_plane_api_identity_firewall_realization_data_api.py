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


class ManagementPlaneApiIdentityFirewallRealizationDataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_nsgroup_vm_details(self, group_id, **kwargs):  # noqa: E501
        """Get all IDFW NSGroup VM details for a given NSGroup  # noqa: E501

        Get all Identity Firewall NSGroup VM details for a given NSGroup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nsgroup_vm_details(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :return: IdfwNsgroupVmDetailListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_nsgroup_vm_details_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_nsgroup_vm_details_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def get_nsgroup_vm_details_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Get all IDFW NSGroup VM details for a given NSGroup  # noqa: E501

        Get all Identity Firewall NSGroup VM details for a given NSGroup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nsgroup_vm_details_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: (required)
        :return: IdfwNsgroupVmDetailListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nsgroup_vm_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_nsgroup_vm_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group-id'] = params['group_id']  # noqa: E501

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
            '/idfw/nsgroup-vm-details/{group-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwNsgroupVmDetailListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_system_stats(self, **kwargs):  # noqa: E501
        """Get IDFW system statistics data  # noqa: E501

        Get IDFW system statistics data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_system_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdfwSystemStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_system_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_system_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_system_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get IDFW system statistics data  # noqa: E501

        Get IDFW system statistics data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_system_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdfwSystemStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/idfw/system-stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwSystemStats',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_stats(self, user_id, **kwargs):  # noqa: E501
        """Get IDFW user login events for a given user  # noqa: E501

        Get IDFW user login events for a given user (all active plus up to 5 most recent archived entries).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_stats(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :return: IdfwUserStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_stats_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_stats_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_stats_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Get IDFW user login events for a given user  # noqa: E501

        Get IDFW user login events for a given user (all active plus up to 5 most recent archived entries).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_stats_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :return: IdfwUserStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user-id'] = params['user_id']  # noqa: E501

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
            '/idfw/user-stats/{user-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwUserStats',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_vm_stats(self, vm_ext_id, **kwargs):  # noqa: E501
        """Get IDFW user login events for a given VM  # noqa: E501

        Get IDFW user login events for a given VM (all active plus up to 5 most recent archived entries).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_vm_stats(vm_ext_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_ext_id: (required)
        :return: IdfwVmStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_vm_stats_with_http_info(vm_ext_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_vm_stats_with_http_info(vm_ext_id, **kwargs)  # noqa: E501
            return data

    def get_vm_stats_with_http_info(self, vm_ext_id, **kwargs):  # noqa: E501
        """Get IDFW user login events for a given VM  # noqa: E501

        Get IDFW user login events for a given VM (all active plus up to 5 most recent archived entries).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_vm_stats_with_http_info(vm_ext_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str vm_ext_id: (required)
        :return: IdfwVmStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vm_ext_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vm_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vm_ext_id' is set
        if ('vm_ext_id' not in params or
                params['vm_ext_id'] is None):
            raise ValueError("Missing the required parameter `vm_ext_id` when calling `get_vm_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vm_ext_id' in params:
            path_params['vm-ext-id'] = params['vm_ext_id']  # noqa: E501

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
            '/idfw/vm-stats/{vm-ext-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwVmStats',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_sessions(self, **kwargs):  # noqa: E501
        """Get user session data  # noqa: E501

        Get user session data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_sessions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdfwUserSessionDataAndMappings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_sessions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_sessions_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_sessions_with_http_info(self, **kwargs):  # noqa: E501
        """Get user session data  # noqa: E501

        Get user session data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_sessions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdfwUserSessionDataAndMappings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_sessions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/idfw/user-session-data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwUserSessionDataAndMappings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)