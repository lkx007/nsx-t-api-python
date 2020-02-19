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


class FeatureUsageCsvRecord(object):
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
        'ccu_usage_count': 'int',
        'vm_usage_count': 'int',
        'vcpu_usage_count': 'int',
        'cpu_usage_count': 'int',
        'feature': 'str',
        'core_usage_count': 'int'
    }
    if hasattr(CsvRecord, "swagger_types"):
        swagger_types.update(CsvRecord.swagger_types)

    attribute_map = {
        'ccu_usage_count': 'ccu_usage_count',
        'vm_usage_count': 'vm_usage_count',
        'vcpu_usage_count': 'vcpu_usage_count',
        'cpu_usage_count': 'cpu_usage_count',
        'feature': 'feature',
        'core_usage_count': 'core_usage_count'
    }
    if hasattr(CsvRecord, "attribute_map"):
        attribute_map.update(CsvRecord.attribute_map)

    def __init__(self, ccu_usage_count=None, vm_usage_count=None, vcpu_usage_count=None, cpu_usage_count=None, feature=None, core_usage_count=None, *args, **kwargs):  # noqa: E501
        """FeatureUsageCsvRecord - a model defined in Swagger"""  # noqa: E501
        self._ccu_usage_count = None
        self._vm_usage_count = None
        self._vcpu_usage_count = None
        self._cpu_usage_count = None
        self._feature = None
        self._core_usage_count = None
        self.discriminator = None
        if ccu_usage_count is not None:
            self.ccu_usage_count = ccu_usage_count
        if vm_usage_count is not None:
            self.vm_usage_count = vm_usage_count
        if vcpu_usage_count is not None:
            self.vcpu_usage_count = vcpu_usage_count
        if cpu_usage_count is not None:
            self.cpu_usage_count = cpu_usage_count
        if feature is not None:
            self.feature = feature
        if core_usage_count is not None:
            self.core_usage_count = core_usage_count
        CsvRecord.__init__(self, *args, **kwargs)

    @property
    def ccu_usage_count(self):
        """Gets the ccu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501

        count of number of concurrent users  # noqa: E501

        :return: The ccu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :rtype: int
        """
        return self._ccu_usage_count

    @ccu_usage_count.setter
    def ccu_usage_count(self, ccu_usage_count):
        """Sets the ccu_usage_count of this FeatureUsageCsvRecord.

        count of number of concurrent users  # noqa: E501

        :param ccu_usage_count: The ccu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :type: int
        """

        self._ccu_usage_count = ccu_usage_count

    @property
    def vm_usage_count(self):
        """Gets the vm_usage_count of this FeatureUsageCsvRecord.  # noqa: E501

        count of number of vms used by this feature  # noqa: E501

        :return: The vm_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :rtype: int
        """
        return self._vm_usage_count

    @vm_usage_count.setter
    def vm_usage_count(self, vm_usage_count):
        """Sets the vm_usage_count of this FeatureUsageCsvRecord.

        count of number of vms used by this feature  # noqa: E501

        :param vm_usage_count: The vm_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :type: int
        """

        self._vm_usage_count = vm_usage_count

    @property
    def vcpu_usage_count(self):
        """Gets the vcpu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501

        count of number of vcpus of public cloud VMs  # noqa: E501

        :return: The vcpu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :rtype: int
        """
        return self._vcpu_usage_count

    @vcpu_usage_count.setter
    def vcpu_usage_count(self, vcpu_usage_count):
        """Sets the vcpu_usage_count of this FeatureUsageCsvRecord.

        count of number of vcpus of public cloud VMs  # noqa: E501

        :param vcpu_usage_count: The vcpu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :type: int
        """

        self._vcpu_usage_count = vcpu_usage_count

    @property
    def cpu_usage_count(self):
        """Gets the cpu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501

        count of number of cpu sockets used by this feature  # noqa: E501

        :return: The cpu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :rtype: int
        """
        return self._cpu_usage_count

    @cpu_usage_count.setter
    def cpu_usage_count(self, cpu_usage_count):
        """Sets the cpu_usage_count of this FeatureUsageCsvRecord.

        count of number of cpu sockets used by this feature  # noqa: E501

        :param cpu_usage_count: The cpu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :type: int
        """

        self._cpu_usage_count = cpu_usage_count

    @property
    def feature(self):
        """Gets the feature of this FeatureUsageCsvRecord.  # noqa: E501

        name of the feature  # noqa: E501

        :return: The feature of this FeatureUsageCsvRecord.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this FeatureUsageCsvRecord.

        name of the feature  # noqa: E501

        :param feature: The feature of this FeatureUsageCsvRecord.  # noqa: E501
        :type: str
        """

        self._feature = feature

    @property
    def core_usage_count(self):
        """Gets the core_usage_count of this FeatureUsageCsvRecord.  # noqa: E501

        Number of CPU cores used by this feature  # noqa: E501

        :return: The core_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :rtype: int
        """
        return self._core_usage_count

    @core_usage_count.setter
    def core_usage_count(self, core_usage_count):
        """Sets the core_usage_count of this FeatureUsageCsvRecord.

        Number of CPU cores used by this feature  # noqa: E501

        :param core_usage_count: The core_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :type: int
        """

        self._core_usage_count = core_usage_count

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
        if issubclass(FeatureUsageCsvRecord, dict):
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
        if not isinstance(other, FeatureUsageCsvRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
