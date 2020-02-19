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


class TraceflowObservationDelivered(object):
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
        'timestamp_micro': 'int',
        'component_sub_type': 'str',
        'resource_type': 'str',
        'component_type': 'str',
        'transport_node_name': 'str',
        'timestamp': 'int',
        'transport_node_id': 'str',
        'sequence_no': 'int',
        'transport_node_type': 'str',
        'component_name': 'str',
        'resolution_type': 'str',
        'lport_name': 'str',
        'target_mac': 'str',
        'vlan_id': 'int',
        'lport_id': 'str'
    }
    if hasattr(TraceflowObservation, "swagger_types"):
        swagger_types.update(TraceflowObservation.swagger_types)

    attribute_map = {
        'timestamp_micro': 'timestamp_micro',
        'component_sub_type': 'component_sub_type',
        'resource_type': 'resource_type',
        'component_type': 'component_type',
        'transport_node_name': 'transport_node_name',
        'timestamp': 'timestamp',
        'transport_node_id': 'transport_node_id',
        'sequence_no': 'sequence_no',
        'transport_node_type': 'transport_node_type',
        'component_name': 'component_name',
        'resolution_type': 'resolution_type',
        'lport_name': 'lport_name',
        'target_mac': 'target_mac',
        'vlan_id': 'vlan_id',
        'lport_id': 'lport_id'
    }
    if hasattr(TraceflowObservation, "attribute_map"):
        attribute_map.update(TraceflowObservation.attribute_map)

    def __init__(self, timestamp_micro=None, component_sub_type=None, resource_type=None, component_type=None, transport_node_name=None, timestamp=None, transport_node_id=None, sequence_no=None, transport_node_type=None, component_name=None, resolution_type=None, lport_name=None, target_mac=None, vlan_id=None, lport_id=None, *args, **kwargs):  # noqa: E501
        """TraceflowObservationDelivered - a model defined in Swagger"""  # noqa: E501
        self._timestamp_micro = None
        self._component_sub_type = None
        self._resource_type = None
        self._component_type = None
        self._transport_node_name = None
        self._timestamp = None
        self._transport_node_id = None
        self._sequence_no = None
        self._transport_node_type = None
        self._component_name = None
        self._resolution_type = None
        self._lport_name = None
        self._target_mac = None
        self._vlan_id = None
        self._lport_id = None
        self.discriminator = None
        if timestamp_micro is not None:
            self.timestamp_micro = timestamp_micro
        if component_sub_type is not None:
            self.component_sub_type = component_sub_type
        self.resource_type = resource_type
        if component_type is not None:
            self.component_type = component_type
        if transport_node_name is not None:
            self.transport_node_name = transport_node_name
        if timestamp is not None:
            self.timestamp = timestamp
        if transport_node_id is not None:
            self.transport_node_id = transport_node_id
        if sequence_no is not None:
            self.sequence_no = sequence_no
        if transport_node_type is not None:
            self.transport_node_type = transport_node_type
        if component_name is not None:
            self.component_name = component_name
        if resolution_type is not None:
            self.resolution_type = resolution_type
        if lport_name is not None:
            self.lport_name = lport_name
        if target_mac is not None:
            self.target_mac = target_mac
        if vlan_id is not None:
            self.vlan_id = vlan_id
        if lport_id is not None:
            self.lport_id = lport_id
        TraceflowObservation.__init__(self, *args, **kwargs)

    @property
    def timestamp_micro(self):
        """Gets the timestamp_micro of this TraceflowObservationDelivered.  # noqa: E501

        Timestamp when the observation was created by the transport node (microseconds epoch)  # noqa: E501

        :return: The timestamp_micro of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: int
        """
        return self._timestamp_micro

    @timestamp_micro.setter
    def timestamp_micro(self, timestamp_micro):
        """Sets the timestamp_micro of this TraceflowObservationDelivered.

        Timestamp when the observation was created by the transport node (microseconds epoch)  # noqa: E501

        :param timestamp_micro: The timestamp_micro of this TraceflowObservationDelivered.  # noqa: E501
        :type: int
        """

        self._timestamp_micro = timestamp_micro

    @property
    def component_sub_type(self):
        """Gets the component_sub_type of this TraceflowObservationDelivered.  # noqa: E501

        The sub type of the component that issued the observation.  # noqa: E501

        :return: The component_sub_type of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._component_sub_type

    @component_sub_type.setter
    def component_sub_type(self, component_sub_type):
        """Sets the component_sub_type of this TraceflowObservationDelivered.

        The sub type of the component that issued the observation.  # noqa: E501

        :param component_sub_type: The component_sub_type of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """
        allowed_values = ["LR_TIER0", "LR_TIER1", "LR_VRF_TIER0", "LS_TRANSIT", "SI_CLASSIFIER", "SI_PROXY", "VDR", "ENI", "AWS_GATEWAY", "TGW_ROUTE", "EDGE_UPLINK", "UNKNOWN"]  # noqa: E501
        if component_sub_type not in allowed_values:
            raise ValueError(
                "Invalid value for `component_sub_type` ({0}), must be one of {1}"  # noqa: E501
                .format(component_sub_type, allowed_values)
            )

        self._component_sub_type = component_sub_type

    @property
    def resource_type(self):
        """Gets the resource_type of this TraceflowObservationDelivered.  # noqa: E501


        :return: The resource_type of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TraceflowObservationDelivered.


        :param resource_type: The resource_type of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TraceflowObservationForwarded", "TraceflowObservationDropped", "TraceflowObservationDelivered", "TraceflowObservationReceived", "TraceflowObservationForwardedLogical", "TraceflowObservationDroppedLogical", "TraceflowObservationReceivedLogical", "TraceflowObservationReplicationLogical", "TraceflowObservationRelayedLogical"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def component_type(self):
        """Gets the component_type of this TraceflowObservationDelivered.  # noqa: E501

        The type of the component that issued the observation.  # noqa: E501

        :return: The component_type of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this TraceflowObservationDelivered.

        The type of the component that issued the observation.  # noqa: E501

        :param component_type: The component_type of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """
        allowed_values = ["PHYSICAL", "LR", "LS", "DFW", "BRIDGE", "EDGE_TUNNEL", "EDGE_HOSTSWITCH", "FW_BRIDGE", "LOAD_BALANCER", "NAT", "IPSEC", "SERVICE_INSERTION", "VMC", "EDGE_FW", "UNKNOWN"]  # noqa: E501
        if component_type not in allowed_values:
            raise ValueError(
                "Invalid value for `component_type` ({0}), must be one of {1}"  # noqa: E501
                .format(component_type, allowed_values)
            )

        self._component_type = component_type

    @property
    def transport_node_name(self):
        """Gets the transport_node_name of this TraceflowObservationDelivered.  # noqa: E501

        name of the transport node that observed a traceflow packet  # noqa: E501

        :return: The transport_node_name of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_name

    @transport_node_name.setter
    def transport_node_name(self, transport_node_name):
        """Sets the transport_node_name of this TraceflowObservationDelivered.

        name of the transport node that observed a traceflow packet  # noqa: E501

        :param transport_node_name: The transport_node_name of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """

        self._transport_node_name = transport_node_name

    @property
    def timestamp(self):
        """Gets the timestamp of this TraceflowObservationDelivered.  # noqa: E501

        Timestamp when the observation was created by the transport node (milliseconds epoch)  # noqa: E501

        :return: The timestamp of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TraceflowObservationDelivered.

        Timestamp when the observation was created by the transport node (milliseconds epoch)  # noqa: E501

        :param timestamp: The timestamp of this TraceflowObservationDelivered.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def transport_node_id(self):
        """Gets the transport_node_id of this TraceflowObservationDelivered.  # noqa: E501

        id of the transport node that observed a traceflow packet  # noqa: E501

        :return: The transport_node_id of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_id

    @transport_node_id.setter
    def transport_node_id(self, transport_node_id):
        """Sets the transport_node_id of this TraceflowObservationDelivered.

        id of the transport node that observed a traceflow packet  # noqa: E501

        :param transport_node_id: The transport_node_id of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """

        self._transport_node_id = transport_node_id

    @property
    def sequence_no(self):
        """Gets the sequence_no of this TraceflowObservationDelivered.  # noqa: E501

        the hop count for observations on the transport node that a traceflow packet is injected in will be 0. The hop count is incremented each time a subsequent transport node receives the traceflow packet. The sequence number of 999 indicates that the hop count could not be determined for the containing observation.  # noqa: E501

        :return: The sequence_no of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        """Sets the sequence_no of this TraceflowObservationDelivered.

        the hop count for observations on the transport node that a traceflow packet is injected in will be 0. The hop count is incremented each time a subsequent transport node receives the traceflow packet. The sequence number of 999 indicates that the hop count could not be determined for the containing observation.  # noqa: E501

        :param sequence_no: The sequence_no of this TraceflowObservationDelivered.  # noqa: E501
        :type: int
        """

        self._sequence_no = sequence_no

    @property
    def transport_node_type(self):
        """Gets the transport_node_type of this TraceflowObservationDelivered.  # noqa: E501

        type of the transport node that observed a traceflow packet  # noqa: E501

        :return: The transport_node_type of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_type

    @transport_node_type.setter
    def transport_node_type(self, transport_node_type):
        """Sets the transport_node_type of this TraceflowObservationDelivered.

        type of the transport node that observed a traceflow packet  # noqa: E501

        :param transport_node_type: The transport_node_type of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """
        allowed_values = ["ESX", "RHELKVM", "UBUNTUKVM", "EDGE", "PUBLIC_CLOUD_GATEWAY_NODE", "OTHERS", "HYPERV"]  # noqa: E501
        if transport_node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transport_node_type, allowed_values)
            )

        self._transport_node_type = transport_node_type

    @property
    def component_name(self):
        """Gets the component_name of this TraceflowObservationDelivered.  # noqa: E501

        The name of the component that issued the observation.  # noqa: E501

        :return: The component_name of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this TraceflowObservationDelivered.

        The name of the component that issued the observation.  # noqa: E501

        :param component_name: The component_name of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """

        self._component_name = component_name

    @property
    def resolution_type(self):
        """Gets the resolution_type of this TraceflowObservationDelivered.  # noqa: E501

        This field specifies the resolution type of ARP ARP_SUPPRESSION_PORT_CACHE - ARP request is suppressed by port DB ARP_SUPPRESSION_TABLE - ARP request is suppressed by ARP table ARP_SUPPRESSION_CP_QUERY - ARP request is suppressed by info derived from CP ARP_VM - No suppression and the ARP request is resolved.  # noqa: E501

        :return: The resolution_type of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._resolution_type

    @resolution_type.setter
    def resolution_type(self, resolution_type):
        """Sets the resolution_type of this TraceflowObservationDelivered.

        This field specifies the resolution type of ARP ARP_SUPPRESSION_PORT_CACHE - ARP request is suppressed by port DB ARP_SUPPRESSION_TABLE - ARP request is suppressed by ARP table ARP_SUPPRESSION_CP_QUERY - ARP request is suppressed by info derived from CP ARP_VM - No suppression and the ARP request is resolved.  # noqa: E501

        :param resolution_type: The resolution_type of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "ARP_SUPPRESSION_PORT_CACHE", "ARP_SUPPRESSION_TABLE", "ARP_SUPPRESSION_CP_QUERY", "ARP_VM"]  # noqa: E501
        if resolution_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resolution_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resolution_type, allowed_values)
            )

        self._resolution_type = resolution_type

    @property
    def lport_name(self):
        """Gets the lport_name of this TraceflowObservationDelivered.  # noqa: E501

        The name of the logical port into which the traceflow packet was delivered  # noqa: E501

        :return: The lport_name of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._lport_name

    @lport_name.setter
    def lport_name(self, lport_name):
        """Sets the lport_name of this TraceflowObservationDelivered.

        The name of the logical port into which the traceflow packet was delivered  # noqa: E501

        :param lport_name: The lport_name of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """

        self._lport_name = lport_name

    @property
    def target_mac(self):
        """Gets the target_mac of this TraceflowObservationDelivered.  # noqa: E501

        The source MAC address of form: \"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$\". For example: 00:00:00:00:00:00.   # noqa: E501

        :return: The target_mac of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._target_mac

    @target_mac.setter
    def target_mac(self, target_mac):
        """Sets the target_mac of this TraceflowObservationDelivered.

        The source MAC address of form: \"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$\". For example: 00:00:00:00:00:00.   # noqa: E501

        :param target_mac: The target_mac of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """

        self._target_mac = target_mac

    @property
    def vlan_id(self):
        """Gets the vlan_id of this TraceflowObservationDelivered.  # noqa: E501

        VLAN on bridged network  # noqa: E501

        :return: The vlan_id of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this TraceflowObservationDelivered.

        VLAN on bridged network  # noqa: E501

        :param vlan_id: The vlan_id of this TraceflowObservationDelivered.  # noqa: E501
        :type: int
        """

        self._vlan_id = vlan_id

    @property
    def lport_id(self):
        """Gets the lport_id of this TraceflowObservationDelivered.  # noqa: E501

        The id of the logical port into which the traceflow packet was delivered  # noqa: E501

        :return: The lport_id of this TraceflowObservationDelivered.  # noqa: E501
        :rtype: str
        """
        return self._lport_id

    @lport_id.setter
    def lport_id(self, lport_id):
        """Sets the lport_id of this TraceflowObservationDelivered.

        The id of the logical port into which the traceflow packet was delivered  # noqa: E501

        :param lport_id: The lport_id of this TraceflowObservationDelivered.  # noqa: E501
        :type: str
        """

        self._lport_id = lport_id

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
        if issubclass(TraceflowObservationDelivered, dict):
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
        if not isinstance(other, TraceflowObservationDelivered):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
