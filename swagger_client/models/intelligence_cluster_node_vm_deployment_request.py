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


class IntelligenceClusterNodeVMDeploymentRequest(object):
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
        'deployment_config': 'IntelligenceClusterNodeVMDeploymentConfig',
        'vm_id': 'str',
        'user_settings': 'NodeUserSettings',
        'form_factor': 'str'
    }

    attribute_map = {
        'deployment_config': 'deployment_config',
        'vm_id': 'vm_id',
        'user_settings': 'user_settings',
        'form_factor': 'form_factor'
    }

    def __init__(self, deployment_config=None, vm_id=None, user_settings=None, form_factor='SMALL'):  # noqa: E501
        """IntelligenceClusterNodeVMDeploymentRequest - a model defined in Swagger"""  # noqa: E501
        self._deployment_config = None
        self._vm_id = None
        self._user_settings = None
        self._form_factor = None
        self.discriminator = None
        self.deployment_config = deployment_config
        if vm_id is not None:
            self.vm_id = vm_id
        if user_settings is not None:
            self.user_settings = user_settings
        if form_factor is not None:
            self.form_factor = form_factor

    @property
    def deployment_config(self):
        """Gets the deployment_config of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501


        :return: The deployment_config of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501
        :rtype: IntelligenceClusterNodeVMDeploymentConfig
        """
        return self._deployment_config

    @deployment_config.setter
    def deployment_config(self, deployment_config):
        """Sets the deployment_config of this IntelligenceClusterNodeVMDeploymentRequest.


        :param deployment_config: The deployment_config of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501
        :type: IntelligenceClusterNodeVMDeploymentConfig
        """
        if deployment_config is None:
            raise ValueError("Invalid value for `deployment_config`, must not be `None`")  # noqa: E501

        self._deployment_config = deployment_config

    @property
    def vm_id(self):
        """Gets the vm_id of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501

        ID of the VM maintained internally. Note: This is automatically generated and cannot be modified.   # noqa: E501

        :return: The vm_id of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this IntelligenceClusterNodeVMDeploymentRequest.

        ID of the VM maintained internally. Note: This is automatically generated and cannot be modified.   # noqa: E501

        :param vm_id: The vm_id of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501
        :type: str
        """

        self._vm_id = vm_id

    @property
    def user_settings(self):
        """Gets the user_settings of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501


        :return: The user_settings of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501
        :rtype: NodeUserSettings
        """
        return self._user_settings

    @user_settings.setter
    def user_settings(self, user_settings):
        """Sets the user_settings of this IntelligenceClusterNodeVMDeploymentRequest.


        :param user_settings: The user_settings of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501
        :type: NodeUserSettings
        """

        self._user_settings = user_settings

    @property
    def form_factor(self):
        """Gets the form_factor of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501

        Specifies the desired \"size\" of the VM   # noqa: E501

        :return: The form_factor of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor):
        """Sets the form_factor of this IntelligenceClusterNodeVMDeploymentRequest.

        Specifies the desired \"size\" of the VM   # noqa: E501

        :param form_factor: The form_factor of this IntelligenceClusterNodeVMDeploymentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["SMALL", "LARGE"]  # noqa: E501
        if form_factor not in allowed_values:
            raise ValueError(
                "Invalid value for `form_factor` ({0}), must be one of {1}"  # noqa: E501
                .format(form_factor, allowed_values)
            )

        self._form_factor = form_factor

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
        if issubclass(IntelligenceClusterNodeVMDeploymentRequest, dict):
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
        if not isinstance(other, IntelligenceClusterNodeVMDeploymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
