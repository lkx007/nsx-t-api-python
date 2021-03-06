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


class IdfwSystemStats(object):
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
        'num_concurrent_users': 'int',
        'num_user_sessions': 'int'
    }

    attribute_map = {
        'num_concurrent_users': 'num_concurrent_users',
        'num_user_sessions': 'num_user_sessions'
    }

    def __init__(self, num_concurrent_users=None, num_user_sessions=None):  # noqa: E501
        """IdfwSystemStats - a model defined in Swagger"""  # noqa: E501
        self._num_concurrent_users = None
        self._num_user_sessions = None
        self.discriminator = None
        self.num_concurrent_users = num_concurrent_users
        self.num_user_sessions = num_user_sessions

    @property
    def num_concurrent_users(self):
        """Gets the num_concurrent_users of this IdfwSystemStats.  # noqa: E501

        Number of concurrent logged on users (across VDI & RDSH).  Multiple logins by the same user is counted as 1.   # noqa: E501

        :return: The num_concurrent_users of this IdfwSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._num_concurrent_users

    @num_concurrent_users.setter
    def num_concurrent_users(self, num_concurrent_users):
        """Sets the num_concurrent_users of this IdfwSystemStats.

        Number of concurrent logged on users (across VDI & RDSH).  Multiple logins by the same user is counted as 1.   # noqa: E501

        :param num_concurrent_users: The num_concurrent_users of this IdfwSystemStats.  # noqa: E501
        :type: int
        """
        if num_concurrent_users is None:
            raise ValueError("Invalid value for `num_concurrent_users`, must not be `None`")  # noqa: E501

        self._num_concurrent_users = num_concurrent_users

    @property
    def num_user_sessions(self):
        """Gets the num_user_sessions of this IdfwSystemStats.  # noqa: E501

        Number of active user sessions/logins in IDFW enabled compute collections (including both UP and DOWN hosts).  N sessions/logins by the same user is counted as n.   # noqa: E501

        :return: The num_user_sessions of this IdfwSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._num_user_sessions

    @num_user_sessions.setter
    def num_user_sessions(self, num_user_sessions):
        """Sets the num_user_sessions of this IdfwSystemStats.

        Number of active user sessions/logins in IDFW enabled compute collections (including both UP and DOWN hosts).  N sessions/logins by the same user is counted as n.   # noqa: E501

        :param num_user_sessions: The num_user_sessions of this IdfwSystemStats.  # noqa: E501
        :type: int
        """
        if num_user_sessions is None:
            raise ValueError("Invalid value for `num_user_sessions`, must not be `None`")  # noqa: E501

        self._num_user_sessions = num_user_sessions

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
        if issubclass(IdfwSystemStats, dict):
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
        if not isinstance(other, IdfwSystemStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
