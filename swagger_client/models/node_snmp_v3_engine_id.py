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


class NodeSnmpV3EngineID(object):
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
        'service_name': 'str',
        'v3_engine_id': 'str'
    }
    if hasattr(NodeServiceProperties, "swagger_types"):
        swagger_types.update(NodeServiceProperties.swagger_types)

    attribute_map = {
        'service_name': 'service_name',
        'v3_engine_id': 'v3_engine_id'
    }
    if hasattr(NodeServiceProperties, "attribute_map"):
        attribute_map.update(NodeServiceProperties.attribute_map)

    def __init__(self, service_name=None, v3_engine_id=None, *args, **kwargs):  # noqa: E501
        """NodeSnmpV3EngineID - a model defined in Swagger"""  # noqa: E501
        self._service_name = None
        self._v3_engine_id = None
        self.discriminator = None
        self.service_name = service_name
        self.v3_engine_id = v3_engine_id
        NodeServiceProperties.__init__(self, *args, **kwargs)

    @property
    def service_name(self):
        """Gets the service_name of this NodeSnmpV3EngineID.  # noqa: E501

        Service name  # noqa: E501

        :return: The service_name of this NodeSnmpV3EngineID.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this NodeSnmpV3EngineID.

        Service name  # noqa: E501

        :param service_name: The service_name of this NodeSnmpV3EngineID.  # noqa: E501
        :type: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def v3_engine_id(self):
        """Gets the v3_engine_id of this NodeSnmpV3EngineID.  # noqa: E501

        SNMP v3 engine id  # noqa: E501

        :return: The v3_engine_id of this NodeSnmpV3EngineID.  # noqa: E501
        :rtype: str
        """
        return self._v3_engine_id

    @v3_engine_id.setter
    def v3_engine_id(self, v3_engine_id):
        """Sets the v3_engine_id of this NodeSnmpV3EngineID.

        SNMP v3 engine id  # noqa: E501

        :param v3_engine_id: The v3_engine_id of this NodeSnmpV3EngineID.  # noqa: E501
        :type: str
        """
        if v3_engine_id is None:
            raise ValueError("Invalid value for `v3_engine_id`, must not be `None`")  # noqa: E501

        self._v3_engine_id = v3_engine_id

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
        if issubclass(NodeSnmpV3EngineID, dict):
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
        if not isinstance(other, NodeSnmpV3EngineID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
