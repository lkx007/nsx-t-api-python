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


class DuplicateAddressBindingEntry(object):
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
        'source': 'str',
        'binding': 'PacketAddressClassifier',
        'binding_timestamp': 'int',
        'conflicting_port': 'str'
    }
    if hasattr(AddressBindingEntry, "swagger_types"):
        swagger_types.update(AddressBindingEntry.swagger_types)

    attribute_map = {
        'source': 'source',
        'binding': 'binding',
        'binding_timestamp': 'binding_timestamp',
        'conflicting_port': 'conflicting_port'
    }
    if hasattr(AddressBindingEntry, "attribute_map"):
        attribute_map.update(AddressBindingEntry.attribute_map)

    def __init__(self, source='UNKNOWN', binding=None, binding_timestamp=None, conflicting_port=None, *args, **kwargs):  # noqa: E501
        """DuplicateAddressBindingEntry - a model defined in Swagger"""  # noqa: E501
        self._source = None
        self._binding = None
        self._binding_timestamp = None
        self._conflicting_port = None
        self.discriminator = None
        if source is not None:
            self.source = source
        if binding is not None:
            self.binding = binding
        if binding_timestamp is not None:
            self.binding_timestamp = binding_timestamp
        if conflicting_port is not None:
            self.conflicting_port = conflicting_port
        AddressBindingEntry.__init__(self, *args, **kwargs)

    @property
    def source(self):
        """Gets the source of this DuplicateAddressBindingEntry.  # noqa: E501

        Source from which the address binding entry was obtained  # noqa: E501

        :return: The source of this DuplicateAddressBindingEntry.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DuplicateAddressBindingEntry.

        Source from which the address binding entry was obtained  # noqa: E501

        :param source: The source of this DuplicateAddressBindingEntry.  # noqa: E501
        :type: str
        """
        allowed_values = ["INVALID", "UNKNOWN", "USER_DEFINED", "ARP_SNOOPING", "DHCP_SNOOPING", "VM_TOOLS", "ND_SNOOPING", "DHCPV6_SNOOPING", "VM_TOOLS_V6"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def binding(self):
        """Gets the binding of this DuplicateAddressBindingEntry.  # noqa: E501


        :return: The binding of this DuplicateAddressBindingEntry.  # noqa: E501
        :rtype: PacketAddressClassifier
        """
        return self._binding

    @binding.setter
    def binding(self, binding):
        """Sets the binding of this DuplicateAddressBindingEntry.


        :param binding: The binding of this DuplicateAddressBindingEntry.  # noqa: E501
        :type: PacketAddressClassifier
        """

        self._binding = binding

    @property
    def binding_timestamp(self):
        """Gets the binding_timestamp of this DuplicateAddressBindingEntry.  # noqa: E501

        Timestamp at which the binding was discovered via snooping or manually specified by the user   # noqa: E501

        :return: The binding_timestamp of this DuplicateAddressBindingEntry.  # noqa: E501
        :rtype: int
        """
        return self._binding_timestamp

    @binding_timestamp.setter
    def binding_timestamp(self, binding_timestamp):
        """Sets the binding_timestamp of this DuplicateAddressBindingEntry.

        Timestamp at which the binding was discovered via snooping or manually specified by the user   # noqa: E501

        :param binding_timestamp: The binding_timestamp of this DuplicateAddressBindingEntry.  # noqa: E501
        :type: int
        """

        self._binding_timestamp = binding_timestamp

    @property
    def conflicting_port(self):
        """Gets the conflicting_port of this DuplicateAddressBindingEntry.  # noqa: E501

        Provides the ID of the port on which the same address bidning exists   # noqa: E501

        :return: The conflicting_port of this DuplicateAddressBindingEntry.  # noqa: E501
        :rtype: str
        """
        return self._conflicting_port

    @conflicting_port.setter
    def conflicting_port(self, conflicting_port):
        """Sets the conflicting_port of this DuplicateAddressBindingEntry.

        Provides the ID of the port on which the same address bidning exists   # noqa: E501

        :param conflicting_port: The conflicting_port of this DuplicateAddressBindingEntry.  # noqa: E501
        :type: str
        """

        self._conflicting_port = conflicting_port

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
        if issubclass(DuplicateAddressBindingEntry, dict):
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
        if not isinstance(other, DuplicateAddressBindingEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other