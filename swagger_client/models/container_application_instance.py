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


class ContainerApplicationInstance(object):
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
        'status': 'str',
        'container_cluster_id': 'str',
        'cluster_node_id': 'str',
        'external_id': 'str',
        'origin_properties': 'list[KeyValuePair]',
        'container_application_ids': 'list[str]',
        'container_project_id': 'str'
    }
    if hasattr(DiscoveredResource, "swagger_types"):
        swagger_types.update(DiscoveredResource.swagger_types)

    attribute_map = {
        'last_sync_time': '_last_sync_time',
        'display_name': 'display_name',
        'description': 'description',
        'resource_type': 'resource_type',
        'tags': 'tags',
        'status': 'status',
        'container_cluster_id': 'container_cluster_id',
        'cluster_node_id': 'cluster_node_id',
        'external_id': 'external_id',
        'origin_properties': 'origin_properties',
        'container_application_ids': 'container_application_ids',
        'container_project_id': 'container_project_id'
    }
    if hasattr(DiscoveredResource, "attribute_map"):
        attribute_map.update(DiscoveredResource.attribute_map)

    def __init__(self, last_sync_time=None, display_name=None, description=None, resource_type=None, tags=None, status=None, container_cluster_id=None, cluster_node_id=None, external_id=None, origin_properties=None, container_application_ids=None, container_project_id=None, *args, **kwargs):  # noqa: E501
        """ContainerApplicationInstance - a model defined in Swagger"""  # noqa: E501
        self._last_sync_time = None
        self._display_name = None
        self._description = None
        self._resource_type = None
        self._tags = None
        self._status = None
        self._container_cluster_id = None
        self._cluster_node_id = None
        self._external_id = None
        self._origin_properties = None
        self._container_application_ids = None
        self._container_project_id = None
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
        if status is not None:
            self.status = status
        if container_cluster_id is not None:
            self.container_cluster_id = container_cluster_id
        if cluster_node_id is not None:
            self.cluster_node_id = cluster_node_id
        self.external_id = external_id
        if origin_properties is not None:
            self.origin_properties = origin_properties
        if container_application_ids is not None:
            self.container_application_ids = container_application_ids
        if container_project_id is not None:
            self.container_project_id = container_project_id
        DiscoveredResource.__init__(self, *args, **kwargs)

    @property
    def last_sync_time(self):
        """Gets the last_sync_time of this ContainerApplicationInstance.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_sync_time of this ContainerApplicationInstance.  # noqa: E501
        :rtype: int
        """
        return self._last_sync_time

    @last_sync_time.setter
    def last_sync_time(self, last_sync_time):
        """Sets the last_sync_time of this ContainerApplicationInstance.

        Timestamp of last modification  # noqa: E501

        :param last_sync_time: The last_sync_time of this ContainerApplicationInstance.  # noqa: E501
        :type: int
        """

        self._last_sync_time = last_sync_time

    @property
    def display_name(self):
        """Gets the display_name of this ContainerApplicationInstance.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this ContainerApplicationInstance.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ContainerApplicationInstance.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this ContainerApplicationInstance.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this ContainerApplicationInstance.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this ContainerApplicationInstance.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ContainerApplicationInstance.

        Description of this resource  # noqa: E501

        :param description: The description of this ContainerApplicationInstance.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def resource_type(self):
        """Gets the resource_type of this ContainerApplicationInstance.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this ContainerApplicationInstance.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ContainerApplicationInstance.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this ContainerApplicationInstance.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def tags(self):
        """Gets the tags of this ContainerApplicationInstance.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this ContainerApplicationInstance.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ContainerApplicationInstance.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this ContainerApplicationInstance.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def status(self):
        """Gets the status of this ContainerApplicationInstance.  # noqa: E501

        Status of the container application instance.  # noqa: E501

        :return: The status of this ContainerApplicationInstance.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ContainerApplicationInstance.

        Status of the container application instance.  # noqa: E501

        :param status: The status of this ContainerApplicationInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "HEALTHY", "UP", "DOWN", "DEGRADED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def container_cluster_id(self):
        """Gets the container_cluster_id of this ContainerApplicationInstance.  # noqa: E501

        Identifier of the container cluster this application instance belongs to.  # noqa: E501

        :return: The container_cluster_id of this ContainerApplicationInstance.  # noqa: E501
        :rtype: str
        """
        return self._container_cluster_id

    @container_cluster_id.setter
    def container_cluster_id(self, container_cluster_id):
        """Sets the container_cluster_id of this ContainerApplicationInstance.

        Identifier of the container cluster this application instance belongs to.  # noqa: E501

        :param container_cluster_id: The container_cluster_id of this ContainerApplicationInstance.  # noqa: E501
        :type: str
        """

        self._container_cluster_id = container_cluster_id

    @property
    def cluster_node_id(self):
        """Gets the cluster_node_id of this ContainerApplicationInstance.  # noqa: E501

        Cluster node id where application instance is running.  # noqa: E501

        :return: The cluster_node_id of this ContainerApplicationInstance.  # noqa: E501
        :rtype: str
        """
        return self._cluster_node_id

    @cluster_node_id.setter
    def cluster_node_id(self, cluster_node_id):
        """Sets the cluster_node_id of this ContainerApplicationInstance.

        Cluster node id where application instance is running.  # noqa: E501

        :param cluster_node_id: The cluster_node_id of this ContainerApplicationInstance.  # noqa: E501
        :type: str
        """

        self._cluster_node_id = cluster_node_id

    @property
    def external_id(self):
        """Gets the external_id of this ContainerApplicationInstance.  # noqa: E501

        Identifier of the container application instance on container cluster.  # noqa: E501

        :return: The external_id of this ContainerApplicationInstance.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ContainerApplicationInstance.

        Identifier of the container application instance on container cluster.  # noqa: E501

        :param external_id: The external_id of this ContainerApplicationInstance.  # noqa: E501
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501

        self._external_id = external_id

    @property
    def origin_properties(self):
        """Gets the origin_properties of this ContainerApplicationInstance.  # noqa: E501

        Array of additional specific properties of container application instance in key-value format.   # noqa: E501

        :return: The origin_properties of this ContainerApplicationInstance.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self._origin_properties

    @origin_properties.setter
    def origin_properties(self, origin_properties):
        """Sets the origin_properties of this ContainerApplicationInstance.

        Array of additional specific properties of container application instance in key-value format.   # noqa: E501

        :param origin_properties: The origin_properties of this ContainerApplicationInstance.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self._origin_properties = origin_properties

    @property
    def container_application_ids(self):
        """Gets the container_application_ids of this ContainerApplicationInstance.  # noqa: E501

        List of identifiers of the container application.  # noqa: E501

        :return: The container_application_ids of this ContainerApplicationInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._container_application_ids

    @container_application_ids.setter
    def container_application_ids(self, container_application_ids):
        """Sets the container_application_ids of this ContainerApplicationInstance.

        List of identifiers of the container application.  # noqa: E501

        :param container_application_ids: The container_application_ids of this ContainerApplicationInstance.  # noqa: E501
        :type: list[str]
        """

        self._container_application_ids = container_application_ids

    @property
    def container_project_id(self):
        """Gets the container_project_id of this ContainerApplicationInstance.  # noqa: E501

        Identifier of the container project which this container application instance belongs to.   # noqa: E501

        :return: The container_project_id of this ContainerApplicationInstance.  # noqa: E501
        :rtype: str
        """
        return self._container_project_id

    @container_project_id.setter
    def container_project_id(self, container_project_id):
        """Sets the container_project_id of this ContainerApplicationInstance.

        Identifier of the container project which this container application instance belongs to.   # noqa: E501

        :param container_project_id: The container_project_id of this ContainerApplicationInstance.  # noqa: E501
        :type: str
        """

        self._container_project_id = container_project_id

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
        if issubclass(ContainerApplicationInstance, dict):
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
        if not isinstance(other, ContainerApplicationInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
