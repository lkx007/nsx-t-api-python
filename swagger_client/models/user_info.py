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


class UserInfo(object):
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
        'user_name': 'str',
        'roles': 'list[NsxRole]'
    }

    attribute_map = {
        'user_name': 'user_name',
        'roles': 'roles'
    }

    def __init__(self, user_name=None, roles=None):  # noqa: E501
        """UserInfo - a model defined in Swagger"""  # noqa: E501
        self._user_name = None
        self._roles = None
        self.discriminator = None
        if user_name is not None:
            self.user_name = user_name
        if roles is not None:
            self.roles = roles

    @property
    def user_name(self):
        """Gets the user_name of this UserInfo.  # noqa: E501

        User Name  # noqa: E501

        :return: The user_name of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserInfo.

        User Name  # noqa: E501

        :param user_name: The user_name of this UserInfo.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def roles(self):
        """Gets the roles of this UserInfo.  # noqa: E501

        Permissions  # noqa: E501

        :return: The roles of this UserInfo.  # noqa: E501
        :rtype: list[NsxRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserInfo.

        Permissions  # noqa: E501

        :param roles: The roles of this UserInfo.  # noqa: E501
        :type: list[NsxRole]
        """

        self._roles = roles

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
        if issubclass(UserInfo, dict):
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
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other