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
from api.management_plane_api_pool_management_ip_blocks_api import ManagementPlaneApiPoolManagementIpBlocksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiPoolManagementIpBlocksApi(unittest.TestCase):
    """ManagementPlaneApiPoolManagementIpBlocksApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_pool_management_ip_blocks_api.ManagementPlaneApiPoolManagementIpBlocksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_allocate_or_release_from_ip_block_subnet(self):
        """Test case for allocate_or_release_from_ip_block_subnet

        Allocate or Release an IP Address from a Ip Subnet  # noqa: E501
        """
        pass

    def test_create_ip_block(self):
        """Test case for create_ip_block

        Create a new IP address block.  # noqa: E501
        """
        pass

    def test_create_ip_block_subnet(self):
        """Test case for create_ip_block_subnet

        Create subnet of specified size within an IP block  # noqa: E501
        """
        pass

    def test_delete_ip_block(self):
        """Test case for delete_ip_block

        Delete an IP Address Block  # noqa: E501
        """
        pass

    def test_delete_ip_block_subnet(self):
        """Test case for delete_ip_block_subnet

        Delete subnet within an IP block  # noqa: E501
        """
        pass

    def test_list_ip_block_subnets(self):
        """Test case for list_ip_block_subnets

        List subnets within an IP block  # noqa: E501
        """
        pass

    def test_list_ip_blocks(self):
        """Test case for list_ip_blocks

        Returns list of configured IP address blocks.  # noqa: E501
        """
        pass

    def test_read_ip_block(self):
        """Test case for read_ip_block

        Get IP address block information.  # noqa: E501
        """
        pass

    def test_read_ip_block_subnet(self):
        """Test case for read_ip_block_subnet

        Get the subnet within an IP block  # noqa: E501
        """
        pass

    def test_update_ip_block(self):
        """Test case for update_ip_block

        Update an IP Address Block  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
