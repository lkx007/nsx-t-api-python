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


class ManagementPlaneApiMigrationMigrationunitsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_migration_unit(self, migration_unit_id, **kwargs):  # noqa: E501
        """Get a specific migration unit  # noqa: E501

        Get a specific migration unit  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_unit(migration_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str migration_unit_id: (required)
        :return: MigrationUnit
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_migration_unit_with_http_info(migration_unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_migration_unit_with_http_info(migration_unit_id, **kwargs)  # noqa: E501
            return data

    def get_migration_unit_with_http_info(self, migration_unit_id, **kwargs):  # noqa: E501
        """Get a specific migration unit  # noqa: E501

        Get a specific migration unit  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_unit_with_http_info(migration_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str migration_unit_id: (required)
        :return: MigrationUnit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['migration_unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_migration_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'migration_unit_id' is set
        if ('migration_unit_id' not in params or
                params['migration_unit_id'] is None):
            raise ValueError("Missing the required parameter `migration_unit_id` when calling `get_migration_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'migration_unit_id' in params:
            path_params['migration-unit-id'] = params['migration_unit_id']  # noqa: E501

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
            '/migration/migration-units/{migration-unit-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MigrationUnit',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_migration_unit_aggregate_info(self, **kwargs):  # noqa: E501
        """Get migration units aggregate-info  # noqa: E501

        Get migration units aggregate-info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_unit_aggregate_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Component type based on which migration units to be filtered
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str group_id: Identifier of group based on which migration units to be filtered
        :param bool has_errors: Flag to indicate whether to return only migration units with errors
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param str metadata: Metadata about migration unit to filter on
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param str selection_status: Flag to indicate whether to return only selected, only deselected or both type of migration units
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: MigrationUnitAggregateInfoListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_migration_unit_aggregate_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_migration_unit_aggregate_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_migration_unit_aggregate_info_with_http_info(self, **kwargs):  # noqa: E501
        """Get migration units aggregate-info  # noqa: E501

        Get migration units aggregate-info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_unit_aggregate_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Component type based on which migration units to be filtered
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str group_id: Identifier of group based on which migration units to be filtered
        :param bool has_errors: Flag to indicate whether to return only migration units with errors
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param str metadata: Metadata about migration unit to filter on
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param str selection_status: Flag to indicate whether to return only selected, only deselected or both type of migration units
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: MigrationUnitAggregateInfoListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_type', 'cursor', 'group_id', 'has_errors', 'included_fields', 'metadata', 'page_size', 'selection_status', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_migration_unit_aggregate_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'component_type' in params:
            query_params.append(('component_type', params['component_type']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'has_errors' in params:
            query_params.append(('has_errors', params['has_errors']))  # noqa: E501
        if 'included_fields' in params:
            query_params.append(('included_fields', params['included_fields']))  # noqa: E501
        if 'metadata' in params:
            query_params.append(('metadata', params['metadata']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'selection_status' in params:
            query_params.append(('selection_status', params['selection_status']))  # noqa: E501
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
            '/migration/migration-units/aggregate-info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MigrationUnitAggregateInfoListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_migration_units(self, **kwargs):  # noqa: E501
        """Get migration units  # noqa: E501

        Get migration units  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_units(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Component type based on which migration units to be filtered
        :param str current_version: Current version of migration unit based on which migration units to be filtered
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str group_id: UUID of group based on which migration units to be filtered
        :param bool has_warnings: Flag to indicate whether to return only migration units with warnings
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param str metadata: Metadata about migration unit to filter on
        :param str migration_unit_type: Migration unit type based on which migration units to be filtered
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: MigrationUnitListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_migration_units_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_migration_units_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_migration_units_with_http_info(self, **kwargs):  # noqa: E501
        """Get migration units  # noqa: E501

        Get migration units  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_units_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Component type based on which migration units to be filtered
        :param str current_version: Current version of migration unit based on which migration units to be filtered
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str group_id: UUID of group based on which migration units to be filtered
        :param bool has_warnings: Flag to indicate whether to return only migration units with warnings
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param str metadata: Metadata about migration unit to filter on
        :param str migration_unit_type: Migration unit type based on which migration units to be filtered
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: MigrationUnitListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_type', 'current_version', 'cursor', 'group_id', 'has_warnings', 'included_fields', 'metadata', 'migration_unit_type', 'page_size', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_migration_units" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'component_type' in params:
            query_params.append(('component_type', params['component_type']))  # noqa: E501
        if 'current_version' in params:
            query_params.append(('current_version', params['current_version']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'has_warnings' in params:
            query_params.append(('has_warnings', params['has_warnings']))  # noqa: E501
        if 'included_fields' in params:
            query_params.append(('included_fields', params['included_fields']))  # noqa: E501
        if 'metadata' in params:
            query_params.append(('metadata', params['metadata']))  # noqa: E501
        if 'migration_unit_type' in params:
            query_params.append(('migration_unit_type', params['migration_unit_type']))  # noqa: E501
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
            '/migration/migration-units', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MigrationUnitListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_migration_units_stats(self, **kwargs):  # noqa: E501
        """Get migration units stats  # noqa: E501

        Get migration units stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_units_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :param bool sync: Synchronize before returning migration unit stats
        :return: MigrationUnitTypeStatsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_migration_units_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_migration_units_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_migration_units_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get migration units stats  # noqa: E501

        Get migration units stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_units_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :param bool sync: Synchronize before returning migration unit stats
        :return: MigrationUnitTypeStatsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor', 'included_fields', 'page_size', 'sort_ascending', 'sort_by', 'sync']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_migration_units_stats" % key
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
        if 'sync' in params:
            query_params.append(('sync', params['sync']))  # noqa: E501

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
            '/migration/migration-units-stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MigrationUnitTypeStatsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
