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


class DirectoryAdGroup(object):
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
        'domain_sync_node_id': 'str',
        'distinguished_name': 'str',
        'domain_id': 'str',
        'resource_type': 'str',
        'domain_name': 'str',
        'object_guid': 'str',
        'secure_id': 'str'
    }
    if hasattr(DirectoryGroup, "swagger_types"):
        swagger_types.update(DirectoryGroup.swagger_types)

    attribute_map = {
        'domain_sync_node_id': 'domain_sync_node_id',
        'distinguished_name': 'distinguished_name',
        'domain_id': 'domain_id',
        'resource_type': 'resource_type',
        'domain_name': 'domain_name',
        'object_guid': 'object_guid',
        'secure_id': 'secure_id'
    }
    if hasattr(DirectoryGroup, "attribute_map"):
        attribute_map.update(DirectoryGroup.attribute_map)

    def __init__(self, domain_sync_node_id=None, distinguished_name=None, domain_id=None, resource_type=None, domain_name=None, object_guid=None, secure_id=None, *args, **kwargs):  # noqa: E501
        """DirectoryAdGroup - a model defined in Swagger"""  # noqa: E501
        self._domain_sync_node_id = None
        self._distinguished_name = None
        self._domain_id = None
        self._resource_type = None
        self._domain_name = None
        self._object_guid = None
        self._secure_id = None
        self.discriminator = None
        if domain_sync_node_id is not None:
            self.domain_sync_node_id = domain_sync_node_id
        self.distinguished_name = distinguished_name
        self.domain_id = domain_id
        self.resource_type = resource_type
        self.domain_name = domain_name
        self.object_guid = object_guid
        self.secure_id = secure_id
        DirectoryGroup.__init__(self, *args, **kwargs)

    @property
    def domain_sync_node_id(self):
        """Gets the domain_sync_node_id of this DirectoryAdGroup.  # noqa: E501

        Domain sync node under which this directory group is located. We currently sync only from Root node and hence this attribute doesn't have a specific value set.  # noqa: E501

        :return: The domain_sync_node_id of this DirectoryAdGroup.  # noqa: E501
        :rtype: str
        """
        return self._domain_sync_node_id

    @domain_sync_node_id.setter
    def domain_sync_node_id(self, domain_sync_node_id):
        """Sets the domain_sync_node_id of this DirectoryAdGroup.

        Domain sync node under which this directory group is located. We currently sync only from Root node and hence this attribute doesn't have a specific value set.  # noqa: E501

        :param domain_sync_node_id: The domain_sync_node_id of this DirectoryAdGroup.  # noqa: E501
        :type: str
        """

        self._domain_sync_node_id = domain_sync_node_id

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this DirectoryAdGroup.  # noqa: E501

        Directory group distinguished name  # noqa: E501

        :return: The distinguished_name of this DirectoryAdGroup.  # noqa: E501
        :rtype: str
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this DirectoryAdGroup.

        Directory group distinguished name  # noqa: E501

        :param distinguished_name: The distinguished_name of this DirectoryAdGroup.  # noqa: E501
        :type: str
        """
        if distinguished_name is None:
            raise ValueError("Invalid value for `distinguished_name`, must not be `None`")  # noqa: E501

        self._distinguished_name = distinguished_name

    @property
    def domain_id(self):
        """Gets the domain_id of this DirectoryAdGroup.  # noqa: E501

        Domain ID this directory group belongs to.  # noqa: E501

        :return: The domain_id of this DirectoryAdGroup.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DirectoryAdGroup.

        Domain ID this directory group belongs to.  # noqa: E501

        :param domain_id: The domain_id of this DirectoryAdGroup.  # noqa: E501
        :type: str
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")  # noqa: E501

        self._domain_id = domain_id

    @property
    def resource_type(self):
        """Gets the resource_type of this DirectoryAdGroup.  # noqa: E501

        Directory group resource type comes from multiple sub-classes extending this base class. For example, DirectoryAdGroup is one accepted resource_type. If there are more sub-classes defined, they will also be accepted resource_type.  # noqa: E501

        :return: The resource_type of this DirectoryAdGroup.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DirectoryAdGroup.

        Directory group resource type comes from multiple sub-classes extending this base class. For example, DirectoryAdGroup is one accepted resource_type. If there are more sub-classes defined, they will also be accepted resource_type.  # noqa: E501

        :param resource_type: The resource_type of this DirectoryAdGroup.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def domain_name(self):
        """Gets the domain_name of this DirectoryAdGroup.  # noqa: E501

        Each active directory domain has a domain naming context (NC), which contains domain-specific data. The root of this naming context is represented by a domain's distinguished name (DN) and is typically referred to as the NC head.  # noqa: E501

        :return: The domain_name of this DirectoryAdGroup.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DirectoryAdGroup.

        Each active directory domain has a domain naming context (NC), which contains domain-specific data. The root of this naming context is represented by a domain's distinguished name (DN) and is typically referred to as the NC head.  # noqa: E501

        :param domain_name: The domain_name of this DirectoryAdGroup.  # noqa: E501
        :type: str
        """
        if domain_name is None:
            raise ValueError("Invalid value for `domain_name`, must not be `None`")  # noqa: E501

        self._domain_name = domain_name

    @property
    def object_guid(self):
        """Gets the object_guid of this DirectoryAdGroup.  # noqa: E501

        GUID is a 128-bit value that is unique not only in the enterprise but also across the world. GUIDs are assigned to every object created by Active Directory, not just User and Group objects.  # noqa: E501

        :return: The object_guid of this DirectoryAdGroup.  # noqa: E501
        :rtype: str
        """
        return self._object_guid

    @object_guid.setter
    def object_guid(self, object_guid):
        """Sets the object_guid of this DirectoryAdGroup.

        GUID is a 128-bit value that is unique not only in the enterprise but also across the world. GUIDs are assigned to every object created by Active Directory, not just User and Group objects.  # noqa: E501

        :param object_guid: The object_guid of this DirectoryAdGroup.  # noqa: E501
        :type: str
        """
        if object_guid is None:
            raise ValueError("Invalid value for `object_guid`, must not be `None`")  # noqa: E501

        self._object_guid = object_guid

    @property
    def secure_id(self):
        """Gets the secure_id of this DirectoryAdGroup.  # noqa: E501

        A security identifier (SID) is a unique value of variable length used to identify a trustee. A SID consists of the following components - The revision level of the SID structure; A 48-bit identifier authority value that identifies the authority that issued the SID; A variable number of subauthority or relative identifier (RID) values that uniquely identify the trustee relative to the authority that issued the SID.  # noqa: E501

        :return: The secure_id of this DirectoryAdGroup.  # noqa: E501
        :rtype: str
        """
        return self._secure_id

    @secure_id.setter
    def secure_id(self, secure_id):
        """Sets the secure_id of this DirectoryAdGroup.

        A security identifier (SID) is a unique value of variable length used to identify a trustee. A SID consists of the following components - The revision level of the SID structure; A 48-bit identifier authority value that identifies the authority that issued the SID; A variable number of subauthority or relative identifier (RID) values that uniquely identify the trustee relative to the authority that issued the SID.  # noqa: E501

        :param secure_id: The secure_id of this DirectoryAdGroup.  # noqa: E501
        :type: str
        """
        if secure_id is None:
            raise ValueError("Invalid value for `secure_id`, must not be `None`")  # noqa: E501

        self._secure_id = secure_id

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
        if issubclass(DirectoryAdGroup, dict):
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
        if not isinstance(other, DirectoryAdGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
