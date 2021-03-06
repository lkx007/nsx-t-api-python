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


class ManagementPlaneApiMigrationPlanApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def abort_migration_abort(self, **kwargs):  # noqa: E501
        """Abort migration  # noqa: E501

        Resets all migration steps done so far, so that migration can be restarted with new setup details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.abort_migration_abort(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.abort_migration_abort_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.abort_migration_abort_with_http_info(**kwargs)  # noqa: E501
            return data

    def abort_migration_abort_with_http_info(self, **kwargs):  # noqa: E501
        """Abort migration  # noqa: E501

        Resets all migration steps done so far, so that migration can be restarted with new setup details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.abort_migration_abort_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method abort_migration_abort" % key
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
            '/migration/plan?action=abort', 'POST',
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

    def continue_migration_continue(self, **kwargs):  # noqa: E501
        """Continue migration  # noqa: E501

        Continue the migration. Resumes the migration from the point where it was paused.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.continue_migration_continue(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool skip: Skip to migration of next component.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.continue_migration_continue_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.continue_migration_continue_with_http_info(**kwargs)  # noqa: E501
            return data

    def continue_migration_continue_with_http_info(self, **kwargs):  # noqa: E501
        """Continue migration  # noqa: E501

        Continue the migration. Resumes the migration from the point where it was paused.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.continue_migration_continue_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool skip: Skip to migration of next component.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method continue_migration_continue" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501

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
            '/migration/plan?action=continue', 'POST',
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

    def finish_migration_finish(self, **kwargs):  # noqa: E501
        """Mark completion of a migration cycle  # noqa: E501

        This API marks the completion of one execution of migration workflow. This API resets internal  execution state and hence needs to be invoked before starting subsequent workflow run.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.finish_migration_finish(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.finish_migration_finish_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.finish_migration_finish_with_http_info(**kwargs)  # noqa: E501
            return data

    def finish_migration_finish_with_http_info(self, **kwargs):  # noqa: E501
        """Mark completion of a migration cycle  # noqa: E501

        This API marks the completion of one execution of migration workflow. This API resets internal  execution state and hence needs to be invoked before starting subsequent workflow run.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.finish_migration_finish_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method finish_migration_finish" % key
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
            '/migration/plan?action=finish', 'POST',
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

    def get_migration_plan_settings(self, component_type, **kwargs):  # noqa: E501
        """Get migration plan settings for the component  # noqa: E501

        Get the migration plan settings for the component.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_plan_settings(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: (required)
        :return: MigrationPlanSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_migration_plan_settings_with_http_info(component_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_migration_plan_settings_with_http_info(component_type, **kwargs)  # noqa: E501
            return data

    def get_migration_plan_settings_with_http_info(self, component_type, **kwargs):  # noqa: E501
        """Get migration plan settings for the component  # noqa: E501

        Get the migration plan settings for the component.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_plan_settings_with_http_info(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: (required)
        :return: MigrationPlanSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_migration_plan_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_type' is set
        if ('component_type' not in params or
                params['component_type'] is None):
            raise ValueError("Missing the required parameter `component_type` when calling `get_migration_plan_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'component_type' in params:
            path_params['component_type'] = params['component_type']  # noqa: E501

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
            '/migration/plan/{component_type}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MigrationPlanSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pause_migration_pause(self, **kwargs):  # noqa: E501
        """Pause migration  # noqa: E501

        Pause the migration. Migration will be paused after migration of all the nodes currently in progress is completed either successfully or with failure. User can make changes in the migration plan when the migration is paused.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pause_migration_pause(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pause_migration_pause_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.pause_migration_pause_with_http_info(**kwargs)  # noqa: E501
            return data

    def pause_migration_pause_with_http_info(self, **kwargs):  # noqa: E501
        """Pause migration  # noqa: E501

        Pause the migration. Migration will be paused after migration of all the nodes currently in progress is completed either successfully or with failure. User can make changes in the migration plan when the migration is paused.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pause_migration_pause_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method pause_migration_pause" % key
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
            '/migration/plan?action=pause', 'POST',
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

    def reset_migration_plan_reset(self, component_type, **kwargs):  # noqa: E501
        """Reset migration plan to default plan  # noqa: E501

        Reset the migration plan to default plan. User has an option to change the default plan. But if after making changes, user wants to go back to the default plan, this is the way to do so.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_migration_plan_reset(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Component type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reset_migration_plan_reset_with_http_info(component_type, **kwargs)  # noqa: E501
        else:
            (data) = self.reset_migration_plan_reset_with_http_info(component_type, **kwargs)  # noqa: E501
            return data

    def reset_migration_plan_reset_with_http_info(self, component_type, **kwargs):  # noqa: E501
        """Reset migration plan to default plan  # noqa: E501

        Reset the migration plan to default plan. User has an option to change the default plan. But if after making changes, user wants to go back to the default plan, this is the way to do so.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_migration_plan_reset_with_http_info(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Component type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_migration_plan_reset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_type' is set
        if ('component_type' not in params or
                params['component_type'] is None):
            raise ValueError("Missing the required parameter `component_type` when calling `reset_migration_plan_reset`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'component_type' in params:
            query_params.append(('component_type', params['component_type']))  # noqa: E501

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
            '/migration/plan?action=reset', 'POST',
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

    def start_migration_start(self, **kwargs):  # noqa: E501
        """Start migration  # noqa: E501

        Start the migration. Migration will start as per the migration plan.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_migration_start(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.start_migration_start_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.start_migration_start_with_http_info(**kwargs)  # noqa: E501
            return data

    def start_migration_start_with_http_info(self, **kwargs):  # noqa: E501
        """Start migration  # noqa: E501

        Start the migration. Migration will start as per the migration plan.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_migration_start_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method start_migration_start" % key
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
            '/migration/plan?action=start', 'POST',
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

    def start_rollback_migration_rollback(self, **kwargs):  # noqa: E501
        """Rollbabck migration  # noqa: E501

        Roll back the migration. Changes applied to target NSX will be reverted. Use the migration status API to monitor progress of roll back.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_rollback_migration_rollback(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.start_rollback_migration_rollback_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.start_rollback_migration_rollback_with_http_info(**kwargs)  # noqa: E501
            return data

    def start_rollback_migration_rollback_with_http_info(self, **kwargs):  # noqa: E501
        """Rollbabck migration  # noqa: E501

        Roll back the migration. Changes applied to target NSX will be reverted. Use the migration status API to monitor progress of roll back.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_rollback_migration_rollback_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method start_rollback_migration_rollback" % key
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
            '/migration/plan?action=rollback', 'POST',
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

    def update_migration_plan_settings(self, body, component_type, **kwargs):  # noqa: E501
        """Update migration plan settings for the component  # noqa: E501

        Update the migration plan settings for the component.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_migration_plan_settings(body, component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MigrationPlanSettings body: (required)
        :param str component_type: (required)
        :return: MigrationPlanSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_migration_plan_settings_with_http_info(body, component_type, **kwargs)  # noqa: E501
        else:
            (data) = self.update_migration_plan_settings_with_http_info(body, component_type, **kwargs)  # noqa: E501
            return data

    def update_migration_plan_settings_with_http_info(self, body, component_type, **kwargs):  # noqa: E501
        """Update migration plan settings for the component  # noqa: E501

        Update the migration plan settings for the component.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_migration_plan_settings_with_http_info(body, component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MigrationPlanSettings body: (required)
        :param str component_type: (required)
        :return: MigrationPlanSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'component_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_migration_plan_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_migration_plan_settings`")  # noqa: E501
        # verify the required parameter 'component_type' is set
        if ('component_type' not in params or
                params['component_type'] is None):
            raise ValueError("Missing the required parameter `component_type` when calling `update_migration_plan_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'component_type' in params:
            path_params['component_type'] = params['component_type']  # noqa: E501

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
            '/migration/plan/{component_type}/settings', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MigrationPlanSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
