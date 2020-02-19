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


class L2VPNSessionRemoteMacsForLS(object):
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
        'remote_mac_addresses': 'list[str]',
        'logical_switch': 'ResourceReference'
    }

    attribute_map = {
        'remote_mac_addresses': 'remote_mac_addresses',
        'logical_switch': 'logical_switch'
    }

    def __init__(self, remote_mac_addresses=None, logical_switch=None):  # noqa: E501
        """L2VPNSessionRemoteMacsForLS - a model defined in Swagger"""  # noqa: E501
        self._remote_mac_addresses = None
        self._logical_switch = None
        self.discriminator = None
        if remote_mac_addresses is not None:
            self.remote_mac_addresses = remote_mac_addresses
        if logical_switch is not None:
            self.logical_switch = logical_switch

    @property
    def remote_mac_addresses(self):
        """Gets the remote_mac_addresses of this L2VPNSessionRemoteMacsForLS.  # noqa: E501

        Mac addresses.  # noqa: E501

        :return: The remote_mac_addresses of this L2VPNSessionRemoteMacsForLS.  # noqa: E501
        :rtype: list[str]
        """
        return self._remote_mac_addresses

    @remote_mac_addresses.setter
    def remote_mac_addresses(self, remote_mac_addresses):
        """Sets the remote_mac_addresses of this L2VPNSessionRemoteMacsForLS.

        Mac addresses.  # noqa: E501

        :param remote_mac_addresses: The remote_mac_addresses of this L2VPNSessionRemoteMacsForLS.  # noqa: E501
        :type: list[str]
        """

        self._remote_mac_addresses = remote_mac_addresses

    @property
    def logical_switch(self):
        """Gets the logical_switch of this L2VPNSessionRemoteMacsForLS.  # noqa: E501


        :return: The logical_switch of this L2VPNSessionRemoteMacsForLS.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._logical_switch

    @logical_switch.setter
    def logical_switch(self, logical_switch):
        """Sets the logical_switch of this L2VPNSessionRemoteMacsForLS.


        :param logical_switch: The logical_switch of this L2VPNSessionRemoteMacsForLS.  # noqa: E501
        :type: ResourceReference
        """

        self._logical_switch = logical_switch

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
        if issubclass(L2VPNSessionRemoteMacsForLS, dict):
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
        if not isinstance(other, L2VPNSessionRemoteMacsForLS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
