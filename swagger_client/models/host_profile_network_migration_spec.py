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


class HostProfileNetworkMigrationSpec(object):
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
        'resource_type': 'str',
        'network_mappings': 'list[VmkToLogicalSwitchMapping]'
    }
    if hasattr(NetworkMigrationSpec, "swagger_types"):
        swagger_types.update(NetworkMigrationSpec.swagger_types)

    attribute_map = {
        'resource_type': 'resource_type',
        'network_mappings': 'network_mappings'
    }
    if hasattr(NetworkMigrationSpec, "attribute_map"):
        attribute_map.update(NetworkMigrationSpec.attribute_map)

    def __init__(self, resource_type=None, network_mappings=None, *args, **kwargs):  # noqa: E501
        """HostProfileNetworkMigrationSpec - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._network_mappings = None
        self.discriminator = None
        self.resource_type = resource_type
        if network_mappings is not None:
            self.network_mappings = network_mappings
        NetworkMigrationSpec.__init__(self, *args, **kwargs)

    @property
    def resource_type(self):
        """Gets the resource_type of this HostProfileNetworkMigrationSpec.  # noqa: E501

        Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.  # noqa: E501

        :return: The resource_type of this HostProfileNetworkMigrationSpec.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this HostProfileNetworkMigrationSpec.

        Note- transport node templates APIs are deprecated and user is recommended to use transport node profiles APIs instead.  # noqa: E501

        :param resource_type: The resource_type of this HostProfileNetworkMigrationSpec.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["HostProfileNetworkMigrationSpec"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def network_mappings(self):
        """Gets the network_mappings of this HostProfileNetworkMigrationSpec.  # noqa: E501

        Based on provided mappings, VMkernal adapters will be migrated to mentioned logical switch. Without mappings specification doesn't make any sense, hence minium one mapping should be specified. Assuming some sane value of 10 maximum migrations which will be supported by any single specification.   # noqa: E501

        :return: The network_mappings of this HostProfileNetworkMigrationSpec.  # noqa: E501
        :rtype: list[VmkToLogicalSwitchMapping]
        """
        return self._network_mappings

    @network_mappings.setter
    def network_mappings(self, network_mappings):
        """Sets the network_mappings of this HostProfileNetworkMigrationSpec.

        Based on provided mappings, VMkernal adapters will be migrated to mentioned logical switch. Without mappings specification doesn't make any sense, hence minium one mapping should be specified. Assuming some sane value of 10 maximum migrations which will be supported by any single specification.   # noqa: E501

        :param network_mappings: The network_mappings of this HostProfileNetworkMigrationSpec.  # noqa: E501
        :type: list[VmkToLogicalSwitchMapping]
        """

        self._network_mappings = network_mappings

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
        if issubclass(HostProfileNetworkMigrationSpec, dict):
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
        if not isinstance(other, HostProfileNetworkMigrationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other