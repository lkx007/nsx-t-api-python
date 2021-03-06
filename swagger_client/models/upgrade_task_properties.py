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


class UpgradeTaskProperties(object):
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
        'bundle_name': 'str',
        'step': 'str',
        'parameters': 'object'
    }

    attribute_map = {
        'bundle_name': 'bundle_name',
        'step': 'step',
        'parameters': 'parameters'
    }

    def __init__(self, bundle_name=None, step=None, parameters=None):  # noqa: E501
        """UpgradeTaskProperties - a model defined in Swagger"""  # noqa: E501
        self._bundle_name = None
        self._step = None
        self._parameters = None
        self.discriminator = None
        self.bundle_name = bundle_name
        if step is not None:
            self.step = step
        if parameters is not None:
            self.parameters = parameters

    @property
    def bundle_name(self):
        """Gets the bundle_name of this UpgradeTaskProperties.  # noqa: E501

        Name of Bundle  # noqa: E501

        :return: The bundle_name of this UpgradeTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._bundle_name

    @bundle_name.setter
    def bundle_name(self, bundle_name):
        """Sets the bundle_name of this UpgradeTaskProperties.

        Name of Bundle  # noqa: E501

        :param bundle_name: The bundle_name of this UpgradeTaskProperties.  # noqa: E501
        :type: str
        """
        if bundle_name is None:
            raise ValueError("Invalid value for `bundle_name`, must not be `None`")  # noqa: E501

        self._bundle_name = bundle_name

    @property
    def step(self):
        """Gets the step of this UpgradeTaskProperties.  # noqa: E501

        Step name  # noqa: E501

        :return: The step of this UpgradeTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this UpgradeTaskProperties.

        Step name  # noqa: E501

        :param step: The step of this UpgradeTaskProperties.  # noqa: E501
        :type: str
        """

        self._step = step

    @property
    def parameters(self):
        """Gets the parameters of this UpgradeTaskProperties.  # noqa: E501

        Bundle arguments  # noqa: E501

        :return: The parameters of this UpgradeTaskProperties.  # noqa: E501
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this UpgradeTaskProperties.

        Bundle arguments  # noqa: E501

        :param parameters: The parameters of this UpgradeTaskProperties.  # noqa: E501
        :type: object
        """

        self._parameters = parameters

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
        if issubclass(UpgradeTaskProperties, dict):
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
        if not isinstance(other, UpgradeTaskProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
