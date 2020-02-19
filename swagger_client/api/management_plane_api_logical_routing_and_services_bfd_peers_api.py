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


class ManagementPlaneApiLogicalRoutingAndServicesBfdPeersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_static_hop_bfd_peer(self, body, logical_router_id, **kwargs):  # noqa: E501
        """Create a static hop BFD peer  # noqa: E501

        Creates a BFD peer for static route. The required parameters includes peer IP address.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_static_hop_bfd_peer(body, logical_router_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StaticHopBfdPeer body: (required)
        :param str logical_router_id: (required)
        :return: StaticHopBfdPeer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_static_hop_bfd_peer_with_http_info(body, logical_router_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_static_hop_bfd_peer_with_http_info(body, logical_router_id, **kwargs)  # noqa: E501
            return data

    def create_static_hop_bfd_peer_with_http_info(self, body, logical_router_id, **kwargs):  # noqa: E501
        """Create a static hop BFD peer  # noqa: E501

        Creates a BFD peer for static route. The required parameters includes peer IP address.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_static_hop_bfd_peer_with_http_info(body, logical_router_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StaticHopBfdPeer body: (required)
        :param str logical_router_id: (required)
        :return: StaticHopBfdPeer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'logical_router_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_static_hop_bfd_peer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_static_hop_bfd_peer`")  # noqa: E501
        # verify the required parameter 'logical_router_id' is set
        if ('logical_router_id' not in params or
                params['logical_router_id'] is None):
            raise ValueError("Missing the required parameter `logical_router_id` when calling `create_static_hop_bfd_peer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'logical_router_id' in params:
            path_params['logical-router-id'] = params['logical_router_id']  # noqa: E501

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
            '/logical-routers/{logical-router-id}/routing/static-routes/bfd-peers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StaticHopBfdPeer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_static_hop_bfd_peer(self, logical_router_id, bfd_peer_id, **kwargs):  # noqa: E501
        """Delete a specified static route BFD peer cofigured on a specified logical router  # noqa: E501

        Deletes the specified BFD peer present on specified logical router.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_static_hop_bfd_peer(logical_router_id, bfd_peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logical_router_id: (required)
        :param str bfd_peer_id: (required)
        :param bool force: Force delete the resource even if it is being used somewhere 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_static_hop_bfd_peer_with_http_info(logical_router_id, bfd_peer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_static_hop_bfd_peer_with_http_info(logical_router_id, bfd_peer_id, **kwargs)  # noqa: E501
            return data

    def delete_static_hop_bfd_peer_with_http_info(self, logical_router_id, bfd_peer_id, **kwargs):  # noqa: E501
        """Delete a specified static route BFD peer cofigured on a specified logical router  # noqa: E501

        Deletes the specified BFD peer present on specified logical router.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_static_hop_bfd_peer_with_http_info(logical_router_id, bfd_peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logical_router_id: (required)
        :param str bfd_peer_id: (required)
        :param bool force: Force delete the resource even if it is being used somewhere 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['logical_router_id', 'bfd_peer_id', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_static_hop_bfd_peer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'logical_router_id' is set
        if ('logical_router_id' not in params or
                params['logical_router_id'] is None):
            raise ValueError("Missing the required parameter `logical_router_id` when calling `delete_static_hop_bfd_peer`")  # noqa: E501
        # verify the required parameter 'bfd_peer_id' is set
        if ('bfd_peer_id' not in params or
                params['bfd_peer_id'] is None):
            raise ValueError("Missing the required parameter `bfd_peer_id` when calling `delete_static_hop_bfd_peer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'logical_router_id' in params:
            path_params['logical-router-id'] = params['logical_router_id']  # noqa: E501
        if 'bfd_peer_id' in params:
            path_params['bfd-peer-id'] = params['bfd_peer_id']  # noqa: E501

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
            '/logical-routers/{logical-router-id}/routing/static-routes/bfd-peers/{bfd-peer-id}', 'DELETE',
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

    def list_static_hop_bfd_peers(self, logical_router_id, **kwargs):  # noqa: E501
        """List static routes BFD Peers  # noqa: E501

        Returns information about all BFD peers created on specified logical router for static routes.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_static_hop_bfd_peers(logical_router_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logical_router_id: (required)
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: StaticHopBfdPeerListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_static_hop_bfd_peers_with_http_info(logical_router_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_static_hop_bfd_peers_with_http_info(logical_router_id, **kwargs)  # noqa: E501
            return data

    def list_static_hop_bfd_peers_with_http_info(self, logical_router_id, **kwargs):  # noqa: E501
        """List static routes BFD Peers  # noqa: E501

        Returns information about all BFD peers created on specified logical router for static routes.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_static_hop_bfd_peers_with_http_info(logical_router_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logical_router_id: (required)
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: StaticHopBfdPeerListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['logical_router_id', 'cursor', 'included_fields', 'page_size', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_static_hop_bfd_peers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'logical_router_id' is set
        if ('logical_router_id' not in params or
                params['logical_router_id'] is None):
            raise ValueError("Missing the required parameter `logical_router_id` when calling `list_static_hop_bfd_peers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'logical_router_id' in params:
            path_params['logical-router-id'] = params['logical_router_id']  # noqa: E501

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
            '/logical-routers/{logical-router-id}/routing/static-routes/bfd-peers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StaticHopBfdPeerListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_static_hop_bfd_peer(self, logical_router_id, bfd_peer_id, **kwargs):  # noqa: E501
        """Read a static route BFD peer  # noqa: E501

        Read the BFD peer having specified ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_static_hop_bfd_peer(logical_router_id, bfd_peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logical_router_id: (required)
        :param str bfd_peer_id: (required)
        :return: StaticHopBfdPeer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_static_hop_bfd_peer_with_http_info(logical_router_id, bfd_peer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_static_hop_bfd_peer_with_http_info(logical_router_id, bfd_peer_id, **kwargs)  # noqa: E501
            return data

    def read_static_hop_bfd_peer_with_http_info(self, logical_router_id, bfd_peer_id, **kwargs):  # noqa: E501
        """Read a static route BFD peer  # noqa: E501

        Read the BFD peer having specified ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_static_hop_bfd_peer_with_http_info(logical_router_id, bfd_peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logical_router_id: (required)
        :param str bfd_peer_id: (required)
        :return: StaticHopBfdPeer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['logical_router_id', 'bfd_peer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_static_hop_bfd_peer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'logical_router_id' is set
        if ('logical_router_id' not in params or
                params['logical_router_id'] is None):
            raise ValueError("Missing the required parameter `logical_router_id` when calling `read_static_hop_bfd_peer`")  # noqa: E501
        # verify the required parameter 'bfd_peer_id' is set
        if ('bfd_peer_id' not in params or
                params['bfd_peer_id'] is None):
            raise ValueError("Missing the required parameter `bfd_peer_id` when calling `read_static_hop_bfd_peer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'logical_router_id' in params:
            path_params['logical-router-id'] = params['logical_router_id']  # noqa: E501
        if 'bfd_peer_id' in params:
            path_params['bfd-peer-id'] = params['bfd_peer_id']  # noqa: E501

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
            '/logical-routers/{logical-router-id}/routing/static-routes/bfd-peers/{bfd-peer-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StaticHopBfdPeer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_static_hop_bfd_peer(self, body, logical_router_id, bfd_peer_id, **kwargs):  # noqa: E501
        """Update a static route BFD peer  # noqa: E501

        Modifies the static route BFD peer. Modifiable parameters includes peer IP, enable flag and configuration of the BFD peer.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_static_hop_bfd_peer(body, logical_router_id, bfd_peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StaticHopBfdPeer body: (required)
        :param str logical_router_id: (required)
        :param str bfd_peer_id: (required)
        :return: StaticHopBfdPeer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_static_hop_bfd_peer_with_http_info(body, logical_router_id, bfd_peer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_static_hop_bfd_peer_with_http_info(body, logical_router_id, bfd_peer_id, **kwargs)  # noqa: E501
            return data

    def update_static_hop_bfd_peer_with_http_info(self, body, logical_router_id, bfd_peer_id, **kwargs):  # noqa: E501
        """Update a static route BFD peer  # noqa: E501

        Modifies the static route BFD peer. Modifiable parameters includes peer IP, enable flag and configuration of the BFD peer.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_static_hop_bfd_peer_with_http_info(body, logical_router_id, bfd_peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StaticHopBfdPeer body: (required)
        :param str logical_router_id: (required)
        :param str bfd_peer_id: (required)
        :return: StaticHopBfdPeer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'logical_router_id', 'bfd_peer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_static_hop_bfd_peer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_static_hop_bfd_peer`")  # noqa: E501
        # verify the required parameter 'logical_router_id' is set
        if ('logical_router_id' not in params or
                params['logical_router_id'] is None):
            raise ValueError("Missing the required parameter `logical_router_id` when calling `update_static_hop_bfd_peer`")  # noqa: E501
        # verify the required parameter 'bfd_peer_id' is set
        if ('bfd_peer_id' not in params or
                params['bfd_peer_id'] is None):
            raise ValueError("Missing the required parameter `bfd_peer_id` when calling `update_static_hop_bfd_peer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'logical_router_id' in params:
            path_params['logical-router-id'] = params['logical_router_id']  # noqa: E501
        if 'bfd_peer_id' in params:
            path_params['bfd-peer-id'] = params['bfd_peer_id']  # noqa: E501

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
            '/logical-routers/{logical-router-id}/routing/static-routes/bfd-peers/{bfd-peer-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StaticHopBfdPeer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)