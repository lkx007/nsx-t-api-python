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


class IPSecVPNIKESessionStatus(object):
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
        'fail_reason': 'str',
        'ike_session_state': 'str'
    }

    attribute_map = {
        'fail_reason': 'fail_reason',
        'ike_session_state': 'ike_session_state'
    }

    def __init__(self, fail_reason=None, ike_session_state=None):  # noqa: E501
        """IPSecVPNIKESessionStatus - a model defined in Swagger"""  # noqa: E501
        self._fail_reason = None
        self._ike_session_state = None
        self.discriminator = None
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if ike_session_state is not None:
            self.ike_session_state = ike_session_state

    @property
    def fail_reason(self):
        """Gets the fail_reason of this IPSecVPNIKESessionStatus.  # noqa: E501

        Reason for failure.  # noqa: E501

        :return: The fail_reason of this IPSecVPNIKESessionStatus.  # noqa: E501
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this IPSecVPNIKESessionStatus.

        Reason for failure.  # noqa: E501

        :param fail_reason: The fail_reason of this IPSecVPNIKESessionStatus.  # noqa: E501
        :type: str
        """

        self._fail_reason = fail_reason

    @property
    def ike_session_state(self):
        """Gets the ike_session_state of this IPSecVPNIKESessionStatus.  # noqa: E501

        IKE session service status UP, DOWN and NEGOTIATING.  # noqa: E501

        :return: The ike_session_state of this IPSecVPNIKESessionStatus.  # noqa: E501
        :rtype: str
        """
        return self._ike_session_state

    @ike_session_state.setter
    def ike_session_state(self, ike_session_state):
        """Sets the ike_session_state of this IPSecVPNIKESessionStatus.

        IKE session service status UP, DOWN and NEGOTIATING.  # noqa: E501

        :param ike_session_state: The ike_session_state of this IPSecVPNIKESessionStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN", "NEGOTIATING"]  # noqa: E501
        if ike_session_state not in allowed_values:
            raise ValueError(
                "Invalid value for `ike_session_state` ({0}), must be one of {1}"  # noqa: E501
                .format(ike_session_state, allowed_values)
            )

        self._ike_session_state = ike_session_state

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
        if issubclass(IPSecVPNIKESessionStatus, dict):
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
        if not isinstance(other, IPSecVPNIKESessionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
