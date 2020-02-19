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


class IdfwVmStats(object):
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
        'vm_ext_id': 'str',
        'active_sessions': 'list[IdfwUserSessionData]',
        'archived_sessions': 'list[IdfwUserSessionData]'
    }

    attribute_map = {
        'vm_ext_id': 'vm_ext_id',
        'active_sessions': 'active_sessions',
        'archived_sessions': 'archived_sessions'
    }

    def __init__(self, vm_ext_id=None, active_sessions=None, archived_sessions=None):  # noqa: E501
        """IdfwVmStats - a model defined in Swagger"""  # noqa: E501
        self._vm_ext_id = None
        self._active_sessions = None
        self._archived_sessions = None
        self.discriminator = None
        self.vm_ext_id = vm_ext_id
        self.active_sessions = active_sessions
        if archived_sessions is not None:
            self.archived_sessions = archived_sessions

    @property
    def vm_ext_id(self):
        """Gets the vm_ext_id of this IdfwVmStats.  # noqa: E501

        Virtual machine (external ID or BIOS UUID) where login/logout event occurred.  # noqa: E501

        :return: The vm_ext_id of this IdfwVmStats.  # noqa: E501
        :rtype: str
        """
        return self._vm_ext_id

    @vm_ext_id.setter
    def vm_ext_id(self, vm_ext_id):
        """Sets the vm_ext_id of this IdfwVmStats.

        Virtual machine (external ID or BIOS UUID) where login/logout event occurred.  # noqa: E501

        :param vm_ext_id: The vm_ext_id of this IdfwVmStats.  # noqa: E501
        :type: str
        """
        if vm_ext_id is None:
            raise ValueError("Invalid value for `vm_ext_id`, must not be `None`")  # noqa: E501

        self._vm_ext_id = vm_ext_id

    @property
    def active_sessions(self):
        """Gets the active_sessions of this IdfwVmStats.  # noqa: E501

        List of active (still logged in) user login/sessions data (no limit)  # noqa: E501

        :return: The active_sessions of this IdfwVmStats.  # noqa: E501
        :rtype: list[IdfwUserSessionData]
        """
        return self._active_sessions

    @active_sessions.setter
    def active_sessions(self, active_sessions):
        """Sets the active_sessions of this IdfwVmStats.

        List of active (still logged in) user login/sessions data (no limit)  # noqa: E501

        :param active_sessions: The active_sessions of this IdfwVmStats.  # noqa: E501
        :type: list[IdfwUserSessionData]
        """
        if active_sessions is None:
            raise ValueError("Invalid value for `active_sessions`, must not be `None`")  # noqa: E501

        self._active_sessions = active_sessions

    @property
    def archived_sessions(self):
        """Gets the archived_sessions of this IdfwVmStats.  # noqa: E501

        Optional list of up to 5 most recent archived (previously logged in) user login/session data.  # noqa: E501

        :return: The archived_sessions of this IdfwVmStats.  # noqa: E501
        :rtype: list[IdfwUserSessionData]
        """
        return self._archived_sessions

    @archived_sessions.setter
    def archived_sessions(self, archived_sessions):
        """Sets the archived_sessions of this IdfwVmStats.

        Optional list of up to 5 most recent archived (previously logged in) user login/session data.  # noqa: E501

        :param archived_sessions: The archived_sessions of this IdfwVmStats.  # noqa: E501
        :type: list[IdfwUserSessionData]
        """

        self._archived_sessions = archived_sessions

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
        if issubclass(IdfwVmStats, dict):
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
        if not isinstance(other, IdfwVmStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other