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
from api.management_plane_api_nsx_component_administration_system_properties_api import ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi(unittest.TestCase):
    """ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_nsx_component_administration_system_properties_api.ManagementPlaneApiNsxComponentAdministrationSystemPropertiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_management_plane_configuration(self):
        """Test case for delete_management_plane_configuration

        Delete the management_plane config  # noqa: E501
        """
        pass

    def test_delete_mpa_configuration(self):
        """Test case for delete_mpa_configuration

        Delete the MPA config file  # noqa: E501
        """
        pass

    def test_read_management_plane_configuration(self):
        """Test case for read_management_plane_configuration

        Management plane this controller is communicating with  # noqa: E501
        """
        pass

    def test_read_mpa_configuration(self):
        """Test case for read_mpa_configuration

        MPA config for the management plane this node is communicating with  # noqa: E501
        """
        pass

    def test_update_management_plane_configuration(self):
        """Test case for update_management_plane_configuration

        Update management plane configuration  # noqa: E501
        """
        pass

    def test_update_mpa_configuration(self):
        """Test case for update_mpa_configuration

        Update management plane agent configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
