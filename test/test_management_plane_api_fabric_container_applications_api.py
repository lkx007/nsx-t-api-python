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
from api.management_plane_api_fabric_container_applications_api import ManagementPlaneApiFabricContainerApplicationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiFabricContainerApplicationsApi(unittest.TestCase):
    """ManagementPlaneApiFabricContainerApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_fabric_container_applications_api.ManagementPlaneApiFabricContainerApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_container_application(self):
        """Test case for get_container_application

        Return a Container Application within a container project  # noqa: E501
        """
        pass

    def test_get_container_application_instance(self):
        """Test case for get_container_application_instance

        Return a container application instance  # noqa: E501
        """
        pass

    def test_list_container_application_instances(self):
        """Test case for list_container_application_instances

        Return the list of container application instance  # noqa: E501
        """
        pass

    def test_list_container_applications(self):
        """Test case for list_container_applications

        Return the List of Container Applications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
