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


class SwitchingProfileStatus(object):
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
        'num_logical_ports': 'int',
        'switching_profile_id': 'str',
        'num_logical_switches': 'int'
    }

    attribute_map = {
        'num_logical_ports': 'num_logical_ports',
        'switching_profile_id': 'switching_profile_id',
        'num_logical_switches': 'num_logical_switches'
    }

    def __init__(self, num_logical_ports=None, switching_profile_id=None, num_logical_switches=None):  # noqa: E501
        """SwitchingProfileStatus - a model defined in Swagger"""  # noqa: E501
        self._num_logical_ports = None
        self._switching_profile_id = None
        self._num_logical_switches = None
        self.discriminator = None
        if num_logical_ports is not None:
            self.num_logical_ports = num_logical_ports
        if switching_profile_id is not None:
            self.switching_profile_id = switching_profile_id
        if num_logical_switches is not None:
            self.num_logical_switches = num_logical_switches

    @property
    def num_logical_ports(self):
        """Gets the num_logical_ports of this SwitchingProfileStatus.  # noqa: E501

        Number of logical ports using a switching profile  # noqa: E501

        :return: The num_logical_ports of this SwitchingProfileStatus.  # noqa: E501
        :rtype: int
        """
        return self._num_logical_ports

    @num_logical_ports.setter
    def num_logical_ports(self, num_logical_ports):
        """Sets the num_logical_ports of this SwitchingProfileStatus.

        Number of logical ports using a switching profile  # noqa: E501

        :param num_logical_ports: The num_logical_ports of this SwitchingProfileStatus.  # noqa: E501
        :type: int
        """

        self._num_logical_ports = num_logical_ports

    @property
    def switching_profile_id(self):
        """Gets the switching_profile_id of this SwitchingProfileStatus.  # noqa: E501

        Identifier for the switching profile  # noqa: E501

        :return: The switching_profile_id of this SwitchingProfileStatus.  # noqa: E501
        :rtype: str
        """
        return self._switching_profile_id

    @switching_profile_id.setter
    def switching_profile_id(self, switching_profile_id):
        """Sets the switching_profile_id of this SwitchingProfileStatus.

        Identifier for the switching profile  # noqa: E501

        :param switching_profile_id: The switching_profile_id of this SwitchingProfileStatus.  # noqa: E501
        :type: str
        """

        self._switching_profile_id = switching_profile_id

    @property
    def num_logical_switches(self):
        """Gets the num_logical_switches of this SwitchingProfileStatus.  # noqa: E501

        Number of logical switches using a switching profile  # noqa: E501

        :return: The num_logical_switches of this SwitchingProfileStatus.  # noqa: E501
        :rtype: int
        """
        return self._num_logical_switches

    @num_logical_switches.setter
    def num_logical_switches(self, num_logical_switches):
        """Sets the num_logical_switches of this SwitchingProfileStatus.

        Number of logical switches using a switching profile  # noqa: E501

        :param num_logical_switches: The num_logical_switches of this SwitchingProfileStatus.  # noqa: E501
        :type: int
        """

        self._num_logical_switches = num_logical_switches

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
        if issubclass(SwitchingProfileStatus, dict):
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
        if not isinstance(other, SwitchingProfileStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
