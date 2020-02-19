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


class ReorderMigrationRequest(object):
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
        'is_before': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'is_before': 'is_before',
        'id': 'id'
    }

    def __init__(self, is_before=True, id=None):  # noqa: E501
        """ReorderMigrationRequest - a model defined in Swagger"""  # noqa: E501
        self._is_before = None
        self._id = None
        self.discriminator = None
        if is_before is not None:
            self.is_before = is_before
        self.id = id

    @property
    def is_before(self):
        """Gets the is_before of this ReorderMigrationRequest.  # noqa: E501

        flag indicating whether the migration unit group/migration unit is to be placed before or after the specified migration unit group/migration unit  # noqa: E501

        :return: The is_before of this ReorderMigrationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_before

    @is_before.setter
    def is_before(self, is_before):
        """Sets the is_before of this ReorderMigrationRequest.

        flag indicating whether the migration unit group/migration unit is to be placed before or after the specified migration unit group/migration unit  # noqa: E501

        :param is_before: The is_before of this ReorderMigrationRequest.  # noqa: E501
        :type: bool
        """

        self._is_before = is_before

    @property
    def id(self):
        """Gets the id of this ReorderMigrationRequest.  # noqa: E501

        id of the migration unit group/migration unit before/after which the migration unit group/migration unit is to be placed  # noqa: E501

        :return: The id of this ReorderMigrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReorderMigrationRequest.

        id of the migration unit group/migration unit before/after which the migration unit group/migration unit is to be placed  # noqa: E501

        :param id: The id of this ReorderMigrationRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if issubclass(ReorderMigrationRequest, dict):
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
        if not isinstance(other, ReorderMigrationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
