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


class MacTableCsvRecord(object):
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
        'vtep_mac_address': 'str',
        'vtep_ip': 'str',
        'mac_address': 'str'
    }
    if hasattr(CsvRecord, "swagger_types"):
        swagger_types.update(CsvRecord.swagger_types)

    attribute_map = {
        'vtep_mac_address': 'vtep_mac_address',
        'vtep_ip': 'vtep_ip',
        'mac_address': 'mac_address'
    }
    if hasattr(CsvRecord, "attribute_map"):
        attribute_map.update(CsvRecord.attribute_map)

    def __init__(self, vtep_mac_address=None, vtep_ip=None, mac_address=None, *args, **kwargs):  # noqa: E501
        """MacTableCsvRecord - a model defined in Swagger"""  # noqa: E501
        self._vtep_mac_address = None
        self._vtep_ip = None
        self._mac_address = None
        self.discriminator = None
        if vtep_mac_address is not None:
            self.vtep_mac_address = vtep_mac_address
        if vtep_ip is not None:
            self.vtep_ip = vtep_ip
        self.mac_address = mac_address
        CsvRecord.__init__(self, *args, **kwargs)

    @property
    def vtep_mac_address(self):
        """Gets the vtep_mac_address of this MacTableCsvRecord.  # noqa: E501

        The virtual tunnel endpoint MAC address  # noqa: E501

        :return: The vtep_mac_address of this MacTableCsvRecord.  # noqa: E501
        :rtype: str
        """
        return self._vtep_mac_address

    @vtep_mac_address.setter
    def vtep_mac_address(self, vtep_mac_address):
        """Sets the vtep_mac_address of this MacTableCsvRecord.

        The virtual tunnel endpoint MAC address  # noqa: E501

        :param vtep_mac_address: The vtep_mac_address of this MacTableCsvRecord.  # noqa: E501
        :type: str
        """

        self._vtep_mac_address = vtep_mac_address

    @property
    def vtep_ip(self):
        """Gets the vtep_ip of this MacTableCsvRecord.  # noqa: E501

        The virtual tunnel endpoint IP address  # noqa: E501

        :return: The vtep_ip of this MacTableCsvRecord.  # noqa: E501
        :rtype: str
        """
        return self._vtep_ip

    @vtep_ip.setter
    def vtep_ip(self, vtep_ip):
        """Sets the vtep_ip of this MacTableCsvRecord.

        The virtual tunnel endpoint IP address  # noqa: E501

        :param vtep_ip: The vtep_ip of this MacTableCsvRecord.  # noqa: E501
        :type: str
        """

        self._vtep_ip = vtep_ip

    @property
    def mac_address(self):
        """Gets the mac_address of this MacTableCsvRecord.  # noqa: E501

        The MAC address  # noqa: E501

        :return: The mac_address of this MacTableCsvRecord.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this MacTableCsvRecord.

        The MAC address  # noqa: E501

        :param mac_address: The mac_address of this MacTableCsvRecord.  # noqa: E501
        :type: str
        """
        if mac_address is None:
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

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
        if issubclass(MacTableCsvRecord, dict):
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
        if not isinstance(other, MacTableCsvRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
