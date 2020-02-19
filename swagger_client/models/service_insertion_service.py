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


class ServiceInsertionService(object):
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
        'service': 'NSServiceElement'
    }
    if hasattr(DSService, "swagger_types"):
        swagger_types.update(DSService.swagger_types)

    attribute_map = {
        'service': 'service'
    }
    if hasattr(DSService, "attribute_map"):
        attribute_map.update(DSService.attribute_map)

    def __init__(self, service=None, *args, **kwargs):  # noqa: E501
        """ServiceInsertionService - a model defined in Swagger"""  # noqa: E501
        self._service = None
        self.discriminator = None
        if service is not None:
            self.service = service
        DSService.__init__(self, *args, **kwargs)

    @property
    def service(self):
        """Gets the service of this ServiceInsertionService.  # noqa: E501


        :return: The service of this ServiceInsertionService.  # noqa: E501
        :rtype: NSServiceElement
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ServiceInsertionService.


        :param service: The service of this ServiceInsertionService.  # noqa: E501
        :type: NSServiceElement
        """

        self._service = service

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
        if issubclass(ServiceInsertionService, dict):
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
        if not isinstance(other, ServiceInsertionService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
