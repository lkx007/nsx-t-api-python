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


class NSXProfileReference(object):
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
        'target_display_name': 'str',
        'is_valid': 'bool',
        'target_id': 'str',
        'target_type': 'str',
        'profile_type': 'str'
    }
    if hasattr(ResourceReference, "swagger_types"):
        swagger_types.update(ResourceReference.swagger_types)

    attribute_map = {
        'target_display_name': 'target_display_name',
        'is_valid': 'is_valid',
        'target_id': 'target_id',
        'target_type': 'target_type',
        'profile_type': 'profile_type'
    }
    if hasattr(ResourceReference, "attribute_map"):
        attribute_map.update(ResourceReference.attribute_map)

    def __init__(self, target_display_name=None, is_valid=None, target_id=None, target_type=None, profile_type=None, *args, **kwargs):  # noqa: E501
        """NSXProfileReference - a model defined in Swagger"""  # noqa: E501
        self._target_display_name = None
        self._is_valid = None
        self._target_id = None
        self._target_type = None
        self._profile_type = None
        self.discriminator = None
        if target_display_name is not None:
            self.target_display_name = target_display_name
        if is_valid is not None:
            self.is_valid = is_valid
        if target_id is not None:
            self.target_id = target_id
        if target_type is not None:
            self.target_type = target_type
        self.profile_type = profile_type
        ResourceReference.__init__(self, *args, **kwargs)

    @property
    def target_display_name(self):
        """Gets the target_display_name of this NSXProfileReference.  # noqa: E501

        Display name of the NSX resource.  # noqa: E501

        :return: The target_display_name of this NSXProfileReference.  # noqa: E501
        :rtype: str
        """
        return self._target_display_name

    @target_display_name.setter
    def target_display_name(self, target_display_name):
        """Sets the target_display_name of this NSXProfileReference.

        Display name of the NSX resource.  # noqa: E501

        :param target_display_name: The target_display_name of this NSXProfileReference.  # noqa: E501
        :type: str
        """

        self._target_display_name = target_display_name

    @property
    def is_valid(self):
        """Gets the is_valid of this NSXProfileReference.  # noqa: E501

        Will be set to false if the referenced NSX resource has been deleted.  # noqa: E501

        :return: The is_valid of this NSXProfileReference.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this NSXProfileReference.

        Will be set to false if the referenced NSX resource has been deleted.  # noqa: E501

        :param is_valid: The is_valid of this NSXProfileReference.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def target_id(self):
        """Gets the target_id of this NSXProfileReference.  # noqa: E501

        Identifier of the NSX resource.  # noqa: E501

        :return: The target_id of this NSXProfileReference.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this NSXProfileReference.

        Identifier of the NSX resource.  # noqa: E501

        :param target_id: The target_id of this NSXProfileReference.  # noqa: E501
        :type: str
        """

        self._target_id = target_id

    @property
    def target_type(self):
        """Gets the target_type of this NSXProfileReference.  # noqa: E501

        Type of the NSX resource.  # noqa: E501

        :return: The target_type of this NSXProfileReference.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this NSXProfileReference.

        Type of the NSX resource.  # noqa: E501

        :param target_type: The target_type of this NSXProfileReference.  # noqa: E501
        :type: str
        """

        self._target_type = target_type

    @property
    def profile_type(self):
        """Gets the profile_type of this NSXProfileReference.  # noqa: E501

        Profile type of the ServiceConfig  # noqa: E501

        :return: The profile_type of this NSXProfileReference.  # noqa: E501
        :rtype: str
        """
        return self._profile_type

    @profile_type.setter
    def profile_type(self, profile_type):
        """Sets the profile_type of this NSXProfileReference.

        Profile type of the ServiceConfig  # noqa: E501

        :param profile_type: The profile_type of this NSXProfileReference.  # noqa: E501
        :type: str
        """
        if profile_type is None:
            raise ValueError("Invalid value for `profile_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FirewallSessionTimerProfile", "FirewallCpuMemThresholdsProfile", "GiServiceProfile", "FirewallFloodProtectionProfile", "FirewallDnsProfile"]  # noqa: E501
        if profile_type not in allowed_values:
            raise ValueError(
                "Invalid value for `profile_type` ({0}), must be one of {1}"  # noqa: E501
                .format(profile_type, allowed_values)
            )

        self._profile_type = profile_type

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
        if issubclass(NSXProfileReference, dict):
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
        if not isinstance(other, NSXProfileReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
