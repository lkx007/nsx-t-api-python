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
from api.management_plane_api_migration_feedback_api import ManagementPlaneApiMigrationFeedbackApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiMigrationFeedbackApi(unittest.TestCase):
    """ManagementPlaneApiMigrationFeedbackApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_migration_feedback_api.ManagementPlaneApiMigrationFeedbackApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_recommended_value_in_feedback_accept_recommended(self):
        """Test case for accept_recommended_value_in_feedback_accept_recommended

        Accept default action for feedbacks  # noqa: E501
        """
        pass

    def test_get_feedback_requests(self):
        """Test case for get_feedback_requests

        NSX-V feedback details  # noqa: E501
        """
        pass

    def test_get_feedback_summary(self):
        """Test case for get_feedback_summary

        Feedback request summary  # noqa: E501
        """
        pass

    def test_get_grouped_feedback_requests(self):
        """Test case for get_grouped_feedback_requests

        NSX-V feedback details  # noqa: E501
        """
        pass

    def test_update_feedback_response(self):
        """Test case for update_feedback_response

        Migration feedback response  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()