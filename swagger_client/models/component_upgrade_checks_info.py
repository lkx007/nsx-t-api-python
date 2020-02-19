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


class ComponentUpgradeChecksInfo(object):
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
        'pre_upgrade_checks_info': 'list[UpgradeCheckInfo]',
        'post_upgrade_checks_info': 'list[UpgradeCheckInfo]',
        'component_type': 'str'
    }

    attribute_map = {
        'pre_upgrade_checks_info': 'pre_upgrade_checks_info',
        'post_upgrade_checks_info': 'post_upgrade_checks_info',
        'component_type': 'component_type'
    }

    def __init__(self, pre_upgrade_checks_info=None, post_upgrade_checks_info=None, component_type=None):  # noqa: E501
        """ComponentUpgradeChecksInfo - a model defined in Swagger"""  # noqa: E501
        self._pre_upgrade_checks_info = None
        self._post_upgrade_checks_info = None
        self._component_type = None
        self.discriminator = None
        if pre_upgrade_checks_info is not None:
            self.pre_upgrade_checks_info = pre_upgrade_checks_info
        if post_upgrade_checks_info is not None:
            self.post_upgrade_checks_info = post_upgrade_checks_info
        self.component_type = component_type

    @property
    def pre_upgrade_checks_info(self):
        """Gets the pre_upgrade_checks_info of this ComponentUpgradeChecksInfo.  # noqa: E501

        Collection of pre-upgrade checks  # noqa: E501

        :return: The pre_upgrade_checks_info of this ComponentUpgradeChecksInfo.  # noqa: E501
        :rtype: list[UpgradeCheckInfo]
        """
        return self._pre_upgrade_checks_info

    @pre_upgrade_checks_info.setter
    def pre_upgrade_checks_info(self, pre_upgrade_checks_info):
        """Sets the pre_upgrade_checks_info of this ComponentUpgradeChecksInfo.

        Collection of pre-upgrade checks  # noqa: E501

        :param pre_upgrade_checks_info: The pre_upgrade_checks_info of this ComponentUpgradeChecksInfo.  # noqa: E501
        :type: list[UpgradeCheckInfo]
        """

        self._pre_upgrade_checks_info = pre_upgrade_checks_info

    @property
    def post_upgrade_checks_info(self):
        """Gets the post_upgrade_checks_info of this ComponentUpgradeChecksInfo.  # noqa: E501

        Collection of post-upgrade checks  # noqa: E501

        :return: The post_upgrade_checks_info of this ComponentUpgradeChecksInfo.  # noqa: E501
        :rtype: list[UpgradeCheckInfo]
        """
        return self._post_upgrade_checks_info

    @post_upgrade_checks_info.setter
    def post_upgrade_checks_info(self, post_upgrade_checks_info):
        """Sets the post_upgrade_checks_info of this ComponentUpgradeChecksInfo.

        Collection of post-upgrade checks  # noqa: E501

        :param post_upgrade_checks_info: The post_upgrade_checks_info of this ComponentUpgradeChecksInfo.  # noqa: E501
        :type: list[UpgradeCheckInfo]
        """

        self._post_upgrade_checks_info = post_upgrade_checks_info

    @property
    def component_type(self):
        """Gets the component_type of this ComponentUpgradeChecksInfo.  # noqa: E501

        Component type of the pre/post-upgrade checks  # noqa: E501

        :return: The component_type of this ComponentUpgradeChecksInfo.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this ComponentUpgradeChecksInfo.

        Component type of the pre/post-upgrade checks  # noqa: E501

        :param component_type: The component_type of this ComponentUpgradeChecksInfo.  # noqa: E501
        :type: str
        """
        if component_type is None:
            raise ValueError("Invalid value for `component_type`, must not be `None`")  # noqa: E501

        self._component_type = component_type

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
        if issubclass(ComponentUpgradeChecksInfo, dict):
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
        if not isinstance(other, ComponentUpgradeChecksInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
