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
from api.management_plane_api_operations_lldp_api import ManagementPlaneApiOperationsLldpApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiOperationsLldpApi(unittest.TestCase):
    """ManagementPlaneApiOperationsLldpApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_operations_lldp_api.ManagementPlaneApiOperationsLldpApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_fabric_node_neighbor_properties(self):
        """Test case for list_fabric_node_neighbor_properties

        List LLDP Neighbor Properties of Fabric Node  # noqa: E501
        """
        pass

    def test_read_fabric_node_neighbor_properties(self):
        """Test case for read_fabric_node_neighbor_properties

        Read LLDP Neighbor Properties of Fabric Node by Interface Name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
