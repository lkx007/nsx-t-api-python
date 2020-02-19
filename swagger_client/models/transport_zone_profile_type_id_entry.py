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


class TransportZoneProfileTypeIdEntry(object):
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
        'profile_id': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'profile_id': 'profile_id',
        'resource_type': 'resource_type'
    }

    def __init__(self, profile_id=None, resource_type=None):  # noqa: E501
        """TransportZoneProfileTypeIdEntry - a model defined in Swagger"""  # noqa: E501
        self._profile_id = None
        self._resource_type = None
        self.discriminator = None
        self.profile_id = profile_id
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def profile_id(self):
        """Gets the profile_id of this TransportZoneProfileTypeIdEntry.  # noqa: E501

        profile id of the resource type  # noqa: E501

        :return: The profile_id of this TransportZoneProfileTypeIdEntry.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this TransportZoneProfileTypeIdEntry.

        profile id of the resource type  # noqa: E501

        :param profile_id: The profile_id of this TransportZoneProfileTypeIdEntry.  # noqa: E501
        :type: str
        """
        if profile_id is None:
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

    @property
    def resource_type(self):
        """Gets the resource_type of this TransportZoneProfileTypeIdEntry.  # noqa: E501

        Selects the type of the transport zone profile  # noqa: E501

        :return: The resource_type of this TransportZoneProfileTypeIdEntry.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TransportZoneProfileTypeIdEntry.

        Selects the type of the transport zone profile  # noqa: E501

        :param resource_type: The resource_type of this TransportZoneProfileTypeIdEntry.  # noqa: E501
        :type: str
        """
        allowed_values = ["BfdHealthMonitoringProfile"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

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
        if issubclass(TransportZoneProfileTypeIdEntry, dict):
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
        if not isinstance(other, TransportZoneProfileTypeIdEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
