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


class EdgeClusterMemberAllocationProfile(object):
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
        'allocation_pool': 'EdgeClusterMemberAllocationPool',
        'enable_standby_relocation': 'bool'
    }

    attribute_map = {
        'allocation_pool': 'allocation_pool',
        'enable_standby_relocation': 'enable_standby_relocation'
    }

    def __init__(self, allocation_pool=None, enable_standby_relocation=False):  # noqa: E501
        """EdgeClusterMemberAllocationProfile - a model defined in Swagger"""  # noqa: E501
        self._allocation_pool = None
        self._enable_standby_relocation = None
        self.discriminator = None
        if allocation_pool is not None:
            self.allocation_pool = allocation_pool
        if enable_standby_relocation is not None:
            self.enable_standby_relocation = enable_standby_relocation

    @property
    def allocation_pool(self):
        """Gets the allocation_pool of this EdgeClusterMemberAllocationProfile.  # noqa: E501


        :return: The allocation_pool of this EdgeClusterMemberAllocationProfile.  # noqa: E501
        :rtype: EdgeClusterMemberAllocationPool
        """
        return self._allocation_pool

    @allocation_pool.setter
    def allocation_pool(self, allocation_pool):
        """Sets the allocation_pool of this EdgeClusterMemberAllocationProfile.


        :param allocation_pool: The allocation_pool of this EdgeClusterMemberAllocationProfile.  # noqa: E501
        :type: EdgeClusterMemberAllocationPool
        """

        self._allocation_pool = allocation_pool

    @property
    def enable_standby_relocation(self):
        """Gets the enable_standby_relocation of this EdgeClusterMemberAllocationProfile.  # noqa: E501

        Flag to enable the auto-relocation of standby service router running on edge cluster and node associated with the logical router. Only dynamically allocated tier1 logical routers are considered for the relocation.   # noqa: E501

        :return: The enable_standby_relocation of this EdgeClusterMemberAllocationProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_standby_relocation

    @enable_standby_relocation.setter
    def enable_standby_relocation(self, enable_standby_relocation):
        """Sets the enable_standby_relocation of this EdgeClusterMemberAllocationProfile.

        Flag to enable the auto-relocation of standby service router running on edge cluster and node associated with the logical router. Only dynamically allocated tier1 logical routers are considered for the relocation.   # noqa: E501

        :param enable_standby_relocation: The enable_standby_relocation of this EdgeClusterMemberAllocationProfile.  # noqa: E501
        :type: bool
        """

        self._enable_standby_relocation = enable_standby_relocation

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
        if issubclass(EdgeClusterMemberAllocationProfile, dict):
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
        if not isinstance(other, EdgeClusterMemberAllocationProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
