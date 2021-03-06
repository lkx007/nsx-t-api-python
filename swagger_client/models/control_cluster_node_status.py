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


class ControlClusterNodeStatus(object):
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
        'mgmt_connection_status': 'MgmtConnStatus',
        'control_cluster_status': 'str'
    }

    attribute_map = {
        'mgmt_connection_status': 'mgmt_connection_status',
        'control_cluster_status': 'control_cluster_status'
    }

    def __init__(self, mgmt_connection_status=None, control_cluster_status=None):  # noqa: E501
        """ControlClusterNodeStatus - a model defined in Swagger"""  # noqa: E501
        self._mgmt_connection_status = None
        self._control_cluster_status = None
        self.discriminator = None
        if mgmt_connection_status is not None:
            self.mgmt_connection_status = mgmt_connection_status
        if control_cluster_status is not None:
            self.control_cluster_status = control_cluster_status

    @property
    def mgmt_connection_status(self):
        """Gets the mgmt_connection_status of this ControlClusterNodeStatus.  # noqa: E501


        :return: The mgmt_connection_status of this ControlClusterNodeStatus.  # noqa: E501
        :rtype: MgmtConnStatus
        """
        return self._mgmt_connection_status

    @mgmt_connection_status.setter
    def mgmt_connection_status(self, mgmt_connection_status):
        """Sets the mgmt_connection_status of this ControlClusterNodeStatus.


        :param mgmt_connection_status: The mgmt_connection_status of this ControlClusterNodeStatus.  # noqa: E501
        :type: MgmtConnStatus
        """

        self._mgmt_connection_status = mgmt_connection_status

    @property
    def control_cluster_status(self):
        """Gets the control_cluster_status of this ControlClusterNodeStatus.  # noqa: E501

        Status of this node's connection to the control cluster  # noqa: E501

        :return: The control_cluster_status of this ControlClusterNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._control_cluster_status

    @control_cluster_status.setter
    def control_cluster_status(self, control_cluster_status):
        """Sets the control_cluster_status of this ControlClusterNodeStatus.

        Status of this node's connection to the control cluster  # noqa: E501

        :param control_cluster_status: The control_cluster_status of this ControlClusterNodeStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONNECTED", "DISCONNECTED", "UNKNOWN"]  # noqa: E501
        if control_cluster_status not in allowed_values:
            raise ValueError(
                "Invalid value for `control_cluster_status` ({0}), must be one of {1}"  # noqa: E501
                .format(control_cluster_status, allowed_values)
            )

        self._control_cluster_status = control_cluster_status

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
        if issubclass(ControlClusterNodeStatus, dict):
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
        if not isinstance(other, ControlClusterNodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
