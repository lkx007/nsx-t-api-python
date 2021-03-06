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


class FirewallSection(object):
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
        'stateful': 'bool',
        'is_default': 'bool',
        'applied_tos': 'list[ResourceReference]',
        'rule_count': 'int',
        'section_type': 'str',
        'priority': 'int',
        'enforced_on': 'str',
        'locked': 'bool',
        'tcp_strict': 'bool',
        'lock_modified_by': 'str',
        'lock_modified_time': 'int',
        'comments': 'str',
        'autoplumbed': 'bool'
    }
    if hasattr(DSSection, "swagger_types"):
        swagger_types.update(DSSection.swagger_types)

    attribute_map = {
        'stateful': 'stateful',
        'is_default': 'is_default',
        'applied_tos': 'applied_tos',
        'rule_count': 'rule_count',
        'section_type': 'section_type',
        'priority': 'priority',
        'enforced_on': 'enforced_on',
        'locked': 'locked',
        'tcp_strict': 'tcp_strict',
        'lock_modified_by': 'lock_modified_by',
        'lock_modified_time': 'lock_modified_time',
        'comments': 'comments',
        'autoplumbed': 'autoplumbed'
    }
    if hasattr(DSSection, "attribute_map"):
        attribute_map.update(DSSection.attribute_map)

    def __init__(self, stateful=None, is_default=None, applied_tos=None, rule_count=None, section_type=None, priority=None, enforced_on=None, locked=False, tcp_strict=False, lock_modified_by=None, lock_modified_time=None, comments=None, autoplumbed=False, *args, **kwargs):  # noqa: E501
        """FirewallSection - a model defined in Swagger"""  # noqa: E501
        self._stateful = None
        self._is_default = None
        self._applied_tos = None
        self._rule_count = None
        self._section_type = None
        self._priority = None
        self._enforced_on = None
        self._locked = None
        self._tcp_strict = None
        self._lock_modified_by = None
        self._lock_modified_time = None
        self._comments = None
        self._autoplumbed = None
        self.discriminator = None
        self.stateful = stateful
        if is_default is not None:
            self.is_default = is_default
        if applied_tos is not None:
            self.applied_tos = applied_tos
        if rule_count is not None:
            self.rule_count = rule_count
        self.section_type = section_type
        if priority is not None:
            self.priority = priority
        if enforced_on is not None:
            self.enforced_on = enforced_on
        if locked is not None:
            self.locked = locked
        if tcp_strict is not None:
            self.tcp_strict = tcp_strict
        if lock_modified_by is not None:
            self.lock_modified_by = lock_modified_by
        if lock_modified_time is not None:
            self.lock_modified_time = lock_modified_time
        if comments is not None:
            self.comments = comments
        if autoplumbed is not None:
            self.autoplumbed = autoplumbed
        DSSection.__init__(self, *args, **kwargs)

    @property
    def stateful(self):
        """Gets the stateful of this FirewallSection.  # noqa: E501

        Stateful or Stateless nature of distributed service section is enforced on all rules inside the section. Layer3 sections can be stateful or stateless. Layer2 sections can only be stateless.  # noqa: E501

        :return: The stateful of this FirewallSection.  # noqa: E501
        :rtype: bool
        """
        return self._stateful

    @stateful.setter
    def stateful(self, stateful):
        """Sets the stateful of this FirewallSection.

        Stateful or Stateless nature of distributed service section is enforced on all rules inside the section. Layer3 sections can be stateful or stateless. Layer2 sections can only be stateless.  # noqa: E501

        :param stateful: The stateful of this FirewallSection.  # noqa: E501
        :type: bool
        """
        if stateful is None:
            raise ValueError("Invalid value for `stateful`, must not be `None`")  # noqa: E501

        self._stateful = stateful

    @property
    def is_default(self):
        """Gets the is_default of this FirewallSection.  # noqa: E501

        It is a boolean flag which reflects whether a distributed service section is default section or not. Each Layer 3 and Layer 2 section will have at least and at most one default section.  # noqa: E501

        :return: The is_default of this FirewallSection.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this FirewallSection.

        It is a boolean flag which reflects whether a distributed service section is default section or not. Each Layer 3 and Layer 2 section will have at least and at most one default section.  # noqa: E501

        :param is_default: The is_default of this FirewallSection.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def applied_tos(self):
        """Gets the applied_tos of this FirewallSection.  # noqa: E501

        List of objects where the rules in this section will be enforced. This will take precedence over rule level appliedTo.  # noqa: E501

        :return: The applied_tos of this FirewallSection.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._applied_tos

    @applied_tos.setter
    def applied_tos(self, applied_tos):
        """Sets the applied_tos of this FirewallSection.

        List of objects where the rules in this section will be enforced. This will take precedence over rule level appliedTo.  # noqa: E501

        :param applied_tos: The applied_tos of this FirewallSection.  # noqa: E501
        :type: list[ResourceReference]
        """

        self._applied_tos = applied_tos

    @property
    def rule_count(self):
        """Gets the rule_count of this FirewallSection.  # noqa: E501

        Number of rules in this section.  # noqa: E501

        :return: The rule_count of this FirewallSection.  # noqa: E501
        :rtype: int
        """
        return self._rule_count

    @rule_count.setter
    def rule_count(self, rule_count):
        """Sets the rule_count of this FirewallSection.

        Number of rules in this section.  # noqa: E501

        :param rule_count: The rule_count of this FirewallSection.  # noqa: E501
        :type: int
        """

        self._rule_count = rule_count

    @property
    def section_type(self):
        """Gets the section_type of this FirewallSection.  # noqa: E501

        Type of the rules which a section can contain. Only homogeneous sections are supported.  # noqa: E501

        :return: The section_type of this FirewallSection.  # noqa: E501
        :rtype: str
        """
        return self._section_type

    @section_type.setter
    def section_type(self, section_type):
        """Sets the section_type of this FirewallSection.

        Type of the rules which a section can contain. Only homogeneous sections are supported.  # noqa: E501

        :param section_type: The section_type of this FirewallSection.  # noqa: E501
        :type: str
        """
        if section_type is None:
            raise ValueError("Invalid value for `section_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LAYER2", "LAYER3", "L3REDIRECT"]  # noqa: E501
        if section_type not in allowed_values:
            raise ValueError(
                "Invalid value for `section_type` ({0}), must be one of {1}"  # noqa: E501
                .format(section_type, allowed_values)
            )

        self._section_type = section_type

    @property
    def priority(self):
        """Gets the priority of this FirewallSection.  # noqa: E501

        Priority of current section with respect to other sections. In case the field is empty, the list section api should be used to get section priority.  # noqa: E501

        :return: The priority of this FirewallSection.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this FirewallSection.

        Priority of current section with respect to other sections. In case the field is empty, the list section api should be used to get section priority.  # noqa: E501

        :param priority: The priority of this FirewallSection.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def enforced_on(self):
        """Gets the enforced_on of this FirewallSection.  # noqa: E501

        This attribute represents enforcement point of firewall section. For example, firewall section enforced on logical port with attachment type bridge endpoint will have 'BRIDGEENDPOINT' value, firewall section enforced on logical router will have 'LOGICALROUTER' value and rest have 'VIF' value.  # noqa: E501

        :return: The enforced_on of this FirewallSection.  # noqa: E501
        :rtype: str
        """
        return self._enforced_on

    @enforced_on.setter
    def enforced_on(self, enforced_on):
        """Sets the enforced_on of this FirewallSection.

        This attribute represents enforcement point of firewall section. For example, firewall section enforced on logical port with attachment type bridge endpoint will have 'BRIDGEENDPOINT' value, firewall section enforced on logical router will have 'LOGICALROUTER' value and rest have 'VIF' value.  # noqa: E501

        :param enforced_on: The enforced_on of this FirewallSection.  # noqa: E501
        :type: str
        """

        self._enforced_on = enforced_on

    @property
    def locked(self):
        """Gets the locked of this FirewallSection.  # noqa: E501

        Section is locked/unlocked.  # noqa: E501

        :return: The locked of this FirewallSection.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this FirewallSection.

        Section is locked/unlocked.  # noqa: E501

        :param locked: The locked of this FirewallSection.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def tcp_strict(self):
        """Gets the tcp_strict of this FirewallSection.  # noqa: E501

        If TCP strict is enabled on a section and a packet matches rule in it, the following check will be performed. If the packet does not belong to an existing session, the kernel will check to see if the SYN flag of the packet is set. If it is not, then it will drop the packet.  # noqa: E501

        :return: The tcp_strict of this FirewallSection.  # noqa: E501
        :rtype: bool
        """
        return self._tcp_strict

    @tcp_strict.setter
    def tcp_strict(self, tcp_strict):
        """Sets the tcp_strict of this FirewallSection.

        If TCP strict is enabled on a section and a packet matches rule in it, the following check will be performed. If the packet does not belong to an existing session, the kernel will check to see if the SYN flag of the packet is set. If it is not, then it will drop the packet.  # noqa: E501

        :param tcp_strict: The tcp_strict of this FirewallSection.  # noqa: E501
        :type: bool
        """

        self._tcp_strict = tcp_strict

    @property
    def lock_modified_by(self):
        """Gets the lock_modified_by of this FirewallSection.  # noqa: E501

        ID of the user who last modified the lock for the section.  # noqa: E501

        :return: The lock_modified_by of this FirewallSection.  # noqa: E501
        :rtype: str
        """
        return self._lock_modified_by

    @lock_modified_by.setter
    def lock_modified_by(self, lock_modified_by):
        """Sets the lock_modified_by of this FirewallSection.

        ID of the user who last modified the lock for the section.  # noqa: E501

        :param lock_modified_by: The lock_modified_by of this FirewallSection.  # noqa: E501
        :type: str
        """

        self._lock_modified_by = lock_modified_by

    @property
    def lock_modified_time(self):
        """Gets the lock_modified_time of this FirewallSection.  # noqa: E501

        Section locked/unlocked time in epoch milliseconds.  # noqa: E501

        :return: The lock_modified_time of this FirewallSection.  # noqa: E501
        :rtype: int
        """
        return self._lock_modified_time

    @lock_modified_time.setter
    def lock_modified_time(self, lock_modified_time):
        """Sets the lock_modified_time of this FirewallSection.

        Section locked/unlocked time in epoch milliseconds.  # noqa: E501

        :param lock_modified_time: The lock_modified_time of this FirewallSection.  # noqa: E501
        :type: int
        """

        self._lock_modified_time = lock_modified_time

    @property
    def comments(self):
        """Gets the comments of this FirewallSection.  # noqa: E501

        Comments for section lock/unlock.  # noqa: E501

        :return: The comments of this FirewallSection.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this FirewallSection.

        Comments for section lock/unlock.  # noqa: E501

        :param comments: The comments of this FirewallSection.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def autoplumbed(self):
        """Gets the autoplumbed of this FirewallSection.  # noqa: E501

        This flag indicates whether it is an auto-plumbed section that is associated to a LogicalRouter. Auto-plumbed sections are system owned and cannot be updated via the API.  # noqa: E501

        :return: The autoplumbed of this FirewallSection.  # noqa: E501
        :rtype: bool
        """
        return self._autoplumbed

    @autoplumbed.setter
    def autoplumbed(self, autoplumbed):
        """Sets the autoplumbed of this FirewallSection.

        This flag indicates whether it is an auto-plumbed section that is associated to a LogicalRouter. Auto-plumbed sections are system owned and cannot be updated via the API.  # noqa: E501

        :param autoplumbed: The autoplumbed of this FirewallSection.  # noqa: E501
        :type: bool
        """

        self._autoplumbed = autoplumbed

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
        if issubclass(FirewallSection, dict):
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
        if not isinstance(other, FirewallSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
