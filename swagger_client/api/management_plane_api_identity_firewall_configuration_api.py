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


class ManagementPlaneApiIdentityFirewallConfigurationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_enabled_compute_collection(self, cc_ext_id, **kwargs):  # noqa: E501
        """Get IDFW compute collection.  # noqa: E501

        Get enable/disable status of individual compute collections for IDFW.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_enabled_compute_collection(cc_ext_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cc_ext_id: (required)
        :return: IdfwEnabledComputeCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_enabled_compute_collection_with_http_info(cc_ext_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_enabled_compute_collection_with_http_info(cc_ext_id, **kwargs)  # noqa: E501
            return data

    def get_enabled_compute_collection_with_http_info(self, cc_ext_id, **kwargs):  # noqa: E501
        """Get IDFW compute collection.  # noqa: E501

        Get enable/disable status of individual compute collections for IDFW.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_enabled_compute_collection_with_http_info(cc_ext_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cc_ext_id: (required)
        :return: IdfwEnabledComputeCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cc_ext_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_enabled_compute_collection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cc_ext_id' is set
        if ('cc_ext_id' not in params or
                params['cc_ext_id'] is None):
            raise ValueError("Missing the required parameter `cc_ext_id` when calling `get_enabled_compute_collection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cc_ext_id' in params:
            path_params['cc-ext-id'] = params['cc_ext_id']  # noqa: E501

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
            '/idfw/idfw-compute-collections/{cc-ext-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwEnabledComputeCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_master_switch_setting(self, **kwargs):  # noqa: E501
        """Get Identity Firewall master switch enabled/disabled  # noqa: E501

        Fetches IDFW master switch setting to check whether master switch is enabled or disabled   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_master_switch_setting(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdfwMasterSwitchSetting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_master_switch_setting_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_master_switch_setting_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_master_switch_setting_with_http_info(self, **kwargs):  # noqa: E501
        """Get Identity Firewall master switch enabled/disabled  # noqa: E501

        Fetches IDFW master switch setting to check whether master switch is enabled or disabled   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_master_switch_setting_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdfwMasterSwitchSetting
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
                    " to method get_master_switch_setting" % key
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
            '/idfw/master-switch-setting', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwMasterSwitchSetting',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_standalone_hosts_switch_setting(self, **kwargs):  # noqa: E501
        """Get Standalone hosts switch enabled/disabled  # noqa: E501

        Fetches IDFW standalone hosts switch setting to check whether standalone hosts is enabled or disabled   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_standalone_hosts_switch_setting(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdfwStandaloneHostsSwitchSetting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_standalone_hosts_switch_setting_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_standalone_hosts_switch_setting_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_standalone_hosts_switch_setting_with_http_info(self, **kwargs):  # noqa: E501
        """Get Standalone hosts switch enabled/disabled  # noqa: E501

        Fetches IDFW standalone hosts switch setting to check whether standalone hosts is enabled or disabled   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_standalone_hosts_switch_setting_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdfwStandaloneHostsSwitchSetting
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
                    " to method get_standalone_hosts_switch_setting" % key
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
            '/idfw/standalone-host-switch-setting', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwStandaloneHostsSwitchSetting',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_enabled_compute_collections(self, **kwargs):  # noqa: E501
        """List all Identity firewall compute collections  # noqa: E501

        List all Identity firewall compute collections.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_enabled_compute_collections(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: IdfwEnabledComputeCollectionListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_enabled_compute_collections_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_enabled_compute_collections_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_enabled_compute_collections_with_http_info(self, **kwargs):  # noqa: E501
        """List all Identity firewall compute collections  # noqa: E501

        List all Identity firewall compute collections.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_enabled_compute_collections_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: IdfwEnabledComputeCollectionListResult
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
                    " to method list_enabled_compute_collections" % key
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
            '/idfw/idfw-compute-collections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwEnabledComputeCollectionListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_enabled_compute_collection(self, body, cc_ext_id, **kwargs):  # noqa: E501
        """Update IDFW compute collection  # noqa: E501

        Enable/disable individual compute collections for IDFW.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_enabled_compute_collection(body, cc_ext_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdfwEnabledComputeCollection body: (required)
        :param str cc_ext_id: (required)
        :return: IdfwEnabledComputeCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_enabled_compute_collection_with_http_info(body, cc_ext_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_enabled_compute_collection_with_http_info(body, cc_ext_id, **kwargs)  # noqa: E501
            return data

    def update_enabled_compute_collection_with_http_info(self, body, cc_ext_id, **kwargs):  # noqa: E501
        """Update IDFW compute collection  # noqa: E501

        Enable/disable individual compute collections for IDFW.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_enabled_compute_collection_with_http_info(body, cc_ext_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdfwEnabledComputeCollection body: (required)
        :param str cc_ext_id: (required)
        :return: IdfwEnabledComputeCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'cc_ext_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_enabled_compute_collection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_enabled_compute_collection`")  # noqa: E501
        # verify the required parameter 'cc_ext_id' is set
        if ('cc_ext_id' not in params or
                params['cc_ext_id'] is None):
            raise ValueError("Missing the required parameter `cc_ext_id` when calling `update_enabled_compute_collection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cc_ext_id' in params:
            path_params['cc-ext-id'] = params['cc_ext_id']  # noqa: E501

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
            '/idfw/idfw-compute-collections/{cc-ext-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwEnabledComputeCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_master_switch_setting(self, body, **kwargs):  # noqa: E501
        """Update IDFW master switch setting enabled/disabled  # noqa: E501

        Update Identity Firewall master switch setting (true=enabled / false=disabled). Identity Firewall master switch setting enables or disables Identity Firewall feature across the system.  It affects compute collections, hypervisor and virtual machines.  This operation is expensive and also has big impact and implication on system perforamce.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_master_switch_setting(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdfwMasterSwitchSetting body: (required)
        :return: IdfwMasterSwitchSetting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_master_switch_setting_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_master_switch_setting_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_master_switch_setting_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update IDFW master switch setting enabled/disabled  # noqa: E501

        Update Identity Firewall master switch setting (true=enabled / false=disabled). Identity Firewall master switch setting enables or disables Identity Firewall feature across the system.  It affects compute collections, hypervisor and virtual machines.  This operation is expensive and also has big impact and implication on system perforamce.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_master_switch_setting_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdfwMasterSwitchSetting body: (required)
        :return: IdfwMasterSwitchSetting
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
                    " to method update_master_switch_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_master_switch_setting`")  # noqa: E501

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
            '/idfw/master-switch-setting', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwMasterSwitchSetting',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_standalone_hosts_switch_setting(self, body, **kwargs):  # noqa: E501
        """Update IDFW master switch setting enabled/disabled  # noqa: E501

        Update Identity Firewall standalone hosts switch setting (true=enabled / false=disabled).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_standalone_hosts_switch_setting(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdfwStandaloneHostsSwitchSetting body: (required)
        :return: IdfwStandaloneHostsSwitchSetting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_standalone_hosts_switch_setting_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_standalone_hosts_switch_setting_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_standalone_hosts_switch_setting_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update IDFW master switch setting enabled/disabled  # noqa: E501

        Update Identity Firewall standalone hosts switch setting (true=enabled / false=disabled).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_standalone_hosts_switch_setting_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdfwStandaloneHostsSwitchSetting body: (required)
        :return: IdfwStandaloneHostsSwitchSetting
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
                    " to method update_standalone_hosts_switch_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_standalone_hosts_switch_setting`")  # noqa: E501

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
            '/idfw/standalone-host-switch-setting', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdfwStandaloneHostsSwitchSetting',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
