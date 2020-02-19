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


class UpgradeCheckInfo(object):
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
        'name': 'str',
        'component_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'component_type': 'component_type',
        'description': 'description'
    }

    def __init__(self, name=None, component_type=None, description=None):  # noqa: E501
        """UpgradeCheckInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._component_type = None
        self._description = None
        self.discriminator = None
        if name is not None:
            self.name = name
        self.component_type = component_type
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this UpgradeCheckInfo.  # noqa: E501

        Display name of the pre/post-upgrade check  # noqa: E501

        :return: The name of this UpgradeCheckInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpgradeCheckInfo.

        Display name of the pre/post-upgrade check  # noqa: E501

        :param name: The name of this UpgradeCheckInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def component_type(self):
        """Gets the component_type of this UpgradeCheckInfo.  # noqa: E501

        Component type of the pre/post-upgrade check  # noqa: E501

        :return: The component_type of this UpgradeCheckInfo.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this UpgradeCheckInfo.

        Component type of the pre/post-upgrade check  # noqa: E501

        :param component_type: The component_type of this UpgradeCheckInfo.  # noqa: E501
        :type: str
        """
        if component_type is None:
            raise ValueError("Invalid value for `component_type`, must not be `None`")  # noqa: E501

        self._component_type = component_type

    @property
    def description(self):
        """Gets the description of this UpgradeCheckInfo.  # noqa: E501

        Description of the pre/post-upgrade check  # noqa: E501

        :return: The description of this UpgradeCheckInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpgradeCheckInfo.

        Description of the pre/post-upgrade check  # noqa: E501

        :param description: The description of this UpgradeCheckInfo.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(UpgradeCheckInfo, dict):
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
        if not isinstance(other, UpgradeCheckInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
