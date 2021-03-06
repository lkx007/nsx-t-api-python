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


class Datasource(object):
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
        'display_name': 'str',
        'urls': 'list[UrlAlias]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'urls': 'urls'
    }

    def __init__(self, display_name=None, urls=None):  # noqa: E501
        """Datasource - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._urls = None
        self.discriminator = None
        self.display_name = display_name
        self.urls = urls

    @property
    def display_name(self):
        """Gets the display_name of this Datasource.  # noqa: E501

        Name of a datasource instance.  # noqa: E501

        :return: The display_name of this Datasource.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Datasource.

        Name of a datasource instance.  # noqa: E501

        :param display_name: The display_name of this Datasource.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def urls(self):
        """Gets the urls of this Datasource.  # noqa: E501

        Array of urls relative to the datasource configuration. For example, api/v1/fabric/nodes is a relative url of nsx-manager instance.  # noqa: E501

        :return: The urls of this Datasource.  # noqa: E501
        :rtype: list[UrlAlias]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this Datasource.

        Array of urls relative to the datasource configuration. For example, api/v1/fabric/nodes is a relative url of nsx-manager instance.  # noqa: E501

        :param urls: The urls of this Datasource.  # noqa: E501
        :type: list[UrlAlias]
        """
        if urls is None:
            raise ValueError("Invalid value for `urls`, must not be `None`")  # noqa: E501

        self._urls = urls

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
        if issubclass(Datasource, dict):
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
        if not isinstance(other, Datasource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
