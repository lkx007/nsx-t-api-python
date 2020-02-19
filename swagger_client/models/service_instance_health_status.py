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


class ServiceInstanceHealthStatus(object):
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
        'is_sva_mux_incompatible': 'bool',
        'connect_timestamp': 'str',
        'mux_incompatible_version': 'str',
        'solution_version': 'str',
        'sync_time': 'str',
        'solution_status': 'str',
        'is_stale': 'bool',
        'mux_connected_status': 'str'
    }

    attribute_map = {
        'is_sva_mux_incompatible': 'is_sva_mux_incompatible',
        'connect_timestamp': 'connect_timestamp',
        'mux_incompatible_version': 'mux_incompatible_version',
        'solution_version': 'solution_version',
        'sync_time': 'sync_time',
        'solution_status': 'solution_status',
        'is_stale': 'is_stale',
        'mux_connected_status': 'mux_connected_status'
    }

    def __init__(self, is_sva_mux_incompatible=None, connect_timestamp=None, mux_incompatible_version=None, solution_version=None, sync_time=None, solution_status=None, is_stale=None, mux_connected_status=None):  # noqa: E501
        """ServiceInstanceHealthStatus - a model defined in Swagger"""  # noqa: E501
        self._is_sva_mux_incompatible = None
        self._connect_timestamp = None
        self._mux_incompatible_version = None
        self._solution_version = None
        self._sync_time = None
        self._solution_status = None
        self._is_stale = None
        self._mux_connected_status = None
        self.discriminator = None
        if is_sva_mux_incompatible is not None:
            self.is_sva_mux_incompatible = is_sva_mux_incompatible
        if connect_timestamp is not None:
            self.connect_timestamp = connect_timestamp
        if mux_incompatible_version is not None:
            self.mux_incompatible_version = mux_incompatible_version
        if solution_version is not None:
            self.solution_version = solution_version
        if sync_time is not None:
            self.sync_time = sync_time
        if solution_status is not None:
            self.solution_status = solution_status
        if is_stale is not None:
            self.is_stale = is_stale
        if mux_connected_status is not None:
            self.mux_connected_status = mux_connected_status

    @property
    def is_sva_mux_incompatible(self):
        """Gets the is_sva_mux_incompatible of this ServiceInstanceHealthStatus.  # noqa: E501

        Protocol version might be different in both Mux and SVA.  # noqa: E501

        :return: The is_sva_mux_incompatible of this ServiceInstanceHealthStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_sva_mux_incompatible

    @is_sva_mux_incompatible.setter
    def is_sva_mux_incompatible(self, is_sva_mux_incompatible):
        """Sets the is_sva_mux_incompatible of this ServiceInstanceHealthStatus.

        Protocol version might be different in both Mux and SVA.  # noqa: E501

        :param is_sva_mux_incompatible: The is_sva_mux_incompatible of this ServiceInstanceHealthStatus.  # noqa: E501
        :type: bool
        """

        self._is_sva_mux_incompatible = is_sva_mux_incompatible

    @property
    def connect_timestamp(self):
        """Gets the connect_timestamp of this ServiceInstanceHealthStatus.  # noqa: E501

        Latest timestamp when mux was connected to SVA.  # noqa: E501

        :return: The connect_timestamp of this ServiceInstanceHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._connect_timestamp

    @connect_timestamp.setter
    def connect_timestamp(self, connect_timestamp):
        """Sets the connect_timestamp of this ServiceInstanceHealthStatus.

        Latest timestamp when mux was connected to SVA.  # noqa: E501

        :param connect_timestamp: The connect_timestamp of this ServiceInstanceHealthStatus.  # noqa: E501
        :type: str
        """

        self._connect_timestamp = connect_timestamp

    @property
    def mux_incompatible_version(self):
        """Gets the mux_incompatible_version of this ServiceInstanceHealthStatus.  # noqa: E501

        Mux version when Mux and SVA are incompatible  # noqa: E501

        :return: The mux_incompatible_version of this ServiceInstanceHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._mux_incompatible_version

    @mux_incompatible_version.setter
    def mux_incompatible_version(self, mux_incompatible_version):
        """Sets the mux_incompatible_version of this ServiceInstanceHealthStatus.

        Mux version when Mux and SVA are incompatible  # noqa: E501

        :param mux_incompatible_version: The mux_incompatible_version of this ServiceInstanceHealthStatus.  # noqa: E501
        :type: str
        """

        self._mux_incompatible_version = mux_incompatible_version

    @property
    def solution_version(self):
        """Gets the solution_version of this ServiceInstanceHealthStatus.  # noqa: E501

        Version of third party partner solution application.  # noqa: E501

        :return: The solution_version of this ServiceInstanceHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._solution_version

    @solution_version.setter
    def solution_version(self, solution_version):
        """Sets the solution_version of this ServiceInstanceHealthStatus.

        Version of third party partner solution application.  # noqa: E501

        :param solution_version: The solution_version of this ServiceInstanceHealthStatus.  # noqa: E501
        :type: str
        """

        self._solution_version = solution_version

    @property
    def sync_time(self):
        """Gets the sync_time of this ServiceInstanceHealthStatus.  # noqa: E501

        Latest timestamp when health status is received.  # noqa: E501

        :return: The sync_time of this ServiceInstanceHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._sync_time

    @sync_time.setter
    def sync_time(self, sync_time):
        """Sets the sync_time of this ServiceInstanceHealthStatus.

        Latest timestamp when health status is received.  # noqa: E501

        :param sync_time: The sync_time of this ServiceInstanceHealthStatus.  # noqa: E501
        :type: str
        """

        self._sync_time = sync_time

    @property
    def solution_status(self):
        """Gets the solution_status of this ServiceInstanceHealthStatus.  # noqa: E501

        Status of third party partner solution application.  # noqa: E501

        :return: The solution_status of this ServiceInstanceHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._solution_status

    @solution_status.setter
    def solution_status(self, solution_status):
        """Sets the solution_status of this ServiceInstanceHealthStatus.

        Status of third party partner solution application.  # noqa: E501

        :param solution_status: The solution_status of this ServiceInstanceHealthStatus.  # noqa: E501
        :type: str
        """

        self._solution_status = solution_status

    @property
    def is_stale(self):
        """Gets the is_stale of this ServiceInstanceHealthStatus.  # noqa: E501

        The parameter is set if the last received health status is older than the predefined interval.   # noqa: E501

        :return: The is_stale of this ServiceInstanceHealthStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_stale

    @is_stale.setter
    def is_stale(self, is_stale):
        """Sets the is_stale of this ServiceInstanceHealthStatus.

        The parameter is set if the last received health status is older than the predefined interval.   # noqa: E501

        :param is_stale: The is_stale of this ServiceInstanceHealthStatus.  # noqa: E501
        :type: bool
        """

        self._is_stale = is_stale

    @property
    def mux_connected_status(self):
        """Gets the mux_connected_status of this ServiceInstanceHealthStatus.  # noqa: E501

        Status of multiplexer which forwards the events from guest virtual machines to the partner appliance.  # noqa: E501

        :return: The mux_connected_status of this ServiceInstanceHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._mux_connected_status

    @mux_connected_status.setter
    def mux_connected_status(self, mux_connected_status):
        """Sets the mux_connected_status of this ServiceInstanceHealthStatus.

        Status of multiplexer which forwards the events from guest virtual machines to the partner appliance.  # noqa: E501

        :param mux_connected_status: The mux_connected_status of this ServiceInstanceHealthStatus.  # noqa: E501
        :type: str
        """

        self._mux_connected_status = mux_connected_status

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
        if issubclass(ServiceInstanceHealthStatus, dict):
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
        if not isinstance(other, ServiceInstanceHealthStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
