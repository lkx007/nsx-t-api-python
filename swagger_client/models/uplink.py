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


class Uplink(object):
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
        'uplink_name': 'str',
        'uplink_type': 'str'
    }

    attribute_map = {
        'uplink_name': 'uplink_name',
        'uplink_type': 'uplink_type'
    }

    def __init__(self, uplink_name=None, uplink_type=None):  # noqa: E501
        """Uplink - a model defined in Swagger"""  # noqa: E501
        self._uplink_name = None
        self._uplink_type = None
        self.discriminator = None
        self.uplink_name = uplink_name
        self.uplink_type = uplink_type

    @property
    def uplink_name(self):
        """Gets the uplink_name of this Uplink.  # noqa: E501

        Name of this uplink  # noqa: E501

        :return: The uplink_name of this Uplink.  # noqa: E501
        :rtype: str
        """
        return self._uplink_name

    @uplink_name.setter
    def uplink_name(self, uplink_name):
        """Sets the uplink_name of this Uplink.

        Name of this uplink  # noqa: E501

        :param uplink_name: The uplink_name of this Uplink.  # noqa: E501
        :type: str
        """
        if uplink_name is None:
            raise ValueError("Invalid value for `uplink_name`, must not be `None`")  # noqa: E501

        self._uplink_name = uplink_name

    @property
    def uplink_type(self):
        """Gets the uplink_type of this Uplink.  # noqa: E501

        Type of the uplink  # noqa: E501

        :return: The uplink_type of this Uplink.  # noqa: E501
        :rtype: str
        """
        return self._uplink_type

    @uplink_type.setter
    def uplink_type(self, uplink_type):
        """Sets the uplink_type of this Uplink.

        Type of the uplink  # noqa: E501

        :param uplink_type: The uplink_type of this Uplink.  # noqa: E501
        :type: str
        """
        if uplink_type is None:
            raise ValueError("Invalid value for `uplink_type`, must not be `None`")  # noqa: E501
        allowed_values = ["PNIC", "LAG"]  # noqa: E501
        if uplink_type not in allowed_values:
            raise ValueError(
                "Invalid value for `uplink_type` ({0}), must be one of {1}"  # noqa: E501
                .format(uplink_type, allowed_values)
            )

        self._uplink_type = uplink_type

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
        if issubclass(Uplink, dict):
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
        if not isinstance(other, Uplink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
