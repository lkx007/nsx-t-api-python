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
from api.management_plane_api_grouping_objects_ns_groups_api import ManagementPlaneApiGroupingObjectsNsGroupsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiGroupingObjectsNsGroupsApi(unittest.TestCase):
    """ManagementPlaneApiGroupingObjectsNsGroupsApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_grouping_objects_ns_groups_api.ManagementPlaneApiGroupingObjectsNsGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_or_remove_ns_group_expression(self):
        """Test case for add_or_remove_ns_group_expression

        Add NSGroup expression  # noqa: E501
        """
        pass

    def test_create_ns_group(self):
        """Test case for create_ns_group

        Create NSGroup  # noqa: E501
        """
        pass

    def test_delete_ns_group(self):
        """Test case for delete_ns_group

        Delete NSGroup  # noqa: E501
        """
        pass

    def test_get_effective_active_directory_groups(self):
        """Test case for get_effective_active_directory_groups

        Get Effective Directory Groups of the specified NSGroup.  # noqa: E501
        """
        pass

    def test_get_effective_ip_address_members(self):
        """Test case for get_effective_ip_address_members

        Get Effective IPAddress translated from the NSGroup  # noqa: E501
        """
        pass

    def test_get_effective_ip_set_members(self):
        """Test case for get_effective_ip_set_members

        Get Effective IPSets of the specified NSGroup.  # noqa: E501
        """
        pass

    def test_get_effective_logical_port_members(self):
        """Test case for get_effective_logical_port_members

        Get Effective Logical Ports translated from the NSgroup  # noqa: E501
        """
        pass

    def test_get_effective_logical_switch_members(self):
        """Test case for get_effective_logical_switch_members

        Get Effective switch members translated from the NSGroup  # noqa: E501
        """
        pass

    def test_get_effective_transport_node_members(self):
        """Test case for get_effective_transport_node_members

        Get effective transport node members translated from the NSGroup  # noqa: E501
        """
        pass

    def test_get_effective_vif_members(self):
        """Test case for get_effective_vif_members

        Get effective VIF members translated from the NSGroup  # noqa: E501
        """
        pass

    def test_get_effective_virtual_machine_members(self):
        """Test case for get_effective_virtual_machine_members

        Get Effective Virtual Machine members of the specified NSGroup.  # noqa: E501
        """
        pass

    def test_get_member_types(self):
        """Test case for get_member_types

        Get member types from NSGroup  # noqa: E501
        """
        pass

    def test_get_service_associations(self):
        """Test case for get_service_associations

        Get services to which the given nsgroup belongs to   # noqa: E501
        """
        pass

    def test_get_unassociated_virtual_machines(self):
        """Test case for get_unassociated_virtual_machines

        Get the list of all the virtual machines that are not a part of any existing NSGroup.  # noqa: E501
        """
        pass

    def test_list_ns_groups(self):
        """Test case for list_ns_groups

        List NSGroups  # noqa: E501
        """
        pass

    def test_read_ns_group(self):
        """Test case for read_ns_group

        Read NSGroup  # noqa: E501
        """
        pass

    def test_update_ns_group(self):
        """Test case for update_ns_group

        Update NSGroup  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
