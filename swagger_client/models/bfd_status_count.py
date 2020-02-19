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


class BFDStatusCount(object):
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
        'bfd_admin_down_count': 'int',
        'bfd_up_count': 'int',
        'bfd_down_count': 'int',
        'bfd_init_count': 'int'
    }

    attribute_map = {
        'bfd_admin_down_count': 'bfd_admin_down_count',
        'bfd_up_count': 'bfd_up_count',
        'bfd_down_count': 'bfd_down_count',
        'bfd_init_count': 'bfd_init_count'
    }

    def __init__(self, bfd_admin_down_count=None, bfd_up_count=None, bfd_down_count=None, bfd_init_count=None):  # noqa: E501
        """BFDStatusCount - a model defined in Swagger"""  # noqa: E501
        self._bfd_admin_down_count = None
        self._bfd_up_count = None
        self._bfd_down_count = None
        self._bfd_init_count = None
        self.discriminator = None
        if bfd_admin_down_count is not None:
            self.bfd_admin_down_count = bfd_admin_down_count
        if bfd_up_count is not None:
            self.bfd_up_count = bfd_up_count
        if bfd_down_count is not None:
            self.bfd_down_count = bfd_down_count
        if bfd_init_count is not None:
            self.bfd_init_count = bfd_init_count

    @property
    def bfd_admin_down_count(self):
        """Gets the bfd_admin_down_count of this BFDStatusCount.  # noqa: E501

        Number of tunnels in BFD admin down state  # noqa: E501

        :return: The bfd_admin_down_count of this BFDStatusCount.  # noqa: E501
        :rtype: int
        """
        return self._bfd_admin_down_count

    @bfd_admin_down_count.setter
    def bfd_admin_down_count(self, bfd_admin_down_count):
        """Sets the bfd_admin_down_count of this BFDStatusCount.

        Number of tunnels in BFD admin down state  # noqa: E501

        :param bfd_admin_down_count: The bfd_admin_down_count of this BFDStatusCount.  # noqa: E501
        :type: int
        """

        self._bfd_admin_down_count = bfd_admin_down_count

    @property
    def bfd_up_count(self):
        """Gets the bfd_up_count of this BFDStatusCount.  # noqa: E501

        Number of tunnels in BFD up state  # noqa: E501

        :return: The bfd_up_count of this BFDStatusCount.  # noqa: E501
        :rtype: int
        """
        return self._bfd_up_count

    @bfd_up_count.setter
    def bfd_up_count(self, bfd_up_count):
        """Sets the bfd_up_count of this BFDStatusCount.

        Number of tunnels in BFD up state  # noqa: E501

        :param bfd_up_count: The bfd_up_count of this BFDStatusCount.  # noqa: E501
        :type: int
        """

        self._bfd_up_count = bfd_up_count

    @property
    def bfd_down_count(self):
        """Gets the bfd_down_count of this BFDStatusCount.  # noqa: E501

        Number of tunnels in BFD down state  # noqa: E501

        :return: The bfd_down_count of this BFDStatusCount.  # noqa: E501
        :rtype: int
        """
        return self._bfd_down_count

    @bfd_down_count.setter
    def bfd_down_count(self, bfd_down_count):
        """Sets the bfd_down_count of this BFDStatusCount.

        Number of tunnels in BFD down state  # noqa: E501

        :param bfd_down_count: The bfd_down_count of this BFDStatusCount.  # noqa: E501
        :type: int
        """

        self._bfd_down_count = bfd_down_count

    @property
    def bfd_init_count(self):
        """Gets the bfd_init_count of this BFDStatusCount.  # noqa: E501

        Number of tunnels in BFD init state  # noqa: E501

        :return: The bfd_init_count of this BFDStatusCount.  # noqa: E501
        :rtype: int
        """
        return self._bfd_init_count

    @bfd_init_count.setter
    def bfd_init_count(self, bfd_init_count):
        """Sets the bfd_init_count of this BFDStatusCount.

        Number of tunnels in BFD init state  # noqa: E501

        :param bfd_init_count: The bfd_init_count of this BFDStatusCount.  # noqa: E501
        :type: int
        """

        self._bfd_init_count = bfd_init_count

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
        if issubclass(BFDStatusCount, dict):
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
        if not isinstance(other, BFDStatusCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
