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
from api.management_plane_api_vpn_statistics_reset_sessions_statistics_api import ManagementPlaneApiVpnStatisticsResetSessionsStatisticsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiVpnStatisticsResetSessionsStatisticsApi(unittest.TestCase):
    """ManagementPlaneApiVpnStatisticsResetSessionsStatisticsApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_vpn_statistics_reset_sessions_statistics_api.ManagementPlaneApiVpnStatisticsResetSessionsStatisticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_reset_ip_sec_vpn_session_statistics_reset(self):
        """Test case for reset_ip_sec_vpn_session_statistics_reset

        Reset the statistics of the given VPN session  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
