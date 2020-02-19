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


class VirtualMachineTagUpdate(object):
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
        'external_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'external_id': 'external_id',
        'tags': 'tags'
    }

    def __init__(self, external_id=None, tags=None):  # noqa: E501
        """VirtualMachineTagUpdate - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._tags = None
        self.discriminator = None
        self.external_id = external_id
        self.tags = tags

    @property
    def external_id(self):
        """Gets the external_id of this VirtualMachineTagUpdate.  # noqa: E501

        External id of the virtual machine to which tags are to be applied  # noqa: E501

        :return: The external_id of this VirtualMachineTagUpdate.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this VirtualMachineTagUpdate.

        External id of the virtual machine to which tags are to be applied  # noqa: E501

        :param external_id: The external_id of this VirtualMachineTagUpdate.  # noqa: E501
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501

        self._external_id = external_id

    @property
    def tags(self):
        """Gets the tags of this VirtualMachineTagUpdate.  # noqa: E501

        List of tags to be applied to the virtual machine  # noqa: E501

        :return: The tags of this VirtualMachineTagUpdate.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VirtualMachineTagUpdate.

        List of tags to be applied to the virtual machine  # noqa: E501

        :param tags: The tags of this VirtualMachineTagUpdate.  # noqa: E501
        :type: list[Tag]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if issubclass(VirtualMachineTagUpdate, dict):
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
        if not isinstance(other, VirtualMachineTagUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
