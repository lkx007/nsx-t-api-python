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


class UcStateProperties(object):
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
        'update_uc_state_properties': 'bool'
    }

    attribute_map = {
        'update_uc_state_properties': 'update_uc_state_properties'
    }

    def __init__(self, update_uc_state_properties=True):  # noqa: E501
        """UcStateProperties - a model defined in Swagger"""  # noqa: E501
        self._update_uc_state_properties = None
        self.discriminator = None
        if update_uc_state_properties is not None:
            self.update_uc_state_properties = update_uc_state_properties

    @property
    def update_uc_state_properties(self):
        """Gets the update_uc_state_properties of this UcStateProperties.  # noqa: E501

        Flag for updating upgrade-coodinator state properties to database  # noqa: E501

        :return: The update_uc_state_properties of this UcStateProperties.  # noqa: E501
        :rtype: bool
        """
        return self._update_uc_state_properties

    @update_uc_state_properties.setter
    def update_uc_state_properties(self, update_uc_state_properties):
        """Sets the update_uc_state_properties of this UcStateProperties.

        Flag for updating upgrade-coodinator state properties to database  # noqa: E501

        :param update_uc_state_properties: The update_uc_state_properties of this UcStateProperties.  # noqa: E501
        :type: bool
        """

        self._update_uc_state_properties = update_uc_state_properties

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
        if issubclass(UcStateProperties, dict):
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
        if not isinstance(other, UcStateProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
