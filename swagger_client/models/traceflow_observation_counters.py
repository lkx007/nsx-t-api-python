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


class TraceflowObservationCounters(object):
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
        'forwarded_count': 'int',
        'dropped_count': 'int',
        'delivered_count': 'int',
        'received_count': 'int'
    }

    attribute_map = {
        'forwarded_count': 'forwarded_count',
        'dropped_count': 'dropped_count',
        'delivered_count': 'delivered_count',
        'received_count': 'received_count'
    }

    def __init__(self, forwarded_count=None, dropped_count=None, delivered_count=None, received_count=None):  # noqa: E501
        """TraceflowObservationCounters - a model defined in Swagger"""  # noqa: E501
        self._forwarded_count = None
        self._dropped_count = None
        self._delivered_count = None
        self._received_count = None
        self.discriminator = None
        if forwarded_count is not None:
            self.forwarded_count = forwarded_count
        if dropped_count is not None:
            self.dropped_count = dropped_count
        if delivered_count is not None:
            self.delivered_count = delivered_count
        if received_count is not None:
            self.received_count = received_count

    @property
    def forwarded_count(self):
        """Gets the forwarded_count of this TraceflowObservationCounters.  # noqa: E501

        Total number of forwarded observations for this traceflow round.  # noqa: E501

        :return: The forwarded_count of this TraceflowObservationCounters.  # noqa: E501
        :rtype: int
        """
        return self._forwarded_count

    @forwarded_count.setter
    def forwarded_count(self, forwarded_count):
        """Sets the forwarded_count of this TraceflowObservationCounters.

        Total number of forwarded observations for this traceflow round.  # noqa: E501

        :param forwarded_count: The forwarded_count of this TraceflowObservationCounters.  # noqa: E501
        :type: int
        """

        self._forwarded_count = forwarded_count

    @property
    def dropped_count(self):
        """Gets the dropped_count of this TraceflowObservationCounters.  # noqa: E501

        Total number of dropped observations for this round.  # noqa: E501

        :return: The dropped_count of this TraceflowObservationCounters.  # noqa: E501
        :rtype: int
        """
        return self._dropped_count

    @dropped_count.setter
    def dropped_count(self, dropped_count):
        """Sets the dropped_count of this TraceflowObservationCounters.

        Total number of dropped observations for this round.  # noqa: E501

        :param dropped_count: The dropped_count of this TraceflowObservationCounters.  # noqa: E501
        :type: int
        """

        self._dropped_count = dropped_count

    @property
    def delivered_count(self):
        """Gets the delivered_count of this TraceflowObservationCounters.  # noqa: E501

        Total number of delivered observations for this traceflow round.  # noqa: E501

        :return: The delivered_count of this TraceflowObservationCounters.  # noqa: E501
        :rtype: int
        """
        return self._delivered_count

    @delivered_count.setter
    def delivered_count(self, delivered_count):
        """Sets the delivered_count of this TraceflowObservationCounters.

        Total number of delivered observations for this traceflow round.  # noqa: E501

        :param delivered_count: The delivered_count of this TraceflowObservationCounters.  # noqa: E501
        :type: int
        """

        self._delivered_count = delivered_count

    @property
    def received_count(self):
        """Gets the received_count of this TraceflowObservationCounters.  # noqa: E501

        Total number of received observations for this traceflow round.  # noqa: E501

        :return: The received_count of this TraceflowObservationCounters.  # noqa: E501
        :rtype: int
        """
        return self._received_count

    @received_count.setter
    def received_count(self, received_count):
        """Sets the received_count of this TraceflowObservationCounters.

        Total number of received observations for this traceflow round.  # noqa: E501

        :param received_count: The received_count of this TraceflowObservationCounters.  # noqa: E501
        :type: int
        """

        self._received_count = received_count

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
        if issubclass(TraceflowObservationCounters, dict):
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
        if not isinstance(other, TraceflowObservationCounters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
