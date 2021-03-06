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


class NSSupportedAttributes(object):
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
        'ns_attributes': 'list[NSAttributes]'
    }

    attribute_map = {
        'ns_attributes': 'ns_attributes'
    }

    def __init__(self, ns_attributes=None):  # noqa: E501
        """NSSupportedAttributes - a model defined in Swagger"""  # noqa: E501
        self._ns_attributes = None
        self.discriminator = None
        self.ns_attributes = ns_attributes

    @property
    def ns_attributes(self):
        """Gets the ns_attributes of this NSSupportedAttributes.  # noqa: E501

        The type represent pre-defined list of supported attributes and sub-attributes that can be used while creating NSProfile   # noqa: E501

        :return: The ns_attributes of this NSSupportedAttributes.  # noqa: E501
        :rtype: list[NSAttributes]
        """
        return self._ns_attributes

    @ns_attributes.setter
    def ns_attributes(self, ns_attributes):
        """Sets the ns_attributes of this NSSupportedAttributes.

        The type represent pre-defined list of supported attributes and sub-attributes that can be used while creating NSProfile   # noqa: E501

        :param ns_attributes: The ns_attributes of this NSSupportedAttributes.  # noqa: E501
        :type: list[NSAttributes]
        """
        if ns_attributes is None:
            raise ValueError("Invalid value for `ns_attributes`, must not be `None`")  # noqa: E501

        self._ns_attributes = ns_attributes

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
        if issubclass(NSSupportedAttributes, dict):
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
        if not isinstance(other, NSSupportedAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
