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


class AttachmentContext(object):
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
        'allocate_addresses': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'allocate_addresses': 'allocate_addresses',
        'resource_type': 'resource_type'
    }

    discriminator_value_class_map = {
          'L2VpnAttachmentContext': 'L2VpnAttachmentContext',
'VifAttachmentContext': 'VifAttachmentContext'    }

    def __init__(self, allocate_addresses=None, resource_type=None):  # noqa: E501
        """AttachmentContext - a model defined in Swagger"""  # noqa: E501
        self._allocate_addresses = None
        self._resource_type = None
        self.discriminator = 'resource_type'
        if allocate_addresses is not None:
            self.allocate_addresses = allocate_addresses
        self.resource_type = resource_type

    @property
    def allocate_addresses(self):
        """Gets the allocate_addresses of this AttachmentContext.  # noqa: E501

        A flag to indicate whether to allocate addresses from allocation     pools bound to the parent logical switch.   # noqa: E501

        :return: The allocate_addresses of this AttachmentContext.  # noqa: E501
        :rtype: str
        """
        return self._allocate_addresses

    @allocate_addresses.setter
    def allocate_addresses(self, allocate_addresses):
        """Sets the allocate_addresses of this AttachmentContext.

        A flag to indicate whether to allocate addresses from allocation     pools bound to the parent logical switch.   # noqa: E501

        :param allocate_addresses: The allocate_addresses of this AttachmentContext.  # noqa: E501
        :type: str
        """
        allowed_values = ["IpPool", "MacPool", "Both", "None"]  # noqa: E501
        if allocate_addresses not in allowed_values:
            raise ValueError(
                "Invalid value for `allocate_addresses` ({0}), must be one of {1}"  # noqa: E501
                .format(allocate_addresses, allowed_values)
            )

        self._allocate_addresses = allocate_addresses

    @property
    def resource_type(self):
        """Gets the resource_type of this AttachmentContext.  # noqa: E501

        Used to identify which concrete class it is  # noqa: E501

        :return: The resource_type of this AttachmentContext.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AttachmentContext.

        Used to identify which concrete class it is  # noqa: E501

        :param resource_type: The resource_type of this AttachmentContext.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(AttachmentContext, dict):
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
        if not isinstance(other, AttachmentContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
