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
from api.management_plane_api_vpn_statistics_sessions_summary_api import ManagementPlaneApiVpnStatisticsSessionsSummaryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiVpnStatisticsSessionsSummaryApi(unittest.TestCase):
    """ManagementPlaneApiVpnStatisticsSessionsSummaryApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_vpn_statistics_sessions_summary_api.ManagementPlaneApiVpnStatisticsSessionsSummaryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_ip_sec_vpn_session_summary(self):
        """Test case for get_ip_sec_vpn_session_summary

        VPN session summary  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
