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


class ServiceInstanceNSGroups(object):
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
        'nsroups': 'list[NSGroupInfo]'
    }

    attribute_map = {
        'nsroups': 'nsroups'
    }

    def __init__(self, nsroups=None):  # noqa: E501
        """ServiceInstanceNSGroups - a model defined in Swagger"""  # noqa: E501
        self._nsroups = None
        self.discriminator = None
        if nsroups is not None:
            self.nsroups = nsroups

    @property
    def nsroups(self):
        """Gets the nsroups of this ServiceInstanceNSGroups.  # noqa: E501

        List of NSGroups Used in ServiceInsertion Rules.  # noqa: E501

        :return: The nsroups of this ServiceInstanceNSGroups.  # noqa: E501
        :rtype: list[NSGroupInfo]
        """
        return self._nsroups

    @nsroups.setter
    def nsroups(self, nsroups):
        """Sets the nsroups of this ServiceInstanceNSGroups.

        List of NSGroups Used in ServiceInsertion Rules.  # noqa: E501

        :param nsroups: The nsroups of this ServiceInstanceNSGroups.  # noqa: E501
        :type: list[NSGroupInfo]
        """

        self._nsroups = nsroups

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
        if issubclass(ServiceInstanceNSGroups, dict):
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
        if not isinstance(other, ServiceInstanceNSGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
