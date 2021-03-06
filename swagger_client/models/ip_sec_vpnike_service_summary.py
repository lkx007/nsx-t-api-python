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


class IPSecVPNIKEServiceSummary(object):
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
        'traffic_summary_per_session': 'list[IPSecVPNSessionTrafficSummary]',
        'last_update_timestamp': 'int',
        'session_summary': 'IPsecVPNIKESessionSummary',
        'aggregate_traffic_counters': 'IPSecVPNTrafficCounters',
        'ipsec_vpn_service_id': 'str',
        'display_name': 'str',
        'logical_router_id': 'str'
    }
    if hasattr(IPSecVPNSessionSummary, "swagger_types"):
        swagger_types.update(IPSecVPNSessionSummary.swagger_types)

    attribute_map = {
        'traffic_summary_per_session': 'traffic_summary_per_session',
        'last_update_timestamp': 'last_update_timestamp',
        'session_summary': 'session_summary',
        'aggregate_traffic_counters': 'aggregate_traffic_counters',
        'ipsec_vpn_service_id': 'ipsec_vpn_service_id',
        'display_name': 'display_name',
        'logical_router_id': 'logical_router_id'
    }
    if hasattr(IPSecVPNSessionSummary, "attribute_map"):
        attribute_map.update(IPSecVPNSessionSummary.attribute_map)

    def __init__(self, traffic_summary_per_session=None, last_update_timestamp=None, session_summary=None, aggregate_traffic_counters=None, ipsec_vpn_service_id=None, display_name=None, logical_router_id=None, *args, **kwargs):  # noqa: E501
        """IPSecVPNIKEServiceSummary - a model defined in Swagger"""  # noqa: E501
        self._traffic_summary_per_session = None
        self._last_update_timestamp = None
        self._session_summary = None
        self._aggregate_traffic_counters = None
        self._ipsec_vpn_service_id = None
        self._display_name = None
        self._logical_router_id = None
        self.discriminator = None
        if traffic_summary_per_session is not None:
            self.traffic_summary_per_session = traffic_summary_per_session
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if session_summary is not None:
            self.session_summary = session_summary
        if aggregate_traffic_counters is not None:
            self.aggregate_traffic_counters = aggregate_traffic_counters
        if ipsec_vpn_service_id is not None:
            self.ipsec_vpn_service_id = ipsec_vpn_service_id
        if display_name is not None:
            self.display_name = display_name
        if logical_router_id is not None:
            self.logical_router_id = logical_router_id
        IPSecVPNSessionSummary.__init__(self, *args, **kwargs)

    @property
    def traffic_summary_per_session(self):
        """Gets the traffic_summary_per_session of this IPSecVPNIKEServiceSummary.  # noqa: E501

        Traffic summary per session.  # noqa: E501

        :return: The traffic_summary_per_session of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :rtype: list[IPSecVPNSessionTrafficSummary]
        """
        return self._traffic_summary_per_session

    @traffic_summary_per_session.setter
    def traffic_summary_per_session(self, traffic_summary_per_session):
        """Sets the traffic_summary_per_session of this IPSecVPNIKEServiceSummary.

        Traffic summary per session.  # noqa: E501

        :param traffic_summary_per_session: The traffic_summary_per_session of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :type: list[IPSecVPNSessionTrafficSummary]
        """

        self._traffic_summary_per_session = traffic_summary_per_session

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this IPSecVPNIKEServiceSummary.  # noqa: E501

        Timestamp when the data was last updated.  # noqa: E501

        :return: The last_update_timestamp of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this IPSecVPNIKEServiceSummary.

        Timestamp when the data was last updated.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def session_summary(self):
        """Gets the session_summary of this IPSecVPNIKEServiceSummary.  # noqa: E501


        :return: The session_summary of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :rtype: IPsecVPNIKESessionSummary
        """
        return self._session_summary

    @session_summary.setter
    def session_summary(self, session_summary):
        """Sets the session_summary of this IPSecVPNIKEServiceSummary.


        :param session_summary: The session_summary of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :type: IPsecVPNIKESessionSummary
        """

        self._session_summary = session_summary

    @property
    def aggregate_traffic_counters(self):
        """Gets the aggregate_traffic_counters of this IPSecVPNIKEServiceSummary.  # noqa: E501


        :return: The aggregate_traffic_counters of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :rtype: IPSecVPNTrafficCounters
        """
        return self._aggregate_traffic_counters

    @aggregate_traffic_counters.setter
    def aggregate_traffic_counters(self, aggregate_traffic_counters):
        """Sets the aggregate_traffic_counters of this IPSecVPNIKEServiceSummary.


        :param aggregate_traffic_counters: The aggregate_traffic_counters of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :type: IPSecVPNTrafficCounters
        """

        self._aggregate_traffic_counters = aggregate_traffic_counters

    @property
    def ipsec_vpn_service_id(self):
        """Gets the ipsec_vpn_service_id of this IPSecVPNIKEServiceSummary.  # noqa: E501

        UUID for a vpn service.  # noqa: E501

        :return: The ipsec_vpn_service_id of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :rtype: str
        """
        return self._ipsec_vpn_service_id

    @ipsec_vpn_service_id.setter
    def ipsec_vpn_service_id(self, ipsec_vpn_service_id):
        """Sets the ipsec_vpn_service_id of this IPSecVPNIKEServiceSummary.

        UUID for a vpn service.  # noqa: E501

        :param ipsec_vpn_service_id: The ipsec_vpn_service_id of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :type: str
        """

        self._ipsec_vpn_service_id = ipsec_vpn_service_id

    @property
    def display_name(self):
        """Gets the display_name of this IPSecVPNIKEServiceSummary.  # noqa: E501

        VPN service display name.  # noqa: E501

        :return: The display_name of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IPSecVPNIKEServiceSummary.

        VPN service display name.  # noqa: E501

        :param display_name: The display_name of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this IPSecVPNIKEServiceSummary.  # noqa: E501

        Logical router identifier associated with vpn service.  # noqa: E501

        :return: The logical_router_id of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this IPSecVPNIKEServiceSummary.

        Logical router identifier associated with vpn service.  # noqa: E501

        :param logical_router_id: The logical_router_id of this IPSecVPNIKEServiceSummary.  # noqa: E501
        :type: str
        """

        self._logical_router_id = logical_router_id

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
        if issubclass(IPSecVPNIKEServiceSummary, dict):
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
        if not isinstance(other, IPSecVPNIKEServiceSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
