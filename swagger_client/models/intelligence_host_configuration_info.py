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


class IntelligenceHostConfigurationInfo(object):
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
        'context_data_collection_interval': 'int',
        'broker_truststore': 'str',
        'broker_certificate': 'str',
        'context_user_uids': 'list[str]',
        'context_process_hashes': 'list[str]',
        'enable_data_collection': 'bool',
        'context_process_names': 'list[str]',
        'private_ip_prefix': 'list[IntelligenceFlowPrivateIpPrefixInfo]',
        'broker_bootstrap_servers': 'list[IntelligenceBrokerEndpointInfo]',
        'max_inactive_flow_count': 'int',
        'context_user_sids': 'list[str]',
        'flow_data_collection_interval': 'int',
        'max_active_flow_count': 'int'
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
        'context_data_collection_interval': 'context_data_collection_interval',
        'broker_truststore': 'broker_truststore',
        'broker_certificate': 'broker_certificate',
        'context_user_uids': 'context_user_uids',
        'context_process_hashes': 'context_process_hashes',
        'enable_data_collection': 'enable_data_collection',
        'context_process_names': 'context_process_names',
        'private_ip_prefix': 'private_ip_prefix',
        'broker_bootstrap_servers': 'broker_bootstrap_servers',
        'max_inactive_flow_count': 'max_inactive_flow_count',
        'context_user_sids': 'context_user_sids',
        'flow_data_collection_interval': 'flow_data_collection_interval',
        'max_active_flow_count': 'max_active_flow_count'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, context_data_collection_interval=None, broker_truststore=None, broker_certificate=None, context_user_uids=None, context_process_hashes=None, enable_data_collection=None, context_process_names=None, private_ip_prefix=None, broker_bootstrap_servers=None, max_inactive_flow_count=None, context_user_sids=None, flow_data_collection_interval=None, max_active_flow_count=None, *args, **kwargs):  # noqa: E501
        """IntelligenceHostConfigurationInfo - a model defined in Swagger"""  # noqa: E501
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
        self._context_data_collection_interval = None
        self._broker_truststore = None
        self._broker_certificate = None
        self._context_user_uids = None
        self._context_process_hashes = None
        self._enable_data_collection = None
        self._context_process_names = None
        self._private_ip_prefix = None
        self._broker_bootstrap_servers = None
        self._max_inactive_flow_count = None
        self._context_user_sids = None
        self._flow_data_collection_interval = None
        self._max_active_flow_count = None
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
        if context_data_collection_interval is not None:
            self.context_data_collection_interval = context_data_collection_interval
        if broker_truststore is not None:
            self.broker_truststore = broker_truststore
        if broker_certificate is not None:
            self.broker_certificate = broker_certificate
        if context_user_uids is not None:
            self.context_user_uids = context_user_uids
        if context_process_hashes is not None:
            self.context_process_hashes = context_process_hashes
        if enable_data_collection is not None:
            self.enable_data_collection = enable_data_collection
        if context_process_names is not None:
            self.context_process_names = context_process_names
        if private_ip_prefix is not None:
            self.private_ip_prefix = private_ip_prefix
        if broker_bootstrap_servers is not None:
            self.broker_bootstrap_servers = broker_bootstrap_servers
        if max_inactive_flow_count is not None:
            self.max_inactive_flow_count = max_inactive_flow_count
        if context_user_sids is not None:
            self.context_user_sids = context_user_sids
        if flow_data_collection_interval is not None:
            self.flow_data_collection_interval = flow_data_collection_interval
        if max_active_flow_count is not None:
            self.max_active_flow_count = max_active_flow_count
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this IntelligenceHostConfigurationInfo.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IntelligenceHostConfigurationInfo.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IntelligenceHostConfigurationInfo.

        Description of this resource  # noqa: E501

        :param description: The description of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IntelligenceHostConfigurationInfo.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this IntelligenceHostConfigurationInfo.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this IntelligenceHostConfigurationInfo.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this IntelligenceHostConfigurationInfo.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IntelligenceHostConfigurationInfo.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this IntelligenceHostConfigurationInfo.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this IntelligenceHostConfigurationInfo.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this IntelligenceHostConfigurationInfo.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IntelligenceHostConfigurationInfo.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this IntelligenceHostConfigurationInfo.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this IntelligenceHostConfigurationInfo.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def context_data_collection_interval(self):
        """Gets the context_data_collection_interval of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Interval in minute of reporting VM guest context data to NSX-Intelligence.   # noqa: E501

        :return: The context_data_collection_interval of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: int
        """
        return self._context_data_collection_interval

    @context_data_collection_interval.setter
    def context_data_collection_interval(self, context_data_collection_interval):
        """Sets the context_data_collection_interval of this IntelligenceHostConfigurationInfo.

        Interval in minute of reporting VM guest context data to NSX-Intelligence.   # noqa: E501

        :param context_data_collection_interval: The context_data_collection_interval of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: int
        """

        self._context_data_collection_interval = context_data_collection_interval

    @property
    def broker_truststore(self):
        """Gets the broker_truststore of this IntelligenceHostConfigurationInfo.  # noqa: E501

        A truststore to establish the trust between NSX and NSX-Intelligence brokers.   # noqa: E501

        :return: The broker_truststore of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: str
        """
        return self._broker_truststore

    @broker_truststore.setter
    def broker_truststore(self, broker_truststore):
        """Sets the broker_truststore of this IntelligenceHostConfigurationInfo.

        A truststore to establish the trust between NSX and NSX-Intelligence brokers.   # noqa: E501

        :param broker_truststore: The broker_truststore of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: str
        """

        self._broker_truststore = broker_truststore

    @property
    def broker_certificate(self):
        """Gets the broker_certificate of this IntelligenceHostConfigurationInfo.  # noqa: E501

        A broker certificate to verify the identity of brokers.   # noqa: E501

        :return: The broker_certificate of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: str
        """
        return self._broker_certificate

    @broker_certificate.setter
    def broker_certificate(self, broker_certificate):
        """Sets the broker_certificate of this IntelligenceHostConfigurationInfo.

        A broker certificate to verify the identity of brokers.   # noqa: E501

        :param broker_certificate: The broker_certificate of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: str
        """

        self._broker_certificate = broker_certificate

    @property
    def context_user_uids(self):
        """Gets the context_user_uids of this IntelligenceHostConfigurationInfo.  # noqa: E501

        List of linux user uid to collect context data. Empty implies all users.   # noqa: E501

        :return: The context_user_uids of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._context_user_uids

    @context_user_uids.setter
    def context_user_uids(self, context_user_uids):
        """Sets the context_user_uids of this IntelligenceHostConfigurationInfo.

        List of linux user uid to collect context data. Empty implies all users.   # noqa: E501

        :param context_user_uids: The context_user_uids of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: list[str]
        """

        self._context_user_uids = context_user_uids

    @property
    def context_process_hashes(self):
        """Gets the context_process_hashes of this IntelligenceHostConfigurationInfo.  # noqa: E501

        List of hashes of processes to collect context data. Empty implies all processes.   # noqa: E501

        :return: The context_process_hashes of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._context_process_hashes

    @context_process_hashes.setter
    def context_process_hashes(self, context_process_hashes):
        """Sets the context_process_hashes of this IntelligenceHostConfigurationInfo.

        List of hashes of processes to collect context data. Empty implies all processes.   # noqa: E501

        :param context_process_hashes: The context_process_hashes of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: list[str]
        """

        self._context_process_hashes = context_process_hashes

    @property
    def enable_data_collection(self):
        """Gets the enable_data_collection of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Enable NSX-Intelligence data collection in host nodes.   # noqa: E501

        :return: The enable_data_collection of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enable_data_collection

    @enable_data_collection.setter
    def enable_data_collection(self, enable_data_collection):
        """Sets the enable_data_collection of this IntelligenceHostConfigurationInfo.

        Enable NSX-Intelligence data collection in host nodes.   # noqa: E501

        :param enable_data_collection: The enable_data_collection of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: bool
        """

        self._enable_data_collection = enable_data_collection

    @property
    def context_process_names(self):
        """Gets the context_process_names of this IntelligenceHostConfigurationInfo.  # noqa: E501

        List of processes to collect context data. Empty implies all processes.   # noqa: E501

        :return: The context_process_names of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._context_process_names

    @context_process_names.setter
    def context_process_names(self, context_process_names):
        """Sets the context_process_names of this IntelligenceHostConfigurationInfo.

        List of processes to collect context data. Empty implies all processes.   # noqa: E501

        :param context_process_names: The context_process_names of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: list[str]
        """

        self._context_process_names = context_process_names

    @property
    def private_ip_prefix(self):
        """Gets the private_ip_prefix of this IntelligenceHostConfigurationInfo.  # noqa: E501

        List of private IP prefix that NSX-Intelligence network flow is collected from.   # noqa: E501

        :return: The private_ip_prefix of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: list[IntelligenceFlowPrivateIpPrefixInfo]
        """
        return self._private_ip_prefix

    @private_ip_prefix.setter
    def private_ip_prefix(self, private_ip_prefix):
        """Sets the private_ip_prefix of this IntelligenceHostConfigurationInfo.

        List of private IP prefix that NSX-Intelligence network flow is collected from.   # noqa: E501

        :param private_ip_prefix: The private_ip_prefix of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: list[IntelligenceFlowPrivateIpPrefixInfo]
        """

        self._private_ip_prefix = private_ip_prefix

    @property
    def broker_bootstrap_servers(self):
        """Gets the broker_bootstrap_servers of this IntelligenceHostConfigurationInfo.  # noqa: E501

        List of NSX-Intelligence broker endpoints that host nodes contact initially.   # noqa: E501

        :return: The broker_bootstrap_servers of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: list[IntelligenceBrokerEndpointInfo]
        """
        return self._broker_bootstrap_servers

    @broker_bootstrap_servers.setter
    def broker_bootstrap_servers(self, broker_bootstrap_servers):
        """Sets the broker_bootstrap_servers of this IntelligenceHostConfigurationInfo.

        List of NSX-Intelligence broker endpoints that host nodes contact initially.   # noqa: E501

        :param broker_bootstrap_servers: The broker_bootstrap_servers of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: list[IntelligenceBrokerEndpointInfo]
        """

        self._broker_bootstrap_servers = broker_bootstrap_servers

    @property
    def max_inactive_flow_count(self):
        """Gets the max_inactive_flow_count of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Maximum inactive network flow to collect in collection interval.   # noqa: E501

        :return: The max_inactive_flow_count of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_inactive_flow_count

    @max_inactive_flow_count.setter
    def max_inactive_flow_count(self, max_inactive_flow_count):
        """Sets the max_inactive_flow_count of this IntelligenceHostConfigurationInfo.

        Maximum inactive network flow to collect in collection interval.   # noqa: E501

        :param max_inactive_flow_count: The max_inactive_flow_count of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: int
        """

        self._max_inactive_flow_count = max_inactive_flow_count

    @property
    def context_user_sids(self):
        """Gets the context_user_sids of this IntelligenceHostConfigurationInfo.  # noqa: E501

        List of windows user sid to collect context data. Empty implies all users.   # noqa: E501

        :return: The context_user_sids of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._context_user_sids

    @context_user_sids.setter
    def context_user_sids(self, context_user_sids):
        """Sets the context_user_sids of this IntelligenceHostConfigurationInfo.

        List of windows user sid to collect context data. Empty implies all users.   # noqa: E501

        :param context_user_sids: The context_user_sids of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: list[str]
        """

        self._context_user_sids = context_user_sids

    @property
    def flow_data_collection_interval(self):
        """Gets the flow_data_collection_interval of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Interval in minute of reporting network flow data to NSX-Intelligence.   # noqa: E501

        :return: The flow_data_collection_interval of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: int
        """
        return self._flow_data_collection_interval

    @flow_data_collection_interval.setter
    def flow_data_collection_interval(self, flow_data_collection_interval):
        """Sets the flow_data_collection_interval of this IntelligenceHostConfigurationInfo.

        Interval in minute of reporting network flow data to NSX-Intelligence.   # noqa: E501

        :param flow_data_collection_interval: The flow_data_collection_interval of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: int
        """

        self._flow_data_collection_interval = flow_data_collection_interval

    @property
    def max_active_flow_count(self):
        """Gets the max_active_flow_count of this IntelligenceHostConfigurationInfo.  # noqa: E501

        Maximum active network flow to collect in collection interval.   # noqa: E501

        :return: The max_active_flow_count of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_active_flow_count

    @max_active_flow_count.setter
    def max_active_flow_count(self, max_active_flow_count):
        """Sets the max_active_flow_count of this IntelligenceHostConfigurationInfo.

        Maximum active network flow to collect in collection interval.   # noqa: E501

        :param max_active_flow_count: The max_active_flow_count of this IntelligenceHostConfigurationInfo.  # noqa: E501
        :type: int
        """

        self._max_active_flow_count = max_active_flow_count

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
        if issubclass(IntelligenceHostConfigurationInfo, dict):
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
        if not isinstance(other, IntelligenceHostConfigurationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
