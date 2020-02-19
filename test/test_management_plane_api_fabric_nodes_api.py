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
from api.management_plane_api_fabric_nodes_api import ManagementPlaneApiFabricNodesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiFabricNodesApi(unittest.TestCase):
    """ManagementPlaneApiFabricNodesApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_fabric_nodes_api.ManagementPlaneApiFabricNodesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_node(self):
        """Test case for add_node

        Register and Install NSX Components on a Node  # noqa: E501
        """
        pass

    def test_delete_node(self):
        """Test case for delete_node

        Delete a Node  # noqa: E501
        """
        pass

    def test_get_fabric_node_modules(self):
        """Test case for get_fabric_node_modules

        Get the module details of a Fabric Node This api is deprecated, use Transport Node API GET /transport-nodes/&lt;transportnode-id&gt;/modules to get fabric node modules.   # noqa: E501
        """
        pass

    def test_get_fabric_node_state(self):
        """Test case for get_fabric_node_state

        Get the Realized State of a Fabric Node.  # noqa: E501
        """
        pass

    def test_get_supported_host_os_types(self):
        """Test case for get_supported_host_os_types

        Return list of supported host OS types  # noqa: E501
        """
        pass

    def test_list_fabric_node_interfaces(self):
        """Test case for list_fabric_node_interfaces

        List the specified node's Network Interfaces  # noqa: E501
        """
        pass

    def test_list_node_capabilities(self):
        """Test case for list_node_capabilities

        Return the List of Capabilities of a Single Node  # noqa: E501
        """
        pass

    def test_list_nodes(self):
        """Test case for list_nodes

        Return the List of Nodes  # noqa: E501
        """
        pass

    def test_perform_host_node_upgrade_action_upgrade_infra(self):
        """Test case for perform_host_node_upgrade_action_upgrade_infra

        Perform a service deployment upgrade on a host node  # noqa: E501
        """
        pass

    def test_perform_node_action(self):
        """Test case for perform_node_action

        Perform an Action on Fabric Node  # noqa: E501
        """
        pass

    def test_read_fabric_node_interface(self):
        """Test case for read_fabric_node_interface

        Read the node's Network Interface  # noqa: E501
        """
        pass

    def test_read_fabric_node_interface_statistics(self):
        """Test case for read_fabric_node_interface_statistics

        Read the NSX Manager's Network Interface Statistics  # noqa: E501
        """
        pass

    def test_read_node(self):
        """Test case for read_node

        Return Node Information  # noqa: E501
        """
        pass

    def test_read_node_status(self):
        """Test case for read_node_status

        Return Runtime Status Information for a Node  # noqa: E501
        """
        pass

    def test_read_nodes_status(self):
        """Test case for read_nodes_status

        Return Runtime Status Information for given Nodes  # noqa: E501
        """
        pass

    def test_restart_inventory_sync_restart_inventory_sync(self):
        """Test case for restart_inventory_sync_restart_inventory_sync

        Restart the inventory sync for the node if it is paused currently.  # noqa: E501
        """
        pass

    def test_update_node(self):
        """Test case for update_node

        Update a Node  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()