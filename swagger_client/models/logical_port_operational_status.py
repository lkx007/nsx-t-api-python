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


class LogicalPortOperationalStatus(object):
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
        'logical_port_id': 'str',
        'status': 'str',
        'last_update_timestamp': 'int'
    }

    attribute_map = {
        'logical_port_id': 'logical_port_id',
        'status': 'status',
        'last_update_timestamp': 'last_update_timestamp'
    }

    def __init__(self, logical_port_id=None, status=None, last_update_timestamp=None):  # noqa: E501
        """LogicalPortOperationalStatus - a model defined in Swagger"""  # noqa: E501
        self._logical_port_id = None
        self._status = None
        self._last_update_timestamp = None
        self.discriminator = None
        if logical_port_id is not None:
            self.logical_port_id = logical_port_id
        self.status = status
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp

    @property
    def logical_port_id(self):
        """Gets the logical_port_id of this LogicalPortOperationalStatus.  # noqa: E501

        The id of the logical port  # noqa: E501

        :return: The logical_port_id of this LogicalPortOperationalStatus.  # noqa: E501
        :rtype: str
        """
        return self._logical_port_id

    @logical_port_id.setter
    def logical_port_id(self, logical_port_id):
        """Sets the logical_port_id of this LogicalPortOperationalStatus.

        The id of the logical port  # noqa: E501

        :param logical_port_id: The logical_port_id of this LogicalPortOperationalStatus.  # noqa: E501
        :type: str
        """

        self._logical_port_id = logical_port_id

    @property
    def status(self):
        """Gets the status of this LogicalPortOperationalStatus.  # noqa: E501

        The Operational status of the logical port  # noqa: E501

        :return: The status of this LogicalPortOperationalStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LogicalPortOperationalStatus.

        The Operational status of the logical port  # noqa: E501

        :param status: The status of this LogicalPortOperationalStatus.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["UP", "DOWN", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this LogicalPortOperationalStatus.  # noqa: E501

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :return: The last_update_timestamp of this LogicalPortOperationalStatus.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this LogicalPortOperationalStatus.

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this LogicalPortOperationalStatus.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

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
        if issubclass(LogicalPortOperationalStatus, dict):
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
        if not isinstance(other, LogicalPortOperationalStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other