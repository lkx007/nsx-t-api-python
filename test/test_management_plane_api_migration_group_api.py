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
from api.management_plane_api_migration_group_api import ManagementPlaneApiMigrationGroupApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiMigrationGroupApi(unittest.TestCase):
    """ManagementPlaneApiMigrationGroupApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_migration_group_api.ManagementPlaneApiMigrationGroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_migration_units_to_group_add_migration_units(self):
        """Test case for add_migration_units_to_group_add_migration_units

        Add migration units to specified migration unit group  # noqa: E501
        """
        pass

    def test_create_migration_unit_group(self):
        """Test case for create_migration_unit_group

        Create a group  # noqa: E501
        """
        pass

    def test_delete_migration_unit_group(self):
        """Test case for delete_migration_unit_group

        Delete the migration unit group  # noqa: E501
        """
        pass

    def test_get_migration_unit_group(self):
        """Test case for get_migration_unit_group

        Return migration unit group information  # noqa: E501
        """
        pass

    def test_get_migration_unit_group_aggregate_info(self):
        """Test case for get_migration_unit_group_aggregate_info

        Return aggregate information of all migration unit groups  # noqa: E501
        """
        pass

    def test_get_migration_unit_group_status(self):
        """Test case for get_migration_unit_group_status

        Get migration status for group  # noqa: E501
        """
        pass

    def test_get_migration_unit_groups(self):
        """Test case for get_migration_unit_groups

        Return information of all migration unit groups  # noqa: E501
        """
        pass

    def test_get_migration_unit_groups_status(self):
        """Test case for get_migration_unit_groups_status

        Get migration status for migration unit groups  # noqa: E501
        """
        pass

    def test_reorder_migration_unit_group_reorder(self):
        """Test case for reorder_migration_unit_group_reorder

        Reorder migration unit group  # noqa: E501
        """
        pass

    def test_reorder_migration_unit_reorder(self):
        """Test case for reorder_migration_unit_reorder

        Reorder an migration unit within the migration unit group  # noqa: E501
        """
        pass

    def test_update_migration_unit_group(self):
        """Test case for update_migration_unit_group

        Update the migration unit group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
