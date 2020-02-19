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


class LbCookiePersistenceProfile(object):
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
        'cookie_garble': 'bool',
        'cookie_fallback': 'bool',
        'cookie_mode': 'str',
        'cookie_domain': 'str',
        'cookie_name': 'str',
        'cookie_time': 'LbCookieTime',
        'cookie_path': 'str'
    }
    if hasattr(LbPersistenceProfile, "swagger_types"):
        swagger_types.update(LbPersistenceProfile.swagger_types)

    attribute_map = {
        'persistence_shared': 'persistence_shared',
        'resource_type': 'resource_type',
        'cookie_garble': 'cookie_garble',
        'cookie_fallback': 'cookie_fallback',
        'cookie_mode': 'cookie_mode',
        'cookie_domain': 'cookie_domain',
        'cookie_name': 'cookie_name',
        'cookie_time': 'cookie_time',
        'cookie_path': 'cookie_path'
    }
    if hasattr(LbPersistenceProfile, "attribute_map"):
        attribute_map.update(LbPersistenceProfile.attribute_map)

    def __init__(self, persistence_shared=False, resource_type=None, cookie_garble=True, cookie_fallback=True, cookie_mode='INSERT', cookie_domain=None, cookie_name=None, cookie_time=None, cookie_path=None, *args, **kwargs):  # noqa: E501
        """LbCookiePersistenceProfile - a model defined in Swagger"""  # noqa: E501
        self._persistence_shared = None
        self._resource_type = None
        self._cookie_garble = None
        self._cookie_fallback = None
        self._cookie_mode = None
        self._cookie_domain = None
        self._cookie_name = None
        self._cookie_time = None
        self._cookie_path = None
        self.discriminator = None
        if persistence_shared is not None:
            self.persistence_shared = persistence_shared
        self.resource_type = resource_type
        if cookie_garble is not None:
            self.cookie_garble = cookie_garble
        if cookie_fallback is not None:
            self.cookie_fallback = cookie_fallback
        if cookie_mode is not None:
            self.cookie_mode = cookie_mode
        if cookie_domain is not None:
            self.cookie_domain = cookie_domain
        self.cookie_name = cookie_name
        if cookie_time is not None:
            self.cookie_time = cookie_time
        if cookie_path is not None:
            self.cookie_path = cookie_path
        LbPersistenceProfile.__init__(self, *args, **kwargs)

    @property
    def persistence_shared(self):
        """Gets the persistence_shared of this LbCookiePersistenceProfile.  # noqa: E501

        The persistence shared flag identifies whether the persistence table is shared among virtual-servers referring this profile. If persistence shared flag is not set in the cookie persistence profile bound to a virtual server, it defaults to cookie persistence that is private to each virtual server and is qualified by the pool. This is accomplished by load balancer inserting a cookie with name in the format &lt;name&gt;.&lt;virtual_server_id&gt;.&lt;pool_id&gt;. If persistence shared flag is set in the cookie persistence profile, in cookie insert mode, cookie persistence could be shared across multiple virtual servers that are bound to the same pools. The cookie name would be changed to &lt;name&gt;.&lt;profile-id&gt;.&lt;pool-id&gt;. If persistence shared flag is not set in the sourceIp persistence profile bound to a virtual server, each virtual server that the profile is bound to maintains its own private persistence table. If persistence shared flag is set in the sourceIp persistence profile, all virtual servers the profile is bound to share the same persistence table. If persistence shared flag is not set in the generic persistence profile, the persistence entries are matched and stored in the table which is identified using both virtual server ID and profile ID. If persistence shared flag is set in the generic persistence profile, the persistence entries are matched and stored in the table which is identified using profile ID. It means that virtual servers which consume the same profile in the LbRule with this flag enabled are sharing the same persistence table.   # noqa: E501

        :return: The persistence_shared of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: bool
        """
        return self._persistence_shared

    @persistence_shared.setter
    def persistence_shared(self, persistence_shared):
        """Sets the persistence_shared of this LbCookiePersistenceProfile.

        The persistence shared flag identifies whether the persistence table is shared among virtual-servers referring this profile. If persistence shared flag is not set in the cookie persistence profile bound to a virtual server, it defaults to cookie persistence that is private to each virtual server and is qualified by the pool. This is accomplished by load balancer inserting a cookie with name in the format &lt;name&gt;.&lt;virtual_server_id&gt;.&lt;pool_id&gt;. If persistence shared flag is set in the cookie persistence profile, in cookie insert mode, cookie persistence could be shared across multiple virtual servers that are bound to the same pools. The cookie name would be changed to &lt;name&gt;.&lt;profile-id&gt;.&lt;pool-id&gt;. If persistence shared flag is not set in the sourceIp persistence profile bound to a virtual server, each virtual server that the profile is bound to maintains its own private persistence table. If persistence shared flag is set in the sourceIp persistence profile, all virtual servers the profile is bound to share the same persistence table. If persistence shared flag is not set in the generic persistence profile, the persistence entries are matched and stored in the table which is identified using both virtual server ID and profile ID. If persistence shared flag is set in the generic persistence profile, the persistence entries are matched and stored in the table which is identified using profile ID. It means that virtual servers which consume the same profile in the LbRule with this flag enabled are sharing the same persistence table.   # noqa: E501

        :param persistence_shared: The persistence_shared of this LbCookiePersistenceProfile.  # noqa: E501
        :type: bool
        """

        self._persistence_shared = persistence_shared

    @property
    def resource_type(self):
        """Gets the resource_type of this LbCookiePersistenceProfile.  # noqa: E501

        The resource_type property identifies persistence profile type.   # noqa: E501

        :return: The resource_type of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this LbCookiePersistenceProfile.

        The resource_type property identifies persistence profile type.   # noqa: E501

        :param resource_type: The resource_type of this LbCookiePersistenceProfile.  # noqa: E501
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
    def cookie_garble(self):
        """Gets the cookie_garble of this LbCookiePersistenceProfile.  # noqa: E501

        If garble is set to true, cookie value (server IP and port) would be encrypted. If garble is set to false, cookie value would be plain text.   # noqa: E501

        :return: The cookie_garble of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: bool
        """
        return self._cookie_garble

    @cookie_garble.setter
    def cookie_garble(self, cookie_garble):
        """Sets the cookie_garble of this LbCookiePersistenceProfile.

        If garble is set to true, cookie value (server IP and port) would be encrypted. If garble is set to false, cookie value would be plain text.   # noqa: E501

        :param cookie_garble: The cookie_garble of this LbCookiePersistenceProfile.  # noqa: E501
        :type: bool
        """

        self._cookie_garble = cookie_garble

    @property
    def cookie_fallback(self):
        """Gets the cookie_fallback of this LbCookiePersistenceProfile.  # noqa: E501

        If fallback is true, once the cookie points to a server that is down (i.e. admin state DISABLED or healthcheck state is DOWN), then a new server is selected by default to handle that request. If fallback is false, it will cause the request to be rejected if cookie points to a server   # noqa: E501

        :return: The cookie_fallback of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: bool
        """
        return self._cookie_fallback

    @cookie_fallback.setter
    def cookie_fallback(self, cookie_fallback):
        """Sets the cookie_fallback of this LbCookiePersistenceProfile.

        If fallback is true, once the cookie points to a server that is down (i.e. admin state DISABLED or healthcheck state is DOWN), then a new server is selected by default to handle that request. If fallback is false, it will cause the request to be rejected if cookie points to a server   # noqa: E501

        :param cookie_fallback: The cookie_fallback of this LbCookiePersistenceProfile.  # noqa: E501
        :type: bool
        """

        self._cookie_fallback = cookie_fallback

    @property
    def cookie_mode(self):
        """Gets the cookie_mode of this LbCookiePersistenceProfile.  # noqa: E501

        cookie persistence mode  # noqa: E501

        :return: The cookie_mode of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._cookie_mode

    @cookie_mode.setter
    def cookie_mode(self, cookie_mode):
        """Sets the cookie_mode of this LbCookiePersistenceProfile.

        cookie persistence mode  # noqa: E501

        :param cookie_mode: The cookie_mode of this LbCookiePersistenceProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["INSERT", "PREFIX", "REWRITE"]  # noqa: E501
        if cookie_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `cookie_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(cookie_mode, allowed_values)
            )

        self._cookie_mode = cookie_mode

    @property
    def cookie_domain(self):
        """Gets the cookie_domain of this LbCookiePersistenceProfile.  # noqa: E501

        HTTP cookie domain could be configured, only available for insert mode.   # noqa: E501

        :return: The cookie_domain of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._cookie_domain

    @cookie_domain.setter
    def cookie_domain(self, cookie_domain):
        """Sets the cookie_domain of this LbCookiePersistenceProfile.

        HTTP cookie domain could be configured, only available for insert mode.   # noqa: E501

        :param cookie_domain: The cookie_domain of this LbCookiePersistenceProfile.  # noqa: E501
        :type: str
        """

        self._cookie_domain = cookie_domain

    @property
    def cookie_name(self):
        """Gets the cookie_name of this LbCookiePersistenceProfile.  # noqa: E501

        cookie name  # noqa: E501

        :return: The cookie_name of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        """Sets the cookie_name of this LbCookiePersistenceProfile.

        cookie name  # noqa: E501

        :param cookie_name: The cookie_name of this LbCookiePersistenceProfile.  # noqa: E501
        :type: str
        """
        if cookie_name is None:
            raise ValueError("Invalid value for `cookie_name`, must not be `None`")  # noqa: E501

        self._cookie_name = cookie_name

    @property
    def cookie_time(self):
        """Gets the cookie_time of this LbCookiePersistenceProfile.  # noqa: E501


        :return: The cookie_time of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: LbCookieTime
        """
        return self._cookie_time

    @cookie_time.setter
    def cookie_time(self, cookie_time):
        """Sets the cookie_time of this LbCookiePersistenceProfile.


        :param cookie_time: The cookie_time of this LbCookiePersistenceProfile.  # noqa: E501
        :type: LbCookieTime
        """

        self._cookie_time = cookie_time

    @property
    def cookie_path(self):
        """Gets the cookie_path of this LbCookiePersistenceProfile.  # noqa: E501

        HTTP cookie path could be set, only available for insert mode.   # noqa: E501

        :return: The cookie_path of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._cookie_path

    @cookie_path.setter
    def cookie_path(self, cookie_path):
        """Sets the cookie_path of this LbCookiePersistenceProfile.

        HTTP cookie path could be set, only available for insert mode.   # noqa: E501

        :param cookie_path: The cookie_path of this LbCookiePersistenceProfile.  # noqa: E501
        :type: str
        """

        self._cookie_path = cookie_path

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
        if issubclass(LbCookiePersistenceProfile, dict):
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
        if not isinstance(other, LbCookiePersistenceProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other