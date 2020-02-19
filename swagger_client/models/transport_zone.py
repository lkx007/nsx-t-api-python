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


class TransportZone(object):
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
        'is_default': 'bool',
        'transport_type': 'str',
        'host_switch_id': 'str',
        'host_switch_name': 'str',
        'host_switch_mode': 'str',
        'nested_nsx': 'bool',
        'uplink_teaming_policy_names': 'list[str]',
        'transport_zone_profile_ids': 'list[TransportZoneProfileTypeIdEntry]'
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
        'is_default': 'is_default',
        'transport_type': 'transport_type',
        'host_switch_id': 'host_switch_id',
        'host_switch_name': 'host_switch_name',
        'host_switch_mode': 'host_switch_mode',
        'nested_nsx': 'nested_nsx',
        'uplink_teaming_policy_names': 'uplink_teaming_policy_names',
        'transport_zone_profile_ids': 'transport_zone_profile_ids'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, is_default=False, transport_type=None, host_switch_id=None, host_switch_name='nsxDefaultHostSwitch', host_switch_mode='STANDARD', nested_nsx=False, uplink_teaming_policy_names=None, transport_zone_profile_ids=None, *args, **kwargs):  # noqa: E501
        """TransportZone - a model defined in Swagger"""  # noqa: E501
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
        self._is_default = None
        self._transport_type = None
        self._host_switch_id = None
        self._host_switch_name = None
        self._host_switch_mode = None
        self._nested_nsx = None
        self._uplink_teaming_policy_names = None
        self._transport_zone_profile_ids = None
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
        if is_default is not None:
            self.is_default = is_default
        self.transport_type = transport_type
        if host_switch_id is not None:
            self.host_switch_id = host_switch_id
        if host_switch_name is not None:
            self.host_switch_name = host_switch_name
        if host_switch_mode is not None:
            self.host_switch_mode = host_switch_mode
        if nested_nsx is not None:
            self.nested_nsx = nested_nsx
        if uplink_teaming_policy_names is not None:
            self.uplink_teaming_policy_names = uplink_teaming_policy_names
        if transport_zone_profile_ids is not None:
            self.transport_zone_profile_ids = transport_zone_profile_ids
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this TransportZone.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this TransportZone.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this TransportZone.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this TransportZone.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this TransportZone.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TransportZone.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this TransportZone.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this TransportZone.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransportZone.

        Description of this resource  # noqa: E501

        :param description: The description of this TransportZone.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this TransportZone.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this TransportZone.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TransportZone.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this TransportZone.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this TransportZone.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this TransportZone.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this TransportZone.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this TransportZone.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this TransportZone.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this TransportZone.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this TransportZone.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this TransportZone.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TransportZone.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this TransportZone.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this TransportZone.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this TransportZone.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this TransportZone.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this TransportZone.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this TransportZone.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this TransportZone.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this TransportZone.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this TransportZone.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransportZone.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this TransportZone.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this TransportZone.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TransportZone.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this TransportZone.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def is_default(self):
        """Gets the is_default of this TransportZone.  # noqa: E501

        Only one transport zone can be the default one for a given transport zone type. APIs that need transport zone can choose to use the default transport zone if a transport zone is not given by the user.  # noqa: E501

        :return: The is_default of this TransportZone.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this TransportZone.

        Only one transport zone can be the default one for a given transport zone type. APIs that need transport zone can choose to use the default transport zone if a transport zone is not given by the user.  # noqa: E501

        :param is_default: The is_default of this TransportZone.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def transport_type(self):
        """Gets the transport_type of this TransportZone.  # noqa: E501

        The transport type of this transport zone.  # noqa: E501

        :return: The transport_type of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """Sets the transport_type of this TransportZone.

        The transport type of this transport zone.  # noqa: E501

        :param transport_type: The transport_type of this TransportZone.  # noqa: E501
        :type: str
        """
        if transport_type is None:
            raise ValueError("Invalid value for `transport_type`, must not be `None`")  # noqa: E501
        allowed_values = ["OVERLAY", "VLAN"]  # noqa: E501
        if transport_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transport_type, allowed_values)
            )

        self._transport_type = transport_type

    @property
    def host_switch_id(self):
        """Gets the host_switch_id of this TransportZone.  # noqa: E501

        the host switch id generated by the system.  # noqa: E501

        :return: The host_switch_id of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._host_switch_id

    @host_switch_id.setter
    def host_switch_id(self, host_switch_id):
        """Sets the host_switch_id of this TransportZone.

        the host switch id generated by the system.  # noqa: E501

        :param host_switch_id: The host_switch_id of this TransportZone.  # noqa: E501
        :type: str
        """

        self._host_switch_id = host_switch_id

    @property
    def host_switch_name(self):
        """Gets the host_switch_name of this TransportZone.  # noqa: E501

        If this name is unset or empty then the default host switch name will be used.  # noqa: E501

        :return: The host_switch_name of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._host_switch_name

    @host_switch_name.setter
    def host_switch_name(self, host_switch_name):
        """Sets the host_switch_name of this TransportZone.

        If this name is unset or empty then the default host switch name will be used.  # noqa: E501

        :param host_switch_name: The host_switch_name of this TransportZone.  # noqa: E501
        :type: str
        """

        self._host_switch_name = host_switch_name

    @property
    def host_switch_mode(self):
        """Gets the host_switch_mode of this TransportZone.  # noqa: E501

        STANDARD mode applies to all the hypervisors. ENS mode stands for Enhanced Networking Stack. This feature is only available for ESX hypervisor. It is not available on KVM, EDGE and Public Cloud Gateway etc. When a Transport Zone mode is set to ENS, only Transport Nodes of type ESX can participate in such a Transport Zone.  # noqa: E501

        :return: The host_switch_mode of this TransportZone.  # noqa: E501
        :rtype: str
        """
        return self._host_switch_mode

    @host_switch_mode.setter
    def host_switch_mode(self, host_switch_mode):
        """Sets the host_switch_mode of this TransportZone.

        STANDARD mode applies to all the hypervisors. ENS mode stands for Enhanced Networking Stack. This feature is only available for ESX hypervisor. It is not available on KVM, EDGE and Public Cloud Gateway etc. When a Transport Zone mode is set to ENS, only Transport Nodes of type ESX can participate in such a Transport Zone.  # noqa: E501

        :param host_switch_mode: The host_switch_mode of this TransportZone.  # noqa: E501
        :type: str
        """
        allowed_values = ["STANDARD", "ENS"]  # noqa: E501
        if host_switch_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `host_switch_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(host_switch_mode, allowed_values)
            )

        self._host_switch_mode = host_switch_mode

    @property
    def nested_nsx(self):
        """Gets the nested_nsx of this TransportZone.  # noqa: E501

        The flag only need to be set in nested NSX environment.  # noqa: E501

        :return: The nested_nsx of this TransportZone.  # noqa: E501
        :rtype: bool
        """
        return self._nested_nsx

    @nested_nsx.setter
    def nested_nsx(self, nested_nsx):
        """Sets the nested_nsx of this TransportZone.

        The flag only need to be set in nested NSX environment.  # noqa: E501

        :param nested_nsx: The nested_nsx of this TransportZone.  # noqa: E501
        :type: bool
        """

        self._nested_nsx = nested_nsx

    @property
    def uplink_teaming_policy_names(self):
        """Gets the uplink_teaming_policy_names of this TransportZone.  # noqa: E501

        The names of switching uplink teaming policies that all transport nodes in this transport zone must support. An exception will be thrown if a transport node within the transport zone does not support a named teaming policy. The user will need to first ensure all trasnport nodes support the desired named teaming policy before assigning it to the transport zone. If the field is not specified, the host switch's default teaming policy will be used.  # noqa: E501

        :return: The uplink_teaming_policy_names of this TransportZone.  # noqa: E501
        :rtype: list[str]
        """
        return self._uplink_teaming_policy_names

    @uplink_teaming_policy_names.setter
    def uplink_teaming_policy_names(self, uplink_teaming_policy_names):
        """Sets the uplink_teaming_policy_names of this TransportZone.

        The names of switching uplink teaming policies that all transport nodes in this transport zone must support. An exception will be thrown if a transport node within the transport zone does not support a named teaming policy. The user will need to first ensure all trasnport nodes support the desired named teaming policy before assigning it to the transport zone. If the field is not specified, the host switch's default teaming policy will be used.  # noqa: E501

        :param uplink_teaming_policy_names: The uplink_teaming_policy_names of this TransportZone.  # noqa: E501
        :type: list[str]
        """

        self._uplink_teaming_policy_names = uplink_teaming_policy_names

    @property
    def transport_zone_profile_ids(self):
        """Gets the transport_zone_profile_ids of this TransportZone.  # noqa: E501

        Identifiers of the transport zone profiles associated with this TransportZone.  # noqa: E501

        :return: The transport_zone_profile_ids of this TransportZone.  # noqa: E501
        :rtype: list[TransportZoneProfileTypeIdEntry]
        """
        return self._transport_zone_profile_ids

    @transport_zone_profile_ids.setter
    def transport_zone_profile_ids(self, transport_zone_profile_ids):
        """Sets the transport_zone_profile_ids of this TransportZone.

        Identifiers of the transport zone profiles associated with this TransportZone.  # noqa: E501

        :param transport_zone_profile_ids: The transport_zone_profile_ids of this TransportZone.  # noqa: E501
        :type: list[TransportZoneProfileTypeIdEntry]
        """

        self._transport_zone_profile_ids = transport_zone_profile_ids

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
        if issubclass(TransportZone, dict):
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
        if not isinstance(other, TransportZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
