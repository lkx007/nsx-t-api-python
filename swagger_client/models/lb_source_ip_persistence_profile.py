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


class LbSourceIpPersistenceProfile(object):
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
        'persistence_shared': 'bool',
        'resource_type': 'str',
        'purge': 'str',
        'ha_persistence_mirroring_enabled': 'bool',
        'timeout': 'int'
    }
    if hasattr(LbPersistenceProfile, "swagger_types"):
        swagger_types.update(LbPersistenceProfile.swagger_types)

    attribute_map = {
        'persistence_shared': 'persistence_shared',
        'resource_type': 'resource_type',
        'purge': 'purge',
        'ha_persistence_mirroring_enabled': 'ha_persistence_mirroring_enabled',
        'timeout': 'timeout'
    }
    if hasattr(LbPersistenceProfile, "attribute_map"):
        attribute_map.update(LbPersistenceProfile.attribute_map)

    def __init__(self, persistence_shared=False, resource_type=None, purge='FULL', ha_persistence_mirroring_enabled=False, timeout=300, *args, **kwargs):  # noqa: E501
        """LbSourceIpPersistenceProfile - a model defined in Swagger"""  # noqa: E501
        self._persistence_shared = None
        self._resource_type = None
        self._purge = None
        self._ha_persistence_mirroring_enabled = None
        self._timeout = None
        self.discriminator = None
        if persistence_shared is not None:
            self.persistence_shared = persistence_shared
        self.resource_type = resource_type
        if purge is not None:
            self.purge = purge
        if ha_persistence_mirroring_enabled is not None:
            self.ha_persistence_mirroring_enabled = ha_persistence_mirroring_enabled
        if timeout is not None:
            self.timeout = timeout
        LbPersistenceProfile.__init__(self, *args, **kwargs)

    @property
    def persistence_shared(self):
        """Gets the persistence_shared of this LbSourceIpPersistenceProfile.  # noqa: E501

        The persistence shared flag identifies whether the persistence table is shared among virtual-servers referring this profile. If persistence shared flag is not set in the cookie persistence profile bound to a virtual server, it defaults to cookie persistence that is private to each virtual server and is qualified by the pool. This is accomplished by load balancer inserting a cookie with name in the format &lt;name&gt;.&lt;virtual_server_id&gt;.&lt;pool_id&gt;. If persistence shared flag is set in the cookie persistence profile, in cookie insert mode, cookie persistence could be shared across multiple virtual servers that are bound to the same pools. The cookie name would be changed to &lt;name&gt;.&lt;profile-id&gt;.&lt;pool-id&gt;. If persistence shared flag is not set in the sourceIp persistence profile bound to a virtual server, each virtual server that the profile is bound to maintains its own private persistence table. If persistence shared flag is set in the sourceIp persistence profile, all virtual servers the profile is bound to share the same persistence table. If persistence shared flag is not set in the generic persistence profile, the persistence entries are matched and stored in the table which is identified using both virtual server ID and profile ID. If persistence shared flag is set in the generic persistence profile, the persistence entries are matched and stored in the table which is identified using profile ID. It means that virtual servers which consume the same profile in the LbRule with this flag enabled are sharing the same persistence table.   # noqa: E501

        :return: The persistence_shared of this LbSourceIpPersistenceProfile.  # noqa: E501
        :rtype: bool
        """
        return self._persistence_shared

    @persistence_shared.setter
    def persistence_shared(self, persistence_shared):
        """Sets the persistence_shared of this LbSourceIpPersistenceProfile.

        The persistence shared flag identifies whether the persistence table is shared among virtual-servers referring this profile. If persistence shared flag is not set in the cookie persistence profile bound to a virtual server, it defaults to cookie persistence that is private to each virtual server and is qualified by the pool. This is accomplished by load balancer inserting a cookie with name in the format &lt;name&gt;.&lt;virtual_server_id&gt;.&lt;pool_id&gt;. If persistence shared flag is set in the cookie persistence profile, in cookie insert mode, cookie persistence could be shared across multiple virtual servers that are bound to the same pools. The cookie name would be changed to &lt;name&gt;.&lt;profile-id&gt;.&lt;pool-id&gt;. If persistence shared flag is not set in the sourceIp persistence profile bound to a virtual server, each virtual server that the profile is bound to maintains its own private persistence table. If persistence shared flag is set in the sourceIp persistence profile, all virtual servers the profile is bound to share the same persistence table. If persistence shared flag is not set in the generic persistence profile, the persistence entries are matched and stored in the table which is identified using both virtual server ID and profile ID. If persistence shared flag is set in the generic persistence profile, the persistence entries are matched and stored in the table which is identified using profile ID. It means that virtual servers which consume the same profile in the LbRule with this flag enabled are sharing the same persistence table.   # noqa: E501

        :param persistence_shared: The persistence_shared of this LbSourceIpPersistenceProfile.  # noqa: E501
        :type: bool
        """

        self._persistence_shared = persistence_shared

    @property
    def resource_type(self):
        """Gets the resource_type of this LbSourceIpPersistenceProfile.  # noqa: E501

        The resource_type property identifies persistence profile type.   # noqa: E501

        :return: The resource_type of this LbSourceIpPersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this LbSourceIpPersistenceProfile.

        The resource_type property identifies persistence profile type.   # noqa: E501

        :param resource_type: The resource_type of this LbSourceIpPersistenceProfile.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LbCookiePersistenceProfile", "LbSourceIpPersistenceProfile", "LbGenericPersistenceProfile"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def purge(self):
        """Gets the purge of this LbSourceIpPersistenceProfile.  # noqa: E501

        persistence purge setting  # noqa: E501

        :return: The purge of this LbSourceIpPersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._purge

    @purge.setter
    def purge(self, purge):
        """Sets the purge of this LbSourceIpPersistenceProfile.

        persistence purge setting  # noqa: E501

        :param purge: The purge of this LbSourceIpPersistenceProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["NO_PURGE", "FULL"]  # noqa: E501
        if purge not in allowed_values:
            raise ValueError(
                "Invalid value for `purge` ({0}), must be one of {1}"  # noqa: E501
                .format(purge, allowed_values)
            )

        self._purge = purge

    @property
    def ha_persistence_mirroring_enabled(self):
        """Gets the ha_persistence_mirroring_enabled of this LbSourceIpPersistenceProfile.  # noqa: E501

        Persistence entries are not synchronized to the HA peer by default.   # noqa: E501

        :return: The ha_persistence_mirroring_enabled of this LbSourceIpPersistenceProfile.  # noqa: E501
        :rtype: bool
        """
        return self._ha_persistence_mirroring_enabled

    @ha_persistence_mirroring_enabled.setter
    def ha_persistence_mirroring_enabled(self, ha_persistence_mirroring_enabled):
        """Sets the ha_persistence_mirroring_enabled of this LbSourceIpPersistenceProfile.

        Persistence entries are not synchronized to the HA peer by default.   # noqa: E501

        :param ha_persistence_mirroring_enabled: The ha_persistence_mirroring_enabled of this LbSourceIpPersistenceProfile.  # noqa: E501
        :type: bool
        """

        self._ha_persistence_mirroring_enabled = ha_persistence_mirroring_enabled

    @property
    def timeout(self):
        """Gets the timeout of this LbSourceIpPersistenceProfile.  # noqa: E501

        When all connections complete (reference count reaches 0), persistence entry timer is started with the expiration time.   # noqa: E501

        :return: The timeout of this LbSourceIpPersistenceProfile.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this LbSourceIpPersistenceProfile.

        When all connections complete (reference count reaches 0), persistence entry timer is started with the expiration time.   # noqa: E501

        :param timeout: The timeout of this LbSourceIpPersistenceProfile.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if issubclass(LbSourceIpPersistenceProfile, dict):
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
        if not isinstance(other, LbSourceIpPersistenceProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
