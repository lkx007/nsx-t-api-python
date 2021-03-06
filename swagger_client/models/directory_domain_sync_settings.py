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


class DirectoryDomainSyncSettings(object):
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
        'full_sync_cron_expr': 'str',
        'delta_sync_interval': 'int'
    }

    attribute_map = {
        'full_sync_cron_expr': 'full_sync_cron_expr',
        'delta_sync_interval': 'delta_sync_interval'
    }

    def __init__(self, full_sync_cron_expr=None, delta_sync_interval=180):  # noqa: E501
        """DirectoryDomainSyncSettings - a model defined in Swagger"""  # noqa: E501
        self._full_sync_cron_expr = None
        self._delta_sync_interval = None
        self.discriminator = None
        if full_sync_cron_expr is not None:
            self.full_sync_cron_expr = full_sync_cron_expr
        if delta_sync_interval is not None:
            self.delta_sync_interval = delta_sync_interval

    @property
    def full_sync_cron_expr(self):
        """Gets the full_sync_cron_expr of this DirectoryDomainSyncSettings.  # noqa: E501

        Directory domain full synchronization schedule using cron expression. For example, cron expression \"0 0 12 ? * SUN *\" means full sync is scheduled every Sunday midnight. If this object is null, it means there is no background cron job running for full sync.  # noqa: E501

        :return: The full_sync_cron_expr of this DirectoryDomainSyncSettings.  # noqa: E501
        :rtype: str
        """
        return self._full_sync_cron_expr

    @full_sync_cron_expr.setter
    def full_sync_cron_expr(self, full_sync_cron_expr):
        """Sets the full_sync_cron_expr of this DirectoryDomainSyncSettings.

        Directory domain full synchronization schedule using cron expression. For example, cron expression \"0 0 12 ? * SUN *\" means full sync is scheduled every Sunday midnight. If this object is null, it means there is no background cron job running for full sync.  # noqa: E501

        :param full_sync_cron_expr: The full_sync_cron_expr of this DirectoryDomainSyncSettings.  # noqa: E501
        :type: str
        """

        self._full_sync_cron_expr = full_sync_cron_expr

    @property
    def delta_sync_interval(self):
        """Gets the delta_sync_interval of this DirectoryDomainSyncSettings.  # noqa: E501

        Directory domain delta synchronization interval time between two delta sync in minutes.  # noqa: E501

        :return: The delta_sync_interval of this DirectoryDomainSyncSettings.  # noqa: E501
        :rtype: int
        """
        return self._delta_sync_interval

    @delta_sync_interval.setter
    def delta_sync_interval(self, delta_sync_interval):
        """Sets the delta_sync_interval of this DirectoryDomainSyncSettings.

        Directory domain delta synchronization interval time between two delta sync in minutes.  # noqa: E501

        :param delta_sync_interval: The delta_sync_interval of this DirectoryDomainSyncSettings.  # noqa: E501
        :type: int
        """

        self._delta_sync_interval = delta_sync_interval

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
        if issubclass(DirectoryDomainSyncSettings, dict):
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
        if not isinstance(other, DirectoryDomainSyncSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
