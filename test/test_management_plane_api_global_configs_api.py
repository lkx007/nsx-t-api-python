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
from api.management_plane_api_global_configs_api import ManagementPlaneApiGlobalConfigsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiGlobalConfigsApi(unittest.TestCase):
    """ManagementPlaneApiGlobalConfigsApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_global_configs_api.ManagementPlaneApiGlobalConfigsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_global_configs(self):
        """Test case for get_global_configs

        Get global configs for a config type  # noqa: E501
        """
        pass

    def test_list_global_configs(self):
        """Test case for list_global_configs

        List global configurations of a NSX domain  # noqa: E501
        """
        pass

    def test_resync_global_configs_resync_config(self):
        """Test case for resync_global_configs_resync_config

        Resyncs global configurations of a config-type  # noqa: E501
        """
        pass

    def test_update_global_configs(self):
        """Test case for update_global_configs

        Update global configurations of a config type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
