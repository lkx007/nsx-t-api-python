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


class NodeFileSystemProperties(object):
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
        'mount': 'str',
        'total': 'int',
        'type': 'str',
        'file_system': 'str',
        'used': 'int'
    }

    attribute_map = {
        'mount': 'mount',
        'total': 'total',
        'type': 'type',
        'file_system': 'file_system',
        'used': 'used'
    }

    def __init__(self, mount=None, total=None, type=None, file_system=None, used=None):  # noqa: E501
        """NodeFileSystemProperties - a model defined in Swagger"""  # noqa: E501
        self._mount = None
        self._total = None
        self._type = None
        self._file_system = None
        self._used = None
        self.discriminator = None
        if mount is not None:
            self.mount = mount
        if total is not None:
            self.total = total
        if type is not None:
            self.type = type
        if file_system is not None:
            self.file_system = file_system
        if used is not None:
            self.used = used

    @property
    def mount(self):
        """Gets the mount of this NodeFileSystemProperties.  # noqa: E501

        File system mount  # noqa: E501

        :return: The mount of this NodeFileSystemProperties.  # noqa: E501
        :rtype: str
        """
        return self._mount

    @mount.setter
    def mount(self, mount):
        """Sets the mount of this NodeFileSystemProperties.

        File system mount  # noqa: E501

        :param mount: The mount of this NodeFileSystemProperties.  # noqa: E501
        :type: str
        """

        self._mount = mount

    @property
    def total(self):
        """Gets the total of this NodeFileSystemProperties.  # noqa: E501

        File system size in kilobytes  # noqa: E501

        :return: The total of this NodeFileSystemProperties.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NodeFileSystemProperties.

        File system size in kilobytes  # noqa: E501

        :param total: The total of this NodeFileSystemProperties.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def type(self):
        """Gets the type of this NodeFileSystemProperties.  # noqa: E501

        File system type  # noqa: E501

        :return: The type of this NodeFileSystemProperties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeFileSystemProperties.

        File system type  # noqa: E501

        :param type: The type of this NodeFileSystemProperties.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def file_system(self):
        """Gets the file_system of this NodeFileSystemProperties.  # noqa: E501

        File system id  # noqa: E501

        :return: The file_system of this NodeFileSystemProperties.  # noqa: E501
        :rtype: str
        """
        return self._file_system

    @file_system.setter
    def file_system(self, file_system):
        """Sets the file_system of this NodeFileSystemProperties.

        File system id  # noqa: E501

        :param file_system: The file_system of this NodeFileSystemProperties.  # noqa: E501
        :type: str
        """

        self._file_system = file_system

    @property
    def used(self):
        """Gets the used of this NodeFileSystemProperties.  # noqa: E501

        Amount of file system used in kilobytes  # noqa: E501

        :return: The used of this NodeFileSystemProperties.  # noqa: E501
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this NodeFileSystemProperties.

        Amount of file system used in kilobytes  # noqa: E501

        :param used: The used of this NodeFileSystemProperties.  # noqa: E501
        :type: int
        """

        self._used = used

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
        if issubclass(NodeFileSystemProperties, dict):
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
        if not isinstance(other, NodeFileSystemProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
