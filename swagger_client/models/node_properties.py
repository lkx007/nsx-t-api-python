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


class NodeProperties(object):
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
        '_self': 'SelfResourceLink',
        'links': 'list[ResourceLink]',
        'schema': 'str',
        'system_time': 'int',
        'node_uuid': 'str',
        'motd': 'object',
        'cli_timeout': 'int',
        'kernel_version': 'str',
        'export_type': 'str',
        'hostname': 'str',
        'product_version': 'str',
        'node_version': 'str',
        'system_datetime': 'str',
        'fully_qualified_domain_name': 'str',
        'timezone': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'system_time': 'system_time',
        'node_uuid': 'node_uuid',
        'motd': 'motd',
        'cli_timeout': 'cli_timeout',
        'kernel_version': 'kernel_version',
        'export_type': 'export_type',
        'hostname': 'hostname',
        'product_version': 'product_version',
        'node_version': 'node_version',
        'system_datetime': 'system_datetime',
        'fully_qualified_domain_name': 'fully_qualified_domain_name',
        'timezone': 'timezone'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, _self=None, links=None, schema=None, system_time=None, node_uuid=None, motd=None, cli_timeout=None, kernel_version=None, export_type=None, hostname=None, product_version=None, node_version=None, system_datetime=None, fully_qualified_domain_name=None, timezone=None, *args, **kwargs):  # noqa: E501
        """NodeProperties - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._links = None
        self._schema = None
        self._system_time = None
        self._node_uuid = None
        self._motd = None
        self._cli_timeout = None
        self._kernel_version = None
        self._export_type = None
        self._hostname = None
        self._product_version = None
        self._node_version = None
        self._system_datetime = None
        self._fully_qualified_domain_name = None
        self._timezone = None
        self.discriminator = None
        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if system_time is not None:
            self.system_time = system_time
        if node_uuid is not None:
            self.node_uuid = node_uuid
        if motd is not None:
            self.motd = motd
        if cli_timeout is not None:
            self.cli_timeout = cli_timeout
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if export_type is not None:
            self.export_type = export_type
        if hostname is not None:
            self.hostname = hostname
        if product_version is not None:
            self.product_version = product_version
        if node_version is not None:
            self.node_version = node_version
        if system_datetime is not None:
            self.system_datetime = system_datetime
        if fully_qualified_domain_name is not None:
            self.fully_qualified_domain_name = fully_qualified_domain_name
        if timezone is not None:
            self.timezone = timezone
        Resource.__init__(self, *args, **kwargs)

    @property
    def _self(self):
        """Gets the _self of this NodeProperties.  # noqa: E501


        :return: The _self of this NodeProperties.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this NodeProperties.


        :param _self: The _self of this NodeProperties.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this NodeProperties.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this NodeProperties.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NodeProperties.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this NodeProperties.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this NodeProperties.  # noqa: E501

        Schema for this resource  # noqa: E501

        :return: The schema of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this NodeProperties.

        Schema for this resource  # noqa: E501

        :param schema: The schema of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def system_time(self):
        """Gets the system_time of this NodeProperties.  # noqa: E501

        Current time expressed in milliseconds since epoch  # noqa: E501

        :return: The system_time of this NodeProperties.  # noqa: E501
        :rtype: int
        """
        return self._system_time

    @system_time.setter
    def system_time(self, system_time):
        """Sets the system_time of this NodeProperties.

        Current time expressed in milliseconds since epoch  # noqa: E501

        :param system_time: The system_time of this NodeProperties.  # noqa: E501
        :type: int
        """

        self._system_time = system_time

    @property
    def node_uuid(self):
        """Gets the node_uuid of this NodeProperties.  # noqa: E501

        Node Unique Identifier  # noqa: E501

        :return: The node_uuid of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._node_uuid

    @node_uuid.setter
    def node_uuid(self, node_uuid):
        """Sets the node_uuid of this NodeProperties.

        Node Unique Identifier  # noqa: E501

        :param node_uuid: The node_uuid of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._node_uuid = node_uuid

    @property
    def motd(self):
        """Gets the motd of this NodeProperties.  # noqa: E501

        Message of the day to display when users login to node using the NSX CLI  # noqa: E501

        :return: The motd of this NodeProperties.  # noqa: E501
        :rtype: object
        """
        return self._motd

    @motd.setter
    def motd(self, motd):
        """Sets the motd of this NodeProperties.

        Message of the day to display when users login to node using the NSX CLI  # noqa: E501

        :param motd: The motd of this NodeProperties.  # noqa: E501
        :type: object
        """

        self._motd = motd

    @property
    def cli_timeout(self):
        """Gets the cli_timeout of this NodeProperties.  # noqa: E501

        NSX CLI inactivity timeout, set to 0 to configure no timeout  # noqa: E501

        :return: The cli_timeout of this NodeProperties.  # noqa: E501
        :rtype: int
        """
        return self._cli_timeout

    @cli_timeout.setter
    def cli_timeout(self, cli_timeout):
        """Sets the cli_timeout of this NodeProperties.

        NSX CLI inactivity timeout, set to 0 to configure no timeout  # noqa: E501

        :param cli_timeout: The cli_timeout of this NodeProperties.  # noqa: E501
        :type: int
        """

        self._cli_timeout = cli_timeout

    @property
    def kernel_version(self):
        """Gets the kernel_version of this NodeProperties.  # noqa: E501

        Kernel version  # noqa: E501

        :return: The kernel_version of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this NodeProperties.

        Kernel version  # noqa: E501

        :param kernel_version: The kernel_version of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._kernel_version = kernel_version

    @property
    def export_type(self):
        """Gets the export_type of this NodeProperties.  # noqa: E501

        Export restrictions in effect, if any  # noqa: E501

        :return: The export_type of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        """Sets the export_type of this NodeProperties.

        Export restrictions in effect, if any  # noqa: E501

        :param export_type: The export_type of this NodeProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["RESTRICTED", "UNRESTRICTED"]  # noqa: E501
        if export_type not in allowed_values:
            raise ValueError(
                "Invalid value for `export_type` ({0}), must be one of {1}"  # noqa: E501
                .format(export_type, allowed_values)
            )

        self._export_type = export_type

    @property
    def hostname(self):
        """Gets the hostname of this NodeProperties.  # noqa: E501

        Host name or fully qualified domain name of node  # noqa: E501

        :return: The hostname of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this NodeProperties.

        Host name or fully qualified domain name of node  # noqa: E501

        :param hostname: The hostname of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def product_version(self):
        """Gets the product_version of this NodeProperties.  # noqa: E501

        Product version  # noqa: E501

        :return: The product_version of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this NodeProperties.

        Product version  # noqa: E501

        :param product_version: The product_version of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._product_version = product_version

    @property
    def node_version(self):
        """Gets the node_version of this NodeProperties.  # noqa: E501

        Node version  # noqa: E501

        :return: The node_version of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._node_version

    @node_version.setter
    def node_version(self, node_version):
        """Sets the node_version of this NodeProperties.

        Node version  # noqa: E501

        :param node_version: The node_version of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._node_version = node_version

    @property
    def system_datetime(self):
        """Gets the system_datetime of this NodeProperties.  # noqa: E501

        System date time in UTC  # noqa: E501

        :return: The system_datetime of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._system_datetime

    @system_datetime.setter
    def system_datetime(self, system_datetime):
        """Sets the system_datetime of this NodeProperties.

        System date time in UTC  # noqa: E501

        :param system_datetime: The system_datetime of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._system_datetime = system_datetime

    @property
    def fully_qualified_domain_name(self):
        """Gets the fully_qualified_domain_name of this NodeProperties.  # noqa: E501

        Fully qualified domain name  # noqa: E501

        :return: The fully_qualified_domain_name of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._fully_qualified_domain_name

    @fully_qualified_domain_name.setter
    def fully_qualified_domain_name(self, fully_qualified_domain_name):
        """Sets the fully_qualified_domain_name of this NodeProperties.

        Fully qualified domain name  # noqa: E501

        :param fully_qualified_domain_name: The fully_qualified_domain_name of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._fully_qualified_domain_name = fully_qualified_domain_name

    @property
    def timezone(self):
        """Gets the timezone of this NodeProperties.  # noqa: E501

        Timezone  # noqa: E501

        :return: The timezone of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this NodeProperties.

        Timezone  # noqa: E501

        :param timezone: The timezone of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if issubclass(NodeProperties, dict):
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
        if not isinstance(other, NodeProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
