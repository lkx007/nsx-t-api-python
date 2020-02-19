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
from api.management_plane_api_logical_switching_switching_profiles_api import ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiLogicalSwitchingSwitchingProfilesApi(unittest.TestCase):
    """ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_logical_switching_switching_profiles_api.ManagementPlaneApiLogicalSwitchingSwitchingProfilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_switching_profile(self):
        """Test case for create_switching_profile

        Create a Switching Profile  # noqa: E501
        """
        pass

    def test_delete_switching_profile(self):
        """Test case for delete_switching_profile

        Delete a Switching Profile  # noqa: E501
        """
        pass

    def test_get_switching_profile(self):
        """Test case for get_switching_profile

        Get Switching Profile by ID  # noqa: E501
        """
        pass

    def test_get_switching_profile_status(self):
        """Test case for get_switching_profile_status

        Get Counts of Ports and Switches Using This Switching Profile  # noqa: E501
        """
        pass

    def test_list_switching_profiles(self):
        """Test case for list_switching_profiles

        List Switching Profiles  # noqa: E501
        """
        pass

    def test_update_switching_profile(self):
        """Test case for update_switching_profile

        Update a Switching Profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
