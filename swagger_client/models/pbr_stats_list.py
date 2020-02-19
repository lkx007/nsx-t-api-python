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


class PBRStatsList(object):
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
        'section_id': 'str',
        'results': 'list[PBRStats]'
    }
    if hasattr(ListResult, "swagger_types"):
        swagger_types.update(ListResult.swagger_types)

    attribute_map = {
        'cursor': 'cursor',
        'sort_ascending': 'sort_ascending',
        'sort_by': 'sort_by',
        'result_count': 'result_count',
        'section_id': 'section_id',
        'results': 'results'
    }
    if hasattr(ListResult, "attribute_map"):
        attribute_map.update(ListResult.attribute_map)

    def __init__(self, cursor=None, sort_ascending=None, sort_by=None, result_count=None, section_id=None, results=None, *args, **kwargs):  # noqa: E501
        """PBRStatsList - a model defined in Swagger"""  # noqa: E501
        self._cursor = None
        self._sort_ascending = None
        self._sort_by = None
        self._result_count = None
        self._section_id = None
        self._results = None
        self.discriminator = None
        if cursor is not None:
            self.cursor = cursor
        if sort_ascending is not None:
            self.sort_ascending = sort_ascending
        if sort_by is not None:
            self.sort_by = sort_by
        if result_count is not None:
            self.result_count = result_count
        if section_id is not None:
            self.section_id = section_id
        if results is not None:
            self.results = results
        ListResult.__init__(self, *args, **kwargs)

    @property
    def cursor(self):
        """Gets the cursor of this PBRStatsList.  # noqa: E501

        Opaque cursor to be used for getting next page of records (supplied by current result page)  # noqa: E501

        :return: The cursor of this PBRStatsList.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this PBRStatsList.

        Opaque cursor to be used for getting next page of records (supplied by current result page)  # noqa: E501

        :param cursor: The cursor of this PBRStatsList.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def sort_ascending(self):
        """Gets the sort_ascending of this PBRStatsList.  # noqa: E501

        If true, results are sorted in ascending order  # noqa: E501

        :return: The sort_ascending of this PBRStatsList.  # noqa: E501
        :rtype: bool
        """
        return self._sort_ascending

    @sort_ascending.setter
    def sort_ascending(self, sort_ascending):
        """Sets the sort_ascending of this PBRStatsList.

        If true, results are sorted in ascending order  # noqa: E501

        :param sort_ascending: The sort_ascending of this PBRStatsList.  # noqa: E501
        :type: bool
        """

        self._sort_ascending = sort_ascending

    @property
    def sort_by(self):
        """Gets the sort_by of this PBRStatsList.  # noqa: E501

        Field by which records are sorted  # noqa: E501

        :return: The sort_by of this PBRStatsList.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this PBRStatsList.

        Field by which records are sorted  # noqa: E501

        :param sort_by: The sort_by of this PBRStatsList.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def result_count(self):
        """Gets the result_count of this PBRStatsList.  # noqa: E501

        Count of results found (across all pages), set only on first page  # noqa: E501

        :return: The result_count of this PBRStatsList.  # noqa: E501
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this PBRStatsList.

        Count of results found (across all pages), set only on first page  # noqa: E501

        :param result_count: The result_count of this PBRStatsList.  # noqa: E501
        :type: int
        """

        self._result_count = result_count

    @property
    def section_id(self):
        """Gets the section_id of this PBRStatsList.  # noqa: E501

        PBR section identifier.  # noqa: E501

        :return: The section_id of this PBRStatsList.  # noqa: E501
        :rtype: str
        """
        return self._section_id

    @section_id.setter
    def section_id(self, section_id):
        """Sets the section_id of this PBRStatsList.

        PBR section identifier.  # noqa: E501

        :param section_id: The section_id of this PBRStatsList.  # noqa: E501
        :type: str
        """

        self._section_id = section_id

    @property
    def results(self):
        """Gets the results of this PBRStatsList.  # noqa: E501

        List of rule statistics.  # noqa: E501

        :return: The results of this PBRStatsList.  # noqa: E501
        :rtype: list[PBRStats]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PBRStatsList.

        List of rule statistics.  # noqa: E501

        :param results: The results of this PBRStatsList.  # noqa: E501
        :type: list[PBRStats]
        """

        self._results = results

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
        if issubclass(PBRStatsList, dict):
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
        if not isinstance(other, PBRStatsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
