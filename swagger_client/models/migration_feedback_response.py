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


class MigrationFeedbackResponse(object):
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
        'action': 'str',
        'values': 'list[str]',
        'id': 'str',
        'value': 'str'
    }

    attribute_map = {
        'action': 'action',
        'values': 'values',
        'id': 'id',
        'value': 'value'
    }

    def __init__(self, action=None, values=None, id=None, value=None):  # noqa: E501
        """MigrationFeedbackResponse - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._values = None
        self._id = None
        self._value = None
        self.discriminator = None
        self.action = action
        if values is not None:
            self.values = values
        self.id = id
        if value is not None:
            self.value = value

    @property
    def action(self):
        """Gets the action of this MigrationFeedbackResponse.  # noqa: E501

        Action selected in response to the feedback request.  # noqa: E501

        :return: The action of this MigrationFeedbackResponse.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this MigrationFeedbackResponse.

        Action selected in response to the feedback request.  # noqa: E501

        :param action: The action of this MigrationFeedbackResponse.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def values(self):
        """Gets the values of this MigrationFeedbackResponse.  # noqa: E501

        User input provided in the form of a list of values in response to the feedback request.  # noqa: E501

        :return: The values of this MigrationFeedbackResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this MigrationFeedbackResponse.

        User input provided in the form of a list of values in response to the feedback request.  # noqa: E501

        :param values: The values of this MigrationFeedbackResponse.  # noqa: E501
        :type: list[str]
        """

        self._values = values

    @property
    def id(self):
        """Gets the id of this MigrationFeedbackResponse.  # noqa: E501

        Identifier of the feedback request.  # noqa: E501

        :return: The id of this MigrationFeedbackResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MigrationFeedbackResponse.

        Identifier of the feedback request.  # noqa: E501

        :param id: The id of this MigrationFeedbackResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def value(self):
        """Gets the value of this MigrationFeedbackResponse.  # noqa: E501

        User input provided in response to the feedback request.  # noqa: E501

        :return: The value of this MigrationFeedbackResponse.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MigrationFeedbackResponse.

        User input provided in response to the feedback request.  # noqa: E501

        :param value: The value of this MigrationFeedbackResponse.  # noqa: E501
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
        if issubclass(MigrationFeedbackResponse, dict):
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
        if not isinstance(other, MigrationFeedbackResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other