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


class FileTransferProtocol(object):
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
        'protocol_name': 'str',
        'ssh_fingerprint': 'str',
        'authentication_scheme': 'FileTransferAuthenticationScheme'
    }

    attribute_map = {
        'protocol_name': 'protocol_name',
        'ssh_fingerprint': 'ssh_fingerprint',
        'authentication_scheme': 'authentication_scheme'
    }

    def __init__(self, protocol_name='sftp', ssh_fingerprint=None, authentication_scheme=None):  # noqa: E501
        """FileTransferProtocol - a model defined in Swagger"""  # noqa: E501
        self._protocol_name = None
        self._ssh_fingerprint = None
        self._authentication_scheme = None
        self.discriminator = None
        self.protocol_name = protocol_name
        self.ssh_fingerprint = ssh_fingerprint
        self.authentication_scheme = authentication_scheme

    @property
    def protocol_name(self):
        """Gets the protocol_name of this FileTransferProtocol.  # noqa: E501

        Protocol name  # noqa: E501

        :return: The protocol_name of this FileTransferProtocol.  # noqa: E501
        :rtype: str
        """
        return self._protocol_name

    @protocol_name.setter
    def protocol_name(self, protocol_name):
        """Sets the protocol_name of this FileTransferProtocol.

        Protocol name  # noqa: E501

        :param protocol_name: The protocol_name of this FileTransferProtocol.  # noqa: E501
        :type: str
        """
        if protocol_name is None:
            raise ValueError("Invalid value for `protocol_name`, must not be `None`")  # noqa: E501
        allowed_values = ["sftp"]  # noqa: E501
        if protocol_name not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol_name` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol_name, allowed_values)
            )

        self._protocol_name = protocol_name

    @property
    def ssh_fingerprint(self):
        """Gets the ssh_fingerprint of this FileTransferProtocol.  # noqa: E501

        The expected SSH fingerprint of the server. If the server's fingerprint does not match this fingerprint, the connection will be terminated.  Only ECDSA fingerprints hashed with SHA256 are supported. To obtain the host's ssh fingerprint, you should connect via some method other than SSH to obtain this information. You can use one of these commands to view the key's fingerprint: 1. ssh-keygen -l -E sha256 -f ssh_host_ecdsa_key.pub 2. awk '{print $2}' ssh_host_ecdsa_key.pub | base64 -d | sha256sum -b |    sed 's/ .*$//' | xxd -r -p | base64 | sed 's/.//44g' |    awk '{print \"SHA256:\"$1}'   # noqa: E501

        :return: The ssh_fingerprint of this FileTransferProtocol.  # noqa: E501
        :rtype: str
        """
        return self._ssh_fingerprint

    @ssh_fingerprint.setter
    def ssh_fingerprint(self, ssh_fingerprint):
        """Sets the ssh_fingerprint of this FileTransferProtocol.

        The expected SSH fingerprint of the server. If the server's fingerprint does not match this fingerprint, the connection will be terminated.  Only ECDSA fingerprints hashed with SHA256 are supported. To obtain the host's ssh fingerprint, you should connect via some method other than SSH to obtain this information. You can use one of these commands to view the key's fingerprint: 1. ssh-keygen -l -E sha256 -f ssh_host_ecdsa_key.pub 2. awk '{print $2}' ssh_host_ecdsa_key.pub | base64 -d | sha256sum -b |    sed 's/ .*$//' | xxd -r -p | base64 | sed 's/.//44g' |    awk '{print \"SHA256:\"$1}'   # noqa: E501

        :param ssh_fingerprint: The ssh_fingerprint of this FileTransferProtocol.  # noqa: E501
        :type: str
        """
        if ssh_fingerprint is None:
            raise ValueError("Invalid value for `ssh_fingerprint`, must not be `None`")  # noqa: E501

        self._ssh_fingerprint = ssh_fingerprint

    @property
    def authentication_scheme(self):
        """Gets the authentication_scheme of this FileTransferProtocol.  # noqa: E501


        :return: The authentication_scheme of this FileTransferProtocol.  # noqa: E501
        :rtype: FileTransferAuthenticationScheme
        """
        return self._authentication_scheme

    @authentication_scheme.setter
    def authentication_scheme(self, authentication_scheme):
        """Sets the authentication_scheme of this FileTransferProtocol.


        :param authentication_scheme: The authentication_scheme of this FileTransferProtocol.  # noqa: E501
        :type: FileTransferAuthenticationScheme
        """
        if authentication_scheme is None:
            raise ValueError("Invalid value for `authentication_scheme`, must not be `None`")  # noqa: E501

        self._authentication_scheme = authentication_scheme

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
        if issubclass(FileTransferProtocol, dict):
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
        if not isinstance(other, FileTransferProtocol):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
