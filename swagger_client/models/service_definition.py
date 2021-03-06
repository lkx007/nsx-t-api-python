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


class ServiceDefinition(object):
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
        'system_owned': 'bool',
        'display_name': 'str',
        'description': 'str',
        'tags': 'list[Tag]',
        'create_user': 'str',
        'protection': 'str',
        'create_time': 'int',
        'last_modified_time': 'int',
        'last_modified_user': 'str',
        'id': 'str',
        'resource_type': 'str',
        'service_deployment_spec': 'ServiceDeploymentSpec',
        'service_capability': 'ServiceCapability',
        'functionalities': 'list[str]',
        'attachment_point': 'list[str]',
        'service_manager_id': 'str',
        'vendor_id': 'str',
        'on_failure_policy': 'str',
        'transports': 'list[str]',
        'implementations': 'list[str]'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'system_owned': '_system_owned',
        'display_name': 'display_name',
        'description': 'description',
        'tags': 'tags',
        'create_user': '_create_user',
        'protection': '_protection',
        'create_time': '_create_time',
        'last_modified_time': '_last_modified_time',
        'last_modified_user': '_last_modified_user',
        'id': 'id',
        'resource_type': 'resource_type',
        'service_deployment_spec': 'service_deployment_spec',
        'service_capability': 'service_capability',
        'functionalities': 'functionalities',
        'attachment_point': 'attachment_point',
        'service_manager_id': 'service_manager_id',
        'vendor_id': 'vendor_id',
        'on_failure_policy': 'on_failure_policy',
        'transports': 'transports',
        'implementations': 'implementations'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, service_deployment_spec=None, service_capability=None, functionalities=None, attachment_point=None, service_manager_id=None, vendor_id=None, on_failure_policy='ALLOW', transports=None, implementations=None, *args, **kwargs):  # noqa: E501
        """ServiceDefinition - a model defined in Swagger"""  # noqa: E501
        self._system_owned = None
        self._display_name = None
        self._description = None
        self._tags = None
        self._create_user = None
        self._protection = None
        self._create_time = None
        self._last_modified_time = None
        self._last_modified_user = None
        self._id = None
        self._resource_type = None
        self._service_deployment_spec = None
        self._service_capability = None
        self._functionalities = None
        self._attachment_point = None
        self._service_manager_id = None
        self._vendor_id = None
        self._on_failure_policy = None
        self._transports = None
        self._implementations = None
        self.discriminator = None
        if system_owned is not None:
            self.system_owned = system_owned
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if create_user is not None:
            self.create_user = create_user
        if protection is not None:
            self.protection = protection
        if create_time is not None:
            self.create_time = create_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if last_modified_user is not None:
            self.last_modified_user = last_modified_user
        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        if service_deployment_spec is not None:
            self.service_deployment_spec = service_deployment_spec
        if service_capability is not None:
            self.service_capability = service_capability
        self.functionalities = functionalities
        if attachment_point is not None:
            self.attachment_point = attachment_point
        if service_manager_id is not None:
            self.service_manager_id = service_manager_id
        self.vendor_id = vendor_id
        if on_failure_policy is not None:
            self.on_failure_policy = on_failure_policy
        if transports is not None:
            self.transports = transports
        self.implementations = implementations
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this ServiceDefinition.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this ServiceDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this ServiceDefinition.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this ServiceDefinition.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this ServiceDefinition.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ServiceDefinition.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this ServiceDefinition.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this ServiceDefinition.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceDefinition.

        Description of this resource  # noqa: E501

        :param description: The description of this ServiceDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this ServiceDefinition.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this ServiceDefinition.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ServiceDefinition.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this ServiceDefinition.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this ServiceDefinition.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ServiceDefinition.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this ServiceDefinition.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this ServiceDefinition.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this ServiceDefinition.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this ServiceDefinition.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this ServiceDefinition.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this ServiceDefinition.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ServiceDefinition.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this ServiceDefinition.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this ServiceDefinition.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this ServiceDefinition.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this ServiceDefinition.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this ServiceDefinition.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this ServiceDefinition.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this ServiceDefinition.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this ServiceDefinition.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this ServiceDefinition.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceDefinition.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this ServiceDefinition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this ServiceDefinition.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ServiceDefinition.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this ServiceDefinition.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def service_deployment_spec(self):
        """Gets the service_deployment_spec of this ServiceDefinition.  # noqa: E501


        :return: The service_deployment_spec of this ServiceDefinition.  # noqa: E501
        :rtype: ServiceDeploymentSpec
        """
        return self._service_deployment_spec

    @service_deployment_spec.setter
    def service_deployment_spec(self, service_deployment_spec):
        """Sets the service_deployment_spec of this ServiceDefinition.


        :param service_deployment_spec: The service_deployment_spec of this ServiceDefinition.  # noqa: E501
        :type: ServiceDeploymentSpec
        """

        self._service_deployment_spec = service_deployment_spec

    @property
    def service_capability(self):
        """Gets the service_capability of this ServiceDefinition.  # noqa: E501


        :return: The service_capability of this ServiceDefinition.  # noqa: E501
        :rtype: ServiceCapability
        """
        return self._service_capability

    @service_capability.setter
    def service_capability(self, service_capability):
        """Sets the service_capability of this ServiceDefinition.


        :param service_capability: The service_capability of this ServiceDefinition.  # noqa: E501
        :type: ServiceCapability
        """

        self._service_capability = service_capability

    @property
    def functionalities(self):
        """Gets the functionalities of this ServiceDefinition.  # noqa: E501

        The capabilities provided by the services. Needs to be one or more of the following | NG_FW - Next Generation Firewall | IDS_IPS - Intrusion detection System / Intrusion Prevention System | NET_MON - Network Monitoring | HCX - Hybrid Cloud Exchange | BYOD - Bring Your Own Device | EPP - Endpoint Protection.(Third party AntiVirus partners using NXGI should use this functionality for the service)  # noqa: E501

        :return: The functionalities of this ServiceDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._functionalities

    @functionalities.setter
    def functionalities(self, functionalities):
        """Sets the functionalities of this ServiceDefinition.

        The capabilities provided by the services. Needs to be one or more of the following | NG_FW - Next Generation Firewall | IDS_IPS - Intrusion detection System / Intrusion Prevention System | NET_MON - Network Monitoring | HCX - Hybrid Cloud Exchange | BYOD - Bring Your Own Device | EPP - Endpoint Protection.(Third party AntiVirus partners using NXGI should use this functionality for the service)  # noqa: E501

        :param functionalities: The functionalities of this ServiceDefinition.  # noqa: E501
        :type: list[str]
        """
        if functionalities is None:
            raise ValueError("Invalid value for `functionalities`, must not be `None`")  # noqa: E501
        allowed_values = ["NG_FW", "IDS_IPS", "NET_MON", "HCX", "BYOD", "EPP"]  # noqa: E501
        if not set(functionalities).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `functionalities` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(functionalities) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._functionalities = functionalities

    @property
    def attachment_point(self):
        """Gets the attachment_point of this ServiceDefinition.  # noqa: E501

        The point at which the service is deployed/attached for redirecting the traffic to the the partner appliance. Attachment Point is required if Service caters to any functionality other than EPP.  # noqa: E501

        :return: The attachment_point of this ServiceDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachment_point

    @attachment_point.setter
    def attachment_point(self, attachment_point):
        """Sets the attachment_point of this ServiceDefinition.

        The point at which the service is deployed/attached for redirecting the traffic to the the partner appliance. Attachment Point is required if Service caters to any functionality other than EPP.  # noqa: E501

        :param attachment_point: The attachment_point of this ServiceDefinition.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["TIER0_LR", "TIER1_LR", "SERVICE_PLANE"]  # noqa: E501
        if not set(attachment_point).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `attachment_point` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(attachment_point) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._attachment_point = attachment_point

    @property
    def service_manager_id(self):
        """Gets the service_manager_id of this ServiceDefinition.  # noqa: E501

        ID of the service manager to which this service is attached with. This field is not set during creation of service. This field will be set explicitly when Service Manager is created successfully using this service.   # noqa: E501

        :return: The service_manager_id of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._service_manager_id

    @service_manager_id.setter
    def service_manager_id(self, service_manager_id):
        """Sets the service_manager_id of this ServiceDefinition.

        ID of the service manager to which this service is attached with. This field is not set during creation of service. This field will be set explicitly when Service Manager is created successfully using this service.   # noqa: E501

        :param service_manager_id: The service_manager_id of this ServiceDefinition.  # noqa: E501
        :type: str
        """

        self._service_manager_id = service_manager_id

    @property
    def vendor_id(self):
        """Gets the vendor_id of this ServiceDefinition.  # noqa: E501

        Id which is unique to a vendor or partner for which the service is created.  # noqa: E501

        :return: The vendor_id of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this ServiceDefinition.

        Id which is unique to a vendor or partner for which the service is created.  # noqa: E501

        :param vendor_id: The vendor_id of this ServiceDefinition.  # noqa: E501
        :type: str
        """
        if vendor_id is None:
            raise ValueError("Invalid value for `vendor_id`, must not be `None`")  # noqa: E501

        self._vendor_id = vendor_id

    @property
    def on_failure_policy(self):
        """Gets the on_failure_policy of this ServiceDefinition.  # noqa: E501

        Failure policy for the service tells datapath, the action to take i.e to Allow or Block traffic during failure scenarios. For north-south ServiceInsertion, failure policy in the service instance takes precedence. For east-west ServiceInsertion, failure policy in the service chain takes precedence. BLOCK is not supported for Endpoint protection (EPP) functionality.  # noqa: E501

        :return: The on_failure_policy of this ServiceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._on_failure_policy

    @on_failure_policy.setter
    def on_failure_policy(self, on_failure_policy):
        """Sets the on_failure_policy of this ServiceDefinition.

        Failure policy for the service tells datapath, the action to take i.e to Allow or Block traffic during failure scenarios. For north-south ServiceInsertion, failure policy in the service instance takes precedence. For east-west ServiceInsertion, failure policy in the service chain takes precedence. BLOCK is not supported for Endpoint protection (EPP) functionality.  # noqa: E501

        :param on_failure_policy: The on_failure_policy of this ServiceDefinition.  # noqa: E501
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
    def transports(self):
        """Gets the transports of this ServiceDefinition.  # noqa: E501

        Transport Type of the service, which is the mechanism of redirecting the traffic to the the partner appliance. Transport type is required if Service caters to any functionality other than EPP.  # noqa: E501

        :return: The transports of this ServiceDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._transports

    @transports.setter
    def transports(self, transports):
        """Sets the transports of this ServiceDefinition.

        Transport Type of the service, which is the mechanism of redirecting the traffic to the the partner appliance. Transport type is required if Service caters to any functionality other than EPP.  # noqa: E501

        :param transports: The transports of this ServiceDefinition.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["L2_BRIDGE", "L3_ROUTED", "NSH"]  # noqa: E501
        if not set(transports).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `transports` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(transports) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._transports = transports

    @property
    def implementations(self):
        """Gets the implementations of this ServiceDefinition.  # noqa: E501

        This indicates the insertion point of the service i.e whether the service will be used to protect North-South or East-West traffic in the datacenter.  # noqa: E501

        :return: The implementations of this ServiceDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._implementations

    @implementations.setter
    def implementations(self, implementations):
        """Sets the implementations of this ServiceDefinition.

        This indicates the insertion point of the service i.e whether the service will be used to protect North-South or East-West traffic in the datacenter.  # noqa: E501

        :param implementations: The implementations of this ServiceDefinition.  # noqa: E501
        :type: list[str]
        """
        if implementations is None:
            raise ValueError("Invalid value for `implementations`, must not be `None`")  # noqa: E501
        allowed_values = ["NORTH_SOUTH", "EAST_WEST"]  # noqa: E501
        if not set(implementations).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `implementations` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(implementations) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._implementations = implementations

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
        if issubclass(ServiceDefinition, dict):
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
        if not isinstance(other, ServiceDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
