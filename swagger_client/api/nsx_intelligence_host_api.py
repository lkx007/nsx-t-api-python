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


class NsxIntelligenceHostApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_pace_host_configuration(self, **kwargs):  # noqa: E501
        """Get NSX-Intelligence host configuration  # noqa: E501

        Get the current NSX-Intelligence host configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pace_host_configuration(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IntelligenceHostConfigurationInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pace_host_configuration_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_pace_host_configuration_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_pace_host_configuration_with_http_info(self, **kwargs):  # noqa: E501
        """Get NSX-Intelligence host configuration  # noqa: E501

        Get the current NSX-Intelligence host configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pace_host_configuration_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IntelligenceHostConfigurationInfo
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
                    " to method get_pace_host_configuration" % key
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
            '/intelligence/host-config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntelligenceHostConfigurationInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_pace_host_configuration(self, body, **kwargs):  # noqa: E501
        """Patch NSX-Intelligence host configuration  # noqa: E501

        Patch the current NSX-Intelligence host configuration. Return error if NSX-Intelligence is not registered with NSX.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_pace_host_configuration(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IntelligenceHostConfigurationInfo body: (required)
        :return: IntelligenceHostConfigurationInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_pace_host_configuration_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_pace_host_configuration_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def patch_pace_host_configuration_with_http_info(self, body, **kwargs):  # noqa: E501
        """Patch NSX-Intelligence host configuration  # noqa: E501

        Patch the current NSX-Intelligence host configuration. Return error if NSX-Intelligence is not registered with NSX.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_pace_host_configuration_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IntelligenceHostConfigurationInfo body: (required)
        :return: IntelligenceHostConfigurationInfo
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
                    " to method patch_pace_host_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_pace_host_configuration`")  # noqa: E501

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
            '/intelligence/host-config', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntelligenceHostConfigurationInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_pace_host_configuration_reset(self, **kwargs):  # noqa: E501
        """Reset NSX-Intelligence host configuration  # noqa: E501

        Reset NSX-Intelligence host configuration to the default setting. Clear NSX-Intelligence host configuration if NSX-Intelligence is not registered with NSX. Return the NSX-Intelligence host configuration after reset operation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_pace_host_configuration_reset(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IntelligenceHostConfigurationInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reset_pace_host_configuration_reset_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.reset_pace_host_configuration_reset_with_http_info(**kwargs)  # noqa: E501
            return data

    def reset_pace_host_configuration_reset_with_http_info(self, **kwargs):  # noqa: E501
        """Reset NSX-Intelligence host configuration  # noqa: E501

        Reset NSX-Intelligence host configuration to the default setting. Clear NSX-Intelligence host configuration if NSX-Intelligence is not registered with NSX. Return the NSX-Intelligence host configuration after reset operation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_pace_host_configuration_reset_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IntelligenceHostConfigurationInfo
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
                    " to method reset_pace_host_configuration_reset" % key
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
            '/intelligence/host-config?action=reset', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntelligenceHostConfigurationInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
