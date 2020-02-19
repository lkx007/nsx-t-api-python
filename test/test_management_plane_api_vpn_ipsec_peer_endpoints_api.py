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
from api.management_plane_api_vpn_ipsec_peer_endpoints_api import ManagementPlaneApiVpnIpsecPeerEndpointsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiVpnIpsecPeerEndpointsApi(unittest.TestCase):
    """ManagementPlaneApiVpnIpsecPeerEndpointsApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_vpn_ipsec_peer_endpoints_api.ManagementPlaneApiVpnIpsecPeerEndpointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ip_sec_vpn_peer_end_point(self):
        """Test case for create_ip_sec_vpn_peer_end_point

        Create custom peer endpoint  # noqa: E501
        """
        pass

    def test_delete_ip_sec_vpn_peer_endpoint(self):
        """Test case for delete_ip_sec_vpn_peer_endpoint

        Delete custom IPSec VPN peer endpoint  # noqa: E501
        """
        pass

    def test_get_ip_sec_vpn_peer_endpoint(self):
        """Test case for get_ip_sec_vpn_peer_endpoint

        Get IPSec VPN peer endpoint  # noqa: E501
        """
        pass

    def test_get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data(self):
        """Test case for get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data

        Get IPSec VPN peer endpoint with PSK  # noqa: E501
        """
        pass

    def test_list_ip_sec_vpn_peer_endpoints(self):
        """Test case for list_ip_sec_vpn_peer_endpoints

        Get IPSecVPNPeerEndpoint List Result  # noqa: E501
        """
        pass

    def test_update_ip_sec_vpn_peer_endpoint(self):
        """Test case for update_ip_sec_vpn_peer_endpoint

        Edit custom IPSecPeerEndpoint  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
