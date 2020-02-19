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


class ConditionalForwarderZone(object):
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
        'upstream_servers': 'list[str]',
        'source_ip': 'str',
        'domain_names': 'list[str]'
    }
    if hasattr(ForwarderZone, "swagger_types"):
        swagger_types.update(ForwarderZone.swagger_types)

    attribute_map = {
        'upstream_servers': 'upstream_servers',
        'source_ip': 'source_ip',
        'domain_names': 'domain_names'
    }
    if hasattr(ForwarderZone, "attribute_map"):
        attribute_map.update(ForwarderZone.attribute_map)

    def __init__(self, upstream_servers=None, source_ip=None, domain_names=None, *args, **kwargs):  # noqa: E501
        """ConditionalForwarderZone - a model defined in Swagger"""  # noqa: E501
        self._upstream_servers = None
        self._source_ip = None
        self._domain_names = None
        self.discriminator = None
        self.upstream_servers = upstream_servers
        if source_ip is not None:
            self.source_ip = source_ip
        self.domain_names = domain_names
        ForwarderZone.__init__(self, *args, **kwargs)

    @property
    def upstream_servers(self):
        """Gets the upstream_servers of this ConditionalForwarderZone.  # noqa: E501

        Ip address of the upstream DNS servers the DNS forwarder accesses.   # noqa: E501

        :return: The upstream_servers of this ConditionalForwarderZone.  # noqa: E501
        :rtype: list[str]
        """
        return self._upstream_servers

    @upstream_servers.setter
    def upstream_servers(self, upstream_servers):
        """Sets the upstream_servers of this ConditionalForwarderZone.

        Ip address of the upstream DNS servers the DNS forwarder accesses.   # noqa: E501

        :param upstream_servers: The upstream_servers of this ConditionalForwarderZone.  # noqa: E501
        :type: list[str]
        """
        if upstream_servers is None:
            raise ValueError("Invalid value for `upstream_servers`, must not be `None`")  # noqa: E501

        self._upstream_servers = upstream_servers

    @property
    def source_ip(self):
        """Gets the source_ip of this ConditionalForwarderZone.  # noqa: E501

        The source ip used by the fowarder of the zone. If no source ip specified, the ip address of listener of the DNS forwarder will be used.   # noqa: E501

        :return: The source_ip of this ConditionalForwarderZone.  # noqa: E501
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this ConditionalForwarderZone.

        The source ip used by the fowarder of the zone. If no source ip specified, the ip address of listener of the DNS forwarder will be used.   # noqa: E501

        :param source_ip: The source_ip of this ConditionalForwarderZone.  # noqa: E501
        :type: str
        """

        self._source_ip = source_ip

    @property
    def domain_names(self):
        """Gets the domain_names of this ConditionalForwarderZone.  # noqa: E501

        A forwarder domain name should be a valid FQDN. If reverse lookup is needed for this zone, reverse lookup domain name like X.in-addr.arpa can be defined. Here the X represents a subnet.   # noqa: E501

        :return: The domain_names of this ConditionalForwarderZone.  # noqa: E501
        :rtype: list[str]
        """
        return self._domain_names

    @domain_names.setter
    def domain_names(self, domain_names):
        """Sets the domain_names of this ConditionalForwarderZone.

        A forwarder domain name should be a valid FQDN. If reverse lookup is needed for this zone, reverse lookup domain name like X.in-addr.arpa can be defined. Here the X represents a subnet.   # noqa: E501

        :param domain_names: The domain_names of this ConditionalForwarderZone.  # noqa: E501
        :type: list[str]
        """
        if domain_names is None:
            raise ValueError("Invalid value for `domain_names`, must not be `None`")  # noqa: E501

        self._domain_names = domain_names

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
        if issubclass(ConditionalForwarderZone, dict):
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
        if not isinstance(other, ConditionalForwarderZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
