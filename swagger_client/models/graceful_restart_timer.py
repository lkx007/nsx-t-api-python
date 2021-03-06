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


class GracefulRestartTimer(object):
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
        'restart_timer': 'int',
        'stale_timer': 'int'
    }

    attribute_map = {
        'restart_timer': 'restart_timer',
        'stale_timer': 'stale_timer'
    }

    def __init__(self, restart_timer=180, stale_timer=600):  # noqa: E501
        """GracefulRestartTimer - a model defined in Swagger"""  # noqa: E501
        self._restart_timer = None
        self._stale_timer = None
        self.discriminator = None
        if restart_timer is not None:
            self.restart_timer = restart_timer
        if stale_timer is not None:
            self.stale_timer = stale_timer

    @property
    def restart_timer(self):
        """Gets the restart_timer of this GracefulRestartTimer.  # noqa: E501

        Maximum time BGP speaker will take for the BGP session to be re-established after a restart. Ranges from 1 sec to 3600 sec. This can be used to speed up routing convergence by its peer in case that the BGP speaker does not come back after a restart. If the session does not get re-established within the \"Restart Time\" that the Restarting Speaker advertised previously, the Receiving Speaker will delete all the stale routes from that peer.   # noqa: E501

        :return: The restart_timer of this GracefulRestartTimer.  # noqa: E501
        :rtype: int
        """
        return self._restart_timer

    @restart_timer.setter
    def restart_timer(self, restart_timer):
        """Sets the restart_timer of this GracefulRestartTimer.

        Maximum time BGP speaker will take for the BGP session to be re-established after a restart. Ranges from 1 sec to 3600 sec. This can be used to speed up routing convergence by its peer in case that the BGP speaker does not come back after a restart. If the session does not get re-established within the \"Restart Time\" that the Restarting Speaker advertised previously, the Receiving Speaker will delete all the stale routes from that peer.   # noqa: E501

        :param restart_timer: The restart_timer of this GracefulRestartTimer.  # noqa: E501
        :type: int
        """

        self._restart_timer = restart_timer

    @property
    def stale_timer(self):
        """Gets the stale_timer of this GracefulRestartTimer.  # noqa: E501

        Maximum time before stale routes are removed from the RIB when the local BGP process restarts. Ranges from 1 sec to 3600 sec.   # noqa: E501

        :return: The stale_timer of this GracefulRestartTimer.  # noqa: E501
        :rtype: int
        """
        return self._stale_timer

    @stale_timer.setter
    def stale_timer(self, stale_timer):
        """Sets the stale_timer of this GracefulRestartTimer.

        Maximum time before stale routes are removed from the RIB when the local BGP process restarts. Ranges from 1 sec to 3600 sec.   # noqa: E501

        :param stale_timer: The stale_timer of this GracefulRestartTimer.  # noqa: E501
        :type: int
        """

        self._stale_timer = stale_timer

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
        if issubclass(GracefulRestartTimer, dict):
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
        if not isinstance(other, GracefulRestartTimer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
