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


class PBRRule(object):
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
        'disabled': 'bool',
        'sources': 'list[ResourceReference]',
        'rule_tag': 'str',
        'services': 'list[PBRService]',
        'notes': 'str',
        'applied_tos': 'list[ResourceReference]',
        'logged': 'bool',
        'action': 'str',
        'destinations': 'list[ResourceReference]'
    }
    if hasattr(EmbeddedResource, "swagger_types"):
        swagger_types.update(EmbeddedResource.swagger_types)

    attribute_map = {
        'owner': '_owner',
        'display_name': 'display_name',
        'id': 'id',
        'resource_type': 'resource_type',
        'description': 'description',
        'disabled': 'disabled',
        'sources': 'sources',
        'rule_tag': 'rule_tag',
        'services': 'services',
        'notes': 'notes',
        'applied_tos': 'applied_tos',
        'logged': 'logged',
        'action': 'action',
        'destinations': 'destinations'
    }
    if hasattr(EmbeddedResource, "attribute_map"):
        attribute_map.update(EmbeddedResource.attribute_map)

    def __init__(self, owner=None, display_name=None, id=None, resource_type=None, description=None, disabled=False, sources=None, rule_tag=None, services=None, notes=None, applied_tos=None, logged=False, action=None, destinations=None, *args, **kwargs):  # noqa: E501
        """PBRRule - a model defined in Swagger"""  # noqa: E501
        self._owner = None
        self._display_name = None
        self._id = None
        self._resource_type = None
        self._description = None
        self._disabled = None
        self._sources = None
        self._rule_tag = None
        self._services = None
        self._notes = None
        self._applied_tos = None
        self._logged = None
        self._action = None
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
        if disabled is not None:
            self.disabled = disabled
        if sources is not None:
            self.sources = sources
        if rule_tag is not None:
            self.rule_tag = rule_tag
        if services is not None:
            self.services = services
        if notes is not None:
            self.notes = notes
        if applied_tos is not None:
            self.applied_tos = applied_tos
        if logged is not None:
            self.logged = logged
        self.action = action
        if destinations is not None:
            self.destinations = destinations
        EmbeddedResource.__init__(self, *args, **kwargs)

    @property
    def owner(self):
        """Gets the owner of this PBRRule.  # noqa: E501


        :return: The owner of this PBRRule.  # noqa: E501
        :rtype: OwnerResourceLink
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this PBRRule.


        :param owner: The owner of this PBRRule.  # noqa: E501
        :type: OwnerResourceLink
        """

        self._owner = owner

    @property
    def display_name(self):
        """Gets the display_name of this PBRRule.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this PBRRule.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PBRRule.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this PBRRule.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this PBRRule.  # noqa: E501

        Identifier of the resource  # noqa: E501

        :return: The id of this PBRRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PBRRule.

        Identifier of the resource  # noqa: E501

        :param id: The id of this PBRRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this PBRRule.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this PBRRule.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PBRRule.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this PBRRule.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def description(self):
        """Gets the description of this PBRRule.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this PBRRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PBRRule.

        Description of this resource  # noqa: E501

        :param description: The description of this PBRRule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disabled(self):
        """Gets the disabled of this PBRRule.  # noqa: E501

        Flag to disable rule. Disabled will only be persisted but never provisioned/realized.  # noqa: E501

        :return: The disabled of this PBRRule.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this PBRRule.

        Flag to disable rule. Disabled will only be persisted but never provisioned/realized.  # noqa: E501

        :param disabled: The disabled of this PBRRule.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def sources(self):
        """Gets the sources of this PBRRule.  # noqa: E501

        List of sources. Null will be treated as any.  # noqa: E501

        :return: The sources of this PBRRule.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this PBRRule.

        List of sources. Null will be treated as any.  # noqa: E501

        :param sources: The sources of this PBRRule.  # noqa: E501
        :type: list[ResourceReference]
        """

        self._sources = sources

    @property
    def rule_tag(self):
        """Gets the rule_tag of this PBRRule.  # noqa: E501

        User level field which will be printed in CLI and packet logs.  # noqa: E501

        :return: The rule_tag of this PBRRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_tag

    @rule_tag.setter
    def rule_tag(self, rule_tag):
        """Sets the rule_tag of this PBRRule.

        User level field which will be printed in CLI and packet logs.  # noqa: E501

        :param rule_tag: The rule_tag of this PBRRule.  # noqa: E501
        :type: str
        """

        self._rule_tag = rule_tag

    @property
    def services(self):
        """Gets the services of this PBRRule.  # noqa: E501

        List of the services. Null will be treated as any.  # noqa: E501

        :return: The services of this PBRRule.  # noqa: E501
        :rtype: list[PBRService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this PBRRule.

        List of the services. Null will be treated as any.  # noqa: E501

        :param services: The services of this PBRRule.  # noqa: E501
        :type: list[PBRService]
        """

        self._services = services

    @property
    def notes(self):
        """Gets the notes of this PBRRule.  # noqa: E501

        User notes specific to the rule.  # noqa: E501

        :return: The notes of this PBRRule.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PBRRule.

        User notes specific to the rule.  # noqa: E501

        :param notes: The notes of this PBRRule.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def applied_tos(self):
        """Gets the applied_tos of this PBRRule.  # noqa: E501

        List of object where rule will be enforced. field overrides this one. Null will be treated as any.  # noqa: E501

        :return: The applied_tos of this PBRRule.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._applied_tos

    @applied_tos.setter
    def applied_tos(self, applied_tos):
        """Sets the applied_tos of this PBRRule.

        List of object where rule will be enforced. field overrides this one. Null will be treated as any.  # noqa: E501

        :param applied_tos: The applied_tos of this PBRRule.  # noqa: E501
        :type: list[ResourceReference]
        """

        self._applied_tos = applied_tos

    @property
    def logged(self):
        """Gets the logged of this PBRRule.  # noqa: E501

        Flag to enable packet logging. Default is disabled.  # noqa: E501

        :return: The logged of this PBRRule.  # noqa: E501
        :rtype: bool
        """
        return self._logged

    @logged.setter
    def logged(self, logged):
        """Sets the logged of this PBRRule.

        Flag to enable packet logging. Default is disabled.  # noqa: E501

        :param logged: The logged of this PBRRule.  # noqa: E501
        :type: bool
        """

        self._logged = logged

    @property
    def action(self):
        """Gets the action of this PBRRule.  # noqa: E501

        Action enforced on the packets which matches the PBR rule.  # noqa: E501

        :return: The action of this PBRRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PBRRule.

        Action enforced on the packets which matches the PBR rule.  # noqa: E501

        :param action: The action of this PBRRule.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["ROUTE_TO_UNDERLAY_NAT", "ROUTE_TO_OVERLAY_NAT", "ROUTE_TO_UNDERLAY", "ROUTE_TO_OVERLAY", "ROUTE_FROM_OVERLAY", "ROUTE_FROM_UNDERLAY"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def destinations(self):
        """Gets the destinations of this PBRRule.  # noqa: E501

        List of the destinations. Null will be treated as any.  # noqa: E501

        :return: The destinations of this PBRRule.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this PBRRule.

        List of the destinations. Null will be treated as any.  # noqa: E501

        :param destinations: The destinations of this PBRRule.  # noqa: E501
        :type: list[ResourceReference]
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
        if issubclass(PBRRule, dict):
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
        if not isinstance(other, PBRRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
