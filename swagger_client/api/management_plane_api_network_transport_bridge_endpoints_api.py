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


class ManagementPlaneApiNetworkTransportBridgeEndpointsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_bridge_endpoint(self, body, **kwargs):  # noqa: E501
        """Create a Bridge Endpoint  # noqa: E501

        Creates a Bridge Endpoint. It describes the physical attributes of the bridge like vlan. A logical port can be attached to a vif providing bridging functionality from the logical overlay network to the physical vlan network   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bridge_endpoint(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BridgeEndpoint body: (required)
        :return: BridgeEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_bridge_endpoint_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_bridge_endpoint_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_bridge_endpoint_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a Bridge Endpoint  # noqa: E501

        Creates a Bridge Endpoint. It describes the physical attributes of the bridge like vlan. A logical port can be attached to a vif providing bridging functionality from the logical overlay network to the physical vlan network   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bridge_endpoint_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BridgeEndpoint body: (required)
        :return: BridgeEndpoint
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
                    " to method create_bridge_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_bridge_endpoint`")  # noqa: E501

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
            '/bridge-endpoints', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_bridge_endpoint(self, bridgeendpoint_id, **kwargs):  # noqa: E501
        """Delete a Bridge Endpoint  # noqa: E501

        Deletes the specified Bridge Endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bridge_endpoint(bridgeendpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridgeendpoint_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_bridge_endpoint_with_http_info(bridgeendpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_bridge_endpoint_with_http_info(bridgeendpoint_id, **kwargs)  # noqa: E501
            return data

    def delete_bridge_endpoint_with_http_info(self, bridgeendpoint_id, **kwargs):  # noqa: E501
        """Delete a Bridge Endpoint  # noqa: E501

        Deletes the specified Bridge Endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bridge_endpoint_with_http_info(bridgeendpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridgeendpoint_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bridgeendpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bridge_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bridgeendpoint_id' is set
        if ('bridgeendpoint_id' not in params or
                params['bridgeendpoint_id'] is None):
            raise ValueError("Missing the required parameter `bridgeendpoint_id` when calling `delete_bridge_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bridgeendpoint_id' in params:
            path_params['bridgeendpoint-id'] = params['bridgeendpoint_id']  # noqa: E501

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
            '/bridge-endpoints/{bridgeendpoint-id}', 'DELETE',
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

    def get_bridge_endpoint(self, bridgeendpoint_id, **kwargs):  # noqa: E501
        """Get Information about a bridge endpoint  # noqa: E501

        Returns information about a specified bridge endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_endpoint(bridgeendpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridgeendpoint_id: (required)
        :return: BridgeEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bridge_endpoint_with_http_info(bridgeendpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bridge_endpoint_with_http_info(bridgeendpoint_id, **kwargs)  # noqa: E501
            return data

    def get_bridge_endpoint_with_http_info(self, bridgeendpoint_id, **kwargs):  # noqa: E501
        """Get Information about a bridge endpoint  # noqa: E501

        Returns information about a specified bridge endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_endpoint_with_http_info(bridgeendpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridgeendpoint_id: (required)
        :return: BridgeEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bridgeendpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bridge_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bridgeendpoint_id' is set
        if ('bridgeendpoint_id' not in params or
                params['bridgeendpoint_id'] is None):
            raise ValueError("Missing the required parameter `bridgeendpoint_id` when calling `get_bridge_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bridgeendpoint_id' in params:
            path_params['bridgeendpoint-id'] = params['bridgeendpoint_id']  # noqa: E501

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
            '/bridge-endpoints/{bridgeendpoint-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bridge_endpoint_statistics(self, endpoint_id, **kwargs):  # noqa: E501
        """Returns statistics of a specified Bridge Endpoint  # noqa: E501

        Get the statistics for the Bridge Endpoint of the given Endpoint id (endpoint-id)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_endpoint_statistics(endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str endpoint_id: (required)
        :param str source: Data source type.
        :return: BridgeEndpointStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bridge_endpoint_statistics_with_http_info(endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bridge_endpoint_statistics_with_http_info(endpoint_id, **kwargs)  # noqa: E501
            return data

    def get_bridge_endpoint_statistics_with_http_info(self, endpoint_id, **kwargs):  # noqa: E501
        """Returns statistics of a specified Bridge Endpoint  # noqa: E501

        Get the statistics for the Bridge Endpoint of the given Endpoint id (endpoint-id)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_endpoint_statistics_with_http_info(endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str endpoint_id: (required)
        :param str source: Data source type.
        :return: BridgeEndpointStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id', 'source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bridge_endpoint_statistics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `get_bridge_endpoint_statistics`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in params:
            path_params['endpoint-id'] = params['endpoint_id']  # noqa: E501

        query_params = []
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501

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
            '/bridge-endpoints/{endpoint-id}/statistics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeEndpointStatistics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bridge_endpoint_status(self, endpoint_id, **kwargs):  # noqa: E501
        """Returns status of a specified Bridge Endpoint  # noqa: E501

        Get the status for the Bridge Endpoint of the given Endpoint id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_endpoint_status(endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str endpoint_id: (required)
        :param str source: Data source type.
        :return: BridgeEndpointStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bridge_endpoint_status_with_http_info(endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bridge_endpoint_status_with_http_info(endpoint_id, **kwargs)  # noqa: E501
            return data

    def get_bridge_endpoint_status_with_http_info(self, endpoint_id, **kwargs):  # noqa: E501
        """Returns status of a specified Bridge Endpoint  # noqa: E501

        Get the status for the Bridge Endpoint of the given Endpoint id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_endpoint_status_with_http_info(endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str endpoint_id: (required)
        :param str source: Data source type.
        :return: BridgeEndpointStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id', 'source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bridge_endpoint_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if ('endpoint_id' not in params or
                params['endpoint_id'] is None):
            raise ValueError("Missing the required parameter `endpoint_id` when calling `get_bridge_endpoint_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in params:
            path_params['endpoint-id'] = params['endpoint_id']  # noqa: E501

        query_params = []
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501

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
            '/bridge-endpoints/{endpoint-id}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeEndpointStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_bridge_endpoints(self, **kwargs):  # noqa: E501
        """List All Bridge Endpoints  # noqa: E501

        Returns information about all configured bridge endoints   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_bridge_endpoints(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridge_cluster_id: Bridge Cluster Identifier
        :param str bridge_endpoint_profile_id: Bridge endpoint profile used by the edge cluster
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param str logical_switch_id: Logical Switch Identifier
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :param str vlan_transport_zone_id: VLAN transport zone id used by the edge cluster
        :return: BridgeEndpointListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_bridge_endpoints_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_bridge_endpoints_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_bridge_endpoints_with_http_info(self, **kwargs):  # noqa: E501
        """List All Bridge Endpoints  # noqa: E501

        Returns information about all configured bridge endoints   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_bridge_endpoints_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridge_cluster_id: Bridge Cluster Identifier
        :param str bridge_endpoint_profile_id: Bridge endpoint profile used by the edge cluster
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param str logical_switch_id: Logical Switch Identifier
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :param str vlan_transport_zone_id: VLAN transport zone id used by the edge cluster
        :return: BridgeEndpointListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bridge_cluster_id', 'bridge_endpoint_profile_id', 'cursor', 'included_fields', 'logical_switch_id', 'page_size', 'sort_ascending', 'sort_by', 'vlan_transport_zone_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_bridge_endpoints" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bridge_cluster_id' in params:
            query_params.append(('bridge_cluster_id', params['bridge_cluster_id']))  # noqa: E501
        if 'bridge_endpoint_profile_id' in params:
            query_params.append(('bridge_endpoint_profile_id', params['bridge_endpoint_profile_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'included_fields' in params:
            query_params.append(('included_fields', params['included_fields']))  # noqa: E501
        if 'logical_switch_id' in params:
            query_params.append(('logical_switch_id', params['logical_switch_id']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_ascending' in params:
            query_params.append(('sort_ascending', params['sort_ascending']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'vlan_transport_zone_id' in params:
            query_params.append(('vlan_transport_zone_id', params['vlan_transport_zone_id']))  # noqa: E501

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
            '/bridge-endpoints', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeEndpointListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_bridge_endpoint(self, body, bridgeendpoint_id, **kwargs):  # noqa: E501
        """Update a Bridge Endpoint  # noqa: E501

        Modifies a existing bridge endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bridge_endpoint(body, bridgeendpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BridgeEndpoint body: (required)
        :param str bridgeendpoint_id: (required)
        :return: BridgeEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_bridge_endpoint_with_http_info(body, bridgeendpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_bridge_endpoint_with_http_info(body, bridgeendpoint_id, **kwargs)  # noqa: E501
            return data

    def update_bridge_endpoint_with_http_info(self, body, bridgeendpoint_id, **kwargs):  # noqa: E501
        """Update a Bridge Endpoint  # noqa: E501

        Modifies a existing bridge endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bridge_endpoint_with_http_info(body, bridgeendpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BridgeEndpoint body: (required)
        :param str bridgeendpoint_id: (required)
        :return: BridgeEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bridgeendpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bridge_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_bridge_endpoint`")  # noqa: E501
        # verify the required parameter 'bridgeendpoint_id' is set
        if ('bridgeendpoint_id' not in params or
                params['bridgeendpoint_id'] is None):
            raise ValueError("Missing the required parameter `bridgeendpoint_id` when calling `update_bridge_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bridgeendpoint_id' in params:
            path_params['bridgeendpoint-id'] = params['bridgeendpoint_id']  # noqa: E501

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
            '/bridge-endpoints/{bridgeendpoint-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeEndpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
