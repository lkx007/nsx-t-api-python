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
from api.management_plane_api_identity_firewall_configuration_api import ManagementPlaneApiIdentityFirewallConfigurationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiIdentityFirewallConfigurationApi(unittest.TestCase):
    """ManagementPlaneApiIdentityFirewallConfigurationApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_identity_firewall_configuration_api.ManagementPlaneApiIdentityFirewallConfigurationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_enabled_compute_collection(self):
        """Test case for get_enabled_compute_collection

        Get IDFW compute collection.  # noqa: E501
        """
        pass

    def test_get_master_switch_setting(self):
        """Test case for get_master_switch_setting

        Get Identity Firewall master switch enabled/disabled  # noqa: E501
        """
        pass

    def test_get_standalone_hosts_switch_setting(self):
        """Test case for get_standalone_hosts_switch_setting

        Get Standalone hosts switch enabled/disabled  # noqa: E501
        """
        pass

    def test_list_enabled_compute_collections(self):
        """Test case for list_enabled_compute_collections

        List all Identity firewall compute collections  # noqa: E501
        """
        pass

    def test_update_enabled_compute_collection(self):
        """Test case for update_enabled_compute_collection

        Update IDFW compute collection  # noqa: E501
        """
        pass

    def test_update_master_switch_setting(self):
        """Test case for update_master_switch_setting

        Update IDFW master switch setting enabled/disabled  # noqa: E501
        """
        pass

    def test_update_standalone_hosts_switch_setting(self):
        """Test case for update_standalone_hosts_switch_setting

        Update IDFW master switch setting enabled/disabled  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
