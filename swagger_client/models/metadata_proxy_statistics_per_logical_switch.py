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


class MetadataProxyStatisticsPerLogicalSwitch(object):
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
        'requests_to_nova_server': 'int',
        'responses_to_clients': 'int',
        'succeeded_responses_from_nova_server': 'int',
        'logical_switch_id': 'str',
        'requests_from_clients': 'int',
        'error_responses_from_nova_server': 'int'
    }

    attribute_map = {
        'requests_to_nova_server': 'requests_to_nova_server',
        'responses_to_clients': 'responses_to_clients',
        'succeeded_responses_from_nova_server': 'succeeded_responses_from_nova_server',
        'logical_switch_id': 'logical_switch_id',
        'requests_from_clients': 'requests_from_clients',
        'error_responses_from_nova_server': 'error_responses_from_nova_server'
    }

    def __init__(self, requests_to_nova_server=None, responses_to_clients=None, succeeded_responses_from_nova_server=None, logical_switch_id=None, requests_from_clients=None, error_responses_from_nova_server=None):  # noqa: E501
        """MetadataProxyStatisticsPerLogicalSwitch - a model defined in Swagger"""  # noqa: E501
        self._requests_to_nova_server = None
        self._responses_to_clients = None
        self._succeeded_responses_from_nova_server = None
        self._logical_switch_id = None
        self._requests_from_clients = None
        self._error_responses_from_nova_server = None
        self.discriminator = None
        self.requests_to_nova_server = requests_to_nova_server
        self.responses_to_clients = responses_to_clients
        self.succeeded_responses_from_nova_server = succeeded_responses_from_nova_server
        self.logical_switch_id = logical_switch_id
        self.requests_from_clients = requests_from_clients
        self.error_responses_from_nova_server = error_responses_from_nova_server

    @property
    def requests_to_nova_server(self):
        """Gets the requests_to_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501

        requests to nova server  # noqa: E501

        :return: The requests_to_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._requests_to_nova_server

    @requests_to_nova_server.setter
    def requests_to_nova_server(self, requests_to_nova_server):
        """Sets the requests_to_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.

        requests to nova server  # noqa: E501

        :param requests_to_nova_server: The requests_to_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :type: int
        """
        if requests_to_nova_server is None:
            raise ValueError("Invalid value for `requests_to_nova_server`, must not be `None`")  # noqa: E501

        self._requests_to_nova_server = requests_to_nova_server

    @property
    def responses_to_clients(self):
        """Gets the responses_to_clients of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501

        responses to clients  # noqa: E501

        :return: The responses_to_clients of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._responses_to_clients

    @responses_to_clients.setter
    def responses_to_clients(self, responses_to_clients):
        """Sets the responses_to_clients of this MetadataProxyStatisticsPerLogicalSwitch.

        responses to clients  # noqa: E501

        :param responses_to_clients: The responses_to_clients of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :type: int
        """
        if responses_to_clients is None:
            raise ValueError("Invalid value for `responses_to_clients`, must not be `None`")  # noqa: E501

        self._responses_to_clients = responses_to_clients

    @property
    def succeeded_responses_from_nova_server(self):
        """Gets the succeeded_responses_from_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501

        succeeded responses from  nova server  # noqa: E501

        :return: The succeeded_responses_from_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._succeeded_responses_from_nova_server

    @succeeded_responses_from_nova_server.setter
    def succeeded_responses_from_nova_server(self, succeeded_responses_from_nova_server):
        """Sets the succeeded_responses_from_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.

        succeeded responses from  nova server  # noqa: E501

        :param succeeded_responses_from_nova_server: The succeeded_responses_from_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :type: int
        """
        if succeeded_responses_from_nova_server is None:
            raise ValueError("Invalid value for `succeeded_responses_from_nova_server`, must not be `None`")  # noqa: E501

        self._succeeded_responses_from_nova_server = succeeded_responses_from_nova_server

    @property
    def logical_switch_id(self):
        """Gets the logical_switch_id of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501

        uuid of attached logical switch  # noqa: E501

        :return: The logical_switch_id of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._logical_switch_id

    @logical_switch_id.setter
    def logical_switch_id(self, logical_switch_id):
        """Sets the logical_switch_id of this MetadataProxyStatisticsPerLogicalSwitch.

        uuid of attached logical switch  # noqa: E501

        :param logical_switch_id: The logical_switch_id of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :type: str
        """
        if logical_switch_id is None:
            raise ValueError("Invalid value for `logical_switch_id`, must not be `None`")  # noqa: E501

        self._logical_switch_id = logical_switch_id

    @property
    def requests_from_clients(self):
        """Gets the requests_from_clients of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501

        requests from clients  # noqa: E501

        :return: The requests_from_clients of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._requests_from_clients

    @requests_from_clients.setter
    def requests_from_clients(self, requests_from_clients):
        """Sets the requests_from_clients of this MetadataProxyStatisticsPerLogicalSwitch.

        requests from clients  # noqa: E501

        :param requests_from_clients: The requests_from_clients of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :type: int
        """
        if requests_from_clients is None:
            raise ValueError("Invalid value for `requests_from_clients`, must not be `None`")  # noqa: E501

        self._requests_from_clients = requests_from_clients

    @property
    def error_responses_from_nova_server(self):
        """Gets the error_responses_from_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501

        error responses from  nova server  # noqa: E501

        :return: The error_responses_from_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._error_responses_from_nova_server

    @error_responses_from_nova_server.setter
    def error_responses_from_nova_server(self, error_responses_from_nova_server):
        """Sets the error_responses_from_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.

        error responses from  nova server  # noqa: E501

        :param error_responses_from_nova_server: The error_responses_from_nova_server of this MetadataProxyStatisticsPerLogicalSwitch.  # noqa: E501
        :type: int
        """
        if error_responses_from_nova_server is None:
            raise ValueError("Invalid value for `error_responses_from_nova_server`, must not be `None`")  # noqa: E501

        self._error_responses_from_nova_server = error_responses_from_nova_server

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
        if issubclass(MetadataProxyStatisticsPerLogicalSwitch, dict):
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
        if not isinstance(other, MetadataProxyStatisticsPerLogicalSwitch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
