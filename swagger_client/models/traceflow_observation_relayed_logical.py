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


class TraceflowObservationRelayedLogical(object):
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
        'message_type': 'str',
        'dst_server_address': 'str',
        'logical_comp_uuid': 'str',
        'relay_server_address': 'str'
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
        'message_type': 'message_type',
        'dst_server_address': 'dst_server_address',
        'logical_comp_uuid': 'logical_comp_uuid',
        'relay_server_address': 'relay_server_address'
    }
    if hasattr(TraceflowObservation, "attribute_map"):
        attribute_map.update(TraceflowObservation.attribute_map)

    def __init__(self, timestamp_micro=None, component_sub_type=None, resource_type=None, component_type=None, transport_node_name=None, timestamp=None, transport_node_id=None, sequence_no=None, transport_node_type=None, component_name=None, message_type='REQUEST', dst_server_address=None, logical_comp_uuid=None, relay_server_address=None, *args, **kwargs):  # noqa: E501
        """TraceflowObservationRelayedLogical - a model defined in Swagger"""  # noqa: E501
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
        self._message_type = None
        self._dst_server_address = None
        self._logical_comp_uuid = None
        self._relay_server_address = None
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
        if message_type is not None:
            self.message_type = message_type
        if dst_server_address is not None:
            self.dst_server_address = dst_server_address
        if logical_comp_uuid is not None:
            self.logical_comp_uuid = logical_comp_uuid
        if relay_server_address is not None:
            self.relay_server_address = relay_server_address
        TraceflowObservation.__init__(self, *args, **kwargs)

    @property
    def timestamp_micro(self):
        """Gets the timestamp_micro of this TraceflowObservationRelayedLogical.  # noqa: E501

        Timestamp when the observation was created by the transport node (microseconds epoch)  # noqa: E501

        :return: The timestamp_micro of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: int
        """
        return self._timestamp_micro

    @timestamp_micro.setter
    def timestamp_micro(self, timestamp_micro):
        """Sets the timestamp_micro of this TraceflowObservationRelayedLogical.

        Timestamp when the observation was created by the transport node (microseconds epoch)  # noqa: E501

        :param timestamp_micro: The timestamp_micro of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: int
        """

        self._timestamp_micro = timestamp_micro

    @property
    def component_sub_type(self):
        """Gets the component_sub_type of this TraceflowObservationRelayedLogical.  # noqa: E501

        The sub type of the component that issued the observation.  # noqa: E501

        :return: The component_sub_type of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._component_sub_type

    @component_sub_type.setter
    def component_sub_type(self, component_sub_type):
        """Sets the component_sub_type of this TraceflowObservationRelayedLogical.

        The sub type of the component that issued the observation.  # noqa: E501

        :param component_sub_type: The component_sub_type of this TraceflowObservationRelayedLogical.  # noqa: E501
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
        """Gets the resource_type of this TraceflowObservationRelayedLogical.  # noqa: E501


        :return: The resource_type of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TraceflowObservationRelayedLogical.


        :param resource_type: The resource_type of this TraceflowObservationRelayedLogical.  # noqa: E501
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
        """Gets the component_type of this TraceflowObservationRelayedLogical.  # noqa: E501

        The type of the component that issued the observation.  # noqa: E501

        :return: The component_type of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this TraceflowObservationRelayedLogical.

        The type of the component that issued the observation.  # noqa: E501

        :param component_type: The component_type of this TraceflowObservationRelayedLogical.  # noqa: E501
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
        """Gets the transport_node_name of this TraceflowObservationRelayedLogical.  # noqa: E501

        name of the transport node that observed a traceflow packet  # noqa: E501

        :return: The transport_node_name of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_name

    @transport_node_name.setter
    def transport_node_name(self, transport_node_name):
        """Sets the transport_node_name of this TraceflowObservationRelayedLogical.

        name of the transport node that observed a traceflow packet  # noqa: E501

        :param transport_node_name: The transport_node_name of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: str
        """

        self._transport_node_name = transport_node_name

    @property
    def timestamp(self):
        """Gets the timestamp of this TraceflowObservationRelayedLogical.  # noqa: E501

        Timestamp when the observation was created by the transport node (milliseconds epoch)  # noqa: E501

        :return: The timestamp of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TraceflowObservationRelayedLogical.

        Timestamp when the observation was created by the transport node (milliseconds epoch)  # noqa: E501

        :param timestamp: The timestamp of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def transport_node_id(self):
        """Gets the transport_node_id of this TraceflowObservationRelayedLogical.  # noqa: E501

        id of the transport node that observed a traceflow packet  # noqa: E501

        :return: The transport_node_id of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_id

    @transport_node_id.setter
    def transport_node_id(self, transport_node_id):
        """Sets the transport_node_id of this TraceflowObservationRelayedLogical.

        id of the transport node that observed a traceflow packet  # noqa: E501

        :param transport_node_id: The transport_node_id of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: str
        """

        self._transport_node_id = transport_node_id

    @property
    def sequence_no(self):
        """Gets the sequence_no of this TraceflowObservationRelayedLogical.  # noqa: E501

        the hop count for observations on the transport node that a traceflow packet is injected in will be 0. The hop count is incremented each time a subsequent transport node receives the traceflow packet. The sequence number of 999 indicates that the hop count could not be determined for the containing observation.  # noqa: E501

        :return: The sequence_no of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        """Sets the sequence_no of this TraceflowObservationRelayedLogical.

        the hop count for observations on the transport node that a traceflow packet is injected in will be 0. The hop count is incremented each time a subsequent transport node receives the traceflow packet. The sequence number of 999 indicates that the hop count could not be determined for the containing observation.  # noqa: E501

        :param sequence_no: The sequence_no of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: int
        """

        self._sequence_no = sequence_no

    @property
    def transport_node_type(self):
        """Gets the transport_node_type of this TraceflowObservationRelayedLogical.  # noqa: E501

        type of the transport node that observed a traceflow packet  # noqa: E501

        :return: The transport_node_type of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_type

    @transport_node_type.setter
    def transport_node_type(self, transport_node_type):
        """Sets the transport_node_type of this TraceflowObservationRelayedLogical.

        type of the transport node that observed a traceflow packet  # noqa: E501

        :param transport_node_type: The transport_node_type of this TraceflowObservationRelayedLogical.  # noqa: E501
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
        """Gets the component_name of this TraceflowObservationRelayedLogical.  # noqa: E501

        The name of the component that issued the observation.  # noqa: E501

        :return: The component_name of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this TraceflowObservationRelayedLogical.

        The name of the component that issued the observation.  # noqa: E501

        :param component_name: The component_name of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: str
        """

        self._component_name = component_name

    @property
    def message_type(self):
        """Gets the message_type of this TraceflowObservationRelayedLogical.  # noqa: E501

        This field specified the message type of the relay service REQUEST - The relay service will relay a request message to the destination server REPLY - The relay service will relay a reply message to the client  # noqa: E501

        :return: The message_type of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this TraceflowObservationRelayedLogical.

        This field specified the message type of the relay service REQUEST - The relay service will relay a request message to the destination server REPLY - The relay service will relay a reply message to the client  # noqa: E501

        :param message_type: The message_type of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: str
        """
        allowed_values = ["REQUEST", "REPLY"]  # noqa: E501
        if message_type not in allowed_values:
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"  # noqa: E501
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def dst_server_address(self):
        """Gets the dst_server_address of this TraceflowObservationRelayedLogical.  # noqa: E501

        This field specified the IP address of the destination which the packet will be relayed.  # noqa: E501

        :return: The dst_server_address of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._dst_server_address

    @dst_server_address.setter
    def dst_server_address(self, dst_server_address):
        """Sets the dst_server_address of this TraceflowObservationRelayedLogical.

        This field specified the IP address of the destination which the packet will be relayed.  # noqa: E501

        :param dst_server_address: The dst_server_address of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: str
        """

        self._dst_server_address = dst_server_address

    @property
    def logical_comp_uuid(self):
        """Gets the logical_comp_uuid of this TraceflowObservationRelayedLogical.  # noqa: E501

        This field specified the logical component that relay service located.  # noqa: E501

        :return: The logical_comp_uuid of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._logical_comp_uuid

    @logical_comp_uuid.setter
    def logical_comp_uuid(self, logical_comp_uuid):
        """Sets the logical_comp_uuid of this TraceflowObservationRelayedLogical.

        This field specified the logical component that relay service located.  # noqa: E501

        :param logical_comp_uuid: The logical_comp_uuid of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: str
        """

        self._logical_comp_uuid = logical_comp_uuid

    @property
    def relay_server_address(self):
        """Gets the relay_server_address of this TraceflowObservationRelayedLogical.  # noqa: E501

        This field specified the IP address of the relay service.  # noqa: E501

        :return: The relay_server_address of this TraceflowObservationRelayedLogical.  # noqa: E501
        :rtype: str
        """
        return self._relay_server_address

    @relay_server_address.setter
    def relay_server_address(self, relay_server_address):
        """Sets the relay_server_address of this TraceflowObservationRelayedLogical.

        This field specified the IP address of the relay service.  # noqa: E501

        :param relay_server_address: The relay_server_address of this TraceflowObservationRelayedLogical.  # noqa: E501
        :type: str
        """

        self._relay_server_address = relay_server_address

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
        if issubclass(TraceflowObservationRelayedLogical, dict):
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
        if not isinstance(other, TraceflowObservationRelayedLogical):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
