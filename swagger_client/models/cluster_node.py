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


class ClusterNode(object):
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
        'entities': 'list[ClusterNodeEntity]',
        'node_uuid': 'str'
    }

    attribute_map = {
        'status': 'status',
        'entities': 'entities',
        'node_uuid': 'node_uuid'
    }

    def __init__(self, status='REMOVED', entities=None, node_uuid=None):  # noqa: E501
        """ClusterNode - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._entities = None
        self._node_uuid = None
        self.discriminator = None
        if status is not None:
            self.status = status
        self.entities = entities
        self.node_uuid = node_uuid

    @property
    def status(self):
        """Gets the status of this ClusterNode.  # noqa: E501

        Current clustering status of the node  # noqa: E501

        :return: The status of this ClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterNode.

        Current clustering status of the node  # noqa: E501

        :param status: The status of this ClusterNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["JOINING", "JOINED", "REMOVING", "REMOVED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def entities(self):
        """Gets the entities of this ClusterNode.  # noqa: E501

        Entities on the node  # noqa: E501

        :return: The entities of this ClusterNode.  # noqa: E501
        :rtype: list[ClusterNodeEntity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ClusterNode.

        Entities on the node  # noqa: E501

        :param entities: The entities of this ClusterNode.  # noqa: E501
        :type: list[ClusterNodeEntity]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")  # noqa: E501

        self._entities = entities

    @property
    def node_uuid(self):
        """Gets the node_uuid of this ClusterNode.  # noqa: E501

        UUID of the node  # noqa: E501

        :return: The node_uuid of this ClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._node_uuid

    @node_uuid.setter
    def node_uuid(self, node_uuid):
        """Sets the node_uuid of this ClusterNode.

        UUID of the node  # noqa: E501

        :param node_uuid: The node_uuid of this ClusterNode.  # noqa: E501
        :type: str
        """
        if node_uuid is None:
            raise ValueError("Invalid value for `node_uuid`, must not be `None`")  # noqa: E501

        self._node_uuid = node_uuid

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
        if issubclass(ClusterNode, dict):
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
        if not isinstance(other, ClusterNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
