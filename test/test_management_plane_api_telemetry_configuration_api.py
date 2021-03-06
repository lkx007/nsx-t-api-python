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
from api.management_plane_api_telemetry_configuration_api import ManagementPlaneApiTelemetryConfigurationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiTelemetryConfigurationApi(unittest.TestCase):
    """ManagementPlaneApiTelemetryConfigurationApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_telemetry_configuration_api.ManagementPlaneApiTelemetryConfigurationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_telemetry_agreement(self):
        """Test case for get_telemetry_agreement

        Returns telemetry agreement information  # noqa: E501
        """
        pass

    def test_get_telemetry_config(self):
        """Test case for get_telemetry_config

        Returns the telemetry configuration  # noqa: E501
        """
        pass

    def test_update_telemetry_agreement(self):
        """Test case for update_telemetry_agreement

        Set telemetry agreement information  # noqa: E501
        """
        pass

    def test_update_telemetry_config(self):
        """Test case for update_telemetry_config

        Creates or updates the telemetry configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
