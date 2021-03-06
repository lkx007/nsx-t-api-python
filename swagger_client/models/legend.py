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


class Legend(object):
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
        'position': 'str',
        'display_count': 'bool',
        'type': 'str',
        'alignment': 'str'
    }

    attribute_map = {
        'position': 'position',
        'display_count': 'display_count',
        'type': 'type',
        'alignment': 'alignment'
    }

    def __init__(self, position='RIGHT', display_count=True, type='CIRCLE', alignment='VERTICAL'):  # noqa: E501
        """Legend - a model defined in Swagger"""  # noqa: E501
        self._position = None
        self._display_count = None
        self._type = None
        self._alignment = None
        self.discriminator = None
        if position is not None:
            self.position = position
        if display_count is not None:
            self.display_count = display_count
        if type is not None:
            self.type = type
        if alignment is not None:
            self.alignment = alignment

    @property
    def position(self):
        """Gets the position of this Legend.  # noqa: E501

        Describes the relative placement of legend. The legend of a widget can be placed either to the TOP or BOTTOM or LEFT or RIGHT relative to the widget. For example, if RIGHT is chosen then legend is placed to the right of the widget.  # noqa: E501

        :return: The position of this Legend.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Legend.

        Describes the relative placement of legend. The legend of a widget can be placed either to the TOP or BOTTOM or LEFT or RIGHT relative to the widget. For example, if RIGHT is chosen then legend is placed to the right of the widget.  # noqa: E501

        :param position: The position of this Legend.  # noqa: E501
        :type: str
        """
        allowed_values = ["TOP", "BOTTOM", "LEFT", "RIGHT", "TOP_RIGHT"]  # noqa: E501
        if position not in allowed_values:
            raise ValueError(
                "Invalid value for `position` ({0}), must be one of {1}"  # noqa: E501
                .format(position, allowed_values)
            )

        self._position = position

    @property
    def display_count(self):
        """Gets the display_count of this Legend.  # noqa: E501

        If set to true, it will display the counts in legend. If set to false, counts of entities are not displayed in the legend.  # noqa: E501

        :return: The display_count of this Legend.  # noqa: E501
        :rtype: bool
        """
        return self._display_count

    @display_count.setter
    def display_count(self, display_count):
        """Sets the display_count of this Legend.

        If set to true, it will display the counts in legend. If set to false, counts of entities are not displayed in the legend.  # noqa: E501

        :param display_count: The display_count of this Legend.  # noqa: E501
        :type: bool
        """

        self._display_count = display_count

    @property
    def type(self):
        """Gets the type of this Legend.  # noqa: E501

        Describes the render type for the legend. The legend for an entity describes the entity in the widget. The supported legend type is a circle against which the entity's details such as display_name are shown. The color of the circle denotes the color of the entity shown inside the widget.  # noqa: E501

        :return: The type of this Legend.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Legend.

        Describes the render type for the legend. The legend for an entity describes the entity in the widget. The supported legend type is a circle against which the entity's details such as display_name are shown. The color of the circle denotes the color of the entity shown inside the widget.  # noqa: E501

        :param type: The type of this Legend.  # noqa: E501
        :type: str
        """
        allowed_values = ["CIRCLE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def alignment(self):
        """Gets the alignment of this Legend.  # noqa: E501

        Describes the alignment of legend. Alignment of a legend denotes how individual items of the legend are aligned in a container. For example, if VERTICAL is chosen then the items of the legend will appear one below the other and if HORIZONTAL is chosen then the items will appear side by side.  # noqa: E501

        :return: The alignment of this Legend.  # noqa: E501
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this Legend.

        Describes the alignment of legend. Alignment of a legend denotes how individual items of the legend are aligned in a container. For example, if VERTICAL is chosen then the items of the legend will appear one below the other and if HORIZONTAL is chosen then the items will appear side by side.  # noqa: E501

        :param alignment: The alignment of this Legend.  # noqa: E501
        :type: str
        """
        allowed_values = ["HORIZONTAL", "VERTICAL"]  # noqa: E501
        if alignment not in allowed_values:
            raise ValueError(
                "Invalid value for `alignment` ({0}), must be one of {1}"  # noqa: E501
                .format(alignment, allowed_values)
            )

        self._alignment = alignment

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
        if issubclass(Legend, dict):
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
        if not isinstance(other, Legend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
