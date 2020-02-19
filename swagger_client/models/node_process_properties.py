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


class NodeProcessProperties(object):
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
        'mem_used': 'int',
        'cpu_time': 'int',
        'ppid': 'int',
        'start_time': 'int',
        'process_name': 'str',
        'pid': 'int',
        'uptime': 'int',
        'mem_resident': 'int'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'mem_used': 'mem_used',
        'cpu_time': 'cpu_time',
        'ppid': 'ppid',
        'start_time': 'start_time',
        'process_name': 'process_name',
        'pid': 'pid',
        'uptime': 'uptime',
        'mem_resident': 'mem_resident'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, _self=None, links=None, schema=None, mem_used=None, cpu_time=None, ppid=None, start_time=None, process_name=None, pid=None, uptime=None, mem_resident=None, *args, **kwargs):  # noqa: E501
        """NodeProcessProperties - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._links = None
        self._schema = None
        self._mem_used = None
        self._cpu_time = None
        self._ppid = None
        self._start_time = None
        self._process_name = None
        self._pid = None
        self._uptime = None
        self._mem_resident = None
        self.discriminator = None
        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if mem_used is not None:
            self.mem_used = mem_used
        if cpu_time is not None:
            self.cpu_time = cpu_time
        if ppid is not None:
            self.ppid = ppid
        if start_time is not None:
            self.start_time = start_time
        if process_name is not None:
            self.process_name = process_name
        if pid is not None:
            self.pid = pid
        if uptime is not None:
            self.uptime = uptime
        if mem_resident is not None:
            self.mem_resident = mem_resident
        Resource.__init__(self, *args, **kwargs)

    @property
    def _self(self):
        """Gets the _self of this NodeProcessProperties.  # noqa: E501


        :return: The _self of this NodeProcessProperties.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this NodeProcessProperties.


        :param _self: The _self of this NodeProcessProperties.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this NodeProcessProperties.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this NodeProcessProperties.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NodeProcessProperties.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this NodeProcessProperties.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this NodeProcessProperties.  # noqa: E501

        Schema for this resource  # noqa: E501

        :return: The schema of this NodeProcessProperties.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this NodeProcessProperties.

        Schema for this resource  # noqa: E501

        :param schema: The schema of this NodeProcessProperties.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def mem_used(self):
        """Gets the mem_used of this NodeProcessProperties.  # noqa: E501

        Virtual memory used by process in bytes  # noqa: E501

        :return: The mem_used of this NodeProcessProperties.  # noqa: E501
        :rtype: int
        """
        return self._mem_used

    @mem_used.setter
    def mem_used(self, mem_used):
        """Sets the mem_used of this NodeProcessProperties.

        Virtual memory used by process in bytes  # noqa: E501

        :param mem_used: The mem_used of this NodeProcessProperties.  # noqa: E501
        :type: int
        """

        self._mem_used = mem_used

    @property
    def cpu_time(self):
        """Gets the cpu_time of this NodeProcessProperties.  # noqa: E501

        CPU time (user and system) consumed by process in milliseconds  # noqa: E501

        :return: The cpu_time of this NodeProcessProperties.  # noqa: E501
        :rtype: int
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        """Sets the cpu_time of this NodeProcessProperties.

        CPU time (user and system) consumed by process in milliseconds  # noqa: E501

        :param cpu_time: The cpu_time of this NodeProcessProperties.  # noqa: E501
        :type: int
        """

        self._cpu_time = cpu_time

    @property
    def ppid(self):
        """Gets the ppid of this NodeProcessProperties.  # noqa: E501

        Parent process id  # noqa: E501

        :return: The ppid of this NodeProcessProperties.  # noqa: E501
        :rtype: int
        """
        return self._ppid

    @ppid.setter
    def ppid(self, ppid):
        """Sets the ppid of this NodeProcessProperties.

        Parent process id  # noqa: E501

        :param ppid: The ppid of this NodeProcessProperties.  # noqa: E501
        :type: int
        """

        self._ppid = ppid

    @property
    def start_time(self):
        """Gets the start_time of this NodeProcessProperties.  # noqa: E501

        Process start time expressed in milliseconds since epoch  # noqa: E501

        :return: The start_time of this NodeProcessProperties.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this NodeProcessProperties.

        Process start time expressed in milliseconds since epoch  # noqa: E501

        :param start_time: The start_time of this NodeProcessProperties.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def process_name(self):
        """Gets the process_name of this NodeProcessProperties.  # noqa: E501

        Process name  # noqa: E501

        :return: The process_name of this NodeProcessProperties.  # noqa: E501
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        """Sets the process_name of this NodeProcessProperties.

        Process name  # noqa: E501

        :param process_name: The process_name of this NodeProcessProperties.  # noqa: E501
        :type: str
        """

        self._process_name = process_name

    @property
    def pid(self):
        """Gets the pid of this NodeProcessProperties.  # noqa: E501

        Process id  # noqa: E501

        :return: The pid of this NodeProcessProperties.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this NodeProcessProperties.

        Process id  # noqa: E501

        :param pid: The pid of this NodeProcessProperties.  # noqa: E501
        :type: int
        """

        self._pid = pid

    @property
    def uptime(self):
        """Gets the uptime of this NodeProcessProperties.  # noqa: E501

        Milliseconds since process started  # noqa: E501

        :return: The uptime of this NodeProcessProperties.  # noqa: E501
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this NodeProcessProperties.

        Milliseconds since process started  # noqa: E501

        :param uptime: The uptime of this NodeProcessProperties.  # noqa: E501
        :type: int
        """

        self._uptime = uptime

    @property
    def mem_resident(self):
        """Gets the mem_resident of this NodeProcessProperties.  # noqa: E501

        Resident set size of process in bytes  # noqa: E501

        :return: The mem_resident of this NodeProcessProperties.  # noqa: E501
        :rtype: int
        """
        return self._mem_resident

    @mem_resident.setter
    def mem_resident(self, mem_resident):
        """Sets the mem_resident of this NodeProcessProperties.

        Resident set size of process in bytes  # noqa: E501

        :param mem_resident: The mem_resident of this NodeProcessProperties.  # noqa: E501
        :type: int
        """

        self._mem_resident = mem_resident

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
        if issubclass(NodeProcessProperties, dict):
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
        if not isinstance(other, NodeProcessProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
