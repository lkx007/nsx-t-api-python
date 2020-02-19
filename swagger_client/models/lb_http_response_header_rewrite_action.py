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


class LbHttpResponseHeaderRewriteAction(object):
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
        'type': 'str',
        'header_value': 'str',
        'header_name': 'str'
    }
    if hasattr(LbRuleAction, "swagger_types"):
        swagger_types.update(LbRuleAction.swagger_types)

    attribute_map = {
        'type': 'type',
        'header_value': 'header_value',
        'header_name': 'header_name'
    }
    if hasattr(LbRuleAction, "attribute_map"):
        attribute_map.update(LbRuleAction.attribute_map)

    def __init__(self, type=None, header_value=None, header_name=None, *args, **kwargs):  # noqa: E501
        """LbHttpResponseHeaderRewriteAction - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._header_value = None
        self._header_name = None
        self.discriminator = None
        self.type = type
        self.header_value = header_value
        self.header_name = header_name
        LbRuleAction.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this LbHttpResponseHeaderRewriteAction.  # noqa: E501

        The property identifies the load balancer rule action type.   # noqa: E501

        :return: The type of this LbHttpResponseHeaderRewriteAction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LbHttpResponseHeaderRewriteAction.

        The property identifies the load balancer rule action type.   # noqa: E501

        :param type: The type of this LbHttpResponseHeaderRewriteAction.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["LbHttpRequestUriRewriteAction", "LbHttpRequestHeaderRewriteAction", "LbHttpRejectAction", "LbHttpRedirectAction", "LbSelectPoolAction", "LbSelectServerAction", "LbHttpResponseHeaderRewriteAction", "LbHttpRequestHeaderDeleteAction", "LbHttpResponseHeaderDeleteAction", "LbVariableAssignmentAction", "LbVariablePersistenceOnAction", "LbVariablePersistenceLearnAction"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def header_value(self):
        """Gets the header_value of this LbHttpResponseHeaderRewriteAction.  # noqa: E501

        Value of header field  # noqa: E501

        :return: The header_value of this LbHttpResponseHeaderRewriteAction.  # noqa: E501
        :rtype: str
        """
        return self._header_value

    @header_value.setter
    def header_value(self, header_value):
        """Sets the header_value of this LbHttpResponseHeaderRewriteAction.

        Value of header field  # noqa: E501

        :param header_value: The header_value of this LbHttpResponseHeaderRewriteAction.  # noqa: E501
        :type: str
        """
        if header_value is None:
            raise ValueError("Invalid value for `header_value`, must not be `None`")  # noqa: E501

        self._header_value = header_value

    @property
    def header_name(self):
        """Gets the header_name of this LbHttpResponseHeaderRewriteAction.  # noqa: E501

        Name of a header field of HTTP request message  # noqa: E501

        :return: The header_name of this LbHttpResponseHeaderRewriteAction.  # noqa: E501
        :rtype: str
        """
        return self._header_name

    @header_name.setter
    def header_name(self, header_name):
        """Sets the header_name of this LbHttpResponseHeaderRewriteAction.

        Name of a header field of HTTP request message  # noqa: E501

        :param header_name: The header_name of this LbHttpResponseHeaderRewriteAction.  # noqa: E501
        :type: str
        """
        if header_name is None:
            raise ValueError("Invalid value for `header_name`, must not be `None`")  # noqa: E501

        self._header_name = header_name

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
        if issubclass(LbHttpResponseHeaderRewriteAction, dict):
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
        if not isinstance(other, LbHttpResponseHeaderRewriteAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
