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


class FirewallSectionsSummary(object):
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
        '_self': 'SelfResourceLink',
        'links': 'list[ResourceLink]',
        'schema': 'str',
        'section_count': 'int',
        'rule_count': 'int',
        'section_type': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'section_count': 'section_count',
        'rule_count': 'rule_count',
        'section_type': 'section_type'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, _self=None, links=None, schema=None, section_count=None, rule_count=None, section_type=None, *args, **kwargs):  # noqa: E501
        """FirewallSectionsSummary - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._links = None
        self._schema = None
        self._section_count = None
        self._rule_count = None
        self._section_type = None
        self.discriminator = None
        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if section_count is not None:
            self.section_count = section_count
        if rule_count is not None:
            self.rule_count = rule_count
        if section_type is not None:
            self.section_type = section_type
        Resource.__init__(self, *args, **kwargs)

    @property
    def _self(self):
        """Gets the _self of this FirewallSectionsSummary.  # noqa: E501


        :return: The _self of this FirewallSectionsSummary.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this FirewallSectionsSummary.


        :param _self: The _self of this FirewallSectionsSummary.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this FirewallSectionsSummary.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this FirewallSectionsSummary.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FirewallSectionsSummary.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this FirewallSectionsSummary.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this FirewallSectionsSummary.  # noqa: E501

        Schema for this resource  # noqa: E501

        :return: The schema of this FirewallSectionsSummary.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this FirewallSectionsSummary.

        Schema for this resource  # noqa: E501

        :param schema: The schema of this FirewallSectionsSummary.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def section_count(self):
        """Gets the section_count of this FirewallSectionsSummary.  # noqa: E501

        Total number of sections for the section type.  # noqa: E501

        :return: The section_count of this FirewallSectionsSummary.  # noqa: E501
        :rtype: int
        """
        return self._section_count

    @section_count.setter
    def section_count(self, section_count):
        """Sets the section_count of this FirewallSectionsSummary.

        Total number of sections for the section type.  # noqa: E501

        :param section_count: The section_count of this FirewallSectionsSummary.  # noqa: E501
        :type: int
        """

        self._section_count = section_count

    @property
    def rule_count(self):
        """Gets the rule_count of this FirewallSectionsSummary.  # noqa: E501

        Total number of rules in the section.  # noqa: E501

        :return: The rule_count of this FirewallSectionsSummary.  # noqa: E501
        :rtype: int
        """
        return self._rule_count

    @rule_count.setter
    def rule_count(self, rule_count):
        """Sets the rule_count of this FirewallSectionsSummary.

        Total number of rules in the section.  # noqa: E501

        :param rule_count: The rule_count of this FirewallSectionsSummary.  # noqa: E501
        :type: int
        """

        self._rule_count = rule_count

    @property
    def section_type(self):
        """Gets the section_type of this FirewallSectionsSummary.  # noqa: E501

        Type of rules which a section can contain.  # noqa: E501

        :return: The section_type of this FirewallSectionsSummary.  # noqa: E501
        :rtype: str
        """
        return self._section_type

    @section_type.setter
    def section_type(self, section_type):
        """Sets the section_type of this FirewallSectionsSummary.

        Type of rules which a section can contain.  # noqa: E501

        :param section_type: The section_type of this FirewallSectionsSummary.  # noqa: E501
        :type: str
        """
        allowed_values = ["L2DFW", "L3DFW", "L3BRIDGEPORTFW", "L3LOGICALROUTERFW"]  # noqa: E501
        if section_type not in allowed_values:
            raise ValueError(
                "Invalid value for `section_type` ({0}), must be one of {1}"  # noqa: E501
                .format(section_type, allowed_values)
            )

        self._section_type = section_type

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
        if issubclass(FirewallSectionsSummary, dict):
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
        if not isinstance(other, FirewallSectionsSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
