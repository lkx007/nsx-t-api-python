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


class PortConnectionLogicalSwitch(object):
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
        'resource': 'ManagedResource',
        'id': 'str',
        'vm_ports_states': 'list[LogicalPortState]',
        'vm_ports': 'list[LogicalPort]',
        'vm_vnics': 'list[VirtualNetworkInterface]',
        'router_ports': 'list[LogicalPort]'
    }
    if hasattr(PortConnectionEntity, "swagger_types"):
        swagger_types.update(PortConnectionEntity.swagger_types)

    attribute_map = {
        'resource': 'resource',
        'id': 'id',
        'vm_ports_states': 'vm_ports_states',
        'vm_ports': 'vm_ports',
        'vm_vnics': 'vm_vnics',
        'router_ports': 'router_ports'
    }
    if hasattr(PortConnectionEntity, "attribute_map"):
        attribute_map.update(PortConnectionEntity.attribute_map)

    def __init__(self, resource=None, id=None, vm_ports_states=None, vm_ports=None, vm_vnics=None, router_ports=None, *args, **kwargs):  # noqa: E501
        """PortConnectionLogicalSwitch - a model defined in Swagger"""  # noqa: E501
        self._resource = None
        self._id = None
        self._vm_ports_states = None
        self._vm_ports = None
        self._vm_vnics = None
        self._router_ports = None
        self.discriminator = None
        if resource is not None:
            self.resource = resource
        if id is not None:
            self.id = id
        if vm_ports_states is not None:
            self.vm_ports_states = vm_ports_states
        if vm_ports is not None:
            self.vm_ports = vm_ports
        if vm_vnics is not None:
            self.vm_vnics = vm_vnics
        if router_ports is not None:
            self.router_ports = router_ports
        PortConnectionEntity.__init__(self, *args, **kwargs)

    @property
    def resource(self):
        """Gets the resource of this PortConnectionLogicalSwitch.  # noqa: E501


        :return: The resource of this PortConnectionLogicalSwitch.  # noqa: E501
        :rtype: ManagedResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this PortConnectionLogicalSwitch.


        :param resource: The resource of this PortConnectionLogicalSwitch.  # noqa: E501
        :type: ManagedResource
        """

        self._resource = resource

    @property
    def id(self):
        """Gets the id of this PortConnectionLogicalSwitch.  # noqa: E501

        Resource ID is mapped to this. (ID is Generated for Edge node groups, since resource will be null)  # noqa: E501

        :return: The id of this PortConnectionLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortConnectionLogicalSwitch.

        Resource ID is mapped to this. (ID is Generated for Edge node groups, since resource will be null)  # noqa: E501

        :param id: The id of this PortConnectionLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def vm_ports_states(self):
        """Gets the vm_ports_states of this PortConnectionLogicalSwitch.  # noqa: E501

        States of Logical Ports that are attached to a VIF/VM  # noqa: E501

        :return: The vm_ports_states of this PortConnectionLogicalSwitch.  # noqa: E501
        :rtype: list[LogicalPortState]
        """
        return self._vm_ports_states

    @vm_ports_states.setter
    def vm_ports_states(self, vm_ports_states):
        """Sets the vm_ports_states of this PortConnectionLogicalSwitch.

        States of Logical Ports that are attached to a VIF/VM  # noqa: E501

        :param vm_ports_states: The vm_ports_states of this PortConnectionLogicalSwitch.  # noqa: E501
        :type: list[LogicalPortState]
        """

        self._vm_ports_states = vm_ports_states

    @property
    def vm_ports(self):
        """Gets the vm_ports of this PortConnectionLogicalSwitch.  # noqa: E501

        Logical Ports that are attached to a VIF/VM  # noqa: E501

        :return: The vm_ports of this PortConnectionLogicalSwitch.  # noqa: E501
        :rtype: list[LogicalPort]
        """
        return self._vm_ports

    @vm_ports.setter
    def vm_ports(self, vm_ports):
        """Sets the vm_ports of this PortConnectionLogicalSwitch.

        Logical Ports that are attached to a VIF/VM  # noqa: E501

        :param vm_ports: The vm_ports of this PortConnectionLogicalSwitch.  # noqa: E501
        :type: list[LogicalPort]
        """

        self._vm_ports = vm_ports

    @property
    def vm_vnics(self):
        """Gets the vm_vnics of this PortConnectionLogicalSwitch.  # noqa: E501

        Virutal Network Interfaces that are attached to the Logical Ports  # noqa: E501

        :return: The vm_vnics of this PortConnectionLogicalSwitch.  # noqa: E501
        :rtype: list[VirtualNetworkInterface]
        """
        return self._vm_vnics

    @vm_vnics.setter
    def vm_vnics(self, vm_vnics):
        """Sets the vm_vnics of this PortConnectionLogicalSwitch.

        Virutal Network Interfaces that are attached to the Logical Ports  # noqa: E501

        :param vm_vnics: The vm_vnics of this PortConnectionLogicalSwitch.  # noqa: E501
        :type: list[VirtualNetworkInterface]
        """

        self._vm_vnics = vm_vnics

    @property
    def router_ports(self):
        """Gets the router_ports of this PortConnectionLogicalSwitch.  # noqa: E501

        Logical Ports that are attached to a router  # noqa: E501

        :return: The router_ports of this PortConnectionLogicalSwitch.  # noqa: E501
        :rtype: list[LogicalPort]
        """
        return self._router_ports

    @router_ports.setter
    def router_ports(self, router_ports):
        """Sets the router_ports of this PortConnectionLogicalSwitch.

        Logical Ports that are attached to a router  # noqa: E501

        :param router_ports: The router_ports of this PortConnectionLogicalSwitch.  # noqa: E501
        :type: list[LogicalPort]
        """

        self._router_ports = router_ports

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
        if issubclass(PortConnectionLogicalSwitch, dict):
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
        if not isinstance(other, PortConnectionLogicalSwitch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
