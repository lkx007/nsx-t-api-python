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


class LbHttpRequestMethodCondition(object):
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
        'inverse': 'bool',
        'type': 'str',
        'method': 'str'
    }
    if hasattr(LbRuleCondition, "swagger_types"):
        swagger_types.update(LbRuleCondition.swagger_types)

    attribute_map = {
        'inverse': 'inverse',
        'type': 'type',
        'method': 'method'
    }
    if hasattr(LbRuleCondition, "attribute_map"):
        attribute_map.update(LbRuleCondition.attribute_map)

    def __init__(self, inverse=False, type=None, method=None, *args, **kwargs):  # noqa: E501
        """LbHttpRequestMethodCondition - a model defined in Swagger"""  # noqa: E501
        self._inverse = None
        self._type = None
        self._method = None
        self.discriminator = None
        if inverse is not None:
            self.inverse = inverse
        self.type = type
        self.method = method
        LbRuleCondition.__init__(self, *args, **kwargs)

    @property
    def inverse(self):
        """Gets the inverse of this LbHttpRequestMethodCondition.  # noqa: E501

        A flag to indicate whether reverse the match result of this condition  # noqa: E501

        :return: The inverse of this LbHttpRequestMethodCondition.  # noqa: E501
        :rtype: bool
        """
        return self._inverse

    @inverse.setter
    def inverse(self, inverse):
        """Sets the inverse of this LbHttpRequestMethodCondition.

        A flag to indicate whether reverse the match result of this condition  # noqa: E501

        :param inverse: The inverse of this LbHttpRequestMethodCondition.  # noqa: E501
        :type: bool
        """

        self._inverse = inverse

    @property
    def type(self):
        """Gets the type of this LbHttpRequestMethodCondition.  # noqa: E501

        Type of load balancer rule condition  # noqa: E501

        :return: The type of this LbHttpRequestMethodCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LbHttpRequestMethodCondition.

        Type of load balancer rule condition  # noqa: E501

        :param type: The type of this LbHttpRequestMethodCondition.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["LbHttpRequestMethodCondition", "LbHttpRequestUriCondition", "LbHttpRequestUriArgumentsCondition", "LbHttpRequestVersionCondition", "LbHttpRequestHeaderCondition", "LbHttpRequestCookieCondition", "LbHttpRequestBodyCondition", "LbHttpResponseHeaderCondition", "LbTcpHeaderCondition", "LbIpHeaderCondition", "LbVariableCondition", "LbHttpSslCondition"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def method(self):
        """Gets the method of this LbHttpRequestMethodCondition.  # noqa: E501

        Type of HTTP request method  # noqa: E501

        :return: The method of this LbHttpRequestMethodCondition.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this LbHttpRequestMethodCondition.

        Type of HTTP request method  # noqa: E501

        :param method: The method of this LbHttpRequestMethodCondition.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["GET", "OPTIONS", "POST", "HEAD", "PUT"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

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
        if issubclass(LbHttpRequestMethodCondition, dict):
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
        if not isinstance(other, LbHttpRequestMethodCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
