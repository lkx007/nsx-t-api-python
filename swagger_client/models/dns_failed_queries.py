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


class DnsFailedQueries(object):
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
        'timestamp': 'str',
        'per_node_failed_queries': 'list[PerNodeDnsFailedQueries]'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'per_node_failed_queries': 'per_node_failed_queries'
    }

    def __init__(self, timestamp=None, per_node_failed_queries=None):  # noqa: E501
        """DnsFailedQueries - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._per_node_failed_queries = None
        self.discriminator = None
        if timestamp is not None:
            self.timestamp = timestamp
        if per_node_failed_queries is not None:
            self.per_node_failed_queries = per_node_failed_queries

    @property
    def timestamp(self):
        """Gets the timestamp of this DnsFailedQueries.  # noqa: E501

        Timestamp of the request, in YYYY-MM-DD HH:MM:SS.zzz format.   # noqa: E501

        :return: The timestamp of this DnsFailedQueries.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DnsFailedQueries.

        Timestamp of the request, in YYYY-MM-DD HH:MM:SS.zzz format.   # noqa: E501

        :param timestamp: The timestamp of this DnsFailedQueries.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def per_node_failed_queries(self):
        """Gets the per_node_failed_queries of this DnsFailedQueries.  # noqa: E501

        The array of failed DNS queries on active and standby transport node. If there is no standby node, the failed queries on standby node will not be present.   # noqa: E501

        :return: The per_node_failed_queries of this DnsFailedQueries.  # noqa: E501
        :rtype: list[PerNodeDnsFailedQueries]
        """
        return self._per_node_failed_queries

    @per_node_failed_queries.setter
    def per_node_failed_queries(self, per_node_failed_queries):
        """Sets the per_node_failed_queries of this DnsFailedQueries.

        The array of failed DNS queries on active and standby transport node. If there is no standby node, the failed queries on standby node will not be present.   # noqa: E501

        :param per_node_failed_queries: The per_node_failed_queries of this DnsFailedQueries.  # noqa: E501
        :type: list[PerNodeDnsFailedQueries]
        """

        self._per_node_failed_queries = per_node_failed_queries

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
        if issubclass(DnsFailedQueries, dict):
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
        if not isinstance(other, DnsFailedQueries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
