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


class ConfigurationState(object):
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
        'state': 'str',
        'details': 'list[ConfigurationStateElement]',
        'failure_code': 'int',
        'failure_message': 'str'
    }

    attribute_map = {
        'state': 'state',
        'details': 'details',
        'failure_code': 'failure_code',
        'failure_message': 'failure_message'
    }

    def __init__(self, state=None, details=None, failure_code=None, failure_message=None):  # noqa: E501
        """ConfigurationState - a model defined in Swagger"""  # noqa: E501
        self._state = None
        self._details = None
        self._failure_code = None
        self._failure_message = None
        self.discriminator = None
        if state is not None:
            self.state = state
        if details is not None:
            self.details = details
        if failure_code is not None:
            self.failure_code = failure_code
        if failure_message is not None:
            self.failure_message = failure_message

    @property
    def state(self):
        """Gets the state of this ConfigurationState.  # noqa: E501

        Gives details of state of desired configuration. Additional enums with more details on progress/success/error states are sent for edge node. The success states are NODE_READY and TRANSPORT_NODE_READY, pending states are {VM_DEPLOYMENT_QUEUED, VM_DEPLOYMENT_IN_PROGRESS, REGISTRATION_PENDING} and other values indicate failures. \"in_sync\" state indicates that the desired configuration has been received by the host to which it applies, but is not yet in effect. When the configuration is actually in effect, the state will change to \"success\". Please note, failed state is deprecated.   # noqa: E501

        :return: The state of this ConfigurationState.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ConfigurationState.

        Gives details of state of desired configuration. Additional enums with more details on progress/success/error states are sent for edge node. The success states are NODE_READY and TRANSPORT_NODE_READY, pending states are {VM_DEPLOYMENT_QUEUED, VM_DEPLOYMENT_IN_PROGRESS, REGISTRATION_PENDING} and other values indicate failures. \"in_sync\" state indicates that the desired configuration has been received by the host to which it applies, but is not yet in effect. When the configuration is actually in effect, the state will change to \"success\". Please note, failed state is deprecated.   # noqa: E501

        :param state: The state of this ConfigurationState.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "in_progress", "success", "failed", "partial_success", "orphaned", "unknown", "error", "in_sync", "NOT_AVAILABLE", "VM_DEPLOYMENT_QUEUED", "VM_DEPLOYMENT_IN_PROGRESS", "VM_DEPLOYMENT_FAILED", "VM_POWER_ON_IN_PROGRESS", "VM_POWER_ON_FAILED", "REGISTRATION_PENDING", "NODE_NOT_READY", "NODE_READY", "VM_POWER_OFF_IN_PROGRESS", "VM_POWER_OFF_FAILED", "VM_UNDEPLOY_IN_PROGRESS", "VM_UNDEPLOY_FAILED", "VM_UNDEPLOY_SUCCESSFUL", "EDGE_CONFIG_ERROR", "VM_DEPLOYMENT_RESTARTED", "REGISTRATION_FAILED", "TRANSPORT_NODE_SYNC_PENDING", "TRANSPORT_NODE_CONFIGURATION_MISSING", "EDGE_HARDWARE_NOT_SUPPORTED", "MULTIPLE_OVERLAY_TZS_NOT_SUPPORTED", "TN_OVERLAY_TZ_IN_USE_BY_EDGE_CLUSTER", "TZ_ENDPOINTS_NOT_SPECIFIED", "NO_PNIC_PREPARED_IN_EDGE", "APPLIANCE_INTERNAL_ERROR", "VTEP_DHCP_NOT_SUPPORTED", "UNSUPPORTED_HOST_SWITCH_PROFILE", "UPLINK_HOST_SWITCH_PROFILE_NOT_SPECIFIED", "HOSTSWITCH_PROFILE_NOT_FOUND", "LLDP_SEND_ENABLED_NOT_SUPPORTED", "UNSUPPORTED_NAMED_TEAMING_POLICY", "LBSRCID_NOT_SUPPORTED_FOR_EDGE_VM", "LACP_NOT_SUPPORTED_FOR_EDGE_VM", "STANDBY_UPLINKS_NOT_SUPPORTED_FOR_EDGE_VM", "MULTIPLE_ACTIVE_UPLINKS_NOT_SUPPORTED_FOR_EDGE", "UNSUPPORTED_LACP_LB_ALGO_FOR_NODE", "EDGE_NODE_VERSION_NOT_SUPPORTED", "NO_PNIC_SPECIFIED_IN_TN", "INVALID_PNIC_DEVICE_NAME", "TRANSPORT_NODE_READY", "VM_NETWORK_EDIT_PENDING", "UNSUPPORTED_DEFAULT_TEAMING_POLICY", "MPA_DISCONNECTED", "VM_RENAME_PENDING", "VM_CONFIG_EDIT_PENDING", "VM_NETWORK_EDIT_FAILED", "VM_RENAME_FAILED", "VM_CONFIG_EDIT_FAILED", "VM_CONFIG_DISCREPANCY", "VM_NODE_REFRESH_FAILED", "VM_PLACEMENT_REFRESH_FAILED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def details(self):
        """Gets the details of this ConfigurationState.  # noqa: E501

        Array of configuration state of various sub systems  # noqa: E501

        :return: The details of this ConfigurationState.  # noqa: E501
        :rtype: list[ConfigurationStateElement]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ConfigurationState.

        Array of configuration state of various sub systems  # noqa: E501

        :param details: The details of this ConfigurationState.  # noqa: E501
        :type: list[ConfigurationStateElement]
        """

        self._details = details

    @property
    def failure_code(self):
        """Gets the failure_code of this ConfigurationState.  # noqa: E501

        Error code  # noqa: E501

        :return: The failure_code of this ConfigurationState.  # noqa: E501
        :rtype: int
        """
        return self._failure_code

    @failure_code.setter
    def failure_code(self, failure_code):
        """Sets the failure_code of this ConfigurationState.

        Error code  # noqa: E501

        :param failure_code: The failure_code of this ConfigurationState.  # noqa: E501
        :type: int
        """

        self._failure_code = failure_code

    @property
    def failure_message(self):
        """Gets the failure_message of this ConfigurationState.  # noqa: E501

        Error message in case of failure  # noqa: E501

        :return: The failure_message of this ConfigurationState.  # noqa: E501
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """Sets the failure_message of this ConfigurationState.

        Error message in case of failure  # noqa: E501

        :param failure_message: The failure_message of this ConfigurationState.  # noqa: E501
        :type: str
        """

        self._failure_message = failure_message

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
        if issubclass(ConfigurationState, dict):
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
        if not isinstance(other, ConfigurationState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
