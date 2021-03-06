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


class NicMetadata(object):
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
        'interface_label': 'str',
        'interface_type': 'str',
        'transports': 'list[str]',
        'user_configurable': 'bool',
        'interface_index': 'int'
    }

    attribute_map = {
        'interface_label': 'interface_label',
        'interface_type': 'interface_type',
        'transports': 'transports',
        'user_configurable': 'user_configurable',
        'interface_index': 'interface_index'
    }

    def __init__(self, interface_label=None, interface_type=None, transports=None, user_configurable=None, interface_index=None):  # noqa: E501
        """NicMetadata - a model defined in Swagger"""  # noqa: E501
        self._interface_label = None
        self._interface_type = None
        self._transports = None
        self._user_configurable = None
        self._interface_index = None
        self.discriminator = None
        self.interface_label = interface_label
        self.interface_type = interface_type
        if transports is not None:
            self.transports = transports
        if user_configurable is not None:
            self.user_configurable = user_configurable
        self.interface_index = interface_index

    @property
    def interface_label(self):
        """Gets the interface_label of this NicMetadata.  # noqa: E501

        Network Interface label.  # noqa: E501

        :return: The interface_label of this NicMetadata.  # noqa: E501
        :rtype: str
        """
        return self._interface_label

    @interface_label.setter
    def interface_label(self, interface_label):
        """Sets the interface_label of this NicMetadata.

        Network Interface label.  # noqa: E501

        :param interface_label: The interface_label of this NicMetadata.  # noqa: E501
        :type: str
        """
        if interface_label is None:
            raise ValueError("Invalid value for `interface_label`, must not be `None`")  # noqa: E501

        self._interface_label = interface_label

    @property
    def interface_type(self):
        """Gets the interface_type of this NicMetadata.  # noqa: E501

        Interface that needs to be configured on the partner appliance. Ex. MANAGEMENT, DATA1, DATA2, HA1, HA2, CONTROL.  # noqa: E501

        :return: The interface_type of this NicMetadata.  # noqa: E501
        :rtype: str
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this NicMetadata.

        Interface that needs to be configured on the partner appliance. Ex. MANAGEMENT, DATA1, DATA2, HA1, HA2, CONTROL.  # noqa: E501

        :param interface_type: The interface_type of this NicMetadata.  # noqa: E501
        :type: str
        """
        if interface_type is None:
            raise ValueError("Invalid value for `interface_type`, must not be `None`")  # noqa: E501
        allowed_values = ["MANAGEMENT", "DATA1", "DATA2", "HA1", "HA2", "CONTROL"]  # noqa: E501
        if interface_type not in allowed_values:
            raise ValueError(
                "Invalid value for `interface_type` ({0}), must be one of {1}"  # noqa: E501
                .format(interface_type, allowed_values)
            )

        self._interface_type = interface_type

    @property
    def transports(self):
        """Gets the transports of this NicMetadata.  # noqa: E501

        Transport Type of the service, which is the mechanism of redirecting the traffic to the the partner appliance. Transport type is required if Service caters to any functionality other than EPP. Here, the transports array specifies the kinds of transport where this particular NIC is user configurable. If nothing is specified, and the \"user_configurable\" flag is true, then user configuration will be allowed for all transports. If any transport is/are specified, then it will be considered as user configurable for the specified transports only.\"  # noqa: E501

        :return: The transports of this NicMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._transports

    @transports.setter
    def transports(self, transports):
        """Sets the transports of this NicMetadata.

        Transport Type of the service, which is the mechanism of redirecting the traffic to the the partner appliance. Transport type is required if Service caters to any functionality other than EPP. Here, the transports array specifies the kinds of transport where this particular NIC is user configurable. If nothing is specified, and the \"user_configurable\" flag is true, then user configuration will be allowed for all transports. If any transport is/are specified, then it will be considered as user configurable for the specified transports only.\"  # noqa: E501

        :param transports: The transports of this NicMetadata.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["L2_BRIDGE", "L3_ROUTED", "NSH"]  # noqa: E501
        if not set(transports).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `transports` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(transports) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._transports = transports

    @property
    def user_configurable(self):
        """Gets the user_configurable of this NicMetadata.  # noqa: E501

        Used to specify if the given interface needs configuration. Management nics will always need the configuration, for others it will be use case specific. For example, a DATA NIC may be user configurable if the appliance is deployed in certain mode, such as L3_ROUTED.  # noqa: E501

        :return: The user_configurable of this NicMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._user_configurable

    @user_configurable.setter
    def user_configurable(self, user_configurable):
        """Sets the user_configurable of this NicMetadata.

        Used to specify if the given interface needs configuration. Management nics will always need the configuration, for others it will be use case specific. For example, a DATA NIC may be user configurable if the appliance is deployed in certain mode, such as L3_ROUTED.  # noqa: E501

        :param user_configurable: The user_configurable of this NicMetadata.  # noqa: E501
        :type: bool
        """

        self._user_configurable = user_configurable

    @property
    def interface_index(self):
        """Gets the interface_index of this NicMetadata.  # noqa: E501

        Network Interface index.  # noqa: E501

        :return: The interface_index of this NicMetadata.  # noqa: E501
        :rtype: int
        """
        return self._interface_index

    @interface_index.setter
    def interface_index(self, interface_index):
        """Sets the interface_index of this NicMetadata.

        Network Interface index.  # noqa: E501

        :param interface_index: The interface_index of this NicMetadata.  # noqa: E501
        :type: int
        """
        if interface_index is None:
            raise ValueError("Invalid value for `interface_index`, must not be `None`")  # noqa: E501

        self._interface_index = interface_index

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
        if issubclass(NicMetadata, dict):
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
        if not isinstance(other, NicMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
