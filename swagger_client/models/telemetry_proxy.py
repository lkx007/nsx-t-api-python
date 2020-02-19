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


class TelemetryProxy(object):
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
        'system_owned': 'bool',
        'display_name': 'str',
        'description': 'str',
        'tags': 'list[Tag]',
        'create_user': 'str',
        'protection': 'str',
        'create_time': 'int',
        'last_modified_time': 'int',
        'last_modified_user': 'str',
        'id': 'str',
        'resource_type': 'str',
        'username': 'str',
        'password': 'str',
        'scheme': 'str',
        'hostname': 'str',
        'port': 'int'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'system_owned': '_system_owned',
        'display_name': 'display_name',
        'description': 'description',
        'tags': 'tags',
        'create_user': '_create_user',
        'protection': '_protection',
        'create_time': '_create_time',
        'last_modified_time': '_last_modified_time',
        'last_modified_user': '_last_modified_user',
        'id': 'id',
        'resource_type': 'resource_type',
        'username': 'username',
        'password': 'password',
        'scheme': 'scheme',
        'hostname': 'hostname',
        'port': 'port'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, username=None, password=None, scheme=None, hostname=None, port=None, *args, **kwargs):  # noqa: E501
        """TelemetryProxy - a model defined in Swagger"""  # noqa: E501
        self._system_owned = None
        self._display_name = None
        self._description = None
        self._tags = None
        self._create_user = None
        self._protection = None
        self._create_time = None
        self._last_modified_time = None
        self._last_modified_user = None
        self._id = None
        self._resource_type = None
        self._username = None
        self._password = None
        self._scheme = None
        self._hostname = None
        self._port = None
        self.discriminator = None
        if system_owned is not None:
            self.system_owned = system_owned
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if create_user is not None:
            self.create_user = create_user
        if protection is not None:
            self.protection = protection
        if create_time is not None:
            self.create_time = create_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if last_modified_user is not None:
            self.last_modified_user = last_modified_user
        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        self.scheme = scheme
        self.hostname = hostname
        self.port = port
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this TelemetryProxy.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this TelemetryProxy.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this TelemetryProxy.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this TelemetryProxy.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this TelemetryProxy.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TelemetryProxy.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this TelemetryProxy.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this TelemetryProxy.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TelemetryProxy.

        Description of this resource  # noqa: E501

        :param description: The description of this TelemetryProxy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this TelemetryProxy.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this TelemetryProxy.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TelemetryProxy.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this TelemetryProxy.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this TelemetryProxy.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this TelemetryProxy.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this TelemetryProxy.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this TelemetryProxy.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this TelemetryProxy.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this TelemetryProxy.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this TelemetryProxy.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this TelemetryProxy.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TelemetryProxy.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this TelemetryProxy.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this TelemetryProxy.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this TelemetryProxy.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this TelemetryProxy.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this TelemetryProxy.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this TelemetryProxy.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this TelemetryProxy.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this TelemetryProxy.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this TelemetryProxy.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TelemetryProxy.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this TelemetryProxy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this TelemetryProxy.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TelemetryProxy.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this TelemetryProxy.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def username(self):
        """Gets the username of this TelemetryProxy.  # noqa: E501

        Specify the user name used to authenticate with the proxy server, if required.   # noqa: E501

        :return: The username of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TelemetryProxy.

        Specify the user name used to authenticate with the proxy server, if required.   # noqa: E501

        :param username: The username of this TelemetryProxy.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this TelemetryProxy.  # noqa: E501

        Specify the password used to authenticate with the proxy server, if required. A GET call on /telemetry/config returns a non-meaningful password to maintain security. To change the password to a new value, issue a PUT call after updating this field. To remove the password, issue a PUT call after emptying this field. To retain a previously set password, issue a PUT call keeping the non-meaningful value obtained from the GET call.   # noqa: E501

        :return: The password of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TelemetryProxy.

        Specify the password used to authenticate with the proxy server, if required. A GET call on /telemetry/config returns a non-meaningful password to maintain security. To change the password to a new value, issue a PUT call after updating this field. To remove the password, issue a PUT call after emptying this field. To retain a previously set password, issue a PUT call keeping the non-meaningful value obtained from the GET call.   # noqa: E501

        :param password: The password of this TelemetryProxy.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def scheme(self):
        """Gets the scheme of this TelemetryProxy.  # noqa: E501

        The scheme accepted by the proxy server. Specify one of HTTP and HTTPS.   # noqa: E501

        :return: The scheme of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this TelemetryProxy.

        The scheme accepted by the proxy server. Specify one of HTTP and HTTPS.   # noqa: E501

        :param scheme: The scheme of this TelemetryProxy.  # noqa: E501
        :type: str
        """
        if scheme is None:
            raise ValueError("Invalid value for `scheme`, must not be `None`")  # noqa: E501
        allowed_values = ["HTTP", "HTTPS"]  # noqa: E501
        if scheme not in allowed_values:
            raise ValueError(
                "Invalid value for `scheme` ({0}), must be one of {1}"  # noqa: E501
                .format(scheme, allowed_values)
            )

        self._scheme = scheme

    @property
    def hostname(self):
        """Gets the hostname of this TelemetryProxy.  # noqa: E501

        Specify the fully qualified domain name, or ip address, of the proxy server.   # noqa: E501

        :return: The hostname of this TelemetryProxy.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this TelemetryProxy.

        Specify the fully qualified domain name, or ip address, of the proxy server.   # noqa: E501

        :param hostname: The hostname of this TelemetryProxy.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this TelemetryProxy.  # noqa: E501

        Specify the port of the proxy server.  # noqa: E501

        :return: The port of this TelemetryProxy.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TelemetryProxy.

        Specify the port of the proxy server.  # noqa: E501

        :param port: The port of this TelemetryProxy.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

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
        if issubclass(TelemetryProxy, dict):
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
        if not isinstance(other, TelemetryProxy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
