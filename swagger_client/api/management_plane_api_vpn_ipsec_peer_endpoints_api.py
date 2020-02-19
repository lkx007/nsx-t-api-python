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


class ManagementPlaneApiVpnIpsecPeerEndpointsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_ip_sec_vpn_peer_end_point(self, body, **kwargs):  # noqa: E501
        """Create custom peer endpoint  # noqa: E501

        Create custom IPSec peer endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ip_sec_vpn_peer_end_point(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IPSecVPNPeerEndpoint body: (required)
        :return: IPSecVPNPeerEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_ip_sec_vpn_peer_end_point_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_ip_sec_vpn_peer_end_point_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_ip_sec_vpn_peer_end_point_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create custom peer endpoint  # noqa: E501

        Create custom IPSec peer endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ip_sec_vpn_peer_end_point_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IPSecVPNPeerEndpoint body: (required)
        :return: IPSecVPNPeerEndpoint
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
                    " to method create_ip_sec_vpn_peer_end_point" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_ip_sec_vpn_peer_end_point`")  # noqa: E501

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
            '/vpn/ipsec/peer-endpoints', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IPSecVPNPeerEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_ip_sec_vpn_peer_endpoint(self, ipsec_vpn_peer_endpoint_id, **kwargs):  # noqa: E501
        """Delete custom IPSec VPN peer endpoint  # noqa: E501

        Delete custom IPSec VPN peer endpoint. All references are strong references and dependent peer endpoints can not be deleted if being referenced.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_ip_sec_vpn_peer_endpoint(ipsec_vpn_peer_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ipsec_vpn_peer_endpoint_id: (required)
        :param bool force: Force delete the resource even if it is being used somewhere 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_ip_sec_vpn_peer_endpoint_with_http_info(ipsec_vpn_peer_endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_ip_sec_vpn_peer_endpoint_with_http_info(ipsec_vpn_peer_endpoint_id, **kwargs)  # noqa: E501
            return data

    def delete_ip_sec_vpn_peer_endpoint_with_http_info(self, ipsec_vpn_peer_endpoint_id, **kwargs):  # noqa: E501
        """Delete custom IPSec VPN peer endpoint  # noqa: E501

        Delete custom IPSec VPN peer endpoint. All references are strong references and dependent peer endpoints can not be deleted if being referenced.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_ip_sec_vpn_peer_endpoint_with_http_info(ipsec_vpn_peer_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ipsec_vpn_peer_endpoint_id: (required)
        :param bool force: Force delete the resource even if it is being used somewhere 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ipsec_vpn_peer_endpoint_id', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_ip_sec_vpn_peer_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ipsec_vpn_peer_endpoint_id' is set
        if ('ipsec_vpn_peer_endpoint_id' not in params or
                params['ipsec_vpn_peer_endpoint_id'] is None):
            raise ValueError("Missing the required parameter `ipsec_vpn_peer_endpoint_id` when calling `delete_ip_sec_vpn_peer_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ipsec_vpn_peer_endpoint_id' in params:
            path_params['ipsec-vpn-peer-endpoint-id'] = params['ipsec_vpn_peer_endpoint_id']  # noqa: E501

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
            '/vpn/ipsec/peer-endpoints/{ipsec-vpn-peer-endpoint-id}', 'DELETE',
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

    def get_ip_sec_vpn_peer_endpoint(self, ipsec_vpn_peer_endpoint_id, **kwargs):  # noqa: E501
        """Get IPSec VPN peer endpoint  # noqa: E501

        Get custom IPSec VPN peer endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_sec_vpn_peer_endpoint(ipsec_vpn_peer_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ipsec_vpn_peer_endpoint_id: (required)
        :return: IPSecVPNPeerEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ip_sec_vpn_peer_endpoint_with_http_info(ipsec_vpn_peer_endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ip_sec_vpn_peer_endpoint_with_http_info(ipsec_vpn_peer_endpoint_id, **kwargs)  # noqa: E501
            return data

    def get_ip_sec_vpn_peer_endpoint_with_http_info(self, ipsec_vpn_peer_endpoint_id, **kwargs):  # noqa: E501
        """Get IPSec VPN peer endpoint  # noqa: E501

        Get custom IPSec VPN peer endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_sec_vpn_peer_endpoint_with_http_info(ipsec_vpn_peer_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ipsec_vpn_peer_endpoint_id: (required)
        :return: IPSecVPNPeerEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ipsec_vpn_peer_endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ip_sec_vpn_peer_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ipsec_vpn_peer_endpoint_id' is set
        if ('ipsec_vpn_peer_endpoint_id' not in params or
                params['ipsec_vpn_peer_endpoint_id'] is None):
            raise ValueError("Missing the required parameter `ipsec_vpn_peer_endpoint_id` when calling `get_ip_sec_vpn_peer_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ipsec_vpn_peer_endpoint_id' in params:
            path_params['ipsec-vpn-peer-endpoint-id'] = params['ipsec_vpn_peer_endpoint_id']  # noqa: E501

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
            '/vpn/ipsec/peer-endpoints/{ipsec-vpn-peer-endpoint-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IPSecVPNPeerEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data(self, ipsec_vpn_peer_endpoint_id, **kwargs):  # noqa: E501
        """Get IPSec VPN peer endpoint with PSK  # noqa: E501

        Get custom IPSec VPN peer endpoint with PSK.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data(ipsec_vpn_peer_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ipsec_vpn_peer_endpoint_id: (required)
        :return: IPSecVPNPeerEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data_with_http_info(ipsec_vpn_peer_endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data_with_http_info(ipsec_vpn_peer_endpoint_id, **kwargs)  # noqa: E501
            return data

    def get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data_with_http_info(self, ipsec_vpn_peer_endpoint_id, **kwargs):  # noqa: E501
        """Get IPSec VPN peer endpoint with PSK  # noqa: E501

        Get custom IPSec VPN peer endpoint with PSK.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data_with_http_info(ipsec_vpn_peer_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ipsec_vpn_peer_endpoint_id: (required)
        :return: IPSecVPNPeerEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ipsec_vpn_peer_endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ipsec_vpn_peer_endpoint_id' is set
        if ('ipsec_vpn_peer_endpoint_id' not in params or
                params['ipsec_vpn_peer_endpoint_id'] is None):
            raise ValueError("Missing the required parameter `ipsec_vpn_peer_endpoint_id` when calling `get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ipsec_vpn_peer_endpoint_id' in params:
            path_params['ipsec-vpn-peer-endpoint-id'] = params['ipsec_vpn_peer_endpoint_id']  # noqa: E501

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
            '/vpn/ipsec/peer-endpoints/{ipsec-vpn-peer-endpoint-id}?action=show-sensitive-data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IPSecVPNPeerEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_ip_sec_vpn_peer_endpoints(self, **kwargs):  # noqa: E501
        """Get IPSecVPNPeerEndpoint List Result  # noqa: E501

        Get paginated list of all peer endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ip_sec_vpn_peer_endpoints(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: IPSecVPNPeerEndpointListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_ip_sec_vpn_peer_endpoints_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_ip_sec_vpn_peer_endpoints_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_ip_sec_vpn_peer_endpoints_with_http_info(self, **kwargs):  # noqa: E501
        """Get IPSecVPNPeerEndpoint List Result  # noqa: E501

        Get paginated list of all peer endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ip_sec_vpn_peer_endpoints_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: IPSecVPNPeerEndpointListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor', 'included_fields', 'page_size', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_ip_sec_vpn_peer_endpoints" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
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
            '/vpn/ipsec/peer-endpoints', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IPSecVPNPeerEndpointListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_ip_sec_vpn_peer_endpoint(self, body, ipsec_vpn_peer_endpoint_id, **kwargs):  # noqa: E501
        """Edit custom IPSecPeerEndpoint  # noqa: E501

        Edit custom IPSec peer endpoint. System owned endpoints are non editable.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_ip_sec_vpn_peer_endpoint(body, ipsec_vpn_peer_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IPSecVPNPeerEndpoint body: (required)
        :param str ipsec_vpn_peer_endpoint_id: (required)
        :return: IPSecVPNPeerEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_ip_sec_vpn_peer_endpoint_with_http_info(body, ipsec_vpn_peer_endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_ip_sec_vpn_peer_endpoint_with_http_info(body, ipsec_vpn_peer_endpoint_id, **kwargs)  # noqa: E501
            return data

    def update_ip_sec_vpn_peer_endpoint_with_http_info(self, body, ipsec_vpn_peer_endpoint_id, **kwargs):  # noqa: E501
        """Edit custom IPSecPeerEndpoint  # noqa: E501

        Edit custom IPSec peer endpoint. System owned endpoints are non editable.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_ip_sec_vpn_peer_endpoint_with_http_info(body, ipsec_vpn_peer_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IPSecVPNPeerEndpoint body: (required)
        :param str ipsec_vpn_peer_endpoint_id: (required)
        :return: IPSecVPNPeerEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'ipsec_vpn_peer_endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_ip_sec_vpn_peer_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_ip_sec_vpn_peer_endpoint`")  # noqa: E501
        # verify the required parameter 'ipsec_vpn_peer_endpoint_id' is set
        if ('ipsec_vpn_peer_endpoint_id' not in params or
                params['ipsec_vpn_peer_endpoint_id'] is None):
            raise ValueError("Missing the required parameter `ipsec_vpn_peer_endpoint_id` when calling `update_ip_sec_vpn_peer_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ipsec_vpn_peer_endpoint_id' in params:
            path_params['ipsec-vpn-peer-endpoint-id'] = params['ipsec_vpn_peer_endpoint_id']  # noqa: E501

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
            '/vpn/ipsec/peer-endpoints/{ipsec-vpn-peer-endpoint-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IPSecVPNPeerEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
