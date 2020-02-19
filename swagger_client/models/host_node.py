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


class HostNode(object):
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
        'discovered_ip_addresses': 'list[str]',
        'ip_addresses': 'list[str]',
        'external_id': 'str',
        'fqdn': 'str',
        'resource_type': 'str',
        'discovered_node_id': 'str',
        'managed_by_server': 'str',
        'host_credential': 'HostNodeLoginCredential',
        'os_version': 'str',
        'os_type': 'str',
        'maintenance_mode_state': 'str'
    }
    if hasattr(Node, "swagger_types"):
        swagger_types.update(Node.swagger_types)

    attribute_map = {
        'discovered_ip_addresses': 'discovered_ip_addresses',
        'ip_addresses': 'ip_addresses',
        'external_id': 'external_id',
        'fqdn': 'fqdn',
        'resource_type': 'resource_type',
        'discovered_node_id': 'discovered_node_id',
        'managed_by_server': 'managed_by_server',
        'host_credential': 'host_credential',
        'os_version': 'os_version',
        'os_type': 'os_type',
        'maintenance_mode_state': 'maintenance_mode_state'
    }
    if hasattr(Node, "attribute_map"):
        attribute_map.update(Node.attribute_map)

    def __init__(self, discovered_ip_addresses=None, ip_addresses=None, external_id=None, fqdn=None, resource_type=None, discovered_node_id=None, managed_by_server=None, host_credential=None, os_version=None, os_type=None, maintenance_mode_state=None, *args, **kwargs):  # noqa: E501
        """HostNode - a model defined in Swagger"""  # noqa: E501
        self._discovered_ip_addresses = None
        self._ip_addresses = None
        self._external_id = None
        self._fqdn = None
        self._resource_type = None
        self._discovered_node_id = None
        self._managed_by_server = None
        self._host_credential = None
        self._os_version = None
        self._os_type = None
        self._maintenance_mode_state = None
        self.discriminator = None
        if discovered_ip_addresses is not None:
            self.discovered_ip_addresses = discovered_ip_addresses
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if external_id is not None:
            self.external_id = external_id
        if fqdn is not None:
            self.fqdn = fqdn
        self.resource_type = resource_type
        if discovered_node_id is not None:
            self.discovered_node_id = discovered_node_id
        if managed_by_server is not None:
            self.managed_by_server = managed_by_server
        if host_credential is not None:
            self.host_credential = host_credential
        if os_version is not None:
            self.os_version = os_version
        self.os_type = os_type
        if maintenance_mode_state is not None:
            self.maintenance_mode_state = maintenance_mode_state
        Node.__init__(self, *args, **kwargs)

    @property
    def discovered_ip_addresses(self):
        """Gets the discovered_ip_addresses of this HostNode.  # noqa: E501

        Discovered IP Addresses of the fabric node, version 4 or 6  # noqa: E501

        :return: The discovered_ip_addresses of this HostNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._discovered_ip_addresses

    @discovered_ip_addresses.setter
    def discovered_ip_addresses(self, discovered_ip_addresses):
        """Sets the discovered_ip_addresses of this HostNode.

        Discovered IP Addresses of the fabric node, version 4 or 6  # noqa: E501

        :param discovered_ip_addresses: The discovered_ip_addresses of this HostNode.  # noqa: E501
        :type: list[str]
        """

        self._discovered_ip_addresses = discovered_ip_addresses

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this HostNode.  # noqa: E501

        IP Addresses of the Node, version 4 or 6. This property is mandatory for all nodes except for automatic deployment of edge virtual machine node. For automatic deployment, the ip address from management_port_subnets property will be considered.   # noqa: E501

        :return: The ip_addresses of this HostNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this HostNode.

        IP Addresses of the Node, version 4 or 6. This property is mandatory for all nodes except for automatic deployment of edge virtual machine node. For automatic deployment, the ip address from management_port_subnets property will be considered.   # noqa: E501

        :param ip_addresses: The ip_addresses of this HostNode.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def external_id(self):
        """Gets the external_id of this HostNode.  # noqa: E501

        ID of the Node maintained on the Node and used to recognize the Node  # noqa: E501

        :return: The external_id of this HostNode.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this HostNode.

        ID of the Node maintained on the Node and used to recognize the Node  # noqa: E501

        :param external_id: The external_id of this HostNode.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def fqdn(self):
        """Gets the fqdn of this HostNode.  # noqa: E501

        Fully qualified domain name of the fabric node  # noqa: E501

        :return: The fqdn of this HostNode.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this HostNode.

        Fully qualified domain name of the fabric node  # noqa: E501

        :param fqdn: The fqdn of this HostNode.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def resource_type(self):
        """Gets the resource_type of this HostNode.  # noqa: E501

        Fabric node type, for example 'HostNode', 'EdgeNode' or 'PublicCloudGatewayNode'  # noqa: E501

        :return: The resource_type of this HostNode.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this HostNode.

        Fabric node type, for example 'HostNode', 'EdgeNode' or 'PublicCloudGatewayNode'  # noqa: E501

        :param resource_type: The resource_type of this HostNode.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def discovered_node_id(self):
        """Gets the discovered_node_id of this HostNode.  # noqa: E501

        Id of discovered node which was converted to create this node  # noqa: E501

        :return: The discovered_node_id of this HostNode.  # noqa: E501
        :rtype: str
        """
        return self._discovered_node_id

    @discovered_node_id.setter
    def discovered_node_id(self, discovered_node_id):
        """Sets the discovered_node_id of this HostNode.

        Id of discovered node which was converted to create this node  # noqa: E501

        :param discovered_node_id: The discovered_node_id of this HostNode.  # noqa: E501
        :type: str
        """

        self._discovered_node_id = discovered_node_id

    @property
    def managed_by_server(self):
        """Gets the managed_by_server of this HostNode.  # noqa: E501

        The id of the vCenter server managing the ESXi type HostNode  # noqa: E501

        :return: The managed_by_server of this HostNode.  # noqa: E501
        :rtype: str
        """
        return self._managed_by_server

    @managed_by_server.setter
    def managed_by_server(self, managed_by_server):
        """Sets the managed_by_server of this HostNode.

        The id of the vCenter server managing the ESXi type HostNode  # noqa: E501

        :param managed_by_server: The managed_by_server of this HostNode.  # noqa: E501
        :type: str
        """

        self._managed_by_server = managed_by_server

    @property
    def host_credential(self):
        """Gets the host_credential of this HostNode.  # noqa: E501


        :return: The host_credential of this HostNode.  # noqa: E501
        :rtype: HostNodeLoginCredential
        """
        return self._host_credential

    @host_credential.setter
    def host_credential(self, host_credential):
        """Sets the host_credential of this HostNode.


        :param host_credential: The host_credential of this HostNode.  # noqa: E501
        :type: HostNodeLoginCredential
        """

        self._host_credential = host_credential

    @property
    def os_version(self):
        """Gets the os_version of this HostNode.  # noqa: E501

        Version of the hypervisor operating system  # noqa: E501

        :return: The os_version of this HostNode.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this HostNode.

        Version of the hypervisor operating system  # noqa: E501

        :param os_version: The os_version of this HostNode.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def os_type(self):
        """Gets the os_type of this HostNode.  # noqa: E501

        Hypervisor type, for example ESXi or RHEL KVM  # noqa: E501

        :return: The os_type of this HostNode.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this HostNode.

        Hypervisor type, for example ESXi or RHEL KVM  # noqa: E501

        :param os_type: The os_type of this HostNode.  # noqa: E501
        :type: str
        """
        if os_type is None:
            raise ValueError("Invalid value for `os_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ESXI", "RHELKVM", "RHELSERVER", "RHELCONTAINER", "UBUNTUKVM", "UBUNTUSERVER", "HYPERV", "CENTOSKVM", "CENTOSSERVER", "CENTOSCONTAINER", "SLESKVM", "SLESSERVER"]  # noqa: E501
        if os_type not in allowed_values:
            raise ValueError(
                "Invalid value for `os_type` ({0}), must be one of {1}"  # noqa: E501
                .format(os_type, allowed_values)
            )

        self._os_type = os_type

    @property
    def maintenance_mode_state(self):
        """Gets the maintenance_mode_state of this HostNode.  # noqa: E501

        Indicates host node's maintenance mode state. The state is ENTERING when a task to put the host in maintenance-mode is in progress.   # noqa: E501

        :return: The maintenance_mode_state of this HostNode.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_mode_state

    @maintenance_mode_state.setter
    def maintenance_mode_state(self, maintenance_mode_state):
        """Sets the maintenance_mode_state of this HostNode.

        Indicates host node's maintenance mode state. The state is ENTERING when a task to put the host in maintenance-mode is in progress.   # noqa: E501

        :param maintenance_mode_state: The maintenance_mode_state of this HostNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["OFF", "ENTERING", "ON"]  # noqa: E501
        if maintenance_mode_state not in allowed_values:
            raise ValueError(
                "Invalid value for `maintenance_mode_state` ({0}), must be one of {1}"  # noqa: E501
                .format(maintenance_mode_state, allowed_values)
            )

        self._maintenance_mode_state = maintenance_mode_state

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
        if issubclass(HostNode, dict):
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
        if not isinstance(other, HostNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
