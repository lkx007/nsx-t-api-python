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


class BridgeEndpointStatistics(object):
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
        'tx_bytes': 'DataCounter',
        'rx_packets': 'DataCounter',
        'tx_packets': 'DataCounter',
        'rx_bytes': 'DataCounter',
        'last_update_timestamp': 'int',
        'endpoint_id': 'str'
    }
    if hasattr(AggregatedDataCounter, "swagger_types"):
        swagger_types.update(AggregatedDataCounter.swagger_types)

    attribute_map = {
        'tx_bytes': 'tx_bytes',
        'rx_packets': 'rx_packets',
        'tx_packets': 'tx_packets',
        'rx_bytes': 'rx_bytes',
        'last_update_timestamp': 'last_update_timestamp',
        'endpoint_id': 'endpoint_id'
    }
    if hasattr(AggregatedDataCounter, "attribute_map"):
        attribute_map.update(AggregatedDataCounter.attribute_map)

    def __init__(self, tx_bytes=None, rx_packets=None, tx_packets=None, rx_bytes=None, last_update_timestamp=None, endpoint_id=None, *args, **kwargs):  # noqa: E501
        """BridgeEndpointStatistics - a model defined in Swagger"""  # noqa: E501
        self._tx_bytes = None
        self._rx_packets = None
        self._tx_packets = None
        self._rx_bytes = None
        self._last_update_timestamp = None
        self._endpoint_id = None
        self.discriminator = None
        if tx_bytes is not None:
            self.tx_bytes = tx_bytes
        if rx_packets is not None:
            self.rx_packets = rx_packets
        if tx_packets is not None:
            self.tx_packets = tx_packets
        if rx_bytes is not None:
            self.rx_bytes = rx_bytes
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        AggregatedDataCounter.__init__(self, *args, **kwargs)

    @property
    def tx_bytes(self):
        """Gets the tx_bytes of this BridgeEndpointStatistics.  # noqa: E501


        :return: The tx_bytes of this BridgeEndpointStatistics.  # noqa: E501
        :rtype: DataCounter
        """
        return self._tx_bytes

    @tx_bytes.setter
    def tx_bytes(self, tx_bytes):
        """Sets the tx_bytes of this BridgeEndpointStatistics.


        :param tx_bytes: The tx_bytes of this BridgeEndpointStatistics.  # noqa: E501
        :type: DataCounter
        """

        self._tx_bytes = tx_bytes

    @property
    def rx_packets(self):
        """Gets the rx_packets of this BridgeEndpointStatistics.  # noqa: E501


        :return: The rx_packets of this BridgeEndpointStatistics.  # noqa: E501
        :rtype: DataCounter
        """
        return self._rx_packets

    @rx_packets.setter
    def rx_packets(self, rx_packets):
        """Sets the rx_packets of this BridgeEndpointStatistics.


        :param rx_packets: The rx_packets of this BridgeEndpointStatistics.  # noqa: E501
        :type: DataCounter
        """

        self._rx_packets = rx_packets

    @property
    def tx_packets(self):
        """Gets the tx_packets of this BridgeEndpointStatistics.  # noqa: E501


        :return: The tx_packets of this BridgeEndpointStatistics.  # noqa: E501
        :rtype: DataCounter
        """
        return self._tx_packets

    @tx_packets.setter
    def tx_packets(self, tx_packets):
        """Sets the tx_packets of this BridgeEndpointStatistics.


        :param tx_packets: The tx_packets of this BridgeEndpointStatistics.  # noqa: E501
        :type: DataCounter
        """

        self._tx_packets = tx_packets

    @property
    def rx_bytes(self):
        """Gets the rx_bytes of this BridgeEndpointStatistics.  # noqa: E501


        :return: The rx_bytes of this BridgeEndpointStatistics.  # noqa: E501
        :rtype: DataCounter
        """
        return self._rx_bytes

    @rx_bytes.setter
    def rx_bytes(self, rx_bytes):
        """Sets the rx_bytes of this BridgeEndpointStatistics.


        :param rx_bytes: The rx_bytes of this BridgeEndpointStatistics.  # noqa: E501
        :type: DataCounter
        """

        self._rx_bytes = rx_bytes

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this BridgeEndpointStatistics.  # noqa: E501

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :return: The last_update_timestamp of this BridgeEndpointStatistics.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this BridgeEndpointStatistics.

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this BridgeEndpointStatistics.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this BridgeEndpointStatistics.  # noqa: E501

        The id of the bridge endpoint  # noqa: E501

        :return: The endpoint_id of this BridgeEndpointStatistics.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this BridgeEndpointStatistics.

        The id of the bridge endpoint  # noqa: E501

        :param endpoint_id: The endpoint_id of this BridgeEndpointStatistics.  # noqa: E501
        :type: str
        """

        self._endpoint_id = endpoint_id

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
        if issubclass(BridgeEndpointStatistics, dict):
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
        if not isinstance(other, BridgeEndpointStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
