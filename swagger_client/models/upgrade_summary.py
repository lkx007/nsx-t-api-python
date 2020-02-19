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


class UpgradeSummary(object):
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
        'upgrade_coordinator_updated': 'bool',
        'target_version': 'str',
        'upgrade_coordinator_version': 'str',
        'upgrade_status': 'str',
        'component_target_versions': 'list[ComponentTargetVersion]',
        'system_version': 'str',
        'upgrade_bundle_file_name': 'str'
    }

    attribute_map = {
        'upgrade_coordinator_updated': 'upgrade_coordinator_updated',
        'target_version': 'target_version',
        'upgrade_coordinator_version': 'upgrade_coordinator_version',
        'upgrade_status': 'upgrade_status',
        'component_target_versions': 'component_target_versions',
        'system_version': 'system_version',
        'upgrade_bundle_file_name': 'upgrade_bundle_file_name'
    }

    def __init__(self, upgrade_coordinator_updated=None, target_version=None, upgrade_coordinator_version=None, upgrade_status=None, component_target_versions=None, system_version=None, upgrade_bundle_file_name=None):  # noqa: E501
        """UpgradeSummary - a model defined in Swagger"""  # noqa: E501
        self._upgrade_coordinator_updated = None
        self._target_version = None
        self._upgrade_coordinator_version = None
        self._upgrade_status = None
        self._component_target_versions = None
        self._system_version = None
        self._upgrade_bundle_file_name = None
        self.discriminator = None
        if upgrade_coordinator_updated is not None:
            self.upgrade_coordinator_updated = upgrade_coordinator_updated
        if target_version is not None:
            self.target_version = target_version
        if upgrade_coordinator_version is not None:
            self.upgrade_coordinator_version = upgrade_coordinator_version
        if upgrade_status is not None:
            self.upgrade_status = upgrade_status
        if component_target_versions is not None:
            self.component_target_versions = component_target_versions
        if system_version is not None:
            self.system_version = system_version
        if upgrade_bundle_file_name is not None:
            self.upgrade_bundle_file_name = upgrade_bundle_file_name

    @property
    def upgrade_coordinator_updated(self):
        """Gets the upgrade_coordinator_updated of this UpgradeSummary.  # noqa: E501

        Has upgrade coordinator been updated after upload of upgrade bundle file  # noqa: E501

        :return: The upgrade_coordinator_updated of this UpgradeSummary.  # noqa: E501
        :rtype: bool
        """
        return self._upgrade_coordinator_updated

    @upgrade_coordinator_updated.setter
    def upgrade_coordinator_updated(self, upgrade_coordinator_updated):
        """Sets the upgrade_coordinator_updated of this UpgradeSummary.

        Has upgrade coordinator been updated after upload of upgrade bundle file  # noqa: E501

        :param upgrade_coordinator_updated: The upgrade_coordinator_updated of this UpgradeSummary.  # noqa: E501
        :type: bool
        """

        self._upgrade_coordinator_updated = upgrade_coordinator_updated

    @property
    def target_version(self):
        """Gets the target_version of this UpgradeSummary.  # noqa: E501

        Target system version  # noqa: E501

        :return: The target_version of this UpgradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this UpgradeSummary.

        Target system version  # noqa: E501

        :param target_version: The target_version of this UpgradeSummary.  # noqa: E501
        :type: str
        """

        self._target_version = target_version

    @property
    def upgrade_coordinator_version(self):
        """Gets the upgrade_coordinator_version of this UpgradeSummary.  # noqa: E501

        Current version of upgrade coordinator  # noqa: E501

        :return: The upgrade_coordinator_version of this UpgradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_coordinator_version

    @upgrade_coordinator_version.setter
    def upgrade_coordinator_version(self, upgrade_coordinator_version):
        """Sets the upgrade_coordinator_version of this UpgradeSummary.

        Current version of upgrade coordinator  # noqa: E501

        :param upgrade_coordinator_version: The upgrade_coordinator_version of this UpgradeSummary.  # noqa: E501
        :type: str
        """

        self._upgrade_coordinator_version = upgrade_coordinator_version

    @property
    def upgrade_status(self):
        """Gets the upgrade_status of this UpgradeSummary.  # noqa: E501

        Status of upgrade  # noqa: E501

        :return: The upgrade_status of this UpgradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        """Sets the upgrade_status of this UpgradeSummary.

        Status of upgrade  # noqa: E501

        :param upgrade_status: The upgrade_status of this UpgradeSummary.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED", "IN_PROGRESS", "NOT_STARTED", "PAUSING", "PAUSED"]  # noqa: E501
        if upgrade_status not in allowed_values:
            raise ValueError(
                "Invalid value for `upgrade_status` ({0}), must be one of {1}"  # noqa: E501
                .format(upgrade_status, allowed_values)
            )

        self._upgrade_status = upgrade_status

    @property
    def component_target_versions(self):
        """Gets the component_target_versions of this UpgradeSummary.  # noqa: E501


        :return: The component_target_versions of this UpgradeSummary.  # noqa: E501
        :rtype: list[ComponentTargetVersion]
        """
        return self._component_target_versions

    @component_target_versions.setter
    def component_target_versions(self, component_target_versions):
        """Sets the component_target_versions of this UpgradeSummary.


        :param component_target_versions: The component_target_versions of this UpgradeSummary.  # noqa: E501
        :type: list[ComponentTargetVersion]
        """

        self._component_target_versions = component_target_versions

    @property
    def system_version(self):
        """Gets the system_version of this UpgradeSummary.  # noqa: E501

        Current system version  # noqa: E501

        :return: The system_version of this UpgradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._system_version

    @system_version.setter
    def system_version(self, system_version):
        """Sets the system_version of this UpgradeSummary.

        Current system version  # noqa: E501

        :param system_version: The system_version of this UpgradeSummary.  # noqa: E501
        :type: str
        """

        self._system_version = system_version

    @property
    def upgrade_bundle_file_name(self):
        """Gets the upgrade_bundle_file_name of this UpgradeSummary.  # noqa: E501

        Name of the last successfully uploaded upgrade bundle file  # noqa: E501

        :return: The upgrade_bundle_file_name of this UpgradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_bundle_file_name

    @upgrade_bundle_file_name.setter
    def upgrade_bundle_file_name(self, upgrade_bundle_file_name):
        """Sets the upgrade_bundle_file_name of this UpgradeSummary.

        Name of the last successfully uploaded upgrade bundle file  # noqa: E501

        :param upgrade_bundle_file_name: The upgrade_bundle_file_name of this UpgradeSummary.  # noqa: E501
        :type: str
        """

        self._upgrade_bundle_file_name = upgrade_bundle_file_name

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
        if issubclass(UpgradeSummary, dict):
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
        if not isinstance(other, UpgradeSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
