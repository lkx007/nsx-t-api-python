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


class FeatureUsageList(object):
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
        'feature_usage_info': 'list[FeatureUsage]'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'feature_usage_info': 'feature_usage_info'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, _self=None, links=None, schema=None, feature_usage_info=None, *args, **kwargs):  # noqa: E501
        """FeatureUsageList - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._links = None
        self._schema = None
        self._feature_usage_info = None
        self.discriminator = None
        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if feature_usage_info is not None:
            self.feature_usage_info = feature_usage_info
        Resource.__init__(self, *args, **kwargs)

    @property
    def _self(self):
        """Gets the _self of this FeatureUsageList.  # noqa: E501


        :return: The _self of this FeatureUsageList.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this FeatureUsageList.


        :param _self: The _self of this FeatureUsageList.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this FeatureUsageList.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this FeatureUsageList.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FeatureUsageList.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this FeatureUsageList.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this FeatureUsageList.  # noqa: E501

        Schema for this resource  # noqa: E501

        :return: The schema of this FeatureUsageList.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this FeatureUsageList.

        Schema for this resource  # noqa: E501

        :param schema: The schema of this FeatureUsageList.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def feature_usage_info(self):
        """Gets the feature_usage_info of this FeatureUsageList.  # noqa: E501

        Feature Usage List  # noqa: E501

        :return: The feature_usage_info of this FeatureUsageList.  # noqa: E501
        :rtype: list[FeatureUsage]
        """
        return self._feature_usage_info

    @feature_usage_info.setter
    def feature_usage_info(self, feature_usage_info):
        """Sets the feature_usage_info of this FeatureUsageList.

        Feature Usage List  # noqa: E501

        :param feature_usage_info: The feature_usage_info of this FeatureUsageList.  # noqa: E501
        :type: list[FeatureUsage]
        """

        self._feature_usage_info = feature_usage_info

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
        if issubclass(FeatureUsageList, dict):
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
        if not isinstance(other, FeatureUsageList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
