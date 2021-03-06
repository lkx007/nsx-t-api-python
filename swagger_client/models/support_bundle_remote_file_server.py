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


class SupportBundleRemoteFileServer(object):
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
        'manager_upload_only': 'bool',
        'directory_path': 'str',
        'protocol': 'SupportBundleFileTransferProtocol',
        'port': 'int',
        'server': 'str'
    }

    attribute_map = {
        'manager_upload_only': 'manager_upload_only',
        'directory_path': 'directory_path',
        'protocol': 'protocol',
        'port': 'port',
        'server': 'server'
    }

    def __init__(self, manager_upload_only=False, directory_path=None, protocol=None, port=22, server=None):  # noqa: E501
        """SupportBundleRemoteFileServer - a model defined in Swagger"""  # noqa: E501
        self._manager_upload_only = None
        self._directory_path = None
        self._protocol = None
        self._port = None
        self._server = None
        self.discriminator = None
        if manager_upload_only is not None:
            self.manager_upload_only = manager_upload_only
        self.directory_path = directory_path
        self.protocol = protocol
        if port is not None:
            self.port = port
        self.server = server

    @property
    def manager_upload_only(self):
        """Gets the manager_upload_only of this SupportBundleRemoteFileServer.  # noqa: E501

        Uploads to the remote file server performed by the manager  # noqa: E501

        :return: The manager_upload_only of this SupportBundleRemoteFileServer.  # noqa: E501
        :rtype: bool
        """
        return self._manager_upload_only

    @manager_upload_only.setter
    def manager_upload_only(self, manager_upload_only):
        """Sets the manager_upload_only of this SupportBundleRemoteFileServer.

        Uploads to the remote file server performed by the manager  # noqa: E501

        :param manager_upload_only: The manager_upload_only of this SupportBundleRemoteFileServer.  # noqa: E501
        :type: bool
        """

        self._manager_upload_only = manager_upload_only

    @property
    def directory_path(self):
        """Gets the directory_path of this SupportBundleRemoteFileServer.  # noqa: E501

        Remote server directory to copy bundle files to  # noqa: E501

        :return: The directory_path of this SupportBundleRemoteFileServer.  # noqa: E501
        :rtype: str
        """
        return self._directory_path

    @directory_path.setter
    def directory_path(self, directory_path):
        """Sets the directory_path of this SupportBundleRemoteFileServer.

        Remote server directory to copy bundle files to  # noqa: E501

        :param directory_path: The directory_path of this SupportBundleRemoteFileServer.  # noqa: E501
        :type: str
        """
        if directory_path is None:
            raise ValueError("Invalid value for `directory_path`, must not be `None`")  # noqa: E501

        self._directory_path = directory_path

    @property
    def protocol(self):
        """Gets the protocol of this SupportBundleRemoteFileServer.  # noqa: E501


        :return: The protocol of this SupportBundleRemoteFileServer.  # noqa: E501
        :rtype: SupportBundleFileTransferProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SupportBundleRemoteFileServer.


        :param protocol: The protocol of this SupportBundleRemoteFileServer.  # noqa: E501
        :type: SupportBundleFileTransferProtocol
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this SupportBundleRemoteFileServer.  # noqa: E501

        Server port  # noqa: E501

        :return: The port of this SupportBundleRemoteFileServer.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SupportBundleRemoteFileServer.

        Server port  # noqa: E501

        :param port: The port of this SupportBundleRemoteFileServer.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def server(self):
        """Gets the server of this SupportBundleRemoteFileServer.  # noqa: E501

        Remote server hostname or IP address  # noqa: E501

        :return: The server of this SupportBundleRemoteFileServer.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this SupportBundleRemoteFileServer.

        Remote server hostname or IP address  # noqa: E501

        :param server: The server of this SupportBundleRemoteFileServer.  # noqa: E501
        :type: str
        """
        if server is None:
            raise ValueError("Invalid value for `server`, must not be `None`")  # noqa: E501

        self._server = server

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
        if issubclass(SupportBundleRemoteFileServer, dict):
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
        if not isinstance(other, SupportBundleRemoteFileServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
