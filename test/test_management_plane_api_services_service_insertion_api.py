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
from api.management_plane_api_services_service_insertion_api import ManagementPlaneApiServicesServiceInsertionApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiServicesServiceInsertionApi(unittest.TestCase):
    """ManagementPlaneApiServicesServiceInsertionApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_services_service_insertion_api.ManagementPlaneApiServicesServiceInsertionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_instance_endpoint(self):
        """Test case for add_instance_endpoint

        Add an InstanceEndpoint for a Service Instance  # noqa: E501
        """
        pass

    def test_add_service_attachment(self):
        """Test case for add_service_attachment

        Add a Service Attachment.  # noqa: E501
        """
        pass

    def test_add_service_chain(self):
        """Test case for add_service_chain

        Add Service Chain  # noqa: E501
        """
        pass

    def test_add_service_insertion_exclude_list_member_add_member(self):
        """Test case for add_service_insertion_exclude_list_member_add_member

        Add a new member in the exclude list  # noqa: E501
        """
        pass

    def test_add_service_insertion_rule_in_section(self):
        """Test case for add_service_insertion_rule_in_section

        Add a Single Rule in a Section  # noqa: E501
        """
        pass

    def test_add_service_insertion_rules_in_section_create_multiple(self):
        """Test case for add_service_insertion_rules_in_section_create_multiple

        Add Multiple Rules in a Section  # noqa: E501
        """
        pass

    def test_add_service_insertion_section(self):
        """Test case for add_service_insertion_section

        Create a New Empty Section  # noqa: E501
        """
        pass

    def test_add_service_insertion_section_with_rules_create_with_rules(self):
        """Test case for add_service_insertion_section_with_rules_create_with_rules

        Create a Section with Rules  # noqa: E501
        """
        pass

    def test_add_service_insertion_service(self):
        """Test case for add_service_insertion_service

        Create a Service-Insertion Service  # noqa: E501
        """
        pass

    def test_add_service_instance(self):
        """Test case for add_service_instance

        Add a Service Instance for a specified Service.  # noqa: E501
        """
        pass

    def test_add_si_service_profile(self):
        """Test case for add_si_service_profile

        Add ServiceProfile for a given Service.  # noqa: E501
        """
        pass

    def test_add_vendor_template(self):
        """Test case for add_vendor_template

        Add Vendor Template for a given Service  # noqa: E501
        """
        pass

    def test_create_solution_config(self):
        """Test case for create_solution_config

        Add Solution Config for a given Service  # noqa: E501
        """
        pass

    def test_delete_instance_endpoint(self):
        """Test case for delete_instance_endpoint

        Delete a particular InstanceEndpoint.  # noqa: E501
        """
        pass

    def test_delete_service_attachment(self):
        """Test case for delete_service_attachment

        Delete an existing service attachment  # noqa: E501
        """
        pass

    def test_delete_service_chain(self):
        """Test case for delete_service_chain

        Delete a Service Chain.  # noqa: E501
        """
        pass

    def test_delete_service_deployment(self):
        """Test case for delete_service_deployment

        Remove service deployment  # noqa: E501
        """
        pass

    def test_delete_service_insertion_rule(self):
        """Test case for delete_service_insertion_rule

        Delete an Existing Rule  # noqa: E501
        """
        pass

    def test_delete_service_insertion_section(self):
        """Test case for delete_service_insertion_section

        Delete an Existing Section and Its Associated Rules  # noqa: E501
        """
        pass

    def test_delete_service_insertion_service(self):
        """Test case for delete_service_insertion_service

        Delete an existing Service and the Service-Instance associated with it.  # noqa: E501
        """
        pass

    def test_delete_service_instance(self):
        """Test case for delete_service_instance

        Delete an existing Service-Instance  # noqa: E501
        """
        pass

    def test_delete_service_manager(self):
        """Test case for delete_service_manager

        Delete service manager  # noqa: E501
        """
        pass

    def test_delete_service_v_ms_delete(self):
        """Test case for delete_service_v_ms_delete

        Remove service VMs either as standalone or HA  # noqa: E501
        """
        pass

    def test_delete_si_service_profile(self):
        """Test case for delete_si_service_profile

        Delete a particular ServiceProfile.  # noqa: E501
        """
        pass

    def test_delete_solution_config(self):
        """Test case for delete_solution_config

        Deletes solution config information.  # noqa: E501
        """
        pass

    def test_delete_vendor_template(self):
        """Test case for delete_vendor_template

        Delete a particular vendor tempalte.  # noqa: E501
        """
        pass

    def test_deploy_service(self):
        """Test case for deploy_service

        Deploys a particular service  # noqa: E501
        """
        pass

    def test_deploy_service_v_ms_deploy(self):
        """Test case for deploy_service_v_ms_deploy

        Deploy and set up service VMs either as standalone or HA  # noqa: E501
        """
        pass

    def test_get_instance_endpoint(self):
        """Test case for get_instance_endpoint

        Get a particular instance endpoint for a service instance.  # noqa: E501
        """
        pass

    def test_get_runtime_interface_operational_status(self):
        """Test case for get_runtime_interface_operational_status

        Get operational status for an interface  # noqa: E501
        """
        pass

    def test_get_runtime_interface_statistics(self):
        """Test case for get_runtime_interface_statistics

        Get statistics for a given interface identified by the interface index  # noqa: E501
        """
        pass

    def test_get_service_attachment(self):
        """Test case for get_service_attachment

        Get a particular service attachment.  # noqa: E501
        """
        pass

    def test_get_service_chain(self):
        """Test case for get_service_chain

        Get a particular service chain.  # noqa: E501
        """
        pass

    def test_get_service_deployment(self):
        """Test case for get_service_deployment

        Get a particular service deployment.  # noqa: E501
        """
        pass

    def test_get_service_deployment_state(self):
        """Test case for get_service_deployment_state

        Get Service-Deployment state for Service.  # noqa: E501
        """
        pass

    def test_get_service_deployment_status(self):
        """Test case for get_service_deployment_status

        Get a particular service deployment status.  # noqa: E501
        """
        pass

    def test_get_service_deployments(self):
        """Test case for get_service_deployments

        Get all service deployments for the given service id  # noqa: E501
        """
        pass

    def test_get_service_insertion_exclude_list(self):
        """Test case for get_service_insertion_exclude_list

        Get list of members in exclude list  # noqa: E501
        """
        pass

    def test_get_service_insertion_rule(self):
        """Test case for get_service_insertion_rule

        Read an Existing Rule  # noqa: E501
        """
        pass

    def test_get_service_insertion_rules(self):
        """Test case for get_service_insertion_rules

        Get All the Rules for a Section  # noqa: E501
        """
        pass

    def test_get_service_insertion_section(self):
        """Test case for get_service_insertion_section

        Get an Existing Section  # noqa: E501
        """
        pass

    def test_get_service_insertion_section_with_rules_list_with_rules(self):
        """Test case for get_service_insertion_section_with_rules_list_with_rules

        Get an Existing Section, Including Rules  # noqa: E501
        """
        pass

    def test_get_service_insertion_service(self):
        """Test case for get_service_insertion_service

        Get an existing Service  # noqa: E501
        """
        pass

    def test_get_service_insertion_status(self):
        """Test case for get_service_insertion_status

        Get ServiceInsertion global status for a context  # noqa: E501
        """
        pass

    def test_get_service_instance(self):
        """Test case for get_service_instance

        Get Service-Instance for Service.  # noqa: E501
        """
        pass

    def test_get_service_instance_ns_groups(self):
        """Test case for get_service_instance_ns_groups

        Get NSgroups for a given ServiceInstance.  # noqa: E501
        """
        pass

    def test_get_service_instance_state(self):
        """Test case for get_service_instance_state

        Get Service-Instance state for Service.  # noqa: E501
        """
        pass

    def test_get_service_instance_status(self):
        """Test case for get_service_instance_status

        Get Service-Instance status for Service.  # noqa: E501
        """
        pass

    def test_get_service_manager(self):
        """Test case for get_service_manager

        Get service manager  # noqa: E501
        """
        pass

    def test_get_service_profile_ns_groups(self):
        """Test case for get_service_profile_ns_groups

        Get NSgroups for a given ServiceProfile.  # noqa: E501
        """
        pass

    def test_get_si_service_profile(self):
        """Test case for get_si_service_profile

        Get a particular ServiceProfile for a Service.  # noqa: E501
        """
        pass

    def test_get_solution_config(self):
        """Test case for get_solution_config

        Get Solution Config Information for a given solution config id.  # noqa: E501
        """
        pass

    def test_get_vendor_template(self):
        """Test case for get_vendor_template

        Get a particular vendor template for a given service.  # noqa: E501
        """
        pass

    def test_list_instance_endpoints(self):
        """Test case for list_instance_endpoints

        List all InstanceEndpoints of a Service Instance.  # noqa: E501
        """
        pass

    def test_list_instance_runtimes(self):
        """Test case for list_instance_runtimes

        Returns list of instance runtimes of service VM being deployed  # noqa: E501
        """
        pass

    def test_list_service_attachments(self):
        """Test case for list_service_attachments

        Get all service attachments.  # noqa: E501
        """
        pass

    def test_list_service_chain_mappings(self):
        """Test case for list_service_chain_mappings

        List all ServiceChainMappings.  # noqa: E501
        """
        pass

    def test_list_service_chains(self):
        """Test case for list_service_chains

        List all ServiceChains.  # noqa: E501
        """
        pass

    def test_list_service_insertion_sections(self):
        """Test case for list_service_insertion_sections

        List All Service Insertion Sections  # noqa: E501
        """
        pass

    def test_list_service_insertion_services(self):
        """Test case for list_service_insertion_services

        List all Service-Insertion Services.  # noqa: E501
        """
        pass

    def test_list_service_insertion_status(self):
        """Test case for list_service_insertion_status

        List all service insertion status for supported contexts  # noqa: E501
        """
        pass

    def test_list_service_instances(self):
        """Test case for list_service_instances

        Get all Service-Instances present in system  # noqa: E501
        """
        pass

    def test_list_service_instances_for_service(self):
        """Test case for list_service_instances_for_service

        Get all Service-Instances for Service.  # noqa: E501
        """
        pass

    def test_list_service_managers(self):
        """Test case for list_service_managers

        List service managers  # noqa: E501
        """
        pass

    def test_list_service_paths(self):
        """Test case for list_service_paths

        List all service paths  # noqa: E501
        """
        pass

    def test_list_si_service_profiles(self):
        """Test case for list_si_service_profiles

        List all Service Profiles of a Service.  # noqa: E501
        """
        pass

    def test_list_solution_configs(self):
        """Test case for list_solution_configs

        Get Solution Config Information associated with a given service.  # noqa: E501
        """
        pass

    def test_list_vendor_templates(self):
        """Test case for list_vendor_templates

        List all VendorTemplates of a Service.  # noqa: E501
        """
        pass

    def test_register_service_manager(self):
        """Test case for register_service_manager

        Register service manager  # noqa: E501
        """
        pass

    def test_remove_service_insertion_exclude_list_member_remove_member(self):
        """Test case for remove_service_insertion_exclude_list_member_remove_member

        Remove an existing object from the exclude list  # noqa: E501
        """
        pass

    def test_resolve_source_entities(self):
        """Test case for resolve_source_entities

        Resolve 'source node id' value to source entities.  # noqa: E501
        """
        pass

    def test_revise_service_insertion_rule_revise(self):
        """Test case for revise_service_insertion_rule_revise

        Update an Existing Rule and Reorder the Rule  # noqa: E501
        """
        pass

    def test_revise_service_insertion_section_revise(self):
        """Test case for revise_service_insertion_section_revise

        Update an Existing Section, Including Its Position  # noqa: E501
        """
        pass

    def test_revise_service_insertion_section_with_rules_revise_with_rules(self):
        """Test case for revise_service_insertion_section_with_rules_revise_with_rules

        Update an Existing Section with Rules  # noqa: E501
        """
        pass

    def test_update_service_deployment(self):
        """Test case for update_service_deployment

        Update an existing Service Deployment.  # noqa: E501
        """
        pass

    def test_update_service_insertion_exclude_list(self):
        """Test case for update_service_insertion_exclude_list

        Modify exclude list  # noqa: E501
        """
        pass

    def test_update_service_insertion_rule(self):
        """Test case for update_service_insertion_rule

        Update an Existing Rule  # noqa: E501
        """
        pass

    def test_update_service_insertion_section(self):
        """Test case for update_service_insertion_section

        Update an Existing Section  # noqa: E501
        """
        pass

    def test_update_service_insertion_section_with_rules_update_with_rules(self):
        """Test case for update_service_insertion_section_with_rules_update_with_rules

        Update an Existing Section, Including Its Rules  # noqa: E501
        """
        pass

    def test_update_service_insertion_service(self):
        """Test case for update_service_insertion_service

        Update an existing Service  # noqa: E501
        """
        pass

    def test_update_service_insertion_status(self):
        """Test case for update_service_insertion_status

        Update global ServiceInsertion status for a context  # noqa: E501
        """
        pass

    def test_update_service_instance(self):
        """Test case for update_service_instance

        Update an existing Service-Instance.  # noqa: E501
        """
        pass

    def test_update_service_manager(self):
        """Test case for update_service_manager

        Update service manager  # noqa: E501
        """
        pass

    def test_update_service_vm_state(self):
        """Test case for update_service_vm_state

        Update maintenance mode or runtime state of a service VM  # noqa: E501
        """
        pass

    def test_update_solution_config(self):
        """Test case for update_solution_config

        Updates Solution Config for a given Service  # noqa: E501
        """
        pass

    def test_upgrade_service_deployment_upgrade(self):
        """Test case for upgrade_service_deployment_upgrade

        Upgrade all VMs part of this service deployment using newer version of OVF. It is currently being disabled.  # noqa: E501
        """
        pass

    def test_upgrade_service_v_ms_upgrade(self):
        """Test case for upgrade_service_v_ms_upgrade

        Upgrade service VMs using newer version of OVF  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
