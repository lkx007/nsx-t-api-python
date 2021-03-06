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


class IpfixServiceAssociationListResult(object):
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
        'service_type': 'str',
        'results': 'list[IpfixConfig]'
    }
    if hasattr(ServiceAssociationListResult, "swagger_types"):
        swagger_types.update(ServiceAssociationListResult.swagger_types)

    attribute_map = {
        'service_type': 'service_type',
        'results': 'results'
    }
    if hasattr(ServiceAssociationListResult, "attribute_map"):
        attribute_map.update(ServiceAssociationListResult.attribute_map)

    def __init__(self, service_type=None, results=None, *args, **kwargs):  # noqa: E501
        """IpfixServiceAssociationListResult - a model defined in Swagger"""  # noqa: E501
        self._service_type = None
        self._results = None
        self.discriminator = None
        self.service_type = service_type
        if results is not None:
            self.results = results
        ServiceAssociationListResult.__init__(self, *args, **kwargs)

    @property
    def service_type(self):
        """Gets the service_type of this IpfixServiceAssociationListResult.  # noqa: E501


        :return: The service_type of this IpfixServiceAssociationListResult.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this IpfixServiceAssociationListResult.


        :param service_type: The service_type of this IpfixServiceAssociationListResult.  # noqa: E501
        :type: str
        """
        if service_type is None:
            raise ValueError("Invalid value for `service_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FireWallServiceAssociationListResult", "IpfixServiceAssociationListResult"]  # noqa: E501
        if service_type not in allowed_values:
            raise ValueError(
                "Invalid value for `service_type` ({0}), must be one of {1}"  # noqa: E501
                .format(service_type, allowed_values)
            )

        self._service_type = service_type

    @property
    def results(self):
        """Gets the results of this IpfixServiceAssociationListResult.  # noqa: E501

        Ipfix config list result with pagination support.  # noqa: E501

        :return: The results of this IpfixServiceAssociationListResult.  # noqa: E501
        :rtype: list[IpfixConfig]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this IpfixServiceAssociationListResult.

        Ipfix config list result with pagination support.  # noqa: E501

        :param results: The results of this IpfixServiceAssociationListResult.  # noqa: E501
        :type: list[IpfixConfig]
        """

        self._results = results

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
        if issubclass(IpfixServiceAssociationListResult, dict):
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
        if not isinstance(other, IpfixServiceAssociationListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
