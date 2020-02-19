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


class ClusterGroupServiceLeader(object):
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
        'service_name': 'str',
        'lease_version': 'int',
        'leader_uuid': 'str'
    }

    attribute_map = {
        'service_name': 'service_name',
        'lease_version': 'lease_version',
        'leader_uuid': 'leader_uuid'
    }

    def __init__(self, service_name=None, lease_version=None, leader_uuid=None):  # noqa: E501
        """ClusterGroupServiceLeader - a model defined in Swagger"""  # noqa: E501
        self._service_name = None
        self._lease_version = None
        self._leader_uuid = None
        self.discriminator = None
        if service_name is not None:
            self.service_name = service_name
        if lease_version is not None:
            self.lease_version = lease_version
        if leader_uuid is not None:
            self.leader_uuid = leader_uuid

    @property
    def service_name(self):
        """Gets the service_name of this ClusterGroupServiceLeader.  # noqa: E501

        Name of the service  # noqa: E501

        :return: The service_name of this ClusterGroupServiceLeader.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ClusterGroupServiceLeader.

        Name of the service  # noqa: E501

        :param service_name: The service_name of this ClusterGroupServiceLeader.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def lease_version(self):
        """Gets the lease_version of this ClusterGroupServiceLeader.  # noqa: E501

        Number of times the lease has been renewed  # noqa: E501

        :return: The lease_version of this ClusterGroupServiceLeader.  # noqa: E501
        :rtype: int
        """
        return self._lease_version

    @lease_version.setter
    def lease_version(self, lease_version):
        """Sets the lease_version of this ClusterGroupServiceLeader.

        Number of times the lease has been renewed  # noqa: E501

        :param lease_version: The lease_version of this ClusterGroupServiceLeader.  # noqa: E501
        :type: int
        """

        self._lease_version = lease_version

    @property
    def leader_uuid(self):
        """Gets the leader_uuid of this ClusterGroupServiceLeader.  # noqa: E501

        Member UUID of the leader  # noqa: E501

        :return: The leader_uuid of this ClusterGroupServiceLeader.  # noqa: E501
        :rtype: str
        """
        return self._leader_uuid

    @leader_uuid.setter
    def leader_uuid(self, leader_uuid):
        """Sets the leader_uuid of this ClusterGroupServiceLeader.

        Member UUID of the leader  # noqa: E501

        :param leader_uuid: The leader_uuid of this ClusterGroupServiceLeader.  # noqa: E501
        :type: str
        """

        self._leader_uuid = leader_uuid

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
        if issubclass(ClusterGroupServiceLeader, dict):
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
        if not isinstance(other, ClusterGroupServiceLeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
