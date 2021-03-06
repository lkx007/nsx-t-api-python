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


class IdfwUserSessionDataAndMappings(object):
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
        'archived_user_sessions': 'list[IdfwUserSessionData]',
        'active_user_sessions': 'list[IdfwUserSessionData]',
        'dir_group_to_user_session_data_mappings': 'list[IdfwDirGroupUserSessionMapping]'
    }

    attribute_map = {
        'archived_user_sessions': 'archived_user_sessions',
        'active_user_sessions': 'active_user_sessions',
        'dir_group_to_user_session_data_mappings': 'dir_group_to_user_session_data_mappings'
    }

    def __init__(self, archived_user_sessions=None, active_user_sessions=None, dir_group_to_user_session_data_mappings=None):  # noqa: E501
        """IdfwUserSessionDataAndMappings - a model defined in Swagger"""  # noqa: E501
        self._archived_user_sessions = None
        self._active_user_sessions = None
        self._dir_group_to_user_session_data_mappings = None
        self.discriminator = None
        self.archived_user_sessions = archived_user_sessions
        self.active_user_sessions = active_user_sessions
        self.dir_group_to_user_session_data_mappings = dir_group_to_user_session_data_mappings

    @property
    def archived_user_sessions(self):
        """Gets the archived_user_sessions of this IdfwUserSessionDataAndMappings.  # noqa: E501

        Archived user session data list  # noqa: E501

        :return: The archived_user_sessions of this IdfwUserSessionDataAndMappings.  # noqa: E501
        :rtype: list[IdfwUserSessionData]
        """
        return self._archived_user_sessions

    @archived_user_sessions.setter
    def archived_user_sessions(self, archived_user_sessions):
        """Sets the archived_user_sessions of this IdfwUserSessionDataAndMappings.

        Archived user session data list  # noqa: E501

        :param archived_user_sessions: The archived_user_sessions of this IdfwUserSessionDataAndMappings.  # noqa: E501
        :type: list[IdfwUserSessionData]
        """
        if archived_user_sessions is None:
            raise ValueError("Invalid value for `archived_user_sessions`, must not be `None`")  # noqa: E501

        self._archived_user_sessions = archived_user_sessions

    @property
    def active_user_sessions(self):
        """Gets the active_user_sessions of this IdfwUserSessionDataAndMappings.  # noqa: E501

        Active user session data list  # noqa: E501

        :return: The active_user_sessions of this IdfwUserSessionDataAndMappings.  # noqa: E501
        :rtype: list[IdfwUserSessionData]
        """
        return self._active_user_sessions

    @active_user_sessions.setter
    def active_user_sessions(self, active_user_sessions):
        """Sets the active_user_sessions of this IdfwUserSessionDataAndMappings.

        Active user session data list  # noqa: E501

        :param active_user_sessions: The active_user_sessions of this IdfwUserSessionDataAndMappings.  # noqa: E501
        :type: list[IdfwUserSessionData]
        """
        if active_user_sessions is None:
            raise ValueError("Invalid value for `active_user_sessions`, must not be `None`")  # noqa: E501

        self._active_user_sessions = active_user_sessions

    @property
    def dir_group_to_user_session_data_mappings(self):
        """Gets the dir_group_to_user_session_data_mappings of this IdfwUserSessionDataAndMappings.  # noqa: E501

        Directory Group to user session data mappings  # noqa: E501

        :return: The dir_group_to_user_session_data_mappings of this IdfwUserSessionDataAndMappings.  # noqa: E501
        :rtype: list[IdfwDirGroupUserSessionMapping]
        """
        return self._dir_group_to_user_session_data_mappings

    @dir_group_to_user_session_data_mappings.setter
    def dir_group_to_user_session_data_mappings(self, dir_group_to_user_session_data_mappings):
        """Sets the dir_group_to_user_session_data_mappings of this IdfwUserSessionDataAndMappings.

        Directory Group to user session data mappings  # noqa: E501

        :param dir_group_to_user_session_data_mappings: The dir_group_to_user_session_data_mappings of this IdfwUserSessionDataAndMappings.  # noqa: E501
        :type: list[IdfwDirGroupUserSessionMapping]
        """
        if dir_group_to_user_session_data_mappings is None:
            raise ValueError("Invalid value for `dir_group_to_user_session_data_mappings`, must not be `None`")  # noqa: E501

        self._dir_group_to_user_session_data_mappings = dir_group_to_user_session_data_mappings

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
        if issubclass(IdfwUserSessionDataAndMappings, dict):
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
        if not isinstance(other, IdfwUserSessionDataAndMappings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
