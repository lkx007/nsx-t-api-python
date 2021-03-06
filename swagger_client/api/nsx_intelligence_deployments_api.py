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


class NsxIntelligenceDeploymentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_pace_cluster_node_vm(self, body, **kwargs):  # noqa: E501
        """Deploy and register a Intelligence cluster node VM  # noqa: E501

        Deploys a Intelligence cluster node VM as specified by the deployment config.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_pace_cluster_node_vm(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddIntelligenceClusterNodeVMInfo body: (required)
        :return: IntelligenceClusterNodeVMDeploymentRequestList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_pace_cluster_node_vm_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_pace_cluster_node_vm_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_pace_cluster_node_vm_with_http_info(self, body, **kwargs):  # noqa: E501
        """Deploy and register a Intelligence cluster node VM  # noqa: E501

        Deploys a Intelligence cluster node VM as specified by the deployment config.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_pace_cluster_node_vm_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddIntelligenceClusterNodeVMInfo body: (required)
        :return: IntelligenceClusterNodeVMDeploymentRequestList
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
                    " to method add_pace_cluster_node_vm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_pace_cluster_node_vm`")  # noqa: E501

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
            '/intelligence/nodes/deployments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntelligenceClusterNodeVMDeploymentRequestList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_auto_deployed_pace_cluster_node_vm_delete(self, node_id, **kwargs):  # noqa: E501
        """Attempt to delete an auto-deployed cluster node VM  # noqa: E501

        Attempts to unregister and undeploy a specified auto-deployed cluster node VM. If it is a member of a cluster, then the VM will be automatically detached from the cluster before being unregistered and undeployed. Alternatively, if the original deployment attempt failed or the VM is not found, cleans up the deployment information associated with the deployment attempt. Note: If a VM has been successfully auto-deployed, then the associated deployment information will not be deleted unless and until the VM is successfully deleted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_auto_deployed_pace_cluster_node_vm_delete(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :param bool force_delete: Delete by force
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_auto_deployed_pace_cluster_node_vm_delete_with_http_info(node_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_auto_deployed_pace_cluster_node_vm_delete_with_http_info(node_id, **kwargs)  # noqa: E501
            return data

    def delete_auto_deployed_pace_cluster_node_vm_delete_with_http_info(self, node_id, **kwargs):  # noqa: E501
        """Attempt to delete an auto-deployed cluster node VM  # noqa: E501

        Attempts to unregister and undeploy a specified auto-deployed cluster node VM. If it is a member of a cluster, then the VM will be automatically detached from the cluster before being unregistered and undeployed. Alternatively, if the original deployment attempt failed or the VM is not found, cleans up the deployment information associated with the deployment attempt. Note: If a VM has been successfully auto-deployed, then the associated deployment information will not be deleted unless and until the VM is successfully deleted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_auto_deployed_pace_cluster_node_vm_delete_with_http_info(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :param bool force_delete: Delete by force
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_id', 'force_delete']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_auto_deployed_pace_cluster_node_vm_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params or
                params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `delete_auto_deployed_pace_cluster_node_vm_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_id' in params:
            path_params['node-id'] = params['node_id']  # noqa: E501

        query_params = []
        if 'force_delete' in params:
            query_params.append(('force_delete', params['force_delete']))  # noqa: E501

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
            '/intelligence/nodes/deployments/{node-id}?action=delete', 'POST',
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

    def list_pace_cluster_node_vm_deployment_requests(self, **kwargs):  # noqa: E501
        """Returns info for all cluster node VM auto-deployment attempts  # noqa: E501

        Returns request information for every attempted deployment of a cluster node VM.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_pace_cluster_node_vm_deployment_requests(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IntelligenceClusterNodeVMDeploymentRequestList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_pace_cluster_node_vm_deployment_requests_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_pace_cluster_node_vm_deployment_requests_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_pace_cluster_node_vm_deployment_requests_with_http_info(self, **kwargs):  # noqa: E501
        """Returns info for all cluster node VM auto-deployment attempts  # noqa: E501

        Returns request information for every attempted deployment of a cluster node VM.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_pace_cluster_node_vm_deployment_requests_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IntelligenceClusterNodeVMDeploymentRequestList
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
                    " to method list_pace_cluster_node_vm_deployment_requests" % key
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
            '/intelligence/nodes/deployments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntelligenceClusterNodeVMDeploymentRequestList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_pace_cluster_node_vm_deployment_request(self, node_id, **kwargs):  # noqa: E501
        """Returns info for a Intelligence cluster node VM auto-deployment attempt  # noqa: E501

        Returns deployment request information for a specific attempted deployment of a cluster node VM.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_pace_cluster_node_vm_deployment_request(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :return: IntelligenceClusterNodeVMDeploymentRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_pace_cluster_node_vm_deployment_request_with_http_info(node_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_pace_cluster_node_vm_deployment_request_with_http_info(node_id, **kwargs)  # noqa: E501
            return data

    def read_pace_cluster_node_vm_deployment_request_with_http_info(self, node_id, **kwargs):  # noqa: E501
        """Returns info for a Intelligence cluster node VM auto-deployment attempt  # noqa: E501

        Returns deployment request information for a specific attempted deployment of a cluster node VM.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_pace_cluster_node_vm_deployment_request_with_http_info(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :return: IntelligenceClusterNodeVMDeploymentRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_pace_cluster_node_vm_deployment_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params or
                params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `read_pace_cluster_node_vm_deployment_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_id' in params:
            path_params['node-id'] = params['node_id']  # noqa: E501

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
            '/intelligence/nodes/deployments/{node-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntelligenceClusterNodeVMDeploymentRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_pace_cluster_node_vm_deployment_status(self, node_id, **kwargs):  # noqa: E501
        """Returns the status of the VM creation/deletion  # noqa: E501

        Returns the current deployment or undeployment status for a VM along with any other relevant current information, such as error messages.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_pace_cluster_node_vm_deployment_status(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :return: IntelligenceClusterNodeVMDeploymentStatusReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_pace_cluster_node_vm_deployment_status_with_http_info(node_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_pace_cluster_node_vm_deployment_status_with_http_info(node_id, **kwargs)  # noqa: E501
            return data

    def read_pace_cluster_node_vm_deployment_status_with_http_info(self, node_id, **kwargs):  # noqa: E501
        """Returns the status of the VM creation/deletion  # noqa: E501

        Returns the current deployment or undeployment status for a VM along with any other relevant current information, such as error messages.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_pace_cluster_node_vm_deployment_status_with_http_info(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :return: IntelligenceClusterNodeVMDeploymentStatusReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_pace_cluster_node_vm_deployment_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params or
                params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `read_pace_cluster_node_vm_deployment_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_id' in params:
            path_params['node-id'] = params['node_id']  # noqa: E501

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
            '/intelligence/nodes/deployments/{node-id}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntelligenceClusterNodeVMDeploymentStatusReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
