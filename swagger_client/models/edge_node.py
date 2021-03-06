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


class EdgeNode(object):
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
        'node_settings': 'EdgeNodeSettings',
        'deployment_config': 'EdgeNodeDeploymentConfig',
        'allocation_list': 'list[str]',
        'deployment_type': 'str'
    }
    if hasattr(Node, "swagger_types"):
        swagger_types.update(Node.swagger_types)

    attribute_map = {
        'discovered_ip_addresses': 'discovered_ip_addresses',
        'ip_addresses': 'ip_addresses',
        'external_id': 'external_id',
        'fqdn': 'fqdn',
        'resource_type': 'resource_type',
        'node_settings': 'node_settings',
        'deployment_config': 'deployment_config',
        'allocation_list': 'allocation_list',
        'deployment_type': 'deployment_type'
    }
    if hasattr(Node, "attribute_map"):
        attribute_map.update(Node.attribute_map)

    def __init__(self, discovered_ip_addresses=None, ip_addresses=None, external_id=None, fqdn=None, resource_type=None, node_settings=None, deployment_config=None, allocation_list=None, deployment_type=None, *args, **kwargs):  # noqa: E501
        """EdgeNode - a model defined in Swagger"""  # noqa: E501
        self._discovered_ip_addresses = None
        self._ip_addresses = None
        self._external_id = None
        self._fqdn = None
        self._resource_type = None
        self._node_settings = None
        self._deployment_config = None
        self._allocation_list = None
        self._deployment_type = None
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
        if node_settings is not None:
            self.node_settings = node_settings
        if deployment_config is not None:
            self.deployment_config = deployment_config
        if allocation_list is not None:
            self.allocation_list = allocation_list
        if deployment_type is not None:
            self.deployment_type = deployment_type
        Node.__init__(self, *args, **kwargs)

    @property
    def discovered_ip_addresses(self):
        """Gets the discovered_ip_addresses of this EdgeNode.  # noqa: E501

        Discovered IP Addresses of the fabric node, version 4 or 6  # noqa: E501

        :return: The discovered_ip_addresses of this EdgeNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._discovered_ip_addresses

    @discovered_ip_addresses.setter
    def discovered_ip_addresses(self, discovered_ip_addresses):
        """Sets the discovered_ip_addresses of this EdgeNode.

        Discovered IP Addresses of the fabric node, version 4 or 6  # noqa: E501

        :param discovered_ip_addresses: The discovered_ip_addresses of this EdgeNode.  # noqa: E501
        :type: list[str]
        """

        self._discovered_ip_addresses = discovered_ip_addresses

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this EdgeNode.  # noqa: E501

        IP Addresses of the Node, version 4 or 6. This property is mandatory for all nodes except for automatic deployment of edge virtual machine node. For automatic deployment, the ip address from management_port_subnets property will be considered.   # noqa: E501

        :return: The ip_addresses of this EdgeNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this EdgeNode.

        IP Addresses of the Node, version 4 or 6. This property is mandatory for all nodes except for automatic deployment of edge virtual machine node. For automatic deployment, the ip address from management_port_subnets property will be considered.   # noqa: E501

        :param ip_addresses: The ip_addresses of this EdgeNode.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def external_id(self):
        """Gets the external_id of this EdgeNode.  # noqa: E501

        ID of the Node maintained on the Node and used to recognize the Node  # noqa: E501

        :return: The external_id of this EdgeNode.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this EdgeNode.

        ID of the Node maintained on the Node and used to recognize the Node  # noqa: E501

        :param external_id: The external_id of this EdgeNode.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def fqdn(self):
        """Gets the fqdn of this EdgeNode.  # noqa: E501

        Fully qualified domain name of the fabric node  # noqa: E501

        :return: The fqdn of this EdgeNode.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this EdgeNode.

        Fully qualified domain name of the fabric node  # noqa: E501

        :param fqdn: The fqdn of this EdgeNode.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def resource_type(self):
        """Gets the resource_type of this EdgeNode.  # noqa: E501

        Fabric node type, for example 'HostNode', 'EdgeNode' or 'PublicCloudGatewayNode'  # noqa: E501

        :return: The resource_type of this EdgeNode.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this EdgeNode.

        Fabric node type, for example 'HostNode', 'EdgeNode' or 'PublicCloudGatewayNode'  # noqa: E501

        :param resource_type: The resource_type of this EdgeNode.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def node_settings(self):
        """Gets the node_settings of this EdgeNode.  # noqa: E501


        :return: The node_settings of this EdgeNode.  # noqa: E501
        :rtype: EdgeNodeSettings
        """
        return self._node_settings

    @node_settings.setter
    def node_settings(self, node_settings):
        """Sets the node_settings of this EdgeNode.


        :param node_settings: The node_settings of this EdgeNode.  # noqa: E501
        :type: EdgeNodeSettings
        """

        self._node_settings = node_settings

    @property
    def deployment_config(self):
        """Gets the deployment_config of this EdgeNode.  # noqa: E501


        :return: The deployment_config of this EdgeNode.  # noqa: E501
        :rtype: EdgeNodeDeploymentConfig
        """
        return self._deployment_config

    @deployment_config.setter
    def deployment_config(self, deployment_config):
        """Sets the deployment_config of this EdgeNode.


        :param deployment_config: The deployment_config of this EdgeNode.  # noqa: E501
        :type: EdgeNodeDeploymentConfig
        """

        self._deployment_config = deployment_config

    @property
    def allocation_list(self):
        """Gets the allocation_list of this EdgeNode.  # noqa: E501

        List of logical router ids to which this edge node is allocated.  # noqa: E501

        :return: The allocation_list of this EdgeNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._allocation_list

    @allocation_list.setter
    def allocation_list(self, allocation_list):
        """Sets the allocation_list of this EdgeNode.

        List of logical router ids to which this edge node is allocated.  # noqa: E501

        :param allocation_list: The allocation_list of this EdgeNode.  # noqa: E501
        :type: list[str]
        """

        self._allocation_list = allocation_list

    @property
    def deployment_type(self):
        """Gets the deployment_type of this EdgeNode.  # noqa: E501

        Supported edge deployment type.  # noqa: E501

        :return: The deployment_type of this EdgeNode.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this EdgeNode.

        Supported edge deployment type.  # noqa: E501

        :param deployment_type: The deployment_type of this EdgeNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["VIRTUAL_MACHINE", "PHYSICAL_MACHINE", "UNKNOWN"]  # noqa: E501
        if deployment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_type, allowed_values)
            )

        self._deployment_type = deployment_type

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
        if issubclass(EdgeNode, dict):
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
        if not isinstance(other, EdgeNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
