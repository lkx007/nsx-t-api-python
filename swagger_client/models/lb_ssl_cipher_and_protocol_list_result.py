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


class LbSslCipherAndProtocolListResult(object):
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
        'ciphers': 'list[LbSslCipherInfo]',
        'protocols': 'list[LbSslProtocolInfo]'
    }
    if hasattr(ListResult, "swagger_types"):
        swagger_types.update(ListResult.swagger_types)

    attribute_map = {
        'cursor': 'cursor',
        'sort_ascending': 'sort_ascending',
        'sort_by': 'sort_by',
        'result_count': 'result_count',
        'ciphers': 'ciphers',
        'protocols': 'protocols'
    }
    if hasattr(ListResult, "attribute_map"):
        attribute_map.update(ListResult.attribute_map)

    def __init__(self, cursor=None, sort_ascending=None, sort_by=None, result_count=None, ciphers=None, protocols=None, *args, **kwargs):  # noqa: E501
        """LbSslCipherAndProtocolListResult - a model defined in Swagger"""  # noqa: E501
        self._cursor = None
        self._sort_ascending = None
        self._sort_by = None
        self._result_count = None
        self._ciphers = None
        self._protocols = None
        self.discriminator = None
        if cursor is not None:
            self.cursor = cursor
        if sort_ascending is not None:
            self.sort_ascending = sort_ascending
        if sort_by is not None:
            self.sort_by = sort_by
        if result_count is not None:
            self.result_count = result_count
        self.ciphers = ciphers
        self.protocols = protocols
        ListResult.__init__(self, *args, **kwargs)

    @property
    def cursor(self):
        """Gets the cursor of this LbSslCipherAndProtocolListResult.  # noqa: E501

        Opaque cursor to be used for getting next page of records (supplied by current result page)  # noqa: E501

        :return: The cursor of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this LbSslCipherAndProtocolListResult.

        Opaque cursor to be used for getting next page of records (supplied by current result page)  # noqa: E501

        :param cursor: The cursor of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def sort_ascending(self):
        """Gets the sort_ascending of this LbSslCipherAndProtocolListResult.  # noqa: E501

        If true, results are sorted in ascending order  # noqa: E501

        :return: The sort_ascending of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :rtype: bool
        """
        return self._sort_ascending

    @sort_ascending.setter
    def sort_ascending(self, sort_ascending):
        """Sets the sort_ascending of this LbSslCipherAndProtocolListResult.

        If true, results are sorted in ascending order  # noqa: E501

        :param sort_ascending: The sort_ascending of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :type: bool
        """

        self._sort_ascending = sort_ascending

    @property
    def sort_by(self):
        """Gets the sort_by of this LbSslCipherAndProtocolListResult.  # noqa: E501

        Field by which records are sorted  # noqa: E501

        :return: The sort_by of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this LbSslCipherAndProtocolListResult.

        Field by which records are sorted  # noqa: E501

        :param sort_by: The sort_by of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def result_count(self):
        """Gets the result_count of this LbSslCipherAndProtocolListResult.  # noqa: E501

        Count of results found (across all pages), set only on first page  # noqa: E501

        :return: The result_count of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this LbSslCipherAndProtocolListResult.

        Count of results found (across all pages), set only on first page  # noqa: E501

        :param result_count: The result_count of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :type: int
        """

        self._result_count = result_count

    @property
    def ciphers(self):
        """Gets the ciphers of this LbSslCipherAndProtocolListResult.  # noqa: E501

        List of SSL ciphers  # noqa: E501

        :return: The ciphers of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :rtype: list[LbSslCipherInfo]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this LbSslCipherAndProtocolListResult.

        List of SSL ciphers  # noqa: E501

        :param ciphers: The ciphers of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :type: list[LbSslCipherInfo]
        """
        if ciphers is None:
            raise ValueError("Invalid value for `ciphers`, must not be `None`")  # noqa: E501

        self._ciphers = ciphers

    @property
    def protocols(self):
        """Gets the protocols of this LbSslCipherAndProtocolListResult.  # noqa: E501

        List of SSL protocols  # noqa: E501

        :return: The protocols of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :rtype: list[LbSslProtocolInfo]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this LbSslCipherAndProtocolListResult.

        List of SSL protocols  # noqa: E501

        :param protocols: The protocols of this LbSslCipherAndProtocolListResult.  # noqa: E501
        :type: list[LbSslProtocolInfo]
        """
        if protocols is None:
            raise ValueError("Invalid value for `protocols`, must not be `None`")  # noqa: E501

        self._protocols = protocols

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
        if issubclass(LbSslCipherAndProtocolListResult, dict):
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
        if not isinstance(other, LbSslCipherAndProtocolListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
