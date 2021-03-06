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


class IpfixDfwConfig(object):
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
        'applied_tos': 'list[ResourceReference]',
        'resource_type': 'str',
        'priority': 'int',
        'collector': 'str',
        'active_flow_export_timeout': 'int',
        'template_parameters': 'IpfixDfwTemplateParameters',
        'observation_domain_id': 'int'
    }
    if hasattr(IpfixConfig, "swagger_types"):
        swagger_types.update(IpfixConfig.swagger_types)

    attribute_map = {
        'applied_tos': 'applied_tos',
        'resource_type': 'resource_type',
        'priority': 'priority',
        'collector': 'collector',
        'active_flow_export_timeout': 'active_flow_export_timeout',
        'template_parameters': 'template_parameters',
        'observation_domain_id': 'observation_domain_id'
    }
    if hasattr(IpfixConfig, "attribute_map"):
        attribute_map.update(IpfixConfig.attribute_map)

    def __init__(self, applied_tos=None, resource_type=None, priority=0, collector=None, active_flow_export_timeout=1, template_parameters=None, observation_domain_id=None, *args, **kwargs):  # noqa: E501
        """IpfixDfwConfig - a model defined in Swagger"""  # noqa: E501
        self._applied_tos = None
        self._resource_type = None
        self._priority = None
        self._collector = None
        self._active_flow_export_timeout = None
        self._template_parameters = None
        self._observation_domain_id = None
        self.discriminator = None
        if applied_tos is not None:
            self.applied_tos = applied_tos
        self.resource_type = resource_type
        self.priority = priority
        self.collector = collector
        if active_flow_export_timeout is not None:
            self.active_flow_export_timeout = active_flow_export_timeout
        if template_parameters is not None:
            self.template_parameters = template_parameters
        self.observation_domain_id = observation_domain_id
        IpfixConfig.__init__(self, *args, **kwargs)

    @property
    def applied_tos(self):
        """Gets the applied_tos of this IpfixDfwConfig.  # noqa: E501

        List of objects where the IPFIX Config will be enabled.  # noqa: E501

        :return: The applied_tos of this IpfixDfwConfig.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._applied_tos

    @applied_tos.setter
    def applied_tos(self, applied_tos):
        """Sets the applied_tos of this IpfixDfwConfig.

        List of objects where the IPFIX Config will be enabled.  # noqa: E501

        :param applied_tos: The applied_tos of this IpfixDfwConfig.  # noqa: E501
        :type: list[ResourceReference]
        """

        self._applied_tos = applied_tos

    @property
    def resource_type(self):
        """Gets the resource_type of this IpfixDfwConfig.  # noqa: E501

        Supported IPFIX Config Types.  # noqa: E501

        :return: The resource_type of this IpfixDfwConfig.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this IpfixDfwConfig.

        Supported IPFIX Config Types.  # noqa: E501

        :param resource_type: The resource_type of this IpfixDfwConfig.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["IpfixSwitchConfig", "IpfixDfwConfig"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def priority(self):
        """Gets the priority of this IpfixDfwConfig.  # noqa: E501

        This priority field is used to resolve conflicts in Logical Ports which are covered by more than one IPFIX profiles. The IPFIX exporter will send records to Collectors in highest priority profile (lowest number) only.   # noqa: E501

        :return: The priority of this IpfixDfwConfig.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this IpfixDfwConfig.

        This priority field is used to resolve conflicts in Logical Ports which are covered by more than one IPFIX profiles. The IPFIX exporter will send records to Collectors in highest priority profile (lowest number) only.   # noqa: E501

        :param priority: The priority of this IpfixDfwConfig.  # noqa: E501
        :type: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def collector(self):
        """Gets the collector of this IpfixDfwConfig.  # noqa: E501

        Each IPFIX DFW config can have its own collector config.   # noqa: E501

        :return: The collector of this IpfixDfwConfig.  # noqa: E501
        :rtype: str
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """Sets the collector of this IpfixDfwConfig.

        Each IPFIX DFW config can have its own collector config.   # noqa: E501

        :param collector: The collector of this IpfixDfwConfig.  # noqa: E501
        :type: str
        """
        if collector is None:
            raise ValueError("Invalid value for `collector`, must not be `None`")  # noqa: E501

        self._collector = collector

    @property
    def active_flow_export_timeout(self):
        """Gets the active_flow_export_timeout of this IpfixDfwConfig.  # noqa: E501

        For long standing active flows, IPFIX records will be sent per timeout period   # noqa: E501

        :return: The active_flow_export_timeout of this IpfixDfwConfig.  # noqa: E501
        :rtype: int
        """
        return self._active_flow_export_timeout

    @active_flow_export_timeout.setter
    def active_flow_export_timeout(self, active_flow_export_timeout):
        """Sets the active_flow_export_timeout of this IpfixDfwConfig.

        For long standing active flows, IPFIX records will be sent per timeout period   # noqa: E501

        :param active_flow_export_timeout: The active_flow_export_timeout of this IpfixDfwConfig.  # noqa: E501
        :type: int
        """

        self._active_flow_export_timeout = active_flow_export_timeout

    @property
    def template_parameters(self):
        """Gets the template_parameters of this IpfixDfwConfig.  # noqa: E501


        :return: The template_parameters of this IpfixDfwConfig.  # noqa: E501
        :rtype: IpfixDfwTemplateParameters
        """
        return self._template_parameters

    @template_parameters.setter
    def template_parameters(self, template_parameters):
        """Sets the template_parameters of this IpfixDfwConfig.


        :param template_parameters: The template_parameters of this IpfixDfwConfig.  # noqa: E501
        :type: IpfixDfwTemplateParameters
        """

        self._template_parameters = template_parameters

    @property
    def observation_domain_id(self):
        """Gets the observation_domain_id of this IpfixDfwConfig.  # noqa: E501

        An identifier that is unique to the exporting process and used to meter the Flows.   # noqa: E501

        :return: The observation_domain_id of this IpfixDfwConfig.  # noqa: E501
        :rtype: int
        """
        return self._observation_domain_id

    @observation_domain_id.setter
    def observation_domain_id(self, observation_domain_id):
        """Sets the observation_domain_id of this IpfixDfwConfig.

        An identifier that is unique to the exporting process and used to meter the Flows.   # noqa: E501

        :param observation_domain_id: The observation_domain_id of this IpfixDfwConfig.  # noqa: E501
        :type: int
        """
        if observation_domain_id is None:
            raise ValueError("Invalid value for `observation_domain_id`, must not be `None`")  # noqa: E501

        self._observation_domain_id = observation_domain_id

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
        if issubclass(IpfixDfwConfig, dict):
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
        if not isinstance(other, IpfixDfwConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
