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


class AddManagementNodeSpec(object):
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
        'mpa_msg_client_info': 'MsgClientInfo',
        'type': 'str',
        'password': 'str',
        'user_name': 'str',
        'remote_address': 'str',
        'cert_thumbprint': 'str'
    }

    attribute_map = {
        'mpa_msg_client_info': 'mpa_msg_client_info',
        'type': 'type',
        'password': 'password',
        'user_name': 'user_name',
        'remote_address': 'remote_address',
        'cert_thumbprint': 'cert_thumbprint'
    }

    def __init__(self, mpa_msg_client_info=None, type=None, password=None, user_name=None, remote_address=None, cert_thumbprint=None):  # noqa: E501
        """AddManagementNodeSpec - a model defined in Swagger"""  # noqa: E501
        self._mpa_msg_client_info = None
        self._type = None
        self._password = None
        self._user_name = None
        self._remote_address = None
        self._cert_thumbprint = None
        self.discriminator = None
        if mpa_msg_client_info is not None:
            self.mpa_msg_client_info = mpa_msg_client_info
        self.type = type
        if password is not None:
            self.password = password
        self.user_name = user_name
        self.remote_address = remote_address
        if cert_thumbprint is not None:
            self.cert_thumbprint = cert_thumbprint

    @property
    def mpa_msg_client_info(self):
        """Gets the mpa_msg_client_info of this AddManagementNodeSpec.  # noqa: E501


        :return: The mpa_msg_client_info of this AddManagementNodeSpec.  # noqa: E501
        :rtype: MsgClientInfo
        """
        return self._mpa_msg_client_info

    @mpa_msg_client_info.setter
    def mpa_msg_client_info(self, mpa_msg_client_info):
        """Sets the mpa_msg_client_info of this AddManagementNodeSpec.


        :param mpa_msg_client_info: The mpa_msg_client_info of this AddManagementNodeSpec.  # noqa: E501
        :type: MsgClientInfo
        """

        self._mpa_msg_client_info = mpa_msg_client_info

    @property
    def type(self):
        """Gets the type of this AddManagementNodeSpec.  # noqa: E501

        must be set to AddManagementNodeSpec  # noqa: E501

        :return: The type of this AddManagementNodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddManagementNodeSpec.

        must be set to AddManagementNodeSpec  # noqa: E501

        :param type: The type of this AddManagementNodeSpec.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["AddManagementNodeSpec"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def password(self):
        """Gets the password of this AddManagementNodeSpec.  # noqa: E501

        The password to be used to authenticate with the remote node.  # noqa: E501

        :return: The password of this AddManagementNodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AddManagementNodeSpec.

        The password to be used to authenticate with the remote node.  # noqa: E501

        :param password: The password of this AddManagementNodeSpec.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def user_name(self):
        """Gets the user_name of this AddManagementNodeSpec.  # noqa: E501

        The username to be used to authenticate with the remote node.  # noqa: E501

        :return: The user_name of this AddManagementNodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AddManagementNodeSpec.

        The username to be used to authenticate with the remote node.  # noqa: E501

        :param user_name: The user_name of this AddManagementNodeSpec.  # noqa: E501
        :type: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def remote_address(self):
        """Gets the remote_address of this AddManagementNodeSpec.  # noqa: E501

        The host address of the remote node to which to send this join request.  # noqa: E501

        :return: The remote_address of this AddManagementNodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._remote_address

    @remote_address.setter
    def remote_address(self, remote_address):
        """Sets the remote_address of this AddManagementNodeSpec.

        The host address of the remote node to which to send this join request.  # noqa: E501

        :param remote_address: The remote_address of this AddManagementNodeSpec.  # noqa: E501
        :type: str
        """
        if remote_address is None:
            raise ValueError("Invalid value for `remote_address`, must not be `None`")  # noqa: E501

        self._remote_address = remote_address

    @property
    def cert_thumbprint(self):
        """Gets the cert_thumbprint of this AddManagementNodeSpec.  # noqa: E501

        The certificate thumbprint of the remote node.  # noqa: E501

        :return: The cert_thumbprint of this AddManagementNodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._cert_thumbprint

    @cert_thumbprint.setter
    def cert_thumbprint(self, cert_thumbprint):
        """Sets the cert_thumbprint of this AddManagementNodeSpec.

        The certificate thumbprint of the remote node.  # noqa: E501

        :param cert_thumbprint: The cert_thumbprint of this AddManagementNodeSpec.  # noqa: E501
        :type: str
        """

        self._cert_thumbprint = cert_thumbprint

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
        if issubclass(AddManagementNodeSpec, dict):
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
        if not isinstance(other, AddManagementNodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other