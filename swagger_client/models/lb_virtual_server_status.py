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


class LbVirtualServerStatus(object):
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
        'status': 'str',
        'last_update_timestamp': 'int',
        'virtual_server_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'last_update_timestamp': 'last_update_timestamp',
        'virtual_server_id': 'virtual_server_id'
    }

    def __init__(self, status=None, last_update_timestamp=None, virtual_server_id=None):  # noqa: E501
        """LbVirtualServerStatus - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._last_update_timestamp = None
        self._virtual_server_id = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        self.virtual_server_id = virtual_server_id

    @property
    def status(self):
        """Gets the status of this LbVirtualServerStatus.  # noqa: E501

        UP means that all primary members in default pool are in UP status. For L7 virtual server, if there is no default pool, the virtual server would be treated as UP. PARTIALLY_UP means that some(not all) primary members in default pool are in UP status. The size of these active primary members should be larger than or equal to the certain number(min_active_members) which is defined in LbPool. When there are no backup members which are in the UP status, the number(min_active_members) would be ignored. PRIMARY_DOWN means that less than certain(min_active_members) primary members in default pool are in UP status but backup members are in UP status, the connections would be dispatched to backup members. DOWN means that all primary and backup members are in DOWN status. DETACHED means that the virtual server is not bound to any service. DISABLED means that the admin state of the virtual server is disabled. UNKNOWN means that no status reported from transport-nodes. The associated load balancer service may be working(or not working).   # noqa: E501

        :return: The status of this LbVirtualServerStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LbVirtualServerStatus.

        UP means that all primary members in default pool are in UP status. For L7 virtual server, if there is no default pool, the virtual server would be treated as UP. PARTIALLY_UP means that some(not all) primary members in default pool are in UP status. The size of these active primary members should be larger than or equal to the certain number(min_active_members) which is defined in LbPool. When there are no backup members which are in the UP status, the number(min_active_members) would be ignored. PRIMARY_DOWN means that less than certain(min_active_members) primary members in default pool are in UP status but backup members are in UP status, the connections would be dispatched to backup members. DOWN means that all primary and backup members are in DOWN status. DETACHED means that the virtual server is not bound to any service. DISABLED means that the admin state of the virtual server is disabled. UNKNOWN means that no status reported from transport-nodes. The associated load balancer service may be working(or not working).   # noqa: E501

        :param status: The status of this LbVirtualServerStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "PARTIALLY_UP", "PRIMARY_DOWN", "DOWN", "DETACHED", "DISABLED", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this LbVirtualServerStatus.  # noqa: E501

        Timestamp when the data was last updated.  # noqa: E501

        :return: The last_update_timestamp of this LbVirtualServerStatus.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this LbVirtualServerStatus.

        Timestamp when the data was last updated.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this LbVirtualServerStatus.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def virtual_server_id(self):
        """Gets the virtual_server_id of this LbVirtualServerStatus.  # noqa: E501

        load balancer virtual server identifier  # noqa: E501

        :return: The virtual_server_id of this LbVirtualServerStatus.  # noqa: E501
        :rtype: str
        """
        return self._virtual_server_id

    @virtual_server_id.setter
    def virtual_server_id(self, virtual_server_id):
        """Sets the virtual_server_id of this LbVirtualServerStatus.

        load balancer virtual server identifier  # noqa: E501

        :param virtual_server_id: The virtual_server_id of this LbVirtualServerStatus.  # noqa: E501
        :type: str
        """
        if virtual_server_id is None:
            raise ValueError("Invalid value for `virtual_server_id`, must not be `None`")  # noqa: E501

        self._virtual_server_id = virtual_server_id

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
        if issubclass(LbVirtualServerStatus, dict):
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
        if not isinstance(other, LbVirtualServerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
