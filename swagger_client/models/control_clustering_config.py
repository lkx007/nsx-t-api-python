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


class ControlClusteringConfig(object):
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
        'clustering_type': 'str',
        'join_to_existing_cluster': 'bool',
        'shared_secret': 'str'
    }
    if hasattr(ClusteringConfig, "swagger_types"):
        swagger_types.update(ClusteringConfig.swagger_types)

    attribute_map = {
        'clustering_type': 'clustering_type',
        'join_to_existing_cluster': 'join_to_existing_cluster',
        'shared_secret': 'shared_secret'
    }
    if hasattr(ClusteringConfig, "attribute_map"):
        attribute_map.update(ClusteringConfig.attribute_map)

    def __init__(self, clustering_type=None, join_to_existing_cluster=None, shared_secret=None, *args, **kwargs):  # noqa: E501
        """ControlClusteringConfig - a model defined in Swagger"""  # noqa: E501
        self._clustering_type = None
        self._join_to_existing_cluster = None
        self._shared_secret = None
        self.discriminator = None
        self.clustering_type = clustering_type
        if join_to_existing_cluster is not None:
            self.join_to_existing_cluster = join_to_existing_cluster
        if shared_secret is not None:
            self.shared_secret = shared_secret
        ClusteringConfig.__init__(self, *args, **kwargs)

    @property
    def clustering_type(self):
        """Gets the clustering_type of this ControlClusteringConfig.  # noqa: E501

        Specifies the type of clustering config to be used.   # noqa: E501

        :return: The clustering_type of this ControlClusteringConfig.  # noqa: E501
        :rtype: str
        """
        return self._clustering_type

    @clustering_type.setter
    def clustering_type(self, clustering_type):
        """Sets the clustering_type of this ControlClusteringConfig.

        Specifies the type of clustering config to be used.   # noqa: E501

        :param clustering_type: The clustering_type of this ControlClusteringConfig.  # noqa: E501
        :type: str
        """
        if clustering_type is None:
            raise ValueError("Invalid value for `clustering_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ControlClusteringConfig"]  # noqa: E501
        if clustering_type not in allowed_values:
            raise ValueError(
                "Invalid value for `clustering_type` ({0}), must be one of {1}"  # noqa: E501
                .format(clustering_type, allowed_values)
            )

        self._clustering_type = clustering_type

    @property
    def join_to_existing_cluster(self):
        """Gets the join_to_existing_cluster of this ControlClusteringConfig.  # noqa: E501

        Specifies whether or not the cluster node VM should try to join to the existing control cluster or initialize a new one. Only required in uncertainty case, i.e. when there are manually- deployed controllers that are registered but not connected to the cluster and no auto-deployed controllers are part of the cluster.   # noqa: E501

        :return: The join_to_existing_cluster of this ControlClusteringConfig.  # noqa: E501
        :rtype: bool
        """
        return self._join_to_existing_cluster

    @join_to_existing_cluster.setter
    def join_to_existing_cluster(self, join_to_existing_cluster):
        """Sets the join_to_existing_cluster of this ControlClusteringConfig.

        Specifies whether or not the cluster node VM should try to join to the existing control cluster or initialize a new one. Only required in uncertainty case, i.e. when there are manually- deployed controllers that are registered but not connected to the cluster and no auto-deployed controllers are part of the cluster.   # noqa: E501

        :param join_to_existing_cluster: The join_to_existing_cluster of this ControlClusteringConfig.  # noqa: E501
        :type: bool
        """

        self._join_to_existing_cluster = join_to_existing_cluster

    @property
    def shared_secret(self):
        """Gets the shared_secret of this ControlClusteringConfig.  # noqa: E501

        Shared secret to be used when joining the cluster node VM to a control cluster or for initializing a new cluster with the VM. Must contain at least 4 unique characters and be at least 6 characters long.   # noqa: E501

        :return: The shared_secret of this ControlClusteringConfig.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this ControlClusteringConfig.

        Shared secret to be used when joining the cluster node VM to a control cluster or for initializing a new cluster with the VM. Must contain at least 4 unique characters and be at least 6 characters long.   # noqa: E501

        :param shared_secret: The shared_secret of this ControlClusteringConfig.  # noqa: E501
        :type: str
        """

        self._shared_secret = shared_secret

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
        if issubclass(ControlClusteringConfig, dict):
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
        if not isinstance(other, ControlClusteringConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
