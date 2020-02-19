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


class LogicalPortMacAddressListResult(object):
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
        'cursor': 'str',
        'sort_ascending': 'bool',
        'sort_by': 'str',
        'result_count': 'int',
        'logical_port_id': 'str',
        'last_update_timestamp': 'int',
        'results': 'list[LogicalPortMacTableEntry]',
        'transport_node_id': 'str'
    }
    if hasattr(ListResult, "swagger_types"):
        swagger_types.update(ListResult.swagger_types)

    attribute_map = {
        'cursor': 'cursor',
        'sort_ascending': 'sort_ascending',
        'sort_by': 'sort_by',
        'result_count': 'result_count',
        'logical_port_id': 'logical_port_id',
        'last_update_timestamp': 'last_update_timestamp',
        'results': 'results',
        'transport_node_id': 'transport_node_id'
    }
    if hasattr(ListResult, "attribute_map"):
        attribute_map.update(ListResult.attribute_map)

    def __init__(self, cursor=None, sort_ascending=None, sort_by=None, result_count=None, logical_port_id=None, last_update_timestamp=None, results=None, transport_node_id=None, *args, **kwargs):  # noqa: E501
        """LogicalPortMacAddressListResult - a model defined in Swagger"""  # noqa: E501
        self._cursor = None
        self._sort_ascending = None
        self._sort_by = None
        self._result_count = None
        self._logical_port_id = None
        self._last_update_timestamp = None
        self._results = None
        self._transport_node_id = None
        self.discriminator = None
        if cursor is not None:
            self.cursor = cursor
        if sort_ascending is not None:
            self.sort_ascending = sort_ascending
        if sort_by is not None:
            self.sort_by = sort_by
        if result_count is not None:
            self.result_count = result_count
        if logical_port_id is not None:
            self.logical_port_id = logical_port_id
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if results is not None:
            self.results = results
        if transport_node_id is not None:
            self.transport_node_id = transport_node_id
        ListResult.__init__(self, *args, **kwargs)

    @property
    def cursor(self):
        """Gets the cursor of this LogicalPortMacAddressListResult.  # noqa: E501

        Opaque cursor to be used for getting next page of records (supplied by current result page)  # noqa: E501

        :return: The cursor of this LogicalPortMacAddressListResult.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this LogicalPortMacAddressListResult.

        Opaque cursor to be used for getting next page of records (supplied by current result page)  # noqa: E501

        :param cursor: The cursor of this LogicalPortMacAddressListResult.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def sort_ascending(self):
        """Gets the sort_ascending of this LogicalPortMacAddressListResult.  # noqa: E501

        If true, results are sorted in ascending order  # noqa: E501

        :return: The sort_ascending of this LogicalPortMacAddressListResult.  # noqa: E501
        :rtype: bool
        """
        return self._sort_ascending

    @sort_ascending.setter
    def sort_ascending(self, sort_ascending):
        """Sets the sort_ascending of this LogicalPortMacAddressListResult.

        If true, results are sorted in ascending order  # noqa: E501

        :param sort_ascending: The sort_ascending of this LogicalPortMacAddressListResult.  # noqa: E501
        :type: bool
        """

        self._sort_ascending = sort_ascending

    @property
    def sort_by(self):
        """Gets the sort_by of this LogicalPortMacAddressListResult.  # noqa: E501

        Field by which records are sorted  # noqa: E501

        :return: The sort_by of this LogicalPortMacAddressListResult.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this LogicalPortMacAddressListResult.

        Field by which records are sorted  # noqa: E501

        :param sort_by: The sort_by of this LogicalPortMacAddressListResult.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def result_count(self):
        """Gets the result_count of this LogicalPortMacAddressListResult.  # noqa: E501

        Count of results found (across all pages), set only on first page  # noqa: E501

        :return: The result_count of this LogicalPortMacAddressListResult.  # noqa: E501
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this LogicalPortMacAddressListResult.

        Count of results found (across all pages), set only on first page  # noqa: E501

        :param result_count: The result_count of this LogicalPortMacAddressListResult.  # noqa: E501
        :type: int
        """

        self._result_count = result_count

    @property
    def logical_port_id(self):
        """Gets the logical_port_id of this LogicalPortMacAddressListResult.  # noqa: E501

        The id of the logical port  # noqa: E501

        :return: The logical_port_id of this LogicalPortMacAddressListResult.  # noqa: E501
        :rtype: str
        """
        return self._logical_port_id

    @logical_port_id.setter
    def logical_port_id(self, logical_port_id):
        """Sets the logical_port_id of this LogicalPortMacAddressListResult.

        The id of the logical port  # noqa: E501

        :param logical_port_id: The logical_port_id of this LogicalPortMacAddressListResult.  # noqa: E501
        :type: str
        """

        self._logical_port_id = logical_port_id

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this LogicalPortMacAddressListResult.  # noqa: E501

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :return: The last_update_timestamp of this LogicalPortMacAddressListResult.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this LogicalPortMacAddressListResult.

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this LogicalPortMacAddressListResult.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def results(self):
        """Gets the results of this LogicalPortMacAddressListResult.  # noqa: E501


        :return: The results of this LogicalPortMacAddressListResult.  # noqa: E501
        :rtype: list[LogicalPortMacTableEntry]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this LogicalPortMacAddressListResult.


        :param results: The results of this LogicalPortMacAddressListResult.  # noqa: E501
        :type: list[LogicalPortMacTableEntry]
        """

        self._results = results

    @property
    def transport_node_id(self):
        """Gets the transport_node_id of this LogicalPortMacAddressListResult.  # noqa: E501

        Transport node identifier  # noqa: E501

        :return: The transport_node_id of this LogicalPortMacAddressListResult.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_id

    @transport_node_id.setter
    def transport_node_id(self, transport_node_id):
        """Sets the transport_node_id of this LogicalPortMacAddressListResult.

        Transport node identifier  # noqa: E501

        :param transport_node_id: The transport_node_id of this LogicalPortMacAddressListResult.  # noqa: E501
        :type: str
        """

        self._transport_node_id = transport_node_id

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
        if issubclass(LogicalPortMacAddressListResult, dict):
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
        if not isinstance(other, LogicalPortMacAddressListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
