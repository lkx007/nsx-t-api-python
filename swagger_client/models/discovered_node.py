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


class DiscoveredNode(object):
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
        'last_sync_time': 'int',
        'display_name': 'str',
        'description': 'str',
        'resource_type': 'str',
        'tags': 'list[Tag]',
        'stateless': 'bool',
        'parent_compute_collection': 'str',
        'certificate': 'str',
        'origin_id': 'str',
        'ip_addresses': 'list[str]',
        'hardware_id': 'str',
        'os_version': 'str',
        'node_type': 'str',
        'os_type': 'str',
        'origin_properties': 'list[KeyValuePair]',
        'external_id': 'str',
        'cm_local_id': 'str'
    }
    if hasattr(DiscoveredResource, "swagger_types"):
        swagger_types.update(DiscoveredResource.swagger_types)

    attribute_map = {
        'last_sync_time': '_last_sync_time',
        'display_name': 'display_name',
        'description': 'description',
        'resource_type': 'resource_type',
        'tags': 'tags',
        'stateless': 'stateless',
        'parent_compute_collection': 'parent_compute_collection',
        'certificate': 'certificate',
        'origin_id': 'origin_id',
        'ip_addresses': 'ip_addresses',
        'hardware_id': 'hardware_id',
        'os_version': 'os_version',
        'node_type': 'node_type',
        'os_type': 'os_type',
        'origin_properties': 'origin_properties',
        'external_id': 'external_id',
        'cm_local_id': 'cm_local_id'
    }
    if hasattr(DiscoveredResource, "attribute_map"):
        attribute_map.update(DiscoveredResource.attribute_map)

    def __init__(self, last_sync_time=None, display_name=None, description=None, resource_type=None, tags=None, stateless=None, parent_compute_collection=None, certificate=None, origin_id=None, ip_addresses=None, hardware_id=None, os_version=None, node_type=None, os_type=None, origin_properties=None, external_id=None, cm_local_id=None, *args, **kwargs):  # noqa: E501
        """DiscoveredNode - a model defined in Swagger"""  # noqa: E501
        self._last_sync_time = None
        self._display_name = None
        self._description = None
        self._resource_type = None
        self._tags = None
        self._stateless = None
        self._parent_compute_collection = None
        self._certificate = None
        self._origin_id = None
        self._ip_addresses = None
        self._hardware_id = None
        self._os_version = None
        self._node_type = None
        self._os_type = None
        self._origin_properties = None
        self._external_id = None
        self._cm_local_id = None
        self.discriminator = None
        if last_sync_time is not None:
            self.last_sync_time = last_sync_time
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        self.resource_type = resource_type
        if tags is not None:
            self.tags = tags
        if stateless is not None:
            self.stateless = stateless
        if parent_compute_collection is not None:
            self.parent_compute_collection = parent_compute_collection
        if certificate is not None:
            self.certificate = certificate
        if origin_id is not None:
            self.origin_id = origin_id
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if hardware_id is not None:
            self.hardware_id = hardware_id
        if os_version is not None:
            self.os_version = os_version
        if node_type is not None:
            self.node_type = node_type
        if os_type is not None:
            self.os_type = os_type
        if origin_properties is not None:
            self.origin_properties = origin_properties
        if external_id is not None:
            self.external_id = external_id
        if cm_local_id is not None:
            self.cm_local_id = cm_local_id
        DiscoveredResource.__init__(self, *args, **kwargs)

    @property
    def last_sync_time(self):
        """Gets the last_sync_time of this DiscoveredNode.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_sync_time of this DiscoveredNode.  # noqa: E501
        :rtype: int
        """
        return self._last_sync_time

    @last_sync_time.setter
    def last_sync_time(self, last_sync_time):
        """Sets the last_sync_time of this DiscoveredNode.

        Timestamp of last modification  # noqa: E501

        :param last_sync_time: The last_sync_time of this DiscoveredNode.  # noqa: E501
        :type: int
        """

        self._last_sync_time = last_sync_time

    @property
    def display_name(self):
        """Gets the display_name of this DiscoveredNode.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DiscoveredNode.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this DiscoveredNode.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DiscoveredNode.

        Description of this resource  # noqa: E501

        :param description: The description of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def resource_type(self):
        """Gets the resource_type of this DiscoveredNode.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DiscoveredNode.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this DiscoveredNode.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def tags(self):
        """Gets the tags of this DiscoveredNode.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this DiscoveredNode.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DiscoveredNode.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this DiscoveredNode.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def stateless(self):
        """Gets the stateless of this DiscoveredNode.  # noqa: E501

        The stateless property describes whether host persists its state across reboot or not. If state persists, value is set as false otherwise true.  # noqa: E501

        :return: The stateless of this DiscoveredNode.  # noqa: E501
        :rtype: bool
        """
        return self._stateless

    @stateless.setter
    def stateless(self, stateless):
        """Sets the stateless of this DiscoveredNode.

        The stateless property describes whether host persists its state across reboot or not. If state persists, value is set as false otherwise true.  # noqa: E501

        :param stateless: The stateless of this DiscoveredNode.  # noqa: E501
        :type: bool
        """

        self._stateless = stateless

    @property
    def parent_compute_collection(self):
        """Gets the parent_compute_collection of this DiscoveredNode.  # noqa: E501

        External id of the compute collection to which this node belongs  # noqa: E501

        :return: The parent_compute_collection of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._parent_compute_collection

    @parent_compute_collection.setter
    def parent_compute_collection(self, parent_compute_collection):
        """Sets the parent_compute_collection of this DiscoveredNode.

        External id of the compute collection to which this node belongs  # noqa: E501

        :param parent_compute_collection: The parent_compute_collection of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._parent_compute_collection = parent_compute_collection

    @property
    def certificate(self):
        """Gets the certificate of this DiscoveredNode.  # noqa: E501

        Certificate of the discovered node  # noqa: E501

        :return: The certificate of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this DiscoveredNode.

        Certificate of the discovered node  # noqa: E501

        :param certificate: The certificate of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._certificate = certificate

    @property
    def origin_id(self):
        """Gets the origin_id of this DiscoveredNode.  # noqa: E501

        Id of the compute manager from where this node was discovered  # noqa: E501

        :return: The origin_id of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._origin_id

    @origin_id.setter
    def origin_id(self, origin_id):
        """Sets the origin_id of this DiscoveredNode.

        Id of the compute manager from where this node was discovered  # noqa: E501

        :param origin_id: The origin_id of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._origin_id = origin_id

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this DiscoveredNode.  # noqa: E501

        IP Addresses of the the discovered node.  # noqa: E501

        :return: The ip_addresses of this DiscoveredNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this DiscoveredNode.

        IP Addresses of the the discovered node.  # noqa: E501

        :param ip_addresses: The ip_addresses of this DiscoveredNode.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def hardware_id(self):
        """Gets the hardware_id of this DiscoveredNode.  # noqa: E501

        Hardware Id is generated using system hardware info. It is used to retrieve fabric node of the esx.  # noqa: E501

        :return: The hardware_id of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._hardware_id

    @hardware_id.setter
    def hardware_id(self, hardware_id):
        """Sets the hardware_id of this DiscoveredNode.

        Hardware Id is generated using system hardware info. It is used to retrieve fabric node of the esx.  # noqa: E501

        :param hardware_id: The hardware_id of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._hardware_id = hardware_id

    @property
    def os_version(self):
        """Gets the os_version of this DiscoveredNode.  # noqa: E501

        OS version of the discovered node  # noqa: E501

        :return: The os_version of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this DiscoveredNode.

        OS version of the discovered node  # noqa: E501

        :param os_version: The os_version of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def node_type(self):
        """Gets the node_type of this DiscoveredNode.  # noqa: E501

        Discovered Node type like Host  # noqa: E501

        :return: The node_type of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this DiscoveredNode.

        Discovered Node type like Host  # noqa: E501

        :param node_type: The node_type of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def os_type(self):
        """Gets the os_type of this DiscoveredNode.  # noqa: E501

        OS type of the discovered node  # noqa: E501

        :return: The os_type of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this DiscoveredNode.

        OS type of the discovered node  # noqa: E501

        :param os_type: The os_type of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def origin_properties(self):
        """Gets the origin_properties of this DiscoveredNode.  # noqa: E501

        Key-Value map of additional specific properties of discovered node in the Compute Manager   # noqa: E501

        :return: The origin_properties of this DiscoveredNode.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self._origin_properties

    @origin_properties.setter
    def origin_properties(self, origin_properties):
        """Sets the origin_properties of this DiscoveredNode.

        Key-Value map of additional specific properties of discovered node in the Compute Manager   # noqa: E501

        :param origin_properties: The origin_properties of this DiscoveredNode.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self._origin_properties = origin_properties

    @property
    def external_id(self):
        """Gets the external_id of this DiscoveredNode.  # noqa: E501

        External id of the discovered node, ex. a mo-ref from VC  # noqa: E501

        :return: The external_id of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this DiscoveredNode.

        External id of the discovered node, ex. a mo-ref from VC  # noqa: E501

        :param external_id: The external_id of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def cm_local_id(self):
        """Gets the cm_local_id of this DiscoveredNode.  # noqa: E501

        Local Id of the discovered node in the Compute Manager  # noqa: E501

        :return: The cm_local_id of this DiscoveredNode.  # noqa: E501
        :rtype: str
        """
        return self._cm_local_id

    @cm_local_id.setter
    def cm_local_id(self, cm_local_id):
        """Sets the cm_local_id of this DiscoveredNode.

        Local Id of the discovered node in the Compute Manager  # noqa: E501

        :param cm_local_id: The cm_local_id of this DiscoveredNode.  # noqa: E501
        :type: str
        """

        self._cm_local_id = cm_local_id

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
        if issubclass(DiscoveredNode, dict):
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
        if not isinstance(other, DiscoveredNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
