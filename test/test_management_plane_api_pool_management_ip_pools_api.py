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
from api.management_plane_api_pool_management_ip_pools_api import ManagementPlaneApiPoolManagementIpPoolsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiPoolManagementIpPoolsApi(unittest.TestCase):
    """ManagementPlaneApiPoolManagementIpPoolsApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_pool_management_ip_pools_api.ManagementPlaneApiPoolManagementIpPoolsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_allocate_or_release_from_ip_pool(self):
        """Test case for allocate_or_release_from_ip_pool

        Allocate or Release an IP Address from a Pool  # noqa: E501
        """
        pass

    def test_create_ip_pool(self):
        """Test case for create_ip_pool

        Create an IP Pool  # noqa: E501
        """
        pass

    def test_delete_ip_pool(self):
        """Test case for delete_ip_pool

        Delete an IP Pool  # noqa: E501
        """
        pass

    def test_list_ip_pool_allocations(self):
        """Test case for list_ip_pool_allocations

        List IP Pool Allocations  # noqa: E501
        """
        pass

    def test_list_ip_pools(self):
        """Test case for list_ip_pools

        List IP Pools  # noqa: E501
        """
        pass

    def test_read_ip_pool(self):
        """Test case for read_ip_pool

        Read IP Pool  # noqa: E501
        """
        pass

    def test_update_ip_pool(self):
        """Test case for update_ip_pool

        Update an IP Pool  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
