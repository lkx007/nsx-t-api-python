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


class ServiceManager(object):
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
        'port': 'int',
        'service_ids': 'list[ResourceReference]',
        'authentication_scheme': 'CallbackAuthenticationScheme',
        'thumbprint': 'str',
        'vendor_id': 'str',
        'uri': 'str',
        'server': 'str'
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
        'port': 'port',
        'service_ids': 'service_ids',
        'authentication_scheme': 'authentication_scheme',
        'thumbprint': 'thumbprint',
        'vendor_id': 'vendor_id',
        'uri': 'uri',
        'server': 'server'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, port=None, service_ids=None, authentication_scheme=None, thumbprint=None, vendor_id=None, uri=None, server=None, *args, **kwargs):  # noqa: E501
        """ServiceManager - a model defined in Swagger"""  # noqa: E501
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
        self._port = None
        self._service_ids = None
        self._authentication_scheme = None
        self._thumbprint = None
        self._vendor_id = None
        self._uri = None
        self._server = None
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
        self.port = port
        self.service_ids = service_ids
        self.authentication_scheme = authentication_scheme
        if thumbprint is not None:
            self.thumbprint = thumbprint
        if vendor_id is not None:
            self.vendor_id = vendor_id
        self.uri = uri
        self.server = server
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this ServiceManager.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this ServiceManager.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this ServiceManager.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this ServiceManager.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this ServiceManager.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ServiceManager.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this ServiceManager.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this ServiceManager.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceManager.

        Description of this resource  # noqa: E501

        :param description: The description of this ServiceManager.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this ServiceManager.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this ServiceManager.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ServiceManager.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this ServiceManager.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this ServiceManager.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ServiceManager.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this ServiceManager.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this ServiceManager.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this ServiceManager.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this ServiceManager.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this ServiceManager.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this ServiceManager.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ServiceManager.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this ServiceManager.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this ServiceManager.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this ServiceManager.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this ServiceManager.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this ServiceManager.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this ServiceManager.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this ServiceManager.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this ServiceManager.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this ServiceManager.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceManager.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this ServiceManager.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this ServiceManager.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ServiceManager.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this ServiceManager.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def port(self):
        """Gets the port of this ServiceManager.  # noqa: E501

        Integer port value to specify a standard/non-standard HTTPS port.  # noqa: E501

        :return: The port of this ServiceManager.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServiceManager.

        Integer port value to specify a standard/non-standard HTTPS port.  # noqa: E501

        :param port: The port of this ServiceManager.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def service_ids(self):
        """Gets the service_ids of this ServiceManager.  # noqa: E501

        The IDs of services, provided by partner.  # noqa: E501

        :return: The service_ids of this ServiceManager.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._service_ids

    @service_ids.setter
    def service_ids(self, service_ids):
        """Sets the service_ids of this ServiceManager.

        The IDs of services, provided by partner.  # noqa: E501

        :param service_ids: The service_ids of this ServiceManager.  # noqa: E501
        :type: list[ResourceReference]
        """
        if service_ids is None:
            raise ValueError("Invalid value for `service_ids`, must not be `None`")  # noqa: E501

        self._service_ids = service_ids

    @property
    def authentication_scheme(self):
        """Gets the authentication_scheme of this ServiceManager.  # noqa: E501


        :return: The authentication_scheme of this ServiceManager.  # noqa: E501
        :rtype: CallbackAuthenticationScheme
        """
        return self._authentication_scheme

    @authentication_scheme.setter
    def authentication_scheme(self, authentication_scheme):
        """Sets the authentication_scheme of this ServiceManager.


        :param authentication_scheme: The authentication_scheme of this ServiceManager.  # noqa: E501
        :type: CallbackAuthenticationScheme
        """
        if authentication_scheme is None:
            raise ValueError("Invalid value for `authentication_scheme`, must not be `None`")  # noqa: E501

        self._authentication_scheme = authentication_scheme

    @property
    def thumbprint(self):
        """Gets the thumbprint of this ServiceManager.  # noqa: E501

        Thumbprint (SHA-256 hash represented in lower case hex) for the certificate on the partner console. This will be required to establish secure communication with the console and to avoid man-in-the-middle attacks.  # noqa: E501

        :return: The thumbprint of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._thumbprint

    @thumbprint.setter
    def thumbprint(self, thumbprint):
        """Sets the thumbprint of this ServiceManager.

        Thumbprint (SHA-256 hash represented in lower case hex) for the certificate on the partner console. This will be required to establish secure communication with the console and to avoid man-in-the-middle attacks.  # noqa: E501

        :param thumbprint: The thumbprint of this ServiceManager.  # noqa: E501
        :type: str
        """

        self._thumbprint = thumbprint

    @property
    def vendor_id(self):
        """Gets the vendor_id of this ServiceManager.  # noqa: E501

        Id which is unique to a vendor or partner for which the service is created.  # noqa: E501

        :return: The vendor_id of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this ServiceManager.

        Id which is unique to a vendor or partner for which the service is created.  # noqa: E501

        :param vendor_id: The vendor_id of this ServiceManager.  # noqa: E501
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def uri(self):
        """Gets the uri of this ServiceManager.  # noqa: E501

        URI on which notification requests should be made on the specified server.  # noqa: E501

        :return: The uri of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ServiceManager.

        URI on which notification requests should be made on the specified server.  # noqa: E501

        :param uri: The uri of this ServiceManager.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def server(self):
        """Gets the server of this ServiceManager.  # noqa: E501

        IP address or fully qualified domain name of the partner REST server.  # noqa: E501

        :return: The server of this ServiceManager.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ServiceManager.

        IP address or fully qualified domain name of the partner REST server.  # noqa: E501

        :param server: The server of this ServiceManager.  # noqa: E501
        :type: str
        """
        if server is None:
            raise ValueError("Invalid value for `server`, must not be `None`")  # noqa: E501

        self._server = server

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
        if issubclass(ServiceManager, dict):
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
        if not isinstance(other, ServiceManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
