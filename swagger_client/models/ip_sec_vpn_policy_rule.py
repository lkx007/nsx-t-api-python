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


class IPSecVPNPolicyRule(object):
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
        'owner': 'OwnerResourceLink',
        'display_name': 'str',
        'id': 'str',
        'resource_type': 'str',
        'description': 'str',
        'sources': 'list[IPSecVPNPolicySubnet]',
        'action': 'str',
        'enabled': 'bool',
        'logged': 'bool',
        'destinations': 'list[IPSecVPNPolicySubnet]'
    }
    if hasattr(EmbeddedResource, "swagger_types"):
        swagger_types.update(EmbeddedResource.swagger_types)

    attribute_map = {
        'owner': '_owner',
        'display_name': 'display_name',
        'id': 'id',
        'resource_type': 'resource_type',
        'description': 'description',
        'sources': 'sources',
        'action': 'action',
        'enabled': 'enabled',
        'logged': 'logged',
        'destinations': 'destinations'
    }
    if hasattr(EmbeddedResource, "attribute_map"):
        attribute_map.update(EmbeddedResource.attribute_map)

    def __init__(self, owner=None, display_name=None, id=None, resource_type=None, description=None, sources=None, action='PROTECT', enabled=True, logged=False, destinations=None, *args, **kwargs):  # noqa: E501
        """IPSecVPNPolicyRule - a model defined in Swagger"""  # noqa: E501
        self._owner = None
        self._display_name = None
        self._id = None
        self._resource_type = None
        self._description = None
        self._sources = None
        self._action = None
        self._enabled = None
        self._logged = None
        self._destinations = None
        self.discriminator = None
        if owner is not None:
            self.owner = owner
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        if description is not None:
            self.description = description
        if sources is not None:
            self.sources = sources
        if action is not None:
            self.action = action
        if enabled is not None:
            self.enabled = enabled
        if logged is not None:
            self.logged = logged
        if destinations is not None:
            self.destinations = destinations
        EmbeddedResource.__init__(self, *args, **kwargs)

    @property
    def owner(self):
        """Gets the owner of this IPSecVPNPolicyRule.  # noqa: E501


        :return: The owner of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: OwnerResourceLink
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this IPSecVPNPolicyRule.


        :param owner: The owner of this IPSecVPNPolicyRule.  # noqa: E501
        :type: OwnerResourceLink
        """

        self._owner = owner

    @property
    def display_name(self):
        """Gets the display_name of this IPSecVPNPolicyRule.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IPSecVPNPolicyRule.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this IPSecVPNPolicyRule.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this IPSecVPNPolicyRule.  # noqa: E501

        Unique policy id.  # noqa: E501

        :return: The id of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IPSecVPNPolicyRule.

        Unique policy id.  # noqa: E501

        :param id: The id of this IPSecVPNPolicyRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this IPSecVPNPolicyRule.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this IPSecVPNPolicyRule.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this IPSecVPNPolicyRule.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def description(self):
        """Gets the description of this IPSecVPNPolicyRule.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IPSecVPNPolicyRule.

        Description of this resource  # noqa: E501

        :param description: The description of this IPSecVPNPolicyRule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def sources(self):
        """Gets the sources of this IPSecVPNPolicyRule.  # noqa: E501

        List of local subnets.  # noqa: E501

        :return: The sources of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: list[IPSecVPNPolicySubnet]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this IPSecVPNPolicyRule.

        List of local subnets.  # noqa: E501

        :param sources: The sources of this IPSecVPNPolicyRule.  # noqa: E501
        :type: list[IPSecVPNPolicySubnet]
        """

        self._sources = sources

    @property
    def action(self):
        """Gets the action of this IPSecVPNPolicyRule.  # noqa: E501

        PROTECT - Protect rules are defined per policy based IPSec VPN session. BYPASS - Bypass rules are defined per IPSec VPN service and affects all policy based IPSec VPN sessions. Bypass rules are prioritized over protect rules.   # noqa: E501

        :return: The action of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IPSecVPNPolicyRule.

        PROTECT - Protect rules are defined per policy based IPSec VPN session. BYPASS - Bypass rules are defined per IPSec VPN service and affects all policy based IPSec VPN sessions. Bypass rules are prioritized over protect rules.   # noqa: E501

        :param action: The action of this IPSecVPNPolicyRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["PROTECT", "BYPASS"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def enabled(self):
        """Gets the enabled of this IPSecVPNPolicyRule.  # noqa: E501

        A flag to enable/disable the policy rule.  # noqa: E501

        :return: The enabled of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IPSecVPNPolicyRule.

        A flag to enable/disable the policy rule.  # noqa: E501

        :param enabled: The enabled of this IPSecVPNPolicyRule.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def logged(self):
        """Gets the logged of this IPSecVPNPolicyRule.  # noqa: E501

        A flag to enable/disable the logging for the policy rule.  # noqa: E501

        :return: The logged of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: bool
        """
        return self._logged

    @logged.setter
    def logged(self, logged):
        """Sets the logged of this IPSecVPNPolicyRule.

        A flag to enable/disable the logging for the policy rule.  # noqa: E501

        :param logged: The logged of this IPSecVPNPolicyRule.  # noqa: E501
        :type: bool
        """

        self._logged = logged

    @property
    def destinations(self):
        """Gets the destinations of this IPSecVPNPolicyRule.  # noqa: E501

        List of peer subnets.  # noqa: E501

        :return: The destinations of this IPSecVPNPolicyRule.  # noqa: E501
        :rtype: list[IPSecVPNPolicySubnet]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this IPSecVPNPolicyRule.

        List of peer subnets.  # noqa: E501

        :param destinations: The destinations of this IPSecVPNPolicyRule.  # noqa: E501
        :type: list[IPSecVPNPolicySubnet]
        """

        self._destinations = destinations

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
        if issubclass(IPSecVPNPolicyRule, dict):
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
        if not isinstance(other, IPSecVPNPolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
