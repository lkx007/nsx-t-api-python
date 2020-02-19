# coding: utf-8

"""
    NSX-T Manager API

    VMware NSX-T Manager REST API  # noqa: E501

    OpenAPI spec version: 2.5.1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.management_plane_api_services_loadbalancer_api import ManagementPlaneApiServicesLoadbalancerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiServicesLoadbalancerApi(unittest.TestCase):
    """ManagementPlaneApiServicesLoadbalancerApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_services_loadbalancer_api.ManagementPlaneApiServicesLoadbalancerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_load_balancer_application_profile(self):
        """Test case for create_load_balancer_application_profile

        Create a load balancer application profile  # noqa: E501
        """
        pass

    def test_create_load_balancer_client_ssl_profile(self):
        """Test case for create_load_balancer_client_ssl_profile

        Create a load balancer client-ssl profile  # noqa: E501
        """
        pass

    def test_create_load_balancer_monitor(self):
        """Test case for create_load_balancer_monitor

        Create a load balancer monitor  # noqa: E501
        """
        pass

    def test_create_load_balancer_persistence_profile(self):
        """Test case for create_load_balancer_persistence_profile

        Create a load balancer persistence profile  # noqa: E501
        """
        pass

    def test_create_load_balancer_pool(self):
        """Test case for create_load_balancer_pool

        Create a load balancer pool  # noqa: E501
        """
        pass

    def test_create_load_balancer_rule(self):
        """Test case for create_load_balancer_rule

        Create a load balancer rule  # noqa: E501
        """
        pass

    def test_create_load_balancer_server_ssl_profile(self):
        """Test case for create_load_balancer_server_ssl_profile

        Create a load balancer server-ssl profile  # noqa: E501
        """
        pass

    def test_create_load_balancer_service(self):
        """Test case for create_load_balancer_service

        Create a load balancer service  # noqa: E501
        """
        pass

    def test_create_load_balancer_tcp_profile(self):
        """Test case for create_load_balancer_tcp_profile

        Create a load balancer TCP profile  # noqa: E501
        """
        pass

    def test_create_load_balancer_virtual_server(self):
        """Test case for create_load_balancer_virtual_server

        Create a load balancer virtual server  # noqa: E501
        """
        pass

    def test_create_load_balancer_virtual_server_with_rules_create_with_rules(self):
        """Test case for create_load_balancer_virtual_server_with_rules_create_with_rules

        Create a load balancer virtual server with rules  # noqa: E501
        """
        pass

    def test_delete_load_balancer_application_profile(self):
        """Test case for delete_load_balancer_application_profile

        Delete a load balancer application profile  # noqa: E501
        """
        pass

    def test_delete_load_balancer_client_ssl_profile(self):
        """Test case for delete_load_balancer_client_ssl_profile

        Delete a load balancer client-ssl profile  # noqa: E501
        """
        pass

    def test_delete_load_balancer_monitor(self):
        """Test case for delete_load_balancer_monitor

        Delete a load balancer monitor  # noqa: E501
        """
        pass

    def test_delete_load_balancer_persistence_profile(self):
        """Test case for delete_load_balancer_persistence_profile

        Delete a load balancer persistence profile  # noqa: E501
        """
        pass

    def test_delete_load_balancer_pool(self):
        """Test case for delete_load_balancer_pool

        Delete a load balancer pool  # noqa: E501
        """
        pass

    def test_delete_load_balancer_rule(self):
        """Test case for delete_load_balancer_rule

        Delete a load balancer rule  # noqa: E501
        """
        pass

    def test_delete_load_balancer_server_ssl_profile(self):
        """Test case for delete_load_balancer_server_ssl_profile

        Delete a load balancer server-ssl profile  # noqa: E501
        """
        pass

    def test_delete_load_balancer_service(self):
        """Test case for delete_load_balancer_service

        Delete a load balancer service  # noqa: E501
        """
        pass

    def test_delete_load_balancer_tcp_profile(self):
        """Test case for delete_load_balancer_tcp_profile

        Delete a load balancer TCP profile  # noqa: E501
        """
        pass

    def test_delete_load_balancer_virtual_server(self):
        """Test case for delete_load_balancer_virtual_server

        Delete a load balancer virtual server  # noqa: E501
        """
        pass

    def test_get_load_balancer_pool_statistics(self):
        """Test case for get_load_balancer_pool_statistics

        Get the statistics of load balancer pool  # noqa: E501
        """
        pass

    def test_get_load_balancer_pool_status(self):
        """Test case for get_load_balancer_pool_status

        Get the status of load balancer pool  # noqa: E501
        """
        pass

    def test_get_load_balancer_service_statistics(self):
        """Test case for get_load_balancer_service_statistics

        Get the statistics of load balancer service  # noqa: E501
        """
        pass

    def test_get_load_balancer_service_status(self):
        """Test case for get_load_balancer_service_status

        Get the status of the given load balancer service  # noqa: E501
        """
        pass

    def test_get_load_balancer_virtual_server_statistics(self):
        """Test case for get_load_balancer_virtual_server_statistics

        Get the statistics of the given load balancer virtual server  # noqa: E501
        """
        pass

    def test_get_load_balancer_virtual_server_status(self):
        """Test case for get_load_balancer_virtual_server_status

        Get the status of the load balancer virtual server  # noqa: E501
        """
        pass

    def test_list_load_balancer_application_profiles(self):
        """Test case for list_load_balancer_application_profiles

        Retrieve a paginated list of load balancer application profiles  # noqa: E501
        """
        pass

    def test_list_load_balancer_client_ssl_profiles(self):
        """Test case for list_load_balancer_client_ssl_profiles

        Retrieve a paginated list of load balancer client-ssl profiles  # noqa: E501
        """
        pass

    def test_list_load_balancer_monitors(self):
        """Test case for list_load_balancer_monitors

        Retrieve a paginated list of load balancer monitors  # noqa: E501
        """
        pass

    def test_list_load_balancer_persistence_profiles(self):
        """Test case for list_load_balancer_persistence_profiles

        Retrieve a paginated list of load balancer persistence profiles  # noqa: E501
        """
        pass

    def test_list_load_balancer_pool_statistics(self):
        """Test case for list_load_balancer_pool_statistics

        Get the statistics list of load balancer pools  # noqa: E501
        """
        pass

    def test_list_load_balancer_pool_statuses(self):
        """Test case for list_load_balancer_pool_statuses

        Get the status list of load balancer pools  # noqa: E501
        """
        pass

    def test_list_load_balancer_pools(self):
        """Test case for list_load_balancer_pools

        Retrieve a paginated list of load balancer pools  # noqa: E501
        """
        pass

    def test_list_load_balancer_rules(self):
        """Test case for list_load_balancer_rules

        Retrieve a paginated list of load balancer rules  # noqa: E501
        """
        pass

    def test_list_load_balancer_server_ssl_profiles(self):
        """Test case for list_load_balancer_server_ssl_profiles

        Retrieve a paginated list of load balancer server-ssl profiles  # noqa: E501
        """
        pass

    def test_list_load_balancer_services(self):
        """Test case for list_load_balancer_services

        Retrieve a paginated list of load balancer services  # noqa: E501
        """
        pass

    def test_list_load_balancer_ssl_ciphers_and_protocols(self):
        """Test case for list_load_balancer_ssl_ciphers_and_protocols

        Retrieve a list of supported SSL ciphers and protocols  # noqa: E501
        """
        pass

    def test_list_load_balancer_tcp_profiles(self):
        """Test case for list_load_balancer_tcp_profiles

        Retrieve a paginated list of load balancer TCP profiles  # noqa: E501
        """
        pass

    def test_list_load_balancer_virtual_server_statuses(self):
        """Test case for list_load_balancer_virtual_server_statuses

        Get the status list of virtual servers in given load balancer service  # noqa: E501
        """
        pass

    def test_list_load_balancer_virtual_servers(self):
        """Test case for list_load_balancer_virtual_servers

        Retrieve a paginated list of load balancer virtual servers  # noqa: E501
        """
        pass

    def test_list_load_balancer_virtual_servers_statistics(self):
        """Test case for list_load_balancer_virtual_servers_statistics

        Get the statistics list of virtual servers  # noqa: E501
        """
        pass

    def test_perform_pool_member_action(self):
        """Test case for perform_pool_member_action

        Add, remove, or modify load balancer pool members  # noqa: E501
        """
        pass

    def test_read_load_balancer_application_profile(self):
        """Test case for read_load_balancer_application_profile

        Retrieve a load balancer application profile  # noqa: E501
        """
        pass

    def test_read_load_balancer_client_ssl_profile(self):
        """Test case for read_load_balancer_client_ssl_profile

        Retrieve a load balancer client-ssl profile  # noqa: E501
        """
        pass

    def test_read_load_balancer_monitor(self):
        """Test case for read_load_balancer_monitor

        Retrieve a load balancer monitor  # noqa: E501
        """
        pass

    def test_read_load_balancer_node_usage(self):
        """Test case for read_load_balancer_node_usage

        Read load balancer usage for the given node  # noqa: E501
        """
        pass

    def test_read_load_balancer_node_usage_summary(self):
        """Test case for read_load_balancer_node_usage_summary

        Read load balancer node usage summary  # noqa: E501
        """
        pass

    def test_read_load_balancer_persistence_profile(self):
        """Test case for read_load_balancer_persistence_profile

        Retrieve a load balancer persistence profile  # noqa: E501
        """
        pass

    def test_read_load_balancer_pool(self):
        """Test case for read_load_balancer_pool

        Retrieve a load balancer pool  # noqa: E501
        """
        pass

    def test_read_load_balancer_rule(self):
        """Test case for read_load_balancer_rule

        Retrieve a load balancer rule  # noqa: E501
        """
        pass

    def test_read_load_balancer_server_ssl_profile(self):
        """Test case for read_load_balancer_server_ssl_profile

        Retrieve a load balancer server-ssl profile  # noqa: E501
        """
        pass

    def test_read_load_balancer_service(self):
        """Test case for read_load_balancer_service

        Retrieve a load balancer service  # noqa: E501
        """
        pass

    def test_read_load_balancer_service_debug_info(self):
        """Test case for read_load_balancer_service_debug_info

        Read the debug information of the load balancer service  # noqa: E501
        """
        pass

    def test_read_load_balancer_service_usage(self):
        """Test case for read_load_balancer_service_usage

        Read the usage information of the given load balancer service  # noqa: E501
        """
        pass

    def test_read_load_balancer_tcp_profile(self):
        """Test case for read_load_balancer_tcp_profile

        Retrieve a load balancer TCP profile  # noqa: E501
        """
        pass

    def test_read_load_balancer_virtual_server(self):
        """Test case for read_load_balancer_virtual_server

        Retrieve a load balancer virtual server  # noqa: E501
        """
        pass

    def test_update_load_balancer_application_profile(self):
        """Test case for update_load_balancer_application_profile

        Update a load balancer application profile  # noqa: E501
        """
        pass

    def test_update_load_balancer_client_ssl_profile(self):
        """Test case for update_load_balancer_client_ssl_profile

        Update a load balancer client-ssl profile  # noqa: E501
        """
        pass

    def test_update_load_balancer_monitor(self):
        """Test case for update_load_balancer_monitor

        Update a load balancer monitor  # noqa: E501
        """
        pass

    def test_update_load_balancer_persistence_profile(self):
        """Test case for update_load_balancer_persistence_profile

        Update a load balancer persistence profile  # noqa: E501
        """
        pass

    def test_update_load_balancer_pool(self):
        """Test case for update_load_balancer_pool

        Update a load balancer pool  # noqa: E501
        """
        pass

    def test_update_load_balancer_rule(self):
        """Test case for update_load_balancer_rule

        Update a load balancer rule  # noqa: E501
        """
        pass

    def test_update_load_balancer_server_ssl_profile(self):
        """Test case for update_load_balancer_server_ssl_profile

        Update a load balancer server-ssl profile  # noqa: E501
        """
        pass

    def test_update_load_balancer_service(self):
        """Test case for update_load_balancer_service

        Update a load balancer service  # noqa: E501
        """
        pass

    def test_update_load_balancer_tcp_profile(self):
        """Test case for update_load_balancer_tcp_profile

        Update a load balancer TCP profile  # noqa: E501
        """
        pass

    def test_update_load_balancer_virtual_server(self):
        """Test case for update_load_balancer_virtual_server

        Update a load balancer virtual server  # noqa: E501
        """
        pass

    def test_update_load_balancer_virtual_server_with_rules_update_with_rules(self):
        """Test case for update_load_balancer_virtual_server_with_rules_update_with_rules

        Update a load balancer virtual server with rules  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
