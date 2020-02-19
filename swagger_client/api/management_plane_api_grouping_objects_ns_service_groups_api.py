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


class ManagementPlaneApiGroupingObjectsNsServiceGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_ns_service_group(self, body, **kwargs):  # noqa: E501
        """Create NSServiceGroup  # noqa: E501

        Creates a new NSServiceGroup which can contain NSServices. A given NSServiceGroup can contain either only ether type of NSServices or only non-ether type of NSServices, i.e. an NSServiceGroup cannot contain a mix of both ether and non-ether types of NSServices.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ns_service_group(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NSServiceGroup body: (required)
        :return: NSServiceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_ns_service_group_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_ns_service_group_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_ns_service_group_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create NSServiceGroup  # noqa: E501

        Creates a new NSServiceGroup which can contain NSServices. A given NSServiceGroup can contain either only ether type of NSServices or only non-ether type of NSServices, i.e. an NSServiceGroup cannot contain a mix of both ether and non-ether types of NSServices.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ns_service_group_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NSServiceGroup body: (required)
        :return: NSServiceGroup
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
                    " to method create_ns_service_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_ns_service_group`")  # noqa: E501

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
            '/ns-service-groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NSServiceGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_ns_service_group(self, ns_service_group_id, **kwargs):  # noqa: E501
        """Delete NSServiceGroup  # noqa: E501

        Deletes the specified NSServiceGroup. By default, if the NSServiceGroup is consumed in a Firewall rule, it won't get deleted. In such situations, pass \"force=true\" as query param to force delete the NSServiceGroup.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_ns_service_group(ns_service_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ns_service_group_id: NSServiceGroup Id (required)
        :param bool force: Force delete the resource even if it is being used somewhere 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_ns_service_group_with_http_info(ns_service_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_ns_service_group_with_http_info(ns_service_group_id, **kwargs)  # noqa: E501
            return data

    def delete_ns_service_group_with_http_info(self, ns_service_group_id, **kwargs):  # noqa: E501
        """Delete NSServiceGroup  # noqa: E501

        Deletes the specified NSServiceGroup. By default, if the NSServiceGroup is consumed in a Firewall rule, it won't get deleted. In such situations, pass \"force=true\" as query param to force delete the NSServiceGroup.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_ns_service_group_with_http_info(ns_service_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ns_service_group_id: NSServiceGroup Id (required)
        :param bool force: Force delete the resource even if it is being used somewhere 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ns_service_group_id', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_ns_service_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ns_service_group_id' is set
        if ('ns_service_group_id' not in params or
                params['ns_service_group_id'] is None):
            raise ValueError("Missing the required parameter `ns_service_group_id` when calling `delete_ns_service_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ns_service_group_id' in params:
            path_params['ns-service-group-id'] = params['ns_service_group_id']  # noqa: E501

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

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
            '/ns-service-groups/{ns-service-group-id}', 'DELETE',
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

    def list_ns_service_groups(self, **kwargs):  # noqa: E501
        """List all NSServiceGroups  # noqa: E501

        Returns paginated list of NSServiceGroups   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ns_service_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param bool default_service: Fetch all default NSServiceGroups
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: NSServiceGroupListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_ns_service_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_ns_service_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_ns_service_groups_with_http_info(self, **kwargs):  # noqa: E501
        """List all NSServiceGroups  # noqa: E501

        Returns paginated list of NSServiceGroups   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ns_service_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param bool default_service: Fetch all default NSServiceGroups
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: NSServiceGroupListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor', 'default_service', 'included_fields', 'page_size', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_ns_service_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'default_service' in params:
            query_params.append(('default_service', params['default_service']))  # noqa: E501
        if 'included_fields' in params:
            query_params.append(('included_fields', params['included_fields']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
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
            '/ns-service-groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NSServiceGroupListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_ns_service_group(self, ns_service_group_id, **kwargs):  # noqa: E501
        """Read NSServiceGroup  # noqa: E501

        Returns information about the specified NSServiceGroup   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_ns_service_group(ns_service_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ns_service_group_id: NSServiceGroup Id (required)
        :return: NSServiceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_ns_service_group_with_http_info(ns_service_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_ns_service_group_with_http_info(ns_service_group_id, **kwargs)  # noqa: E501
            return data

    def read_ns_service_group_with_http_info(self, ns_service_group_id, **kwargs):  # noqa: E501
        """Read NSServiceGroup  # noqa: E501

        Returns information about the specified NSServiceGroup   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_ns_service_group_with_http_info(ns_service_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ns_service_group_id: NSServiceGroup Id (required)
        :return: NSServiceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ns_service_group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_ns_service_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ns_service_group_id' is set
        if ('ns_service_group_id' not in params or
                params['ns_service_group_id'] is None):
            raise ValueError("Missing the required parameter `ns_service_group_id` when calling `read_ns_service_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ns_service_group_id' in params:
            path_params['ns-service-group-id'] = params['ns_service_group_id']  # noqa: E501

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
            '/ns-service-groups/{ns-service-group-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NSServiceGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_ns_service_group(self, body, ns_service_group_id, **kwargs):  # noqa: E501
        """Update NSServiceGroup  # noqa: E501

        Updates the specified NSService. Modifiable parameters include the description, display_name and members.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_ns_service_group(body, ns_service_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NSServiceGroup body: (required)
        :param str ns_service_group_id: NSServiceGroup Id (required)
        :return: NSServiceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_ns_service_group_with_http_info(body, ns_service_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_ns_service_group_with_http_info(body, ns_service_group_id, **kwargs)  # noqa: E501
            return data

    def update_ns_service_group_with_http_info(self, body, ns_service_group_id, **kwargs):  # noqa: E501
        """Update NSServiceGroup  # noqa: E501

        Updates the specified NSService. Modifiable parameters include the description, display_name and members.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_ns_service_group_with_http_info(body, ns_service_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NSServiceGroup body: (required)
        :param str ns_service_group_id: NSServiceGroup Id (required)
        :return: NSServiceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'ns_service_group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_ns_service_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_ns_service_group`")  # noqa: E501
        # verify the required parameter 'ns_service_group_id' is set
        if ('ns_service_group_id' not in params or
                params['ns_service_group_id'] is None):
            raise ValueError("Missing the required parameter `ns_service_group_id` when calling `update_ns_service_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ns_service_group_id' in params:
            path_params['ns-service-group-id'] = params['ns_service_group_id']  # noqa: E501

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
            '/ns-service-groups/{ns-service-group-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NSServiceGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)