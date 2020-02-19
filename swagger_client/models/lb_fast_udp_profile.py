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


class LbFastUdpProfile(object):
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
        'idle_timeout': 'int',
        'flow_mirroring_enabled': 'bool'
    }
    if hasattr(LbAppProfile, "swagger_types"):
        swagger_types.update(LbAppProfile.swagger_types)

    attribute_map = {
        'resource_type': 'resource_type',
        'idle_timeout': 'idle_timeout',
        'flow_mirroring_enabled': 'flow_mirroring_enabled'
    }
    if hasattr(LbAppProfile, "attribute_map"):
        attribute_map.update(LbAppProfile.attribute_map)

    def __init__(self, resource_type=None, idle_timeout=300, flow_mirroring_enabled=False, *args, **kwargs):  # noqa: E501
        """LbFastUdpProfile - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._idle_timeout = None
        self._flow_mirroring_enabled = None
        self.discriminator = None
        self.resource_type = resource_type
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if flow_mirroring_enabled is not None:
            self.flow_mirroring_enabled = flow_mirroring_enabled
        LbAppProfile.__init__(self, *args, **kwargs)

    @property
    def resource_type(self):
        """Gets the resource_type of this LbFastUdpProfile.  # noqa: E501

        An application profile can be bound to a virtual server to specify the application protocol characteristics. It is used to influence how load balancing is performed. Currently, three types of application profiles are supported: LbFastTCPProfile, LbFastUDPProfile and LbHttpProfile. LbFastTCPProfile or LbFastUDPProfile is typically used when the application is using a custom protocol or a standard protocol not supported by the load balancer. It is also used in cases where the user only wants L4 load balancing mainly because L4 load balancing has much higher performance and scalability, and/or supports connection mirroring. LbHttpProfile is used for both HTTP and HTTPS applications. Though application rules, if bound to the virtual server, can be used to accomplish the same goal, LbHttpProfile is intended to simplify enabling certain common use cases.   # noqa: E501

        :return: The resource_type of this LbFastUdpProfile.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this LbFastUdpProfile.

        An application profile can be bound to a virtual server to specify the application protocol characteristics. It is used to influence how load balancing is performed. Currently, three types of application profiles are supported: LbFastTCPProfile, LbFastUDPProfile and LbHttpProfile. LbFastTCPProfile or LbFastUDPProfile is typically used when the application is using a custom protocol or a standard protocol not supported by the load balancer. It is also used in cases where the user only wants L4 load balancing mainly because L4 load balancing has much higher performance and scalability, and/or supports connection mirroring. LbHttpProfile is used for both HTTP and HTTPS applications. Though application rules, if bound to the virtual server, can be used to accomplish the same goal, LbHttpProfile is intended to simplify enabling certain common use cases.   # noqa: E501

        :param resource_type: The resource_type of this LbFastUdpProfile.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LbHttpProfile", "LbFastTcpProfile", "LbFastUdpProfile"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def idle_timeout(self):
        """Gets the idle_timeout of this LbFastUdpProfile.  # noqa: E501

        Though UDP is a connectionless protocol, for the purposes of load balancing, all UDP packets with the same flow signature (source and destination IP/ports and IP protocol) received within the idle timeout period are considered to belong to the same connection and are sent to the same backend server. If no packets are received for idle timeout period, the connection (association between flow signature and the selected server) is cleaned up.   # noqa: E501

        :return: The idle_timeout of this LbFastUdpProfile.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """Sets the idle_timeout of this LbFastUdpProfile.

        Though UDP is a connectionless protocol, for the purposes of load balancing, all UDP packets with the same flow signature (source and destination IP/ports and IP protocol) received within the idle timeout period are considered to belong to the same connection and are sent to the same backend server. If no packets are received for idle timeout period, the connection (association between flow signature and the selected server) is cleaned up.   # noqa: E501

        :param idle_timeout: The idle_timeout of this LbFastUdpProfile.  # noqa: E501
        :type: int
        """

        self._idle_timeout = idle_timeout

    @property
    def flow_mirroring_enabled(self):
        """Gets the flow_mirroring_enabled of this LbFastUdpProfile.  # noqa: E501

        If flow mirroring is enabled, all the flows to the bounded virtual server are mirrored to the standby node.   # noqa: E501

        :return: The flow_mirroring_enabled of this LbFastUdpProfile.  # noqa: E501
        :rtype: bool
        """
        return self._flow_mirroring_enabled

    @flow_mirroring_enabled.setter
    def flow_mirroring_enabled(self, flow_mirroring_enabled):
        """Sets the flow_mirroring_enabled of this LbFastUdpProfile.

        If flow mirroring is enabled, all the flows to the bounded virtual server are mirrored to the standby node.   # noqa: E501

        :param flow_mirroring_enabled: The flow_mirroring_enabled of this LbFastUdpProfile.  # noqa: E501
        :type: bool
        """

        self._flow_mirroring_enabled = flow_mirroring_enabled

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
        if issubclass(LbFastUdpProfile, dict):
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
        if not isinstance(other, LbFastUdpProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
