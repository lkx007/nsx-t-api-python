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


class DeploymentConfig(object):
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
        'placement_type': 'str'
    }

    attribute_map = {
        'placement_type': 'placement_type'
    }

    discriminator_value_class_map = {
          'VsphereDeploymentConfig': 'VsphereDeploymentConfig'    }

    def __init__(self, placement_type=None):  # noqa: E501
        """DeploymentConfig - a model defined in Swagger"""  # noqa: E501
        self._placement_type = None
        self.discriminator = 'placement_type'
        self.placement_type = placement_type

    @property
    def placement_type(self):
        """Gets the placement_type of this DeploymentConfig.  # noqa: E501


        :return: The placement_type of this DeploymentConfig.  # noqa: E501
        :rtype: str
        """
        return self._placement_type

    @placement_type.setter
    def placement_type(self, placement_type):
        """Sets the placement_type of this DeploymentConfig.


        :param placement_type: The placement_type of this DeploymentConfig.  # noqa: E501
        :type: str
        """
        if placement_type is None:
            raise ValueError("Invalid value for `placement_type`, must not be `None`")  # noqa: E501
        allowed_values = ["VsphereDeploymentConfig"]  # noqa: E501
        if placement_type not in allowed_values:
            raise ValueError(
                "Invalid value for `placement_type` ({0}), must be one of {1}"  # noqa: E501
                .format(placement_type, allowed_values)
            )

        self._placement_type = placement_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(DeploymentConfig, dict):
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
        if not isinstance(other, DeploymentConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
