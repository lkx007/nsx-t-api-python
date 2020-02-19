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


class GracefulRestartConfig(object):
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
        'graceful_restart_mode': 'str',
        'graceful_restart_timer': 'GracefulRestartTimer'
    }

    attribute_map = {
        'graceful_restart_mode': 'graceful_restart_mode',
        'graceful_restart_timer': 'graceful_restart_timer'
    }

    def __init__(self, graceful_restart_mode='HELPER_ONLY', graceful_restart_timer=None):  # noqa: E501
        """GracefulRestartConfig - a model defined in Swagger"""  # noqa: E501
        self._graceful_restart_mode = None
        self._graceful_restart_timer = None
        self.discriminator = None
        if graceful_restart_mode is not None:
            self.graceful_restart_mode = graceful_restart_mode
        if graceful_restart_timer is not None:
            self.graceful_restart_timer = graceful_restart_timer

    @property
    def graceful_restart_mode(self):
        """Gets the graceful_restart_mode of this GracefulRestartConfig.  # noqa: E501

        BGP Graceful Restart mode  # noqa: E501

        :return: The graceful_restart_mode of this GracefulRestartConfig.  # noqa: E501
        :rtype: str
        """
        return self._graceful_restart_mode

    @graceful_restart_mode.setter
    def graceful_restart_mode(self, graceful_restart_mode):
        """Sets the graceful_restart_mode of this GracefulRestartConfig.

        BGP Graceful Restart mode  # noqa: E501

        :param graceful_restart_mode: The graceful_restart_mode of this GracefulRestartConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["DISABLE", "HELPER_ONLY", "GR_AND_HELPER"]  # noqa: E501
        if graceful_restart_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `graceful_restart_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(graceful_restart_mode, allowed_values)
            )

        self._graceful_restart_mode = graceful_restart_mode

    @property
    def graceful_restart_timer(self):
        """Gets the graceful_restart_timer of this GracefulRestartConfig.  # noqa: E501


        :return: The graceful_restart_timer of this GracefulRestartConfig.  # noqa: E501
        :rtype: GracefulRestartTimer
        """
        return self._graceful_restart_timer

    @graceful_restart_timer.setter
    def graceful_restart_timer(self, graceful_restart_timer):
        """Sets the graceful_restart_timer of this GracefulRestartConfig.


        :param graceful_restart_timer: The graceful_restart_timer of this GracefulRestartConfig.  # noqa: E501
        :type: GracefulRestartTimer
        """

        self._graceful_restart_timer = graceful_restart_timer

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
        if issubclass(GracefulRestartConfig, dict):
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
        if not isinstance(other, GracefulRestartConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
