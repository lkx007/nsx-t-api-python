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


class UpgradeBundleUploadStatus(object):
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
        'url': 'str',
        'status': 'str',
        'detailed_status': 'str',
        'percent': 'float'
    }

    attribute_map = {
        'url': 'url',
        'status': 'status',
        'detailed_status': 'detailed_status',
        'percent': 'percent'
    }

    def __init__(self, url=None, status=None, detailed_status=None, percent=None):  # noqa: E501
        """UpgradeBundleUploadStatus - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._status = None
        self._detailed_status = None
        self._percent = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if detailed_status is not None:
            self.detailed_status = detailed_status
        if percent is not None:
            self.percent = percent

    @property
    def url(self):
        """Gets the url of this UpgradeBundleUploadStatus.  # noqa: E501

        URL for uploading upgrade bundle  # noqa: E501

        :return: The url of this UpgradeBundleUploadStatus.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpgradeBundleUploadStatus.

        URL for uploading upgrade bundle  # noqa: E501

        :param url: The url of this UpgradeBundleUploadStatus.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def status(self):
        """Gets the status of this UpgradeBundleUploadStatus.  # noqa: E501

        Current status of upgrade bundle upload  # noqa: E501

        :return: The status of this UpgradeBundleUploadStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpgradeBundleUploadStatus.

        Current status of upgrade bundle upload  # noqa: E501

        :param status: The status of this UpgradeBundleUploadStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["UPLOADING", "VERIFYING", "SUCCESS", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def detailed_status(self):
        """Gets the detailed_status of this UpgradeBundleUploadStatus.  # noqa: E501

        Detailed status of upgrade bundle upload  # noqa: E501

        :return: The detailed_status of this UpgradeBundleUploadStatus.  # noqa: E501
        :rtype: str
        """
        return self._detailed_status

    @detailed_status.setter
    def detailed_status(self, detailed_status):
        """Sets the detailed_status of this UpgradeBundleUploadStatus.

        Detailed status of upgrade bundle upload  # noqa: E501

        :param detailed_status: The detailed_status of this UpgradeBundleUploadStatus.  # noqa: E501
        :type: str
        """

        self._detailed_status = detailed_status

    @property
    def percent(self):
        """Gets the percent of this UpgradeBundleUploadStatus.  # noqa: E501

        Percent of bundle uploaded from URL  # noqa: E501

        :return: The percent of this UpgradeBundleUploadStatus.  # noqa: E501
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this UpgradeBundleUploadStatus.

        Percent of bundle uploaded from URL  # noqa: E501

        :param percent: The percent of this UpgradeBundleUploadStatus.  # noqa: E501
        :type: float
        """

        self._percent = percent

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
        if issubclass(UpgradeBundleUploadStatus, dict):
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
        if not isinstance(other, UpgradeBundleUploadStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
