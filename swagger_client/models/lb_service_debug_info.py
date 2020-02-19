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


class LbServiceDebugInfo(object):
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
        'pools': 'list[LbPool]',
        'tcp_profiles': 'list[LbTcpProfile]',
        'virtual_servers': 'list[LbVirtualServer]',
        'client_ssl_profiles': 'list[LbClientSslProfile]',
        'server_ssl_profiles': 'list[LbServerSslProfile]',
        'service': 'LbService',
        'rules': 'list[LbRule]',
        'application_profiles': 'list[LbAppProfile]',
        'persistence_profiles': 'list[LbPersistenceProfile]',
        'monitors': 'list[LbMonitor]'
    }

    attribute_map = {
        'pools': 'pools',
        'tcp_profiles': 'tcp_profiles',
        'virtual_servers': 'virtual_servers',
        'client_ssl_profiles': 'client_ssl_profiles',
        'server_ssl_profiles': 'server_ssl_profiles',
        'service': 'service',
        'rules': 'rules',
        'application_profiles': 'application_profiles',
        'persistence_profiles': 'persistence_profiles',
        'monitors': 'monitors'
    }

    def __init__(self, pools=None, tcp_profiles=None, virtual_servers=None, client_ssl_profiles=None, server_ssl_profiles=None, service=None, rules=None, application_profiles=None, persistence_profiles=None, monitors=None):  # noqa: E501
        """LbServiceDebugInfo - a model defined in Swagger"""  # noqa: E501
        self._pools = None
        self._tcp_profiles = None
        self._virtual_servers = None
        self._client_ssl_profiles = None
        self._server_ssl_profiles = None
        self._service = None
        self._rules = None
        self._application_profiles = None
        self._persistence_profiles = None
        self._monitors = None
        self.discriminator = None
        if pools is not None:
            self.pools = pools
        if tcp_profiles is not None:
            self.tcp_profiles = tcp_profiles
        if virtual_servers is not None:
            self.virtual_servers = virtual_servers
        if client_ssl_profiles is not None:
            self.client_ssl_profiles = client_ssl_profiles
        if server_ssl_profiles is not None:
            self.server_ssl_profiles = server_ssl_profiles
        if service is not None:
            self.service = service
        if rules is not None:
            self.rules = rules
        if application_profiles is not None:
            self.application_profiles = application_profiles
        if persistence_profiles is not None:
            self.persistence_profiles = persistence_profiles
        if monitors is not None:
            self.monitors = monitors

    @property
    def pools(self):
        """Gets the pools of this LbServiceDebugInfo.  # noqa: E501

        The pools which are associated to the given load balancer service would be included. The pools could be defined in virtual server default pool, sorry pool or load balancer rule action.   # noqa: E501

        :return: The pools of this LbServiceDebugInfo.  # noqa: E501
        :rtype: list[LbPool]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this LbServiceDebugInfo.

        The pools which are associated to the given load balancer service would be included. The pools could be defined in virtual server default pool, sorry pool or load balancer rule action.   # noqa: E501

        :param pools: The pools of this LbServiceDebugInfo.  # noqa: E501
        :type: list[LbPool]
        """

        self._pools = pools

    @property
    def tcp_profiles(self):
        """Gets the tcp_profiles of this LbServiceDebugInfo.  # noqa: E501

        The TCP profiles are associated to virtual servers   # noqa: E501

        :return: The tcp_profiles of this LbServiceDebugInfo.  # noqa: E501
        :rtype: list[LbTcpProfile]
        """
        return self._tcp_profiles

    @tcp_profiles.setter
    def tcp_profiles(self, tcp_profiles):
        """Sets the tcp_profiles of this LbServiceDebugInfo.

        The TCP profiles are associated to virtual servers   # noqa: E501

        :param tcp_profiles: The tcp_profiles of this LbServiceDebugInfo.  # noqa: E501
        :type: list[LbTcpProfile]
        """

        self._tcp_profiles = tcp_profiles

    @property
    def virtual_servers(self):
        """Gets the virtual_servers of this LbServiceDebugInfo.  # noqa: E501

        The virtual servers which are associated to the given load balancer service would be included.   # noqa: E501

        :return: The virtual_servers of this LbServiceDebugInfo.  # noqa: E501
        :rtype: list[LbVirtualServer]
        """
        return self._virtual_servers

    @virtual_servers.setter
    def virtual_servers(self, virtual_servers):
        """Sets the virtual_servers of this LbServiceDebugInfo.

        The virtual servers which are associated to the given load balancer service would be included.   # noqa: E501

        :param virtual_servers: The virtual_servers of this LbServiceDebugInfo.  # noqa: E501
        :type: list[LbVirtualServer]
        """

        self._virtual_servers = virtual_servers

    @property
    def client_ssl_profiles(self):
        """Gets the client_ssl_profiles of this LbServiceDebugInfo.  # noqa: E501

        The client SSL profiles are associated to virtual servers   # noqa: E501

        :return: The client_ssl_profiles of this LbServiceDebugInfo.  # noqa: E501
        :rtype: list[LbClientSslProfile]
        """
        return self._client_ssl_profiles

    @client_ssl_profiles.setter
    def client_ssl_profiles(self, client_ssl_profiles):
        """Sets the client_ssl_profiles of this LbServiceDebugInfo.

        The client SSL profiles are associated to virtual servers   # noqa: E501

        :param client_ssl_profiles: The client_ssl_profiles of this LbServiceDebugInfo.  # noqa: E501
        :type: list[LbClientSslProfile]
        """

        self._client_ssl_profiles = client_ssl_profiles

    @property
    def server_ssl_profiles(self):
        """Gets the server_ssl_profiles of this LbServiceDebugInfo.  # noqa: E501

        The server SSL profiles are associated to virtual servers   # noqa: E501

        :return: The server_ssl_profiles of this LbServiceDebugInfo.  # noqa: E501
        :rtype: list[LbServerSslProfile]
        """
        return self._server_ssl_profiles

    @server_ssl_profiles.setter
    def server_ssl_profiles(self, server_ssl_profiles):
        """Sets the server_ssl_profiles of this LbServiceDebugInfo.

        The server SSL profiles are associated to virtual servers   # noqa: E501

        :param server_ssl_profiles: The server_ssl_profiles of this LbServiceDebugInfo.  # noqa: E501
        :type: list[LbServerSslProfile]
        """

        self._server_ssl_profiles = server_ssl_profiles

    @property
    def service(self):
        """Gets the service of this LbServiceDebugInfo.  # noqa: E501


        :return: The service of this LbServiceDebugInfo.  # noqa: E501
        :rtype: LbService
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this LbServiceDebugInfo.


        :param service: The service of this LbServiceDebugInfo.  # noqa: E501
        :type: LbService
        """

        self._service = service

    @property
    def rules(self):
        """Gets the rules of this LbServiceDebugInfo.  # noqa: E501

        The load balancer rules are associated to virtual servers   # noqa: E501

        :return: The rules of this LbServiceDebugInfo.  # noqa: E501
        :rtype: list[LbRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this LbServiceDebugInfo.

        The load balancer rules are associated to virtual servers   # noqa: E501

        :param rules: The rules of this LbServiceDebugInfo.  # noqa: E501
        :type: list[LbRule]
        """

        self._rules = rules

    @property
    def application_profiles(self):
        """Gets the application_profiles of this LbServiceDebugInfo.  # noqa: E501

        The application profiles are associated to virtual servers   # noqa: E501

        :return: The application_profiles of this LbServiceDebugInfo.  # noqa: E501
        :rtype: list[LbAppProfile]
        """
        return self._application_profiles

    @application_profiles.setter
    def application_profiles(self, application_profiles):
        """Sets the application_profiles of this LbServiceDebugInfo.

        The application profiles are associated to virtual servers   # noqa: E501

        :param application_profiles: The application_profiles of this LbServiceDebugInfo.  # noqa: E501
        :type: list[LbAppProfile]
        """

        self._application_profiles = application_profiles

    @property
    def persistence_profiles(self):
        """Gets the persistence_profiles of this LbServiceDebugInfo.  # noqa: E501

        The persistence profiles are associated to virtual servers   # noqa: E501

        :return: The persistence_profiles of this LbServiceDebugInfo.  # noqa: E501
        :rtype: list[LbPersistenceProfile]
        """
        return self._persistence_profiles

    @persistence_profiles.setter
    def persistence_profiles(self, persistence_profiles):
        """Sets the persistence_profiles of this LbServiceDebugInfo.

        The persistence profiles are associated to virtual servers   # noqa: E501

        :param persistence_profiles: The persistence_profiles of this LbServiceDebugInfo.  # noqa: E501
        :type: list[LbPersistenceProfile]
        """

        self._persistence_profiles = persistence_profiles

    @property
    def monitors(self):
        """Gets the monitors of this LbServiceDebugInfo.  # noqa: E501

        The load balancer monitors are associated to pools.   # noqa: E501

        :return: The monitors of this LbServiceDebugInfo.  # noqa: E501
        :rtype: list[LbMonitor]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """Sets the monitors of this LbServiceDebugInfo.

        The load balancer monitors are associated to pools.   # noqa: E501

        :param monitors: The monitors of this LbServiceDebugInfo.  # noqa: E501
        :type: list[LbMonitor]
        """

        self._monitors = monitors

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
        if issubclass(LbServiceDebugInfo, dict):
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
        if not isinstance(other, LbServiceDebugInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other