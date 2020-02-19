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


class NsxRole(object):
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
        'role': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'role': 'role',
        'permissions': 'permissions'
    }

    def __init__(self, role=None, permissions=None):  # noqa: E501
        """NsxRole - a model defined in Swagger"""  # noqa: E501
        self._role = None
        self._permissions = None
        self.discriminator = None
        self.role = role
        if permissions is not None:
            self.permissions = permissions

    @property
    def role(self):
        """Gets the role of this NsxRole.  # noqa: E501

        Role name  # noqa: E501

        :return: The role of this NsxRole.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this NsxRole.

        Role name  # noqa: E501

        :param role: The role of this NsxRole.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["read_only_api_users", "read_write_api_users", "enterprise_admin", "auditor", "network_engineer", "network_op", "security_engineer", "security_op", "lb_admin", "lb_auditor", "cloud_service_admin", "cloud_service_auditor", "site_reliability_engineer", "site_reliability_auditor", "cloud_admin", "cloud_auditor"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def permissions(self):
        """Gets the permissions of this NsxRole.  # noqa: E501

        Please use the /user-info/permissions api to get the permission that the user has on each feature.  # noqa: E501

        :return: The permissions of this NsxRole.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this NsxRole.

        Please use the /user-info/permissions api to get the permission that the user has on each feature.  # noqa: E501

        :param permissions: The permissions of this NsxRole.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["read-api", "read-write-api", "crud", "read", "execute", "none"]  # noqa: E501
        if not set(permissions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._permissions = permissions

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
        if issubclass(NsxRole, dict):
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
        if not isinstance(other, NsxRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
