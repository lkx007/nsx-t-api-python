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


class PerStepRestoreStatus(object):
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
        'description': 'str',
        'value': 'str'
    }

    attribute_map = {
        'description': 'description',
        'value': 'value'
    }

    def __init__(self, description=None, value=None):  # noqa: E501
        """PerStepRestoreStatus - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._value = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value

    @property
    def description(self):
        """Gets the description of this PerStepRestoreStatus.  # noqa: E501

        A description of the restore status  # noqa: E501

        :return: The description of this PerStepRestoreStatus.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PerStepRestoreStatus.

        A description of the restore status  # noqa: E501

        :param description: The description of this PerStepRestoreStatus.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this PerStepRestoreStatus.  # noqa: E501

        Per step restore status value  # noqa: E501

        :return: The value of this PerStepRestoreStatus.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PerStepRestoreStatus.

        Per step restore status value  # noqa: E501

        :param value: The value of this PerStepRestoreStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["INITIAL", "RUNNING", "SUSPENDED_BY_USER", "SUSPENDED_FOR_USER_ACTION", "FAILED", "SUCCESS"]  # noqa: E501
        if value not in allowed_values:
            raise ValueError(
                "Invalid value for `value` ({0}), must be one of {1}"  # noqa: E501
                .format(value, allowed_values)
            )

        self._value = value

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
        if issubclass(PerStepRestoreStatus, dict):
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
        if not isinstance(other, PerStepRestoreStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
