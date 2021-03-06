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
from api.management_plane_api_nsx_component_administration_backup_restore_management_restore_api import ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementRestoreApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementRestoreApi(unittest.TestCase):
    """ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementRestoreApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_nsx_component_administration_backup_restore_management_restore_api.ManagementPlaneApiNsxComponentAdministrationBackupRestoreManagementRestoreApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_advance_cluster_restore_advance(self):
        """Test case for advance_cluster_restore_advance

        Advance any suspended restore operation  # noqa: E501
        """
        pass

    def test_cancel_cluster_restore_cancel(self):
        """Test case for cancel_cluster_restore_cancel

        Cancel any running restore operation  # noqa: E501
        """
        pass

    def test_configure_restore_config(self):
        """Test case for configure_restore_config

        Configure Restore SFTP server credentials  # noqa: E501
        """
        pass

    def test_get_restore_config(self):
        """Test case for get_restore_config

        Get Restore configuration  # noqa: E501
        """
        pass

    def test_initiate_cluster_restore_start(self):
        """Test case for initiate_cluster_restore_start

        Initiate a restore operation  # noqa: E501
        """
        pass

    def test_list_cluster_backup_timestamps(self):
        """Test case for list_cluster_backup_timestamps

        List timestamps of all available Cluster Backups.  # noqa: E501
        """
        pass

    def test_list_restore_instruction_resources(self):
        """Test case for list_restore_instruction_resources

        List resources for a given instruction, to be shown to/executed by users.   # noqa: E501
        """
        pass

    def test_query_cluster_restore_status(self):
        """Test case for query_cluster_restore_status

        Query Restore Request Status  # noqa: E501
        """
        pass

    def test_retry_cluster_restore_retry(self):
        """Test case for retry_cluster_restore_retry

        Retry any failed restore operation  # noqa: E501
        """
        pass

    def test_suspend_cluster_restore_suspend(self):
        """Test case for suspend_cluster_restore_suspend

        Suspend any running restore operation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
