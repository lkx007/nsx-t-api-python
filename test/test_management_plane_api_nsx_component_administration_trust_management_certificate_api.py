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
from api.management_plane_api_nsx_component_administration_trust_management_certificate_api import ManagementPlaneApiNsxComponentAdministrationTrustManagementCertificateApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneApiNsxComponentAdministrationTrustManagementCertificateApi(unittest.TestCase):
    """ManagementPlaneApiNsxComponentAdministrationTrustManagementCertificateApi unit test stubs"""

    def setUp(self):
        self.api = api.management_plane_api_nsx_component_administration_trust_management_certificate_api.ManagementPlaneApiNsxComponentAdministrationTrustManagementCertificateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_certificate_import(self):
        """Test case for add_certificate_import

        Add a New Certificate  # noqa: E501
        """
        pass

    def test_delete_certificate(self):
        """Test case for delete_certificate

        Delete Certificate for the Given Certificate ID  # noqa: E501
        """
        pass

    def test_get_certificate(self):
        """Test case for get_certificate

        Show Certificate Data for the Given Certificate ID  # noqa: E501
        """
        pass

    def test_get_certificates(self):
        """Test case for get_certificates

        Return All the User-Facing Components' Certificates  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
