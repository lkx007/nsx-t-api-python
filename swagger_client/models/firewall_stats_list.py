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


class FirewallStatsList(object):
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
        'result_count': 'int',
        'section_id': 'str',
        'results': 'list[FirewallStats]'
    }

    attribute_map = {
        'result_count': 'result_count',
        'section_id': 'section_id',
        'results': 'results'
    }

    def __init__(self, result_count=None, section_id=None, results=None):  # noqa: E501
        """FirewallStatsList - a model defined in Swagger"""  # noqa: E501
        self._result_count = None
        self._section_id = None
        self._results = None
        self.discriminator = None
        if result_count is not None:
            self.result_count = result_count
        if section_id is not None:
            self.section_id = section_id
        if results is not None:
            self.results = results

    @property
    def result_count(self):
        """Gets the result_count of this FirewallStatsList.  # noqa: E501

        Total count for firewall rule statistics in results set  # noqa: E501

        :return: The result_count of this FirewallStatsList.  # noqa: E501
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this FirewallStatsList.

        Total count for firewall rule statistics in results set  # noqa: E501

        :param result_count: The result_count of this FirewallStatsList.  # noqa: E501
        :type: int
        """

        self._result_count = result_count

    @property
    def section_id(self):
        """Gets the section_id of this FirewallStatsList.  # noqa: E501

        Corresponding firewall section identifier for list of rule statistics  # noqa: E501

        :return: The section_id of this FirewallStatsList.  # noqa: E501
        :rtype: str
        """
        return self._section_id

    @section_id.setter
    def section_id(self, section_id):
        """Sets the section_id of this FirewallStatsList.

        Corresponding firewall section identifier for list of rule statistics  # noqa: E501

        :param section_id: The section_id of this FirewallStatsList.  # noqa: E501
        :type: str
        """

        self._section_id = section_id

    @property
    def results(self):
        """Gets the results of this FirewallStatsList.  # noqa: E501

        List of rule statistics  # noqa: E501

        :return: The results of this FirewallStatsList.  # noqa: E501
        :rtype: list[FirewallStats]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this FirewallStatsList.

        List of rule statistics  # noqa: E501

        :param results: The results of this FirewallStatsList.  # noqa: E501
        :type: list[FirewallStats]
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
        if issubclass(FirewallStatsList, dict):
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
        if not isinstance(other, FirewallStatsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other