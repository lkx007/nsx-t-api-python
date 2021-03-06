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


class Axes(object):
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
        'x_label': 'Label',
        'y_label': 'Label'
    }

    attribute_map = {
        'x_label': 'x_label',
        'y_label': 'y_label'
    }

    def __init__(self, x_label=None, y_label=None):  # noqa: E501
        """Axes - a model defined in Swagger"""  # noqa: E501
        self._x_label = None
        self._y_label = None
        self.discriminator = None
        if x_label is not None:
            self.x_label = x_label
        if y_label is not None:
            self.y_label = y_label

    @property
    def x_label(self):
        """Gets the x_label of this Axes.  # noqa: E501


        :return: The x_label of this Axes.  # noqa: E501
        :rtype: Label
        """
        return self._x_label

    @x_label.setter
    def x_label(self, x_label):
        """Sets the x_label of this Axes.


        :param x_label: The x_label of this Axes.  # noqa: E501
        :type: Label
        """

        self._x_label = x_label

    @property
    def y_label(self):
        """Gets the y_label of this Axes.  # noqa: E501


        :return: The y_label of this Axes.  # noqa: E501
        :rtype: Label
        """
        return self._y_label

    @y_label.setter
    def y_label(self, y_label):
        """Sets the y_label of this Axes.


        :param y_label: The y_label of this Axes.  # noqa: E501
        :type: Label
        """

        self._y_label = y_label

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
        if issubclass(Axes, dict):
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
        if not isinstance(other, Axes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
