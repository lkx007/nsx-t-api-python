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


class EdgeCluster(object):
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
        'member_node_type': 'str',
        'cluster_profile_bindings': 'list[ClusterProfileTypeIdEntry]',
        'allocation_rules': 'list[AllocationRule]',
        'members': 'list[EdgeClusterMember]',
        'deployment_type': 'str'
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
        'member_node_type': 'member_node_type',
        'cluster_profile_bindings': 'cluster_profile_bindings',
        'allocation_rules': 'allocation_rules',
        'members': 'members',
        'deployment_type': 'deployment_type'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, member_node_type=None, cluster_profile_bindings=None, allocation_rules=None, members=None, deployment_type=None, *args, **kwargs):  # noqa: E501
        """EdgeCluster - a model defined in Swagger"""  # noqa: E501
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
        self._member_node_type = None
        self._cluster_profile_bindings = None
        self._allocation_rules = None
        self._members = None
        self._deployment_type = None
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
        if member_node_type is not None:
            self.member_node_type = member_node_type
        if cluster_profile_bindings is not None:
            self.cluster_profile_bindings = cluster_profile_bindings
        if allocation_rules is not None:
            self.allocation_rules = allocation_rules
        if members is not None:
            self.members = members
        if deployment_type is not None:
            self.deployment_type = deployment_type
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this EdgeCluster.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this EdgeCluster.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this EdgeCluster.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this EdgeCluster.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this EdgeCluster.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this EdgeCluster.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this EdgeCluster.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this EdgeCluster.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this EdgeCluster.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this EdgeCluster.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdgeCluster.

        Description of this resource  # noqa: E501

        :param description: The description of this EdgeCluster.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this EdgeCluster.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this EdgeCluster.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EdgeCluster.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this EdgeCluster.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this EdgeCluster.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this EdgeCluster.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this EdgeCluster.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this EdgeCluster.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this EdgeCluster.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this EdgeCluster.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this EdgeCluster.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this EdgeCluster.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this EdgeCluster.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this EdgeCluster.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this EdgeCluster.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this EdgeCluster.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this EdgeCluster.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this EdgeCluster.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this EdgeCluster.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this EdgeCluster.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this EdgeCluster.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this EdgeCluster.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this EdgeCluster.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this EdgeCluster.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this EdgeCluster.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this EdgeCluster.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdgeCluster.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this EdgeCluster.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this EdgeCluster.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this EdgeCluster.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this EdgeCluster.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this EdgeCluster.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def member_node_type(self):
        """Gets the member_node_type of this EdgeCluster.  # noqa: E501

        Edge cluster is homogenous collection of transport nodes. Hence all transport nodes of the cluster must be of same type. This readonly field shows the type of transport nodes.   # noqa: E501

        :return: The member_node_type of this EdgeCluster.  # noqa: E501
        :rtype: str
        """
        return self._member_node_type

    @member_node_type.setter
    def member_node_type(self, member_node_type):
        """Sets the member_node_type of this EdgeCluster.

        Edge cluster is homogenous collection of transport nodes. Hence all transport nodes of the cluster must be of same type. This readonly field shows the type of transport nodes.   # noqa: E501

        :param member_node_type: The member_node_type of this EdgeCluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["EDGE_NODE", "PUBLIC_CLOUD_GATEWAY_NODE", "UNKNOWN"]  # noqa: E501
        if member_node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `member_node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(member_node_type, allowed_values)
            )

        self._member_node_type = member_node_type

    @property
    def cluster_profile_bindings(self):
        """Gets the cluster_profile_bindings of this EdgeCluster.  # noqa: E501

        Edge cluster profile bindings  # noqa: E501

        :return: The cluster_profile_bindings of this EdgeCluster.  # noqa: E501
        :rtype: list[ClusterProfileTypeIdEntry]
        """
        return self._cluster_profile_bindings

    @cluster_profile_bindings.setter
    def cluster_profile_bindings(self, cluster_profile_bindings):
        """Sets the cluster_profile_bindings of this EdgeCluster.

        Edge cluster profile bindings  # noqa: E501

        :param cluster_profile_bindings: The cluster_profile_bindings of this EdgeCluster.  # noqa: E501
        :type: list[ClusterProfileTypeIdEntry]
        """

        self._cluster_profile_bindings = cluster_profile_bindings

    @property
    def allocation_rules(self):
        """Gets the allocation_rules of this EdgeCluster.  # noqa: E501

        Set of allocation rules and respected action for auto placement of logical router, DHCP and MDProxy on edge cluster members.   # noqa: E501

        :return: The allocation_rules of this EdgeCluster.  # noqa: E501
        :rtype: list[AllocationRule]
        """
        return self._allocation_rules

    @allocation_rules.setter
    def allocation_rules(self, allocation_rules):
        """Sets the allocation_rules of this EdgeCluster.

        Set of allocation rules and respected action for auto placement of logical router, DHCP and MDProxy on edge cluster members.   # noqa: E501

        :param allocation_rules: The allocation_rules of this EdgeCluster.  # noqa: E501
        :type: list[AllocationRule]
        """

        self._allocation_rules = allocation_rules

    @property
    def members(self):
        """Gets the members of this EdgeCluster.  # noqa: E501

        EdgeCluster only supports homogeneous members. These member should be backed by either EdgeNode or PublicCloudGatewayNode. TransportNode type of these nodes should be the same. DeploymentType (VIRTUAL_MACHINE|PHYSICAL_MACHINE) of these EdgeNodes is recommended to be the same. EdgeCluster supports members of different deployment types.   # noqa: E501

        :return: The members of this EdgeCluster.  # noqa: E501
        :rtype: list[EdgeClusterMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this EdgeCluster.

        EdgeCluster only supports homogeneous members. These member should be backed by either EdgeNode or PublicCloudGatewayNode. TransportNode type of these nodes should be the same. DeploymentType (VIRTUAL_MACHINE|PHYSICAL_MACHINE) of these EdgeNodes is recommended to be the same. EdgeCluster supports members of different deployment types.   # noqa: E501

        :param members: The members of this EdgeCluster.  # noqa: E501
        :type: list[EdgeClusterMember]
        """

        self._members = members

    @property
    def deployment_type(self):
        """Gets the deployment_type of this EdgeCluster.  # noqa: E501

        This field is a readonly field which shows the deployment_type of members. It returns UNKNOWN if there are no members, and returns VIRTUAL_MACHINE| PHYSICAL_MACHINE if all edge members are VIRTUAL_MACHINE|PHYSICAL_MACHINE. It returns HYBRID if the cluster contains edge members of both types VIRTUAL_MACHINE and PHYSICAL_MACHINE.   # noqa: E501

        :return: The deployment_type of this EdgeCluster.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this EdgeCluster.

        This field is a readonly field which shows the deployment_type of members. It returns UNKNOWN if there are no members, and returns VIRTUAL_MACHINE| PHYSICAL_MACHINE if all edge members are VIRTUAL_MACHINE|PHYSICAL_MACHINE. It returns HYBRID if the cluster contains edge members of both types VIRTUAL_MACHINE and PHYSICAL_MACHINE.   # noqa: E501

        :param deployment_type: The deployment_type of this EdgeCluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["VIRTUAL_MACHINE", "PHYSICAL_MACHINE", "UNKNOWN"]  # noqa: E501
        if deployment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_type, allowed_values)
            )

        self._deployment_type = deployment_type

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
        if issubclass(EdgeCluster, dict):
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
        if not isinstance(other, EdgeCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
