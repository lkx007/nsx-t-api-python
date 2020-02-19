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


class IpfixSwitchUpmProfile(object):
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
        'resource_type': 'str',
        'priority': 'int',
        'collector_profile': 'str',
        'idle_timeout': 'int',
        'max_flows': 'int',
        'observation_domain_id': 'int',
        'active_timeout': 'int',
        'export_overlay_flow': 'bool',
        'applied_tos': 'AppliedTos',
        'packet_sample_probability': 'float'
    }
    if hasattr(IpfixUpmProfile, "swagger_types"):
        swagger_types.update(IpfixUpmProfile.swagger_types)

    attribute_map = {
        'resource_type': 'resource_type',
        'priority': 'priority',
        'collector_profile': 'collector_profile',
        'idle_timeout': 'idle_timeout',
        'max_flows': 'max_flows',
        'observation_domain_id': 'observation_domain_id',
        'active_timeout': 'active_timeout',
        'export_overlay_flow': 'export_overlay_flow',
        'applied_tos': 'applied_tos',
        'packet_sample_probability': 'packet_sample_probability'
    }
    if hasattr(IpfixUpmProfile, "attribute_map"):
        attribute_map.update(IpfixUpmProfile.attribute_map)

    def __init__(self, resource_type=None, priority=None, collector_profile=None, idle_timeout=300, max_flows=16384, observation_domain_id=None, active_timeout=300, export_overlay_flow=True, applied_tos=None, packet_sample_probability=None, *args, **kwargs):  # noqa: E501
        """IpfixSwitchUpmProfile - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._priority = None
        self._collector_profile = None
        self._idle_timeout = None
        self._max_flows = None
        self._observation_domain_id = None
        self._active_timeout = None
        self._export_overlay_flow = None
        self._applied_tos = None
        self._packet_sample_probability = None
        self.discriminator = None
        self.resource_type = resource_type
        self.priority = priority
        self.collector_profile = collector_profile
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if max_flows is not None:
            self.max_flows = max_flows
        self.observation_domain_id = observation_domain_id
        if active_timeout is not None:
            self.active_timeout = active_timeout
        if export_overlay_flow is not None:
            self.export_overlay_flow = export_overlay_flow
        if applied_tos is not None:
            self.applied_tos = applied_tos
        if packet_sample_probability is not None:
            self.packet_sample_probability = packet_sample_probability
        IpfixUpmProfile.__init__(self, *args, **kwargs)

    @property
    def resource_type(self):
        """Gets the resource_type of this IpfixSwitchUpmProfile.  # noqa: E501

        All IPFIX profile types.  # noqa: E501

        :return: The resource_type of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this IpfixSwitchUpmProfile.

        All IPFIX profile types.  # noqa: E501

        :param resource_type: The resource_type of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["IpfixSwitchUpmProfile"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def priority(self):
        """Gets the priority of this IpfixSwitchUpmProfile.  # noqa: E501

        This priority field is used to resolve conflicts in logical ports/switch  which inherit multiple switch IPFIX profiles from NSGroups.  Override rule is : for multiple profiles inherited from NSGroups, the one with highest priority (lowest number) overrides others; the profile directly applied to logical switch overrides profiles inherited from NSGroup; the profile directly applied to logical port overides profiles inherited from logical switch and/or nsgroup;  The IPFIX exporter will send records to collectors of final effective profile only.   # noqa: E501

        :return: The priority of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this IpfixSwitchUpmProfile.

        This priority field is used to resolve conflicts in logical ports/switch  which inherit multiple switch IPFIX profiles from NSGroups.  Override rule is : for multiple profiles inherited from NSGroups, the one with highest priority (lowest number) overrides others; the profile directly applied to logical switch overrides profiles inherited from NSGroup; the profile directly applied to logical port overides profiles inherited from logical switch and/or nsgroup;  The IPFIX exporter will send records to collectors of final effective profile only.   # noqa: E501

        :param priority: The priority of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def collector_profile(self):
        """Gets the collector_profile of this IpfixSwitchUpmProfile.  # noqa: E501

        Each IPFIX switching profile can have its own collector profile.   # noqa: E501

        :return: The collector_profile of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: str
        """
        return self._collector_profile

    @collector_profile.setter
    def collector_profile(self, collector_profile):
        """Sets the collector_profile of this IpfixSwitchUpmProfile.

        Each IPFIX switching profile can have its own collector profile.   # noqa: E501

        :param collector_profile: The collector_profile of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: str
        """
        if collector_profile is None:
            raise ValueError("Invalid value for `collector_profile`, must not be `None`")  # noqa: E501

        self._collector_profile = collector_profile

    @property
    def idle_timeout(self):
        """Gets the idle_timeout of this IpfixSwitchUpmProfile.  # noqa: E501

        The time in seconds after a flow is expired if no more packets matching this flow are received by the cache.   # noqa: E501

        :return: The idle_timeout of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """Sets the idle_timeout of this IpfixSwitchUpmProfile.

        The time in seconds after a flow is expired if no more packets matching this flow are received by the cache.   # noqa: E501

        :param idle_timeout: The idle_timeout of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: int
        """

        self._idle_timeout = idle_timeout

    @property
    def max_flows(self):
        """Gets the max_flows of this IpfixSwitchUpmProfile.  # noqa: E501

        The maximum number of flow entries in each exporter flow cache.   # noqa: E501

        :return: The max_flows of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_flows

    @max_flows.setter
    def max_flows(self, max_flows):
        """Sets the max_flows of this IpfixSwitchUpmProfile.

        The maximum number of flow entries in each exporter flow cache.   # noqa: E501

        :param max_flows: The max_flows of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: int
        """

        self._max_flows = max_flows

    @property
    def observation_domain_id(self):
        """Gets the observation_domain_id of this IpfixSwitchUpmProfile.  # noqa: E501

        An identifier that is unique to the exporting process and used to meter the Flows.   # noqa: E501

        :return: The observation_domain_id of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: int
        """
        return self._observation_domain_id

    @observation_domain_id.setter
    def observation_domain_id(self, observation_domain_id):
        """Sets the observation_domain_id of this IpfixSwitchUpmProfile.

        An identifier that is unique to the exporting process and used to meter the Flows.   # noqa: E501

        :param observation_domain_id: The observation_domain_id of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: int
        """
        if observation_domain_id is None:
            raise ValueError("Invalid value for `observation_domain_id`, must not be `None`")  # noqa: E501

        self._observation_domain_id = observation_domain_id

    @property
    def active_timeout(self):
        """Gets the active_timeout of this IpfixSwitchUpmProfile.  # noqa: E501

        The time in seconds after a flow is expired even if more packets matching this Flow are received by the cache.   # noqa: E501

        :return: The active_timeout of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: int
        """
        return self._active_timeout

    @active_timeout.setter
    def active_timeout(self, active_timeout):
        """Sets the active_timeout of this IpfixSwitchUpmProfile.

        The time in seconds after a flow is expired even if more packets matching this Flow are received by the cache.   # noqa: E501

        :param active_timeout: The active_timeout of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: int
        """

        self._active_timeout = active_timeout

    @property
    def export_overlay_flow(self):
        """Gets the export_overlay_flow of this IpfixSwitchUpmProfile.  # noqa: E501

        It controls whether sample result includes overlay flow info.   # noqa: E501

        :return: The export_overlay_flow of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: bool
        """
        return self._export_overlay_flow

    @export_overlay_flow.setter
    def export_overlay_flow(self, export_overlay_flow):
        """Sets the export_overlay_flow of this IpfixSwitchUpmProfile.

        It controls whether sample result includes overlay flow info.   # noqa: E501

        :param export_overlay_flow: The export_overlay_flow of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: bool
        """

        self._export_overlay_flow = export_overlay_flow

    @property
    def applied_tos(self):
        """Gets the applied_tos of this IpfixSwitchUpmProfile.  # noqa: E501


        :return: The applied_tos of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: AppliedTos
        """
        return self._applied_tos

    @applied_tos.setter
    def applied_tos(self, applied_tos):
        """Sets the applied_tos of this IpfixSwitchUpmProfile.


        :param applied_tos: The applied_tos of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: AppliedTos
        """

        self._applied_tos = applied_tos

    @property
    def packet_sample_probability(self):
        """Gets the packet_sample_probability of this IpfixSwitchUpmProfile.  # noqa: E501

        The probability in percentage that a packet is sampled. The value should be  in range (0,100] and can only have three decimal places at most. The probability  is equal for every packet.   # noqa: E501

        :return: The packet_sample_probability of this IpfixSwitchUpmProfile.  # noqa: E501
        :rtype: float
        """
        return self._packet_sample_probability

    @packet_sample_probability.setter
    def packet_sample_probability(self, packet_sample_probability):
        """Sets the packet_sample_probability of this IpfixSwitchUpmProfile.

        The probability in percentage that a packet is sampled. The value should be  in range (0,100] and can only have three decimal places at most. The probability  is equal for every packet.   # noqa: E501

        :param packet_sample_probability: The packet_sample_probability of this IpfixSwitchUpmProfile.  # noqa: E501
        :type: float
        """

        self._packet_sample_probability = packet_sample_probability

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
        if issubclass(IpfixSwitchUpmProfile, dict):
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
        if not isinstance(other, IpfixSwitchUpmProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
