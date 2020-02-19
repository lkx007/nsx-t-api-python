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
from api.management_plane_api_migration_nodes_api import ManagementPlaneApiMigrationNodesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiMigrationNodesApi(unittest.TestCase):
    """ManagementPlaneApiMigrationNodesApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_migration_nodes_api.ManagementPlaneApiMigrationNodesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_migration_nodes(self):
        """Test case for get_migration_nodes

        Get list of nodes across all types  # noqa: E501
        """
        pass

    def test_get_migration_nodes_summary(self):
        """Test case for get_migration_nodes_summary

        Get summary of nodes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()