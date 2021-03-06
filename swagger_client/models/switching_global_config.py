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


class SwitchingGlobalConfig(object):
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
        'global_replication_mode_enabled': 'bool',
        'uplink_mtu_threshold': 'int',
        'physical_uplink_mtu': 'int'
    }
    if hasattr(GlobalConfigs, "swagger_types"):
        swagger_types.update(GlobalConfigs.swagger_types)

    attribute_map = {
        'resource_type': 'resource_type',
        'global_replication_mode_enabled': 'global_replication_mode_enabled',
        'uplink_mtu_threshold': 'uplink_mtu_threshold',
        'physical_uplink_mtu': 'physical_uplink_mtu'
    }
    if hasattr(GlobalConfigs, "attribute_map"):
        attribute_map.update(GlobalConfigs.attribute_map)

    def __init__(self, resource_type=None, global_replication_mode_enabled=False, uplink_mtu_threshold=9000, physical_uplink_mtu=1700, *args, **kwargs):  # noqa: E501
        """SwitchingGlobalConfig - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._global_replication_mode_enabled = None
        self._uplink_mtu_threshold = None
        self._physical_uplink_mtu = None
        self.discriminator = None
        self.resource_type = resource_type
        if global_replication_mode_enabled is not None:
            self.global_replication_mode_enabled = global_replication_mode_enabled
        if uplink_mtu_threshold is not None:
            self.uplink_mtu_threshold = uplink_mtu_threshold
        if physical_uplink_mtu is not None:
            self.physical_uplink_mtu = physical_uplink_mtu
        GlobalConfigs.__init__(self, *args, **kwargs)

    @property
    def resource_type(self):
        """Gets the resource_type of this SwitchingGlobalConfig.  # noqa: E501

        Valid Global configuration types  # noqa: E501

        :return: The resource_type of this SwitchingGlobalConfig.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this SwitchingGlobalConfig.

        Valid Global configuration types  # noqa: E501

        :param resource_type: The resource_type of this SwitchingGlobalConfig.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["SwitchingGlobalConfig", "RoutingGlobalConfig", "OperationCollectorGlobalConfig", "FirewallGlobalConfig", "EsxGlobalOpaqueConfig", "SecurityGlobalConfig", "FipsGlobalConfig"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def global_replication_mode_enabled(self):
        """Gets the global_replication_mode_enabled of this SwitchingGlobalConfig.  # noqa: E501

        When this flag is set true, certain types of BUM packets will be sent to all VTEPs in the global VTEP table, ignoring the logical switching span.  # noqa: E501

        :return: The global_replication_mode_enabled of this SwitchingGlobalConfig.  # noqa: E501
        :rtype: bool
        """
        return self._global_replication_mode_enabled

    @global_replication_mode_enabled.setter
    def global_replication_mode_enabled(self, global_replication_mode_enabled):
        """Sets the global_replication_mode_enabled of this SwitchingGlobalConfig.

        When this flag is set true, certain types of BUM packets will be sent to all VTEPs in the global VTEP table, ignoring the logical switching span.  # noqa: E501

        :param global_replication_mode_enabled: The global_replication_mode_enabled of this SwitchingGlobalConfig.  # noqa: E501
        :type: bool
        """

        self._global_replication_mode_enabled = global_replication_mode_enabled

    @property
    def uplink_mtu_threshold(self):
        """Gets the uplink_mtu_threshold of this SwitchingGlobalConfig.  # noqa: E501

        This value defines the upper threshold for the MTU value that can be configured at a physical uplink level or a logical routing uplink level in a NSX domain. All Uplink profiles validate against this value so that the MTU specified in an Uplink profile does not exceed this global upper threshold. Similarly, when this value is modified, the new value must be greater than or equal to any existing Uplink profile's MTU. This value is also validated to be greater than or equal to physical_uplink_mtu in SwitchingGlobalConfig and logical_uplink_mtu in RoutingGlobalConfig.  # noqa: E501

        :return: The uplink_mtu_threshold of this SwitchingGlobalConfig.  # noqa: E501
        :rtype: int
        """
        return self._uplink_mtu_threshold

    @uplink_mtu_threshold.setter
    def uplink_mtu_threshold(self, uplink_mtu_threshold):
        """Sets the uplink_mtu_threshold of this SwitchingGlobalConfig.

        This value defines the upper threshold for the MTU value that can be configured at a physical uplink level or a logical routing uplink level in a NSX domain. All Uplink profiles validate against this value so that the MTU specified in an Uplink profile does not exceed this global upper threshold. Similarly, when this value is modified, the new value must be greater than or equal to any existing Uplink profile's MTU. This value is also validated to be greater than or equal to physical_uplink_mtu in SwitchingGlobalConfig and logical_uplink_mtu in RoutingGlobalConfig.  # noqa: E501

        :param uplink_mtu_threshold: The uplink_mtu_threshold of this SwitchingGlobalConfig.  # noqa: E501
        :type: int
        """

        self._uplink_mtu_threshold = uplink_mtu_threshold

    @property
    def physical_uplink_mtu(self):
        """Gets the physical_uplink_mtu of this SwitchingGlobalConfig.  # noqa: E501

        This is the global default MTU for all the physical uplinks in a NSX domain. This is the default value for the optional uplink profile MTU field. When the MTU value is not specified in the uplink profile, this global value will be used. This value can be overridden by providing a value for the optional MTU field in the uplink profile. Whenever this value is updated, the updated value will only be propagated to the uplinks that don't have the MTU value in their uplink profiles. If this value is not set, the default value of 1700 will be used. The Transport Node state can be monitored to confirm if the updated MTU value has been realized.  # noqa: E501

        :return: The physical_uplink_mtu of this SwitchingGlobalConfig.  # noqa: E501
        :rtype: int
        """
        return self._physical_uplink_mtu

    @physical_uplink_mtu.setter
    def physical_uplink_mtu(self, physical_uplink_mtu):
        """Sets the physical_uplink_mtu of this SwitchingGlobalConfig.

        This is the global default MTU for all the physical uplinks in a NSX domain. This is the default value for the optional uplink profile MTU field. When the MTU value is not specified in the uplink profile, this global value will be used. This value can be overridden by providing a value for the optional MTU field in the uplink profile. Whenever this value is updated, the updated value will only be propagated to the uplinks that don't have the MTU value in their uplink profiles. If this value is not set, the default value of 1700 will be used. The Transport Node state can be monitored to confirm if the updated MTU value has been realized.  # noqa: E501

        :param physical_uplink_mtu: The physical_uplink_mtu of this SwitchingGlobalConfig.  # noqa: E501
        :type: int
        """

        self._physical_uplink_mtu = physical_uplink_mtu

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
        if issubclass(SwitchingGlobalConfig, dict):
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
        if not isinstance(other, SwitchingGlobalConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
