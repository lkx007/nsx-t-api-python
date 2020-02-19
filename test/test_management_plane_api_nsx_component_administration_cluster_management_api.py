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
from api.management_plane_api_nsx_component_administration_cluster_management_api import ManagementPlaneApiNsxComponentAdministrationClusterManagementApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiNsxComponentAdministrationClusterManagementApi(unittest.TestCase):
    """ManagementPlaneApiNsxComponentAdministrationClusterManagementApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_nsx_component_administration_cluster_management_api.ManagementPlaneApiNsxComponentAdministrationClusterManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_cluster_node(self):
        """Test case for add_cluster_node

        Add a controller to the cluster  # noqa: E501
        """
        pass

    def test_clear_cluster_certificate_clear_cluster_certificate(self):
        """Test case for clear_cluster_certificate_clear_cluster_certificate

        Clear the cluster certificate  # noqa: E501
        """
        pass

    def test_clear_cluster_virtual_ip_clear_virtual_ip(self):
        """Test case for clear_cluster_virtual_ip_clear_virtual_ip

        Clear cluster virtual IP address  # noqa: E501
        """
        pass

    def test_delete_cluster_node_config(self):
        """Test case for delete_cluster_node_config

        Remove a controller from the cluster  # noqa: E501
        """
        pass

    def test_detach_cluster_node_remove_node(self):
        """Test case for detach_cluster_node_remove_node

        Detach a node from the Cluster  # noqa: E501
        """
        pass

    def test_get_api_service_config(self):
        """Test case for get_api_service_config

        Read API service properties  # noqa: E501
        """
        pass

    def test_get_cluster_certificate_id(self):
        """Test case for get_cluster_certificate_id

        Read cluster certificate ID  # noqa: E501
        """
        pass

    def test_get_cluster_node_config(self):
        """Test case for get_cluster_node_config

        Read cluster node configuration  # noqa: E501
        """
        pass

    def test_get_cluster_virtual_ip(self):
        """Test case for get_cluster_virtual_ip

        Read cluster virtual IP address  # noqa: E501
        """
        pass

    def test_join_cluster_join_cluster(self):
        """Test case for join_cluster_join_cluster

        Join this node to a NSX Cluster  # noqa: E501
        """
        pass

    def test_list_cluster_node_configs(self):
        """Test case for list_cluster_node_configs

        List Cluster Node Configurations  # noqa: E501
        """
        pass

    def test_list_cluster_node_interfaces(self):
        """Test case for list_cluster_node_interfaces

        List the specified node's Network Interfaces  # noqa: E501
        """
        pass

    def test_read_cluster_config(self):
        """Test case for read_cluster_config

        Read Cluster Configuration  # noqa: E501
        """
        pass

    def test_read_cluster_node_config(self):
        """Test case for read_cluster_node_config

        Read Cluster Node Configuration  # noqa: E501
        """
        pass

    def test_read_cluster_node_interface(self):
        """Test case for read_cluster_node_interface

        Read the node's Network Interface  # noqa: E501
        """
        pass

    def test_read_cluster_node_interface_statistics(self):
        """Test case for read_cluster_node_interface_statistics

        Read the NSX Manager/Controller's Network Interface Statistics  # noqa: E501
        """
        pass

    def test_read_cluster_node_status(self):
        """Test case for read_cluster_node_status

        Read cluster node runtime status  # noqa: E501
        """
        pass

    def test_read_cluster_nodes_aggregate_status(self):
        """Test case for read_cluster_nodes_aggregate_status

        Read cluster runtime status  # noqa: E501
        """
        pass

    def test_read_cluster_status(self):
        """Test case for read_cluster_status

        Read Cluster Status  # noqa: E501
        """
        pass

    def test_set_cluster_certificate_set_cluster_certificate(self):
        """Test case for set_cluster_certificate_set_cluster_certificate

        Set the cluster certificate  # noqa: E501
        """
        pass

    def test_set_cluster_virtual_ip_set_virtual_ip(self):
        """Test case for set_cluster_virtual_ip_set_virtual_ip

        Set cluster virtual IP address  # noqa: E501
        """
        pass

    def test_update_api_service_config(self):
        """Test case for update_api_service_config

        Update API service properties  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()