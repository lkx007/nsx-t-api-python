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


class SVMConfigureIssue(object):
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
        'errors': 'list[SIErrorClass]',
        'service_instance_id': 'str'
    }

    attribute_map = {
        'errors': 'errors',
        'service_instance_id': 'service_instance_id'
    }

    def __init__(self, errors=None, service_instance_id=None):  # noqa: E501
        """SVMConfigureIssue - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._service_instance_id = None
        self.discriminator = None
        if errors is not None:
            self.errors = errors
        if service_instance_id is not None:
            self.service_instance_id = service_instance_id

    @property
    def errors(self):
        """Gets the errors of this SVMConfigureIssue.  # noqa: E501

        List of errors along with details like errorId and error messages.  # noqa: E501

        :return: The errors of this SVMConfigureIssue.  # noqa: E501
        :rtype: list[SIErrorClass]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this SVMConfigureIssue.

        List of errors along with details like errorId and error messages.  # noqa: E501

        :param errors: The errors of this SVMConfigureIssue.  # noqa: E501
        :type: list[SIErrorClass]
        """

        self._errors = errors

    @property
    def service_instance_id(self):
        """Gets the service_instance_id of this SVMConfigureIssue.  # noqa: E501

        The ID of service instance which was deployed.  # noqa: E501

        :return: The service_instance_id of this SVMConfigureIssue.  # noqa: E501
        :rtype: str
        """
        return self._service_instance_id

    @service_instance_id.setter
    def service_instance_id(self, service_instance_id):
        """Sets the service_instance_id of this SVMConfigureIssue.

        The ID of service instance which was deployed.  # noqa: E501

        :param service_instance_id: The service_instance_id of this SVMConfigureIssue.  # noqa: E501
        :type: str
        """

        self._service_instance_id = service_instance_id

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
        if issubclass(SVMConfigureIssue, dict):
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
        if not isinstance(other, SVMConfigureIssue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other