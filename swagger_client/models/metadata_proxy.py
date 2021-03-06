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


class MetadataProxy(object):
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
        'secret': 'str',
        'metadata_server_ca_ids': 'list[str]',
        'edge_cluster_member_indexes': 'list[int]',
        'crypto_protocols': 'list[str]',
        'metadata_server_url': 'str',
        'attached_logical_port_id': 'str',
        'enable_standby_relocation': 'bool',
        'edge_cluster_id': 'str'
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
        'secret': 'secret',
        'metadata_server_ca_ids': 'metadata_server_ca_ids',
        'edge_cluster_member_indexes': 'edge_cluster_member_indexes',
        'crypto_protocols': 'crypto_protocols',
        'metadata_server_url': 'metadata_server_url',
        'attached_logical_port_id': 'attached_logical_port_id',
        'enable_standby_relocation': 'enable_standby_relocation',
        'edge_cluster_id': 'edge_cluster_id'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, secret=None, metadata_server_ca_ids=None, edge_cluster_member_indexes=None, crypto_protocols=None, metadata_server_url=None, attached_logical_port_id=None, enable_standby_relocation=False, edge_cluster_id=None, *args, **kwargs):  # noqa: E501
        """MetadataProxy - a model defined in Swagger"""  # noqa: E501
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
        self._secret = None
        self._metadata_server_ca_ids = None
        self._edge_cluster_member_indexes = None
        self._crypto_protocols = None
        self._metadata_server_url = None
        self._attached_logical_port_id = None
        self._enable_standby_relocation = None
        self._edge_cluster_id = None
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
        if secret is not None:
            self.secret = secret
        if metadata_server_ca_ids is not None:
            self.metadata_server_ca_ids = metadata_server_ca_ids
        if edge_cluster_member_indexes is not None:
            self.edge_cluster_member_indexes = edge_cluster_member_indexes
        if crypto_protocols is not None:
            self.crypto_protocols = crypto_protocols
        self.metadata_server_url = metadata_server_url
        if attached_logical_port_id is not None:
            self.attached_logical_port_id = attached_logical_port_id
        if enable_standby_relocation is not None:
            self.enable_standby_relocation = enable_standby_relocation
        self.edge_cluster_id = edge_cluster_id
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this MetadataProxy.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this MetadataProxy.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this MetadataProxy.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this MetadataProxy.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this MetadataProxy.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this MetadataProxy.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this MetadataProxy.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this MetadataProxy.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MetadataProxy.

        Description of this resource  # noqa: E501

        :param description: The description of this MetadataProxy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this MetadataProxy.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this MetadataProxy.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MetadataProxy.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this MetadataProxy.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this MetadataProxy.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this MetadataProxy.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this MetadataProxy.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this MetadataProxy.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this MetadataProxy.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this MetadataProxy.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this MetadataProxy.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this MetadataProxy.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this MetadataProxy.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this MetadataProxy.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this MetadataProxy.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this MetadataProxy.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this MetadataProxy.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this MetadataProxy.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this MetadataProxy.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this MetadataProxy.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this MetadataProxy.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this MetadataProxy.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetadataProxy.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this MetadataProxy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this MetadataProxy.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this MetadataProxy.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this MetadataProxy.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def secret(self):
        """Gets the secret of this MetadataProxy.  # noqa: E501

        secret to access metadata server  # noqa: E501

        :return: The secret of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this MetadataProxy.

        secret to access metadata server  # noqa: E501

        :param secret: The secret of this MetadataProxy.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def metadata_server_ca_ids(self):
        """Gets the metadata_server_ca_ids of this MetadataProxy.  # noqa: E501

        The CAs referenced here must be uploaded to the truststore using the API POST /api/v1/trust-management/certificates?action=import. User needs to ensure a correct CA for this metedata server is used. The REST API can not detect a wrong CA which was used to verify a different server. If the Metadata Proxy reports an ERROR or NO_BACKUP status, user can check the metadata proxy log at transport node for a possible CA issue.   # noqa: E501

        :return: The metadata_server_ca_ids of this MetadataProxy.  # noqa: E501
        :rtype: list[str]
        """
        return self._metadata_server_ca_ids

    @metadata_server_ca_ids.setter
    def metadata_server_ca_ids(self, metadata_server_ca_ids):
        """Sets the metadata_server_ca_ids of this MetadataProxy.

        The CAs referenced here must be uploaded to the truststore using the API POST /api/v1/trust-management/certificates?action=import. User needs to ensure a correct CA for this metedata server is used. The REST API can not detect a wrong CA which was used to verify a different server. If the Metadata Proxy reports an ERROR or NO_BACKUP status, user can check the metadata proxy log at transport node for a possible CA issue.   # noqa: E501

        :param metadata_server_ca_ids: The metadata_server_ca_ids of this MetadataProxy.  # noqa: E501
        :type: list[str]
        """

        self._metadata_server_ca_ids = metadata_server_ca_ids

    @property
    def edge_cluster_member_indexes(self):
        """Gets the edge_cluster_member_indexes of this MetadataProxy.  # noqa: E501

        If none is provided, the NSX will auto-select two edge-nodes from the given edge cluster. If user provides only one edge node, there will be no HA support.   # noqa: E501

        :return: The edge_cluster_member_indexes of this MetadataProxy.  # noqa: E501
        :rtype: list[int]
        """
        return self._edge_cluster_member_indexes

    @edge_cluster_member_indexes.setter
    def edge_cluster_member_indexes(self, edge_cluster_member_indexes):
        """Sets the edge_cluster_member_indexes of this MetadataProxy.

        If none is provided, the NSX will auto-select two edge-nodes from the given edge cluster. If user provides only one edge node, there will be no HA support.   # noqa: E501

        :param edge_cluster_member_indexes: The edge_cluster_member_indexes of this MetadataProxy.  # noqa: E501
        :type: list[int]
        """

        self._edge_cluster_member_indexes = edge_cluster_member_indexes

    @property
    def crypto_protocols(self):
        """Gets the crypto_protocols of this MetadataProxy.  # noqa: E501

        The cryptographic protocols listed here are supported by the metadata proxy. The TLSv1.1 and TLSv1.2 are supported by default.   # noqa: E501

        :return: The crypto_protocols of this MetadataProxy.  # noqa: E501
        :rtype: list[str]
        """
        return self._crypto_protocols

    @crypto_protocols.setter
    def crypto_protocols(self, crypto_protocols):
        """Sets the crypto_protocols of this MetadataProxy.

        The cryptographic protocols listed here are supported by the metadata proxy. The TLSv1.1 and TLSv1.2 are supported by default.   # noqa: E501

        :param crypto_protocols: The crypto_protocols of this MetadataProxy.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["TLS_V1", "TLS_V1_1", "TLS_V1_2"]  # noqa: E501
        if not set(crypto_protocols).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `crypto_protocols` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(crypto_protocols) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._crypto_protocols = crypto_protocols

    @property
    def metadata_server_url(self):
        """Gets the metadata_server_url of this MetadataProxy.  # noqa: E501

        The URL in format scheme://host:port/path. Please note, the scheme supports only http and https as of now, port supports range 3000 - 9000, inclusive.   # noqa: E501

        :return: The metadata_server_url of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._metadata_server_url

    @metadata_server_url.setter
    def metadata_server_url(self, metadata_server_url):
        """Sets the metadata_server_url of this MetadataProxy.

        The URL in format scheme://host:port/path. Please note, the scheme supports only http and https as of now, port supports range 3000 - 9000, inclusive.   # noqa: E501

        :param metadata_server_url: The metadata_server_url of this MetadataProxy.  # noqa: E501
        :type: str
        """
        if metadata_server_url is None:
            raise ValueError("Invalid value for `metadata_server_url`, must not be `None`")  # noqa: E501

        self._metadata_server_url = metadata_server_url

    @property
    def attached_logical_port_id(self):
        """Gets the attached_logical_port_id of this MetadataProxy.  # noqa: E501

        id of attached logical port  # noqa: E501

        :return: The attached_logical_port_id of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._attached_logical_port_id

    @attached_logical_port_id.setter
    def attached_logical_port_id(self, attached_logical_port_id):
        """Sets the attached_logical_port_id of this MetadataProxy.

        id of attached logical port  # noqa: E501

        :param attached_logical_port_id: The attached_logical_port_id of this MetadataProxy.  # noqa: E501
        :type: str
        """

        self._attached_logical_port_id = attached_logical_port_id

    @property
    def enable_standby_relocation(self):
        """Gets the enable_standby_relocation of this MetadataProxy.  # noqa: E501

        Flag to enable the auto-relocation of standby Metadata Proxy in case of edge node failure. Only tier 1 and auto placed Metadata Proxy are considered for the relocation.   # noqa: E501

        :return: The enable_standby_relocation of this MetadataProxy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_standby_relocation

    @enable_standby_relocation.setter
    def enable_standby_relocation(self, enable_standby_relocation):
        """Sets the enable_standby_relocation of this MetadataProxy.

        Flag to enable the auto-relocation of standby Metadata Proxy in case of edge node failure. Only tier 1 and auto placed Metadata Proxy are considered for the relocation.   # noqa: E501

        :param enable_standby_relocation: The enable_standby_relocation of this MetadataProxy.  # noqa: E501
        :type: bool
        """

        self._enable_standby_relocation = enable_standby_relocation

    @property
    def edge_cluster_id(self):
        """Gets the edge_cluster_id of this MetadataProxy.  # noqa: E501

        edge cluster uuid  # noqa: E501

        :return: The edge_cluster_id of this MetadataProxy.  # noqa: E501
        :rtype: str
        """
        return self._edge_cluster_id

    @edge_cluster_id.setter
    def edge_cluster_id(self, edge_cluster_id):
        """Sets the edge_cluster_id of this MetadataProxy.

        edge cluster uuid  # noqa: E501

        :param edge_cluster_id: The edge_cluster_id of this MetadataProxy.  # noqa: E501
        :type: str
        """
        if edge_cluster_id is None:
            raise ValueError("Invalid value for `edge_cluster_id`, must not be `None`")  # noqa: E501

        self._edge_cluster_id = edge_cluster_id

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
        if issubclass(MetadataProxy, dict):
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
        if not isinstance(other, MetadataProxy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
