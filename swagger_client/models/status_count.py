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


class StatusCount(object):
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
        'status': 'str',
        'degraded_count': 'int',
        'down_count': 'int',
        'up_count': 'int'
    }

    attribute_map = {
        'status': 'status',
        'degraded_count': 'degraded_count',
        'down_count': 'down_count',
        'up_count': 'up_count'
    }

    def __init__(self, status=None, degraded_count=None, down_count=None, up_count=None):  # noqa: E501
        """StatusCount - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._degraded_count = None
        self._down_count = None
        self._up_count = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if degraded_count is not None:
            self.degraded_count = degraded_count
        if down_count is not None:
            self.down_count = down_count
        if up_count is not None:
            self.up_count = up_count

    @property
    def status(self):
        """Gets the status of this StatusCount.  # noqa: E501

        Roll-up status  # noqa: E501

        :return: The status of this StatusCount.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StatusCount.

        Roll-up status  # noqa: E501

        :param status: The status of this StatusCount.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN", "DEGRADED", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def degraded_count(self):
        """Gets the degraded_count of this StatusCount.  # noqa: E501

        Degraded count  # noqa: E501

        :return: The degraded_count of this StatusCount.  # noqa: E501
        :rtype: int
        """
        return self._degraded_count

    @degraded_count.setter
    def degraded_count(self, degraded_count):
        """Sets the degraded_count of this StatusCount.

        Degraded count  # noqa: E501

        :param degraded_count: The degraded_count of this StatusCount.  # noqa: E501
        :type: int
        """

        self._degraded_count = degraded_count

    @property
    def down_count(self):
        """Gets the down_count of this StatusCount.  # noqa: E501

        Down count  # noqa: E501

        :return: The down_count of this StatusCount.  # noqa: E501
        :rtype: int
        """
        return self._down_count

    @down_count.setter
    def down_count(self, down_count):
        """Sets the down_count of this StatusCount.

        Down count  # noqa: E501

        :param down_count: The down_count of this StatusCount.  # noqa: E501
        :type: int
        """

        self._down_count = down_count

    @property
    def up_count(self):
        """Gets the up_count of this StatusCount.  # noqa: E501

        Up count  # noqa: E501

        :return: The up_count of this StatusCount.  # noqa: E501
        :rtype: int
        """
        return self._up_count

    @up_count.setter
    def up_count(self, up_count):
        """Sets the up_count of this StatusCount.

        Up count  # noqa: E501

        :param up_count: The up_count of this StatusCount.  # noqa: E501
        :type: int
        """

        self._up_count = up_count

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
        if issubclass(StatusCount, dict):
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
        if not isinstance(other, StatusCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
