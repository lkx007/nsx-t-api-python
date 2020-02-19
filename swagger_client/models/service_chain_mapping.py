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


class ServiceChainMapping(object):
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
        'service_chain_id': 'str',
        'direction': 'str',
        'service_index': 'int'
    }

    attribute_map = {
        'service_chain_id': 'service_chain_id',
        'direction': 'direction',
        'service_index': 'service_index'
    }

    def __init__(self, service_chain_id=None, direction=None, service_index=None):  # noqa: E501
        """ServiceChainMapping - a model defined in Swagger"""  # noqa: E501
        self._service_chain_id = None
        self._direction = None
        self._service_index = None
        self.discriminator = None
        if service_chain_id is not None:
            self.service_chain_id = service_chain_id
        if direction is not None:
            self.direction = direction
        if service_index is not None:
            self.service_index = service_index

    @property
    def service_chain_id(self):
        """Gets the service_chain_id of this ServiceChainMapping.  # noqa: E501

        A unique id generated for every ServiceChain. This is not a uuid.  # noqa: E501

        :return: The service_chain_id of this ServiceChainMapping.  # noqa: E501
        :rtype: str
        """
        return self._service_chain_id

    @service_chain_id.setter
    def service_chain_id(self, service_chain_id):
        """Sets the service_chain_id of this ServiceChainMapping.

        A unique id generated for every ServiceChain. This is not a uuid.  # noqa: E501

        :param service_chain_id: The service_chain_id of this ServiceChainMapping.  # noqa: E501
        :type: str
        """

        self._service_chain_id = service_chain_id

    @property
    def direction(self):
        """Gets the direction of this ServiceChainMapping.  # noqa: E501

        Each ServiceChain has forward_path_service_profiles and reverse_path_service_profiles. This property will indicate which of them being used. FORWARD - forward_path_service_profiles REVERSE - reverse_path_service_profiles  # noqa: E501

        :return: The direction of this ServiceChainMapping.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ServiceChainMapping.

        Each ServiceChain has forward_path_service_profiles and reverse_path_service_profiles. This property will indicate which of them being used. FORWARD - forward_path_service_profiles REVERSE - reverse_path_service_profiles  # noqa: E501

        :param direction: The direction of this ServiceChainMapping.  # noqa: E501
        :type: str
        """
        allowed_values = ["FORWARD", "REVERSE"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def service_index(self):
        """Gets the service_index of this ServiceChainMapping.  # noqa: E501

        Service Index represents a numerical position of a ServiceInsertionServiceProfile in a ServiceChain. It will be in reverse order. Service Index can point to either forward_path_service_profiles or reverse_path_service_profiles indicated by direction property. Example - For a ServiceChain A-B-C, A will have index of 3, B will have index of 2 and C will have index of 1.  # noqa: E501

        :return: The service_index of this ServiceChainMapping.  # noqa: E501
        :rtype: int
        """
        return self._service_index

    @service_index.setter
    def service_index(self, service_index):
        """Sets the service_index of this ServiceChainMapping.

        Service Index represents a numerical position of a ServiceInsertionServiceProfile in a ServiceChain. It will be in reverse order. Service Index can point to either forward_path_service_profiles or reverse_path_service_profiles indicated by direction property. Example - For a ServiceChain A-B-C, A will have index of 3, B will have index of 2 and C will have index of 1.  # noqa: E501

        :param service_index: The service_index of this ServiceChainMapping.  # noqa: E501
        :type: int
        """

        self._service_index = service_index

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
        if issubclass(ServiceChainMapping, dict):
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
        if not isinstance(other, ServiceChainMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
