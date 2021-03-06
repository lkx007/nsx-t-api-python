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


class ColumnItem(object):
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
        'sort_key': 'str',
        'type': 'str',
        'tooltip': 'list[Tooltip]',
        'label': 'Label',
        'field': 'str',
        'sort_ascending': 'bool',
        'drilldown_id': 'str',
        'hidden': 'bool',
        'navigation': 'str',
        'column_identifier': 'str',
        'render_configuration': 'list[RenderConfiguration]'
    }

    attribute_map = {
        'sort_key': 'sort_key',
        'type': 'type',
        'tooltip': 'tooltip',
        'label': 'label',
        'field': 'field',
        'sort_ascending': 'sort_ascending',
        'drilldown_id': 'drilldown_id',
        'hidden': 'hidden',
        'navigation': 'navigation',
        'column_identifier': 'column_identifier',
        'render_configuration': 'render_configuration'
    }

    def __init__(self, sort_key=None, type='String', tooltip=None, label=None, field=None, sort_ascending=True, drilldown_id=None, hidden=False, navigation=None, column_identifier=None, render_configuration=None):  # noqa: E501
        """ColumnItem - a model defined in Swagger"""  # noqa: E501
        self._sort_key = None
        self._type = None
        self._tooltip = None
        self._label = None
        self._field = None
        self._sort_ascending = None
        self._drilldown_id = None
        self._hidden = None
        self._navigation = None
        self._column_identifier = None
        self._render_configuration = None
        self.discriminator = None
        if sort_key is not None:
            self.sort_key = sort_key
        self.type = type
        if tooltip is not None:
            self.tooltip = tooltip
        self.label = label
        self.field = field
        if sort_ascending is not None:
            self.sort_ascending = sort_ascending
        if drilldown_id is not None:
            self.drilldown_id = drilldown_id
        if hidden is not None:
            self.hidden = hidden
        if navigation is not None:
            self.navigation = navigation
        if column_identifier is not None:
            self.column_identifier = column_identifier
        if render_configuration is not None:
            self.render_configuration = render_configuration

    @property
    def sort_key(self):
        """Gets the sort_key of this ColumnItem.  # noqa: E501

        Sorting on column is based on the sort_key. sort_key represents the field in the output data on which sort is requested.  # noqa: E501

        :return: The sort_key of this ColumnItem.  # noqa: E501
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ColumnItem.

        Sorting on column is based on the sort_key. sort_key represents the field in the output data on which sort is requested.  # noqa: E501

        :param sort_key: The sort_key of this ColumnItem.  # noqa: E501
        :type: str
        """

        self._sort_key = sort_key

    @property
    def type(self):
        """Gets the type of this ColumnItem.  # noqa: E501

        Data type of the field.  # noqa: E501

        :return: The type of this ColumnItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ColumnItem.

        Data type of the field.  # noqa: E501

        :param type: The type of this ColumnItem.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["String", "Number", "Date"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def tooltip(self):
        """Gets the tooltip of this ColumnItem.  # noqa: E501

        Multi-line text to be shown on tooltip while hovering over a cell in the grid.  # noqa: E501

        :return: The tooltip of this ColumnItem.  # noqa: E501
        :rtype: list[Tooltip]
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this ColumnItem.

        Multi-line text to be shown on tooltip while hovering over a cell in the grid.  # noqa: E501

        :param tooltip: The tooltip of this ColumnItem.  # noqa: E501
        :type: list[Tooltip]
        """

        self._tooltip = tooltip

    @property
    def label(self):
        """Gets the label of this ColumnItem.  # noqa: E501


        :return: The label of this ColumnItem.  # noqa: E501
        :rtype: Label
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ColumnItem.


        :param label: The label of this ColumnItem.  # noqa: E501
        :type: Label
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def field(self):
        """Gets the field of this ColumnItem.  # noqa: E501

        Field from which values of the column will be derived.  # noqa: E501

        :return: The field of this ColumnItem.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this ColumnItem.

        Field from which values of the column will be derived.  # noqa: E501

        :param field: The field of this ColumnItem.  # noqa: E501
        :type: str
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def sort_ascending(self):
        """Gets the sort_ascending of this ColumnItem.  # noqa: E501

        If true, the value of the column are sorted in ascending order. Otherwise, in descending order.  # noqa: E501

        :return: The sort_ascending of this ColumnItem.  # noqa: E501
        :rtype: bool
        """
        return self._sort_ascending

    @sort_ascending.setter
    def sort_ascending(self, sort_ascending):
        """Sets the sort_ascending of this ColumnItem.

        If true, the value of the column are sorted in ascending order. Otherwise, in descending order.  # noqa: E501

        :param sort_ascending: The sort_ascending of this ColumnItem.  # noqa: E501
        :type: bool
        """

        self._sort_ascending = sort_ascending

    @property
    def drilldown_id(self):
        """Gets the drilldown_id of this ColumnItem.  # noqa: E501

        Id of drilldown widget, if any. Id should be a valid id of an existing widget.  # noqa: E501

        :return: The drilldown_id of this ColumnItem.  # noqa: E501
        :rtype: str
        """
        return self._drilldown_id

    @drilldown_id.setter
    def drilldown_id(self, drilldown_id):
        """Sets the drilldown_id of this ColumnItem.

        Id of drilldown widget, if any. Id should be a valid id of an existing widget.  # noqa: E501

        :param drilldown_id: The drilldown_id of this ColumnItem.  # noqa: E501
        :type: str
        """

        self._drilldown_id = drilldown_id

    @property
    def hidden(self):
        """Gets the hidden of this ColumnItem.  # noqa: E501

        If set to true, hides the column  # noqa: E501

        :return: The hidden of this ColumnItem.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ColumnItem.

        If set to true, hides the column  # noqa: E501

        :param hidden: The hidden of this ColumnItem.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def navigation(self):
        """Gets the navigation of this ColumnItem.  # noqa: E501

        Hyperlink of the specified UI page that provides details. If drilldown_id is provided, then navigation cannot be used.  # noqa: E501

        :return: The navigation of this ColumnItem.  # noqa: E501
        :rtype: str
        """
        return self._navigation

    @navigation.setter
    def navigation(self, navigation):
        """Sets the navigation of this ColumnItem.

        Hyperlink of the specified UI page that provides details. If drilldown_id is provided, then navigation cannot be used.  # noqa: E501

        :param navigation: The navigation of this ColumnItem.  # noqa: E501
        :type: str
        """

        self._navigation = navigation

    @property
    def column_identifier(self):
        """Gets the column_identifier of this ColumnItem.  # noqa: E501

        Identifies the column and used for fetching content upon an user click or drilldown. If column identifier is not provided, the column's data will not participate in searches and drilldowns.  # noqa: E501

        :return: The column_identifier of this ColumnItem.  # noqa: E501
        :rtype: str
        """
        return self._column_identifier

    @column_identifier.setter
    def column_identifier(self, column_identifier):
        """Sets the column_identifier of this ColumnItem.

        Identifies the column and used for fetching content upon an user click or drilldown. If column identifier is not provided, the column's data will not participate in searches and drilldowns.  # noqa: E501

        :param column_identifier: The column_identifier of this ColumnItem.  # noqa: E501
        :type: str
        """

        self._column_identifier = column_identifier

    @property
    def render_configuration(self):
        """Gets the render_configuration of this ColumnItem.  # noqa: E501

        Render configuration to be applied, if any.  # noqa: E501

        :return: The render_configuration of this ColumnItem.  # noqa: E501
        :rtype: list[RenderConfiguration]
        """
        return self._render_configuration

    @render_configuration.setter
    def render_configuration(self, render_configuration):
        """Sets the render_configuration of this ColumnItem.

        Render configuration to be applied, if any.  # noqa: E501

        :param render_configuration: The render_configuration of this ColumnItem.  # noqa: E501
        :type: list[RenderConfiguration]
        """

        self._render_configuration = render_configuration

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
        if issubclass(ColumnItem, dict):
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
        if not isinstance(other, ColumnItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
