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


class AddClusterNodeVMInfo(object):
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
        'deployment_requests': 'list[ClusterNodeVMDeploymentRequest]',
        'clustering_config': 'ClusteringConfig'
    }

    attribute_map = {
        'deployment_requests': 'deployment_requests',
        'clustering_config': 'clustering_config'
    }

    def __init__(self, deployment_requests=None, clustering_config=None):  # noqa: E501
        """AddClusterNodeVMInfo - a model defined in Swagger"""  # noqa: E501
        self._deployment_requests = None
        self._clustering_config = None
        self.discriminator = None
        self.deployment_requests = deployment_requests
        if clustering_config is not None:
            self.clustering_config = clustering_config

    @property
    def deployment_requests(self):
        """Gets the deployment_requests of this AddClusterNodeVMInfo.  # noqa: E501

        Cluster node VM deployment requests to be deployed by the Manager.   # noqa: E501

        :return: The deployment_requests of this AddClusterNodeVMInfo.  # noqa: E501
        :rtype: list[ClusterNodeVMDeploymentRequest]
        """
        return self._deployment_requests

    @deployment_requests.setter
    def deployment_requests(self, deployment_requests):
        """Sets the deployment_requests of this AddClusterNodeVMInfo.

        Cluster node VM deployment requests to be deployed by the Manager.   # noqa: E501

        :param deployment_requests: The deployment_requests of this AddClusterNodeVMInfo.  # noqa: E501
        :type: list[ClusterNodeVMDeploymentRequest]
        """
        if deployment_requests is None:
            raise ValueError("Invalid value for `deployment_requests`, must not be `None`")  # noqa: E501

        self._deployment_requests = deployment_requests

    @property
    def clustering_config(self):
        """Gets the clustering_config of this AddClusterNodeVMInfo.  # noqa: E501


        :return: The clustering_config of this AddClusterNodeVMInfo.  # noqa: E501
        :rtype: ClusteringConfig
        """
        return self._clustering_config

    @clustering_config.setter
    def clustering_config(self, clustering_config):
        """Sets the clustering_config of this AddClusterNodeVMInfo.


        :param clustering_config: The clustering_config of this AddClusterNodeVMInfo.  # noqa: E501
        :type: ClusteringConfig
        """

        self._clustering_config = clustering_config

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
        if issubclass(AddClusterNodeVMInfo, dict):
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
        if not isinstance(other, AddClusterNodeVMInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
