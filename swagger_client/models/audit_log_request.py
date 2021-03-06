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


class AuditLogRequest(object):
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
        'log_filter': 'str',
        'log_age_limit': 'int',
        'log_filter_type': 'str'
    }

    attribute_map = {
        'log_filter': 'log_filter',
        'log_age_limit': 'log_age_limit',
        'log_filter_type': 'log_filter_type'
    }

    def __init__(self, log_filter=None, log_age_limit=None, log_filter_type='TEXT'):  # noqa: E501
        """AuditLogRequest - a model defined in Swagger"""  # noqa: E501
        self._log_filter = None
        self._log_age_limit = None
        self._log_filter_type = None
        self.discriminator = None
        if log_filter is not None:
            self.log_filter = log_filter
        if log_age_limit is not None:
            self.log_age_limit = log_age_limit
        if log_filter_type is not None:
            self.log_filter_type = log_filter_type

    @property
    def log_filter(self):
        """Gets the log_filter of this AuditLogRequest.  # noqa: E501

        Audit logs should meet the filter condition  # noqa: E501

        :return: The log_filter of this AuditLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._log_filter

    @log_filter.setter
    def log_filter(self, log_filter):
        """Sets the log_filter of this AuditLogRequest.

        Audit logs should meet the filter condition  # noqa: E501

        :param log_filter: The log_filter of this AuditLogRequest.  # noqa: E501
        :type: str
        """

        self._log_filter = log_filter

    @property
    def log_age_limit(self):
        """Gets the log_age_limit of this AuditLogRequest.  # noqa: E501

        Include logs with timstamps not past the age limit in days  # noqa: E501

        :return: The log_age_limit of this AuditLogRequest.  # noqa: E501
        :rtype: int
        """
        return self._log_age_limit

    @log_age_limit.setter
    def log_age_limit(self, log_age_limit):
        """Sets the log_age_limit of this AuditLogRequest.

        Include logs with timstamps not past the age limit in days  # noqa: E501

        :param log_age_limit: The log_age_limit of this AuditLogRequest.  # noqa: E501
        :type: int
        """

        self._log_age_limit = log_age_limit

    @property
    def log_filter_type(self):
        """Gets the log_filter_type of this AuditLogRequest.  # noqa: E501

        Type of log filter  # noqa: E501

        :return: The log_filter_type of this AuditLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._log_filter_type

    @log_filter_type.setter
    def log_filter_type(self, log_filter_type):
        """Sets the log_filter_type of this AuditLogRequest.

        Type of log filter  # noqa: E501

        :param log_filter_type: The log_filter_type of this AuditLogRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["TEXT", "REGEX"]  # noqa: E501
        if log_filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `log_filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(log_filter_type, allowed_values)
            )

        self._log_filter_type = log_filter_type

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
        if issubclass(AuditLogRequest, dict):
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
        if not isinstance(other, AuditLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
