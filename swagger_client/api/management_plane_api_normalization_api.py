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


class ManagementPlaneApiNormalizationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_normalizations(self, preferred_normalization_type, resource_id, resource_type, **kwargs):  # noqa: E501
        """Get normalizations based on the query parameters  # noqa: E501

        Returns the list of normalized resources based on the query parameters. Id and Type of the resource on which the normalizations is to be performed, are to be specified as query parameters in the URI. The target resource types to which normalization is to be done should also be specified as query parameter.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_normalizations(preferred_normalization_type, resource_id, resource_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str preferred_normalization_type: Resource type valid for use as target in normalization API. (required)
        :param str resource_id: Identifier of the resource on which normalization is to be performed (required)
        :param str resource_type: Resource type valid for use as source in normalization API. (required)
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: NormalizedResourceListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_normalizations_with_http_info(preferred_normalization_type, resource_id, resource_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_normalizations_with_http_info(preferred_normalization_type, resource_id, resource_type, **kwargs)  # noqa: E501
            return data

    def get_normalizations_with_http_info(self, preferred_normalization_type, resource_id, resource_type, **kwargs):  # noqa: E501
        """Get normalizations based on the query parameters  # noqa: E501

        Returns the list of normalized resources based on the query parameters. Id and Type of the resource on which the normalizations is to be performed, are to be specified as query parameters in the URI. The target resource types to which normalization is to be done should also be specified as query parameter.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_normalizations_with_http_info(preferred_normalization_type, resource_id, resource_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str preferred_normalization_type: Resource type valid for use as target in normalization API. (required)
        :param str resource_id: Identifier of the resource on which normalization is to be performed (required)
        :param str resource_type: Resource type valid for use as source in normalization API. (required)
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: NormalizedResourceListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['preferred_normalization_type', 'resource_id', 'resource_type', 'cursor', 'included_fields', 'page_size', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_normalizations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'preferred_normalization_type' is set
        if ('preferred_normalization_type' not in params or
                params['preferred_normalization_type'] is None):
            raise ValueError("Missing the required parameter `preferred_normalization_type` when calling `get_normalizations`")  # noqa: E501
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params or
                params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `get_normalizations`")  # noqa: E501
        # verify the required parameter 'resource_type' is set
        if ('resource_type' not in params or
                params['resource_type'] is None):
            raise ValueError("Missing the required parameter `resource_type` when calling `get_normalizations`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'included_fields' in params:
            query_params.append(('included_fields', params['included_fields']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'preferred_normalization_type' in params:
            query_params.append(('preferred_normalization_type', params['preferred_normalization_type']))  # noqa: E501
        if 'resource_id' in params:
            query_params.append(('resource_id', params['resource_id']))  # noqa: E501
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
            '/normalizations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NormalizedResourceListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)