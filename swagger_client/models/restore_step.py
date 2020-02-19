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


class RestoreStep(object):
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
        'status': 'PerStepRestoreStatus',
        'step_number': 'int',
        'description': 'str',
        'value': 'str'
    }

    attribute_map = {
        'status': 'status',
        'step_number': 'step_number',
        'description': 'description',
        'value': 'value'
    }

    def __init__(self, status=None, step_number=None, description=None, value=None):  # noqa: E501
        """RestoreStep - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._step_number = None
        self._description = None
        self._value = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if step_number is not None:
            self.step_number = step_number
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value

    @property
    def status(self):
        """Gets the status of this RestoreStep.  # noqa: E501


        :return: The status of this RestoreStep.  # noqa: E501
        :rtype: PerStepRestoreStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RestoreStep.


        :param status: The status of this RestoreStep.  # noqa: E501
        :type: PerStepRestoreStatus
        """

        self._status = status

    @property
    def step_number(self):
        """Gets the step_number of this RestoreStep.  # noqa: E501

        Restore step number  # noqa: E501

        :return: The step_number of this RestoreStep.  # noqa: E501
        :rtype: int
        """
        return self._step_number

    @step_number.setter
    def step_number(self, step_number):
        """Sets the step_number of this RestoreStep.

        Restore step number  # noqa: E501

        :param step_number: The step_number of this RestoreStep.  # noqa: E501
        :type: int
        """

        self._step_number = step_number

    @property
    def description(self):
        """Gets the description of this RestoreStep.  # noqa: E501

        Restore step description  # noqa: E501

        :return: The description of this RestoreStep.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RestoreStep.

        Restore step description  # noqa: E501

        :param description: The description of this RestoreStep.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this RestoreStep.  # noqa: E501

        Restore step value  # noqa: E501

        :return: The value of this RestoreStep.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RestoreStep.

        Restore step value  # noqa: E501

        :param value: The value of this RestoreStep.  # noqa: E501
        :type: str
        """

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
        if issubclass(RestoreStep, dict):
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
        if not isinstance(other, RestoreStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
