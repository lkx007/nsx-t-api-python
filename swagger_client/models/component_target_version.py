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


class ComponentTargetVersion(object):
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
        'target_version': 'str',
        'component_type': 'str'
    }

    attribute_map = {
        'target_version': 'target_version',
        'component_type': 'component_type'
    }

    def __init__(self, target_version=None, component_type=None):  # noqa: E501
        """ComponentTargetVersion - a model defined in Swagger"""  # noqa: E501
        self._target_version = None
        self._component_type = None
        self.discriminator = None
        if target_version is not None:
            self.target_version = target_version
        if component_type is not None:
            self.component_type = component_type

    @property
    def target_version(self):
        """Gets the target_version of this ComponentTargetVersion.  # noqa: E501


        :return: The target_version of this ComponentTargetVersion.  # noqa: E501
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this ComponentTargetVersion.


        :param target_version: The target_version of this ComponentTargetVersion.  # noqa: E501
        :type: str
        """

        self._target_version = target_version

    @property
    def component_type(self):
        """Gets the component_type of this ComponentTargetVersion.  # noqa: E501


        :return: The component_type of this ComponentTargetVersion.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this ComponentTargetVersion.


        :param component_type: The component_type of this ComponentTargetVersion.  # noqa: E501
        :type: str
        """

        self._component_type = component_type

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
        if issubclass(ComponentTargetVersion, dict):
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
        if not isinstance(other, ComponentTargetVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
