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


class ServiceInstance(object):
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
        'on_failure_policy': 'str',
        'transport_type': 'str',
        'resource_type': 'str',
        'service_id': 'str',
        'deployment_spec_name': 'str',
        'instance_deployment_template': 'DeploymentTemplate',
        'implementation_type': 'str',
        'attachment_point': 'str',
        'instance_deployment_config': 'InstanceDeploymentConfig',
        'deployment_mode': 'str',
        'deployed_to': 'list[ResourceReference]',
        'service_deployment_id': 'str'
    }
    if hasattr(BaseServiceInstance, "swagger_types"):
        swagger_types.update(BaseServiceInstance.swagger_types)

    attribute_map = {
        'on_failure_policy': 'on_failure_policy',
        'transport_type': 'transport_type',
        'resource_type': 'resource_type',
        'service_id': 'service_id',
        'deployment_spec_name': 'deployment_spec_name',
        'instance_deployment_template': 'instance_deployment_template',
        'implementation_type': 'implementation_type',
        'attachment_point': 'attachment_point',
        'instance_deployment_config': 'instance_deployment_config',
        'deployment_mode': 'deployment_mode',
        'deployed_to': 'deployed_to',
        'service_deployment_id': 'service_deployment_id'
    }
    if hasattr(BaseServiceInstance, "attribute_map"):
        attribute_map.update(BaseServiceInstance.attribute_map)

    def __init__(self, on_failure_policy=None, transport_type=None, resource_type=None, service_id=None, deployment_spec_name=None, instance_deployment_template=None, implementation_type=None, attachment_point=None, instance_deployment_config=None, deployment_mode='ACTIVE_STANDBY', deployed_to=None, service_deployment_id=None, *args, **kwargs):  # noqa: E501
        """ServiceInstance - a model defined in Swagger"""  # noqa: E501
        self._on_failure_policy = None
        self._transport_type = None
        self._resource_type = None
        self._service_id = None
        self._deployment_spec_name = None
        self._instance_deployment_template = None
        self._implementation_type = None
        self._attachment_point = None
        self._instance_deployment_config = None
        self._deployment_mode = None
        self._deployed_to = None
        self._service_deployment_id = None
        self.discriminator = None
        if on_failure_policy is not None:
            self.on_failure_policy = on_failure_policy
        self.transport_type = transport_type
        self.resource_type = resource_type
        if service_id is not None:
            self.service_id = service_id
        self.deployment_spec_name = deployment_spec_name
        self.instance_deployment_template = instance_deployment_template
        self.implementation_type = implementation_type
        self.attachment_point = attachment_point
        if instance_deployment_config is not None:
            self.instance_deployment_config = instance_deployment_config
        self.deployment_mode = deployment_mode
        self.deployed_to = deployed_to
        if service_deployment_id is not None:
            self.service_deployment_id = service_deployment_id
        BaseServiceInstance.__init__(self, *args, **kwargs)

    @property
    def on_failure_policy(self):
        """Gets the on_failure_policy of this ServiceInstance.  # noqa: E501

        Failure policy of the service instance - if it has to be different from the service. By default the service instance inherits the FailurePolicy of the service it belongs to.  # noqa: E501

        :return: The on_failure_policy of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._on_failure_policy

    @on_failure_policy.setter
    def on_failure_policy(self, on_failure_policy):
        """Sets the on_failure_policy of this ServiceInstance.

        Failure policy of the service instance - if it has to be different from the service. By default the service instance inherits the FailurePolicy of the service it belongs to.  # noqa: E501

        :param on_failure_policy: The on_failure_policy of this ServiceInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALLOW", "BLOCK"]  # noqa: E501
        if on_failure_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `on_failure_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(on_failure_policy, allowed_values)
            )

        self._on_failure_policy = on_failure_policy

    @property
    def transport_type(self):
        """Gets the transport_type of this ServiceInstance.  # noqa: E501

        Transport to be used by this service instance for deploying the Service-VM. This field is to be set Not Applicable(NA) if the service only caters to functionality EPP(Endpoint Protection).  # noqa: E501

        :return: The transport_type of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """Sets the transport_type of this ServiceInstance.

        Transport to be used by this service instance for deploying the Service-VM. This field is to be set Not Applicable(NA) if the service only caters to functionality EPP(Endpoint Protection).  # noqa: E501

        :param transport_type: The transport_type of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if transport_type is None:
            raise ValueError("Invalid value for `transport_type`, must not be `None`")  # noqa: E501
        allowed_values = ["L2_BRIDGE", "L3_ROUTED", "NSH", "NA"]  # noqa: E501
        if transport_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transport_type, allowed_values)
            )

        self._transport_type = transport_type

    @property
    def resource_type(self):
        """Gets the resource_type of this ServiceInstance.  # noqa: E501

        ServiceInstance is used when NSX handles the lifecyle of   appliance. Deployment and appliance related all the information is necessary. ByodServiceInstance is a custom instance to be used when NSX is not handling   the lifecycles of appliance/s. User will manage their own appliance (BYOD)   to connect with NSX. VirtualServiceInstance is a a custom instance to be used when NSX is not   handling the lifecycle of an appliance and when the user is not bringing   their own appliance.   # noqa: E501

        :return: The resource_type of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ServiceInstance.

        ServiceInstance is used when NSX handles the lifecyle of   appliance. Deployment and appliance related all the information is necessary. ByodServiceInstance is a custom instance to be used when NSX is not handling   the lifecycles of appliance/s. User will manage their own appliance (BYOD)   to connect with NSX. VirtualServiceInstance is a a custom instance to be used when NSX is not   handling the lifecycle of an appliance and when the user is not bringing   their own appliance.   # noqa: E501

        :param resource_type: The resource_type of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ServiceInstance", "ByodServiceInstance", "VirtualServiceInstance"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def service_id(self):
        """Gets the service_id of this ServiceInstance.  # noqa: E501

        The Service to which the service instance is associated.  # noqa: E501

        :return: The service_id of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ServiceInstance.

        The Service to which the service instance is associated.  # noqa: E501

        :param service_id: The service_id of this ServiceInstance.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def deployment_spec_name(self):
        """Gets the deployment_spec_name of this ServiceInstance.  # noqa: E501

        Name of the deployment spec to be used by this service instance.  # noqa: E501

        :return: The deployment_spec_name of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._deployment_spec_name

    @deployment_spec_name.setter
    def deployment_spec_name(self, deployment_spec_name):
        """Sets the deployment_spec_name of this ServiceInstance.

        Name of the deployment spec to be used by this service instance.  # noqa: E501

        :param deployment_spec_name: The deployment_spec_name of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if deployment_spec_name is None:
            raise ValueError("Invalid value for `deployment_spec_name`, must not be `None`")  # noqa: E501

        self._deployment_spec_name = deployment_spec_name

    @property
    def instance_deployment_template(self):
        """Gets the instance_deployment_template of this ServiceInstance.  # noqa: E501


        :return: The instance_deployment_template of this ServiceInstance.  # noqa: E501
        :rtype: DeploymentTemplate
        """
        return self._instance_deployment_template

    @instance_deployment_template.setter
    def instance_deployment_template(self, instance_deployment_template):
        """Sets the instance_deployment_template of this ServiceInstance.


        :param instance_deployment_template: The instance_deployment_template of this ServiceInstance.  # noqa: E501
        :type: DeploymentTemplate
        """
        if instance_deployment_template is None:
            raise ValueError("Invalid value for `instance_deployment_template`, must not be `None`")  # noqa: E501

        self._instance_deployment_template = instance_deployment_template

    @property
    def implementation_type(self):
        """Gets the implementation_type of this ServiceInstance.  # noqa: E501

        Implementation to be used by this service instance for deploying the Service-VM.  # noqa: E501

        :return: The implementation_type of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._implementation_type

    @implementation_type.setter
    def implementation_type(self, implementation_type):
        """Sets the implementation_type of this ServiceInstance.

        Implementation to be used by this service instance for deploying the Service-VM.  # noqa: E501

        :param implementation_type: The implementation_type of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if implementation_type is None:
            raise ValueError("Invalid value for `implementation_type`, must not be `None`")  # noqa: E501
        allowed_values = ["NORTH_SOUTH", "EAST_WEST"]  # noqa: E501
        if implementation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `implementation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(implementation_type, allowed_values)
            )

        self._implementation_type = implementation_type

    @property
    def attachment_point(self):
        """Gets the attachment_point of this ServiceInstance.  # noqa: E501

        Attachment point to be used by this service instance for deploying the Service-VM.  # noqa: E501

        :return: The attachment_point of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._attachment_point

    @attachment_point.setter
    def attachment_point(self, attachment_point):
        """Sets the attachment_point of this ServiceInstance.

        Attachment point to be used by this service instance for deploying the Service-VM.  # noqa: E501

        :param attachment_point: The attachment_point of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if attachment_point is None:
            raise ValueError("Invalid value for `attachment_point`, must not be `None`")  # noqa: E501
        allowed_values = ["TIER0_LR", "TIER1_LR", "SERVICE_PLANE", "HOST"]  # noqa: E501
        if attachment_point not in allowed_values:
            raise ValueError(
                "Invalid value for `attachment_point` ({0}), must be one of {1}"  # noqa: E501
                .format(attachment_point, allowed_values)
            )

        self._attachment_point = attachment_point

    @property
    def instance_deployment_config(self):
        """Gets the instance_deployment_config of this ServiceInstance.  # noqa: E501


        :return: The instance_deployment_config of this ServiceInstance.  # noqa: E501
        :rtype: InstanceDeploymentConfig
        """
        return self._instance_deployment_config

    @instance_deployment_config.setter
    def instance_deployment_config(self, instance_deployment_config):
        """Sets the instance_deployment_config of this ServiceInstance.


        :param instance_deployment_config: The instance_deployment_config of this ServiceInstance.  # noqa: E501
        :type: InstanceDeploymentConfig
        """

        self._instance_deployment_config = instance_deployment_config

    @property
    def deployment_mode(self):
        """Gets the deployment_mode of this ServiceInstance.  # noqa: E501

        Deployment mode specifies where the partner appliance will be deployed in HA or non-HA i.e standalone mode.  # noqa: E501

        :return: The deployment_mode of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._deployment_mode

    @deployment_mode.setter
    def deployment_mode(self, deployment_mode):
        """Sets the deployment_mode of this ServiceInstance.

        Deployment mode specifies where the partner appliance will be deployed in HA or non-HA i.e standalone mode.  # noqa: E501

        :param deployment_mode: The deployment_mode of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if deployment_mode is None:
            raise ValueError("Invalid value for `deployment_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["STAND_ALONE", "ACTIVE_STANDBY"]  # noqa: E501
        if deployment_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_mode, allowed_values)
            )

        self._deployment_mode = deployment_mode

    @property
    def deployed_to(self):
        """Gets the deployed_to of this ServiceInstance.  # noqa: E501

        List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion.  # noqa: E501

        :return: The deployed_to of this ServiceInstance.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._deployed_to

    @deployed_to.setter
    def deployed_to(self, deployed_to):
        """Sets the deployed_to of this ServiceInstance.

        List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion.  # noqa: E501

        :param deployed_to: The deployed_to of this ServiceInstance.  # noqa: E501
        :type: list[ResourceReference]
        """
        if deployed_to is None:
            raise ValueError("Invalid value for `deployed_to`, must not be `None`")  # noqa: E501

        self._deployed_to = deployed_to

    @property
    def service_deployment_id(self):
        """Gets the service_deployment_id of this ServiceInstance.  # noqa: E501

        Id of the Service Deployment using which the instances were deployed. Its available only for instances that were deployed using service deployment API.  # noqa: E501

        :return: The service_deployment_id of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._service_deployment_id

    @service_deployment_id.setter
    def service_deployment_id(self, service_deployment_id):
        """Sets the service_deployment_id of this ServiceInstance.

        Id of the Service Deployment using which the instances were deployed. Its available only for instances that were deployed using service deployment API.  # noqa: E501

        :param service_deployment_id: The service_deployment_id of this ServiceInstance.  # noqa: E501
        :type: str
        """

        self._service_deployment_id = service_deployment_id

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
        if issubclass(ServiceInstance, dict):
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
        if not isinstance(other, ServiceInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
