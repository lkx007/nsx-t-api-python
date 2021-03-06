# coding: utf-8

"""
    NSX-T Manager API

    VMware NSX-T Manager REST API  # noqa: E501

    OpenAPI spec version: 2.5.1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ServiceDeploymentStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'deployment_issues': 'list[ServiceDeploymentIssue]',
        'last_update_timestamp': 'int',
        'deployment_status': 'str',
        'sva_current_version': 'str',
        'service_deployment_id': 'str',
        'sva_max_available_version': 'str'
    }

    attribute_map = {
        'deployment_issues': 'deployment_issues',
        'last_update_timestamp': 'last_update_timestamp',
        'deployment_status': 'deployment_status',
        'sva_current_version': 'sva_current_version',
        'service_deployment_id': 'service_deployment_id',
        'sva_max_available_version': 'sva_max_available_version'
    }

    def __init__(self, deployment_issues=None, last_update_timestamp=None, deployment_status=None, sva_current_version=None, service_deployment_id=None, sva_max_available_version=None):  # noqa: E501
        """ServiceDeploymentStatus - a model defined in Swagger"""  # noqa: E501
        self._deployment_issues = None
        self._last_update_timestamp = None
        self._deployment_status = None
        self._sva_current_version = None
        self._service_deployment_id = None
        self._sva_max_available_version = None
        self.discriminator = None
        if deployment_issues is not None:
            self.deployment_issues = deployment_issues
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if deployment_status is not None:
            self.deployment_status = deployment_status
        if sva_current_version is not None:
            self.sva_current_version = sva_current_version
        if service_deployment_id is not None:
            self.service_deployment_id = service_deployment_id
        if sva_max_available_version is not None:
            self.sva_max_available_version = sva_max_available_version

    @property
    def deployment_issues(self):
        """Gets the deployment_issues of this ServiceDeploymentStatus.  # noqa: E501

        List of issue and detailed description of the issue in case of deployment failure.  # noqa: E501

        :return: The deployment_issues of this ServiceDeploymentStatus.  # noqa: E501
        :rtype: list[ServiceDeploymentIssue]
        """
        return self._deployment_issues

    @deployment_issues.setter
    def deployment_issues(self, deployment_issues):
        """Sets the deployment_issues of this ServiceDeploymentStatus.

        List of issue and detailed description of the issue in case of deployment failure.  # noqa: E501

        :param deployment_issues: The deployment_issues of this ServiceDeploymentStatus.  # noqa: E501
        :type: list[ServiceDeploymentIssue]
        """

        self._deployment_issues = deployment_issues

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this ServiceDeploymentStatus.  # noqa: E501

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :return: The last_update_timestamp of this ServiceDeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this ServiceDeploymentStatus.

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this ServiceDeploymentStatus.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def deployment_status(self):
        """Gets the deployment_status of this ServiceDeploymentStatus.  # noqa: E501

        Deployment status of NXGI Partner Service-VM on a compute collection. It shows the latest status during the process of deployment, redeploy, upgrade, and un-deployment on a compute collection such as VC cluster.  # noqa: E501

        :return: The deployment_status of this ServiceDeploymentStatus.  # noqa: E501
        :rtype: str
        """
        return self._deployment_status

    @deployment_status.setter
    def deployment_status(self, deployment_status):
        """Sets the deployment_status of this ServiceDeploymentStatus.

        Deployment status of NXGI Partner Service-VM on a compute collection. It shows the latest status during the process of deployment, redeploy, upgrade, and un-deployment on a compute collection such as VC cluster.  # noqa: E501

        :param deployment_status: The deployment_status of this ServiceDeploymentStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["UPGRADE_IN_PROGRESS", "UPGRADE_FAILED", "DEPLOYMENT_QUEUED", "DEPLOYMENT_IN_PROGRESS", "DEPLOYMENT_FAILED", "DEPLOYMENT_SUCCESSFUL", "UNDEPLOYMENT_QUEUED", "UNDEPLOYMENT_IN_PROGRESS", "UNDEPLOYMENT_FAILED", "UNDEPLOYMENT_SUCCESSFUL", "UPGRADE_QUEUED"]  # noqa: E501
        if deployment_status not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_status` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_status, allowed_values)
            )

        self._deployment_status = deployment_status

    @property
    def sva_current_version(self):
        """Gets the sva_current_version of this ServiceDeploymentStatus.  # noqa: E501

        Currently deployed Service Virtual Appliance version.  # noqa: E501

        :return: The sva_current_version of this ServiceDeploymentStatus.  # noqa: E501
        :rtype: str
        """
        return self._sva_current_version

    @sva_current_version.setter
    def sva_current_version(self, sva_current_version):
        """Sets the sva_current_version of this ServiceDeploymentStatus.

        Currently deployed Service Virtual Appliance version.  # noqa: E501

        :param sva_current_version: The sva_current_version of this ServiceDeploymentStatus.  # noqa: E501
        :type: str
        """

        self._sva_current_version = sva_current_version

    @property
    def service_deployment_id(self):
        """Gets the service_deployment_id of this ServiceDeploymentStatus.  # noqa: E501

        Id of service deployment.  # noqa: E501

        :return: The service_deployment_id of this ServiceDeploymentStatus.  # noqa: E501
        :rtype: str
        """
        return self._service_deployment_id

    @service_deployment_id.setter
    def service_deployment_id(self, service_deployment_id):
        """Sets the service_deployment_id of this ServiceDeploymentStatus.

        Id of service deployment.  # noqa: E501

        :param service_deployment_id: The service_deployment_id of this ServiceDeploymentStatus.  # noqa: E501
        :type: str
        """

        self._service_deployment_id = service_deployment_id

    @property
    def sva_max_available_version(self):
        """Gets the sva_max_available_version of this ServiceDeploymentStatus.  # noqa: E501

        Max available SVA version for upgrade  # noqa: E501

        :return: The sva_max_available_version of this ServiceDeploymentStatus.  # noqa: E501
        :rtype: str
        """
        return self._sva_max_available_version

    @sva_max_available_version.setter
    def sva_max_available_version(self, sva_max_available_version):
        """Sets the sva_max_available_version of this ServiceDeploymentStatus.

        Max available SVA version for upgrade  # noqa: E501

        :param sva_max_available_version: The sva_max_available_version of this ServiceDeploymentStatus.  # noqa: E501
        :type: str
        """

        self._sva_max_available_version = sva_max_available_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ServiceDeploymentStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServiceDeploymentStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
