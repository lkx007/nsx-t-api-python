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


class ManagementPlaneApiNetworkTransportFailureDomainsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_failure_domain(self, body, **kwargs):  # noqa: E501
        """Create Failure Domain  # noqa: E501

        Creates a new failure domain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_failure_domain(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FailureDomain body: (required)
        :return: FailureDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_failure_domain_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_failure_domain_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_failure_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Failure Domain  # noqa: E501

        Creates a new failure domain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_failure_domain_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FailureDomain body: (required)
        :return: FailureDomain
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
                    " to method create_failure_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_failure_domain`")  # noqa: E501

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
            '/failure-domains', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FailureDomain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_failure_domain(self, failure_domain_id, **kwargs):  # noqa: E501
        """Delete Failure Domain  # noqa: E501

        Deletes an existing failure domain. You can not delete system generated default failure domain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_failure_domain(failure_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str failure_domain_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_failure_domain_with_http_info(failure_domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_failure_domain_with_http_info(failure_domain_id, **kwargs)  # noqa: E501
            return data

    def delete_failure_domain_with_http_info(self, failure_domain_id, **kwargs):  # noqa: E501
        """Delete Failure Domain  # noqa: E501

        Deletes an existing failure domain. You can not delete system generated default failure domain.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_failure_domain_with_http_info(failure_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str failure_domain_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['failure_domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_failure_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'failure_domain_id' is set
        if ('failure_domain_id' not in params or
                params['failure_domain_id'] is None):
            raise ValueError("Missing the required parameter `failure_domain_id` when calling `delete_failure_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'failure_domain_id' in params:
            path_params['failure-domain-id'] = params['failure_domain_id']  # noqa: E501

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
            '/failure-domains/{failure-domain-id}', 'DELETE',
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

    def get_failure_domain(self, failure_domain_id, **kwargs):  # noqa: E501
        """Get a Failure Domain  # noqa: E501

        Returns information about a single failure domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_failure_domain(failure_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str failure_domain_id: (required)
        :return: FailureDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_failure_domain_with_http_info(failure_domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_failure_domain_with_http_info(failure_domain_id, **kwargs)  # noqa: E501
            return data

    def get_failure_domain_with_http_info(self, failure_domain_id, **kwargs):  # noqa: E501
        """Get a Failure Domain  # noqa: E501

        Returns information about a single failure domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_failure_domain_with_http_info(failure_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str failure_domain_id: (required)
        :return: FailureDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['failure_domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_failure_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'failure_domain_id' is set
        if ('failure_domain_id' not in params or
                params['failure_domain_id'] is None):
            raise ValueError("Missing the required parameter `failure_domain_id` when calling `get_failure_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'failure_domain_id' in params:
            path_params['failure-domain-id'] = params['failure_domain_id']  # noqa: E501

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
            '/failure-domains/{failure-domain-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FailureDomain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_failure_domains(self, **kwargs):  # noqa: E501
        """List Failure Domains  # noqa: E501

        Returns information about configured failure domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_failure_domains(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FailureDomainListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_failure_domains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_failure_domains_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_failure_domains_with_http_info(self, **kwargs):  # noqa: E501
        """List Failure Domains  # noqa: E501

        Returns information about configured failure domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_failure_domains_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FailureDomainListResult
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
                    " to method list_failure_domains" % key
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
            '/failure-domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FailureDomainListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_failure_domain(self, body, failure_domain_id, **kwargs):  # noqa: E501
        """Update Failure Domain  # noqa: E501

        Updates an existing failure domain. Modifiable parameters are display_name, preferred_active_edge_services flag.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_failure_domain(body, failure_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FailureDomain body: (required)
        :param str failure_domain_id: (required)
        :return: FailureDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_failure_domain_with_http_info(body, failure_domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_failure_domain_with_http_info(body, failure_domain_id, **kwargs)  # noqa: E501
            return data

    def update_failure_domain_with_http_info(self, body, failure_domain_id, **kwargs):  # noqa: E501
        """Update Failure Domain  # noqa: E501

        Updates an existing failure domain. Modifiable parameters are display_name, preferred_active_edge_services flag.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_failure_domain_with_http_info(body, failure_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FailureDomain body: (required)
        :param str failure_domain_id: (required)
        :return: FailureDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'failure_domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_failure_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_failure_domain`")  # noqa: E501
        # verify the required parameter 'failure_domain_id' is set
        if ('failure_domain_id' not in params or
                params['failure_domain_id'] is None):
            raise ValueError("Missing the required parameter `failure_domain_id` when calling `update_failure_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'failure_domain_id' in params:
            path_params['failure-domain-id'] = params['failure_domain_id']  # noqa: E501

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
            '/failure-domains/{failure-domain-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FailureDomain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
