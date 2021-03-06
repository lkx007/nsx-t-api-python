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


class BgpConfig(object):
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
        'inter_sr_ibgp': 'InterSRRoutingConfig',
        'as_number': 'int',
        'route_aggregation': 'list[BgpRouteAggregation]',
        'logical_router_id': 'str',
        'graceful_restart': 'bool',
        'as_num': 'str',
        'enabled': 'bool',
        'graceful_restart_config': 'GracefulRestartConfig',
        'multipath_relax': 'bool',
        'ecmp': 'bool'
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
        'inter_sr_ibgp': 'inter_sr_ibgp',
        'as_number': 'as_number',
        'route_aggregation': 'route_aggregation',
        'logical_router_id': 'logical_router_id',
        'graceful_restart': 'graceful_restart',
        'as_num': 'as_num',
        'enabled': 'enabled',
        'graceful_restart_config': 'graceful_restart_config',
        'multipath_relax': 'multipath_relax',
        'ecmp': 'ecmp'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, inter_sr_ibgp=None, as_number=None, route_aggregation=None, logical_router_id=None, graceful_restart=None, as_num=None, enabled=False, graceful_restart_config=None, multipath_relax=True, ecmp=True, *args, **kwargs):  # noqa: E501
        """BgpConfig - a model defined in Swagger"""  # noqa: E501
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
        self._inter_sr_ibgp = None
        self._as_number = None
        self._route_aggregation = None
        self._logical_router_id = None
        self._graceful_restart = None
        self._as_num = None
        self._enabled = None
        self._graceful_restart_config = None
        self._multipath_relax = None
        self._ecmp = None
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
        if inter_sr_ibgp is not None:
            self.inter_sr_ibgp = inter_sr_ibgp
        if as_number is not None:
            self.as_number = as_number
        if route_aggregation is not None:
            self.route_aggregation = route_aggregation
        if logical_router_id is not None:
            self.logical_router_id = logical_router_id
        if graceful_restart is not None:
            self.graceful_restart = graceful_restart
        if as_num is not None:
            self.as_num = as_num
        if enabled is not None:
            self.enabled = enabled
        if graceful_restart_config is not None:
            self.graceful_restart_config = graceful_restart_config
        if multipath_relax is not None:
            self.multipath_relax = multipath_relax
        if ecmp is not None:
            self.ecmp = ecmp
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this BgpConfig.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this BgpConfig.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this BgpConfig.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this BgpConfig.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this BgpConfig.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BgpConfig.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this BgpConfig.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this BgpConfig.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BgpConfig.

        Description of this resource  # noqa: E501

        :param description: The description of this BgpConfig.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this BgpConfig.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this BgpConfig.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BgpConfig.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this BgpConfig.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this BgpConfig.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this BgpConfig.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this BgpConfig.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this BgpConfig.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this BgpConfig.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this BgpConfig.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this BgpConfig.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this BgpConfig.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BgpConfig.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this BgpConfig.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this BgpConfig.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this BgpConfig.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this BgpConfig.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this BgpConfig.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this BgpConfig.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this BgpConfig.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this BgpConfig.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this BgpConfig.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BgpConfig.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this BgpConfig.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this BgpConfig.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BgpConfig.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this BgpConfig.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def inter_sr_ibgp(self):
        """Gets the inter_sr_ibgp of this BgpConfig.  # noqa: E501


        :return: The inter_sr_ibgp of this BgpConfig.  # noqa: E501
        :rtype: InterSRRoutingConfig
        """
        return self._inter_sr_ibgp

    @inter_sr_ibgp.setter
    def inter_sr_ibgp(self, inter_sr_ibgp):
        """Sets the inter_sr_ibgp of this BgpConfig.


        :param inter_sr_ibgp: The inter_sr_ibgp of this BgpConfig.  # noqa: E501
        :type: InterSRRoutingConfig
        """

        self._inter_sr_ibgp = inter_sr_ibgp

    @property
    def as_number(self):
        """Gets the as_number of this BgpConfig.  # noqa: E501

        This is a deprecated property, Please use 'as_num' instead.  # noqa: E501

        :return: The as_number of this BgpConfig.  # noqa: E501
        :rtype: int
        """
        return self._as_number

    @as_number.setter
    def as_number(self, as_number):
        """Sets the as_number of this BgpConfig.

        This is a deprecated property, Please use 'as_num' instead.  # noqa: E501

        :param as_number: The as_number of this BgpConfig.  # noqa: E501
        :type: int
        """

        self._as_number = as_number

    @property
    def route_aggregation(self):
        """Gets the route_aggregation of this BgpConfig.  # noqa: E501

        List of routes to be aggregated  # noqa: E501

        :return: The route_aggregation of this BgpConfig.  # noqa: E501
        :rtype: list[BgpRouteAggregation]
        """
        return self._route_aggregation

    @route_aggregation.setter
    def route_aggregation(self, route_aggregation):
        """Sets the route_aggregation of this BgpConfig.

        List of routes to be aggregated  # noqa: E501

        :param route_aggregation: The route_aggregation of this BgpConfig.  # noqa: E501
        :type: list[BgpRouteAggregation]
        """

        self._route_aggregation = route_aggregation

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this BgpConfig.  # noqa: E501

        Logical router id  # noqa: E501

        :return: The logical_router_id of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this BgpConfig.

        Logical router id  # noqa: E501

        :param logical_router_id: The logical_router_id of this BgpConfig.  # noqa: E501
        :type: str
        """

        self._logical_router_id = logical_router_id

    @property
    def graceful_restart(self):
        """Gets the graceful_restart of this BgpConfig.  # noqa: E501

        Flag to enable graceful restart. This field is deprecated, kindly use graceful_restart_config parameter for graceful restart configuration. If both parameters are set and consistent with each other [i.e. graceful_restart=false and graceful_restart_mode=HELPER_ONLY OR graceful_restart=true and graceful_restart_mode=GR_AND_HELPER] then this is allowed, but if inconsistent with each other then this is not allowed and validation error will be thrown.   # noqa: E501

        :return: The graceful_restart of this BgpConfig.  # noqa: E501
        :rtype: bool
        """
        return self._graceful_restart

    @graceful_restart.setter
    def graceful_restart(self, graceful_restart):
        """Sets the graceful_restart of this BgpConfig.

        Flag to enable graceful restart. This field is deprecated, kindly use graceful_restart_config parameter for graceful restart configuration. If both parameters are set and consistent with each other [i.e. graceful_restart=false and graceful_restart_mode=HELPER_ONLY OR graceful_restart=true and graceful_restart_mode=GR_AND_HELPER] then this is allowed, but if inconsistent with each other then this is not allowed and validation error will be thrown.   # noqa: E501

        :param graceful_restart: The graceful_restart of this BgpConfig.  # noqa: E501
        :type: bool
        """

        self._graceful_restart = graceful_restart

    @property
    def as_num(self):
        """Gets the as_num of this BgpConfig.  # noqa: E501

        4 Byte ASN in ASPLAIN/ASDOT Format  # noqa: E501

        :return: The as_num of this BgpConfig.  # noqa: E501
        :rtype: str
        """
        return self._as_num

    @as_num.setter
    def as_num(self, as_num):
        """Sets the as_num of this BgpConfig.

        4 Byte ASN in ASPLAIN/ASDOT Format  # noqa: E501

        :param as_num: The as_num of this BgpConfig.  # noqa: E501
        :type: str
        """

        self._as_num = as_num

    @property
    def enabled(self):
        """Gets the enabled of this BgpConfig.  # noqa: E501

        While creation of BGP config this flag will be set to - true for Tier0 logical router with Active-Active high-availability mode - false for Tier0 logical router with Active-Standby high-availanility mode. User can change this value while updating the config. If this property is not specified in the payload, the default value will be considered as false irrespective of the high-availability mode.   # noqa: E501

        :return: The enabled of this BgpConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this BgpConfig.

        While creation of BGP config this flag will be set to - true for Tier0 logical router with Active-Active high-availability mode - false for Tier0 logical router with Active-Standby high-availanility mode. User can change this value while updating the config. If this property is not specified in the payload, the default value will be considered as false irrespective of the high-availability mode.   # noqa: E501

        :param enabled: The enabled of this BgpConfig.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def graceful_restart_config(self):
        """Gets the graceful_restart_config of this BgpConfig.  # noqa: E501


        :return: The graceful_restart_config of this BgpConfig.  # noqa: E501
        :rtype: GracefulRestartConfig
        """
        return self._graceful_restart_config

    @graceful_restart_config.setter
    def graceful_restart_config(self, graceful_restart_config):
        """Sets the graceful_restart_config of this BgpConfig.


        :param graceful_restart_config: The graceful_restart_config of this BgpConfig.  # noqa: E501
        :type: GracefulRestartConfig
        """

        self._graceful_restart_config = graceful_restart_config

    @property
    def multipath_relax(self):
        """Gets the multipath_relax of this BgpConfig.  # noqa: E501

        Flag to enable BGP multipath relax option  # noqa: E501

        :return: The multipath_relax of this BgpConfig.  # noqa: E501
        :rtype: bool
        """
        return self._multipath_relax

    @multipath_relax.setter
    def multipath_relax(self, multipath_relax):
        """Sets the multipath_relax of this BgpConfig.

        Flag to enable BGP multipath relax option  # noqa: E501

        :param multipath_relax: The multipath_relax of this BgpConfig.  # noqa: E501
        :type: bool
        """

        self._multipath_relax = multipath_relax

    @property
    def ecmp(self):
        """Gets the ecmp of this BgpConfig.  # noqa: E501

        While creation of BGP config this flag will be set to - true for Tier0 logical router with Active-Active high-availability mode - false for Tier0 logical router with Active-Standby high-availability mode. User can change this value while updating BGP config. If this property is not specified in the payload, the default value will be considered as true irrespective of the high-availability mode.   # noqa: E501

        :return: The ecmp of this BgpConfig.  # noqa: E501
        :rtype: bool
        """
        return self._ecmp

    @ecmp.setter
    def ecmp(self, ecmp):
        """Sets the ecmp of this BgpConfig.

        While creation of BGP config this flag will be set to - true for Tier0 logical router with Active-Active high-availability mode - false for Tier0 logical router with Active-Standby high-availability mode. User can change this value while updating BGP config. If this property is not specified in the payload, the default value will be considered as true irrespective of the high-availability mode.   # noqa: E501

        :param ecmp: The ecmp of this BgpConfig.  # noqa: E501
        :type: bool
        """

        self._ecmp = ecmp

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
        if issubclass(BgpConfig, dict):
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
        if not isinstance(other, BgpConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
