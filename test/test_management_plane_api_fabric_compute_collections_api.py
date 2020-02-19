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
from api.management_plane_api_fabric_compute_collections_api import ManagementPlaneApiFabricComputeCollectionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiFabricComputeCollectionsApi(unittest.TestCase):
    """ManagementPlaneApiFabricComputeCollectionsApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_fabric_compute_collections_api.ManagementPlaneApiFabricComputeCollectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_compute_collection_fabric_template(self):
        """Test case for create_compute_collection_fabric_template

        Create a compute collection fabric template  # noqa: E501
        """
        pass

    def test_delete_compute_collection_fabric_template(self):
        """Test case for delete_compute_collection_fabric_template

        Deletes compute collection fabric template  # noqa: E501
        """
        pass

    def test_get_compute_collection_fabric_template(self):
        """Test case for get_compute_collection_fabric_template

        Get compute collection fabric template by id  # noqa: E501
        """
        pass

    def test_get_host_node_status_on_compute_collection(self):
        """Test case for get_host_node_status_on_compute_collection

        Get status of member host nodes of the compute-collection. Only nsx prepared host nodes in the specified compute-collection are included in the response. cc-ext-id should be of type VC_Cluster.  # noqa: E501
        """
        pass

    def test_list_compute_collection_fabric_templates(self):
        """Test case for list_compute_collection_fabric_templates

        Get compute collection fabric templates  # noqa: E501
        """
        pass

    def test_list_compute_collection_physical_network_interfaces(self):
        """Test case for list_compute_collection_physical_network_interfaces

        List the Physical Network Interface for all discovered nodes  # noqa: E501
        """
        pass

    def test_list_compute_collections(self):
        """Test case for list_compute_collections

        Return the List of Compute Collections  # noqa: E501
        """
        pass

    def test_perform_action_on_compute_collection(self):
        """Test case for perform_action_on_compute_collection

        Perform action specific to NSX on the compute-collection. cc-ext-id should be of type VC_Cluster.  # noqa: E501
        """
        pass

    def test_read_compute_collection(self):
        """Test case for read_compute_collection

        Return Compute Collection Information  # noqa: E501
        """
        pass

    def test_update_compute_collection_fabric_template(self):
        """Test case for update_compute_collection_fabric_template

        Updates compute collection fabric template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
