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
from api.management_plane_api_service_config_api import ManagementPlaneApiServiceConfigApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiServiceConfigApi(unittest.TestCase):
    """ManagementPlaneApiServiceConfigApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_service_config_api.ManagementPlaneApiServiceConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_service_config(self):
        """Test case for create_service_config

        Create service config  # noqa: E501
        """
        pass

    def test_delete_service_config(self):
        """Test case for delete_service_config

        Delete Service Config  # noqa: E501
        """
        pass

    def test_effective_profiles(self):
        """Test case for effective_profiles

        Get Effective Profiles for an Entity  # noqa: E501
        """
        pass

    def test_list_service_configs(self):
        """Test case for list_service_configs

        List service configs  # noqa: E501
        """
        pass

    def test_read_service_config(self):
        """Test case for read_service_config

        Read Service Config  # noqa: E501
        """
        pass

    def test_service_config_batch_operation(self):
        """Test case for service_config_batch_operation

        Creates/Updates service configs sent in batch request  # noqa: E501
        """
        pass

    def test_update_service_config(self):
        """Test case for update_service_config

        Update service config  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
