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


class NicInfo(object):
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
        'subnet_mask': 'str',
        'gateway_address': 'str',
        'ip_allocation_type': 'str',
        'nic_metadata': 'NicMetadata',
        'network_id': 'str',
        'ip_pool_id': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'subnet_mask': 'subnet_mask',
        'gateway_address': 'gateway_address',
        'ip_allocation_type': 'ip_allocation_type',
        'nic_metadata': 'nic_metadata',
        'network_id': 'network_id',
        'ip_pool_id': 'ip_pool_id',
        'ip_address': 'ip_address'
    }

    def __init__(self, subnet_mask=None, gateway_address=None, ip_allocation_type=None, nic_metadata=None, network_id=None, ip_pool_id=None, ip_address=None):  # noqa: E501
        """NicInfo - a model defined in Swagger"""  # noqa: E501
        self._subnet_mask = None
        self._gateway_address = None
        self._ip_allocation_type = None
        self._nic_metadata = None
        self._network_id = None
        self._ip_pool_id = None
        self._ip_address = None
        self.discriminator = None
        if subnet_mask is not None:
            self.subnet_mask = subnet_mask
        if gateway_address is not None:
            self.gateway_address = gateway_address
        if ip_allocation_type is not None:
            self.ip_allocation_type = ip_allocation_type
        if nic_metadata is not None:
            self.nic_metadata = nic_metadata
        if network_id is not None:
            self.network_id = network_id
        if ip_pool_id is not None:
            self.ip_pool_id = ip_pool_id
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this NicInfo.  # noqa: E501

        Subnet mask associated with the NIC metadata.  # noqa: E501

        :return: The subnet_mask of this NicInfo.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this NicInfo.

        Subnet mask associated with the NIC metadata.  # noqa: E501

        :param subnet_mask: The subnet_mask of this NicInfo.  # noqa: E501
        :type: str
        """

        self._subnet_mask = subnet_mask

    @property
    def gateway_address(self):
        """Gets the gateway_address of this NicInfo.  # noqa: E501

        Gateway address associated with the NIC metadata.  # noqa: E501

        :return: The gateway_address of this NicInfo.  # noqa: E501
        :rtype: str
        """
        return self._gateway_address

    @gateway_address.setter
    def gateway_address(self, gateway_address):
        """Sets the gateway_address of this NicInfo.

        Gateway address associated with the NIC metadata.  # noqa: E501

        :param gateway_address: The gateway_address of this NicInfo.  # noqa: E501
        :type: str
        """

        self._gateway_address = gateway_address

    @property
    def ip_allocation_type(self):
        """Gets the ip_allocation_type of this NicInfo.  # noqa: E501

        IP allocation type with values STATIC, DHCP, or NONE indicating that IP address is not required.  # noqa: E501

        :return: The ip_allocation_type of this NicInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip_allocation_type

    @ip_allocation_type.setter
    def ip_allocation_type(self, ip_allocation_type):
        """Sets the ip_allocation_type of this NicInfo.

        IP allocation type with values STATIC, DHCP, or NONE indicating that IP address is not required.  # noqa: E501

        :param ip_allocation_type: The ip_allocation_type of this NicInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATIC", "DHCP", "NONE"]  # noqa: E501
        if ip_allocation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `ip_allocation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(ip_allocation_type, allowed_values)
            )

        self._ip_allocation_type = ip_allocation_type

    @property
    def nic_metadata(self):
        """Gets the nic_metadata of this NicInfo.  # noqa: E501


        :return: The nic_metadata of this NicInfo.  # noqa: E501
        :rtype: NicMetadata
        """
        return self._nic_metadata

    @nic_metadata.setter
    def nic_metadata(self, nic_metadata):
        """Sets the nic_metadata of this NicInfo.


        :param nic_metadata: The nic_metadata of this NicInfo.  # noqa: E501
        :type: NicMetadata
        """

        self._nic_metadata = nic_metadata

    @property
    def network_id(self):
        """Gets the network_id of this NicInfo.  # noqa: E501

        Network Id associated with the NIC metadata. It can be a moref, or a logical switch ID. If it is to be taken from 'Agent VM Settings', then it should be empty.  # noqa: E501

        :return: The network_id of this NicInfo.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NicInfo.

        Network Id associated with the NIC metadata. It can be a moref, or a logical switch ID. If it is to be taken from 'Agent VM Settings', then it should be empty.  # noqa: E501

        :param network_id: The network_id of this NicInfo.  # noqa: E501
        :type: str
        """

        self._network_id = network_id

    @property
    def ip_pool_id(self):
        """Gets the ip_pool_id of this NicInfo.  # noqa: E501

        If the nic should get IP using a static IP pool then IP pool id should be provided here.  # noqa: E501

        :return: The ip_pool_id of this NicInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip_pool_id

    @ip_pool_id.setter
    def ip_pool_id(self, ip_pool_id):
        """Sets the ip_pool_id of this NicInfo.

        If the nic should get IP using a static IP pool then IP pool id should be provided here.  # noqa: E501

        :param ip_pool_id: The ip_pool_id of this NicInfo.  # noqa: E501
        :type: str
        """

        self._ip_pool_id = ip_pool_id

    @property
    def ip_address(self):
        """Gets the ip_address of this NicInfo.  # noqa: E501

        IP address associated with the NIC metadata. Required only when assigning IP statically for a deployment that is for a single VM instance.  # noqa: E501

        :return: The ip_address of this NicInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this NicInfo.

        IP address associated with the NIC metadata. Required only when assigning IP statically for a deployment that is for a single VM instance.  # noqa: E501

        :param ip_address: The ip_address of this NicInfo.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

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
        if issubclass(NicInfo, dict):
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
        if not isinstance(other, NicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
