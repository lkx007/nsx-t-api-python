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


class PacketCaptureSession(object):
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
        'system_owned': 'bool',
        'display_name': 'str',
        'description': 'str',
        'tags': 'list[Tag]',
        'create_user': 'str',
        'protection': 'str',
        'create_time': 'int',
        'last_modified_time': 'int',
        'last_modified_user': 'str',
        'id': 'str',
        'resource_type': 'str',
        'sessionid': 'str',
        'filelocation': 'str',
        'filesize': 'int',
        'sessionname': 'str',
        'errormsg': 'str',
        'endtime': 'int',
        'request': 'PacketCaptureRequest',
        'starttime': 'int',
        'sessionstatus': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'system_owned': '_system_owned',
        'display_name': 'display_name',
        'description': 'description',
        'tags': 'tags',
        'create_user': '_create_user',
        'protection': '_protection',
        'create_time': '_create_time',
        'last_modified_time': '_last_modified_time',
        'last_modified_user': '_last_modified_user',
        'id': 'id',
        'resource_type': 'resource_type',
        'sessionid': 'sessionid',
        'filelocation': 'filelocation',
        'filesize': 'filesize',
        'sessionname': 'sessionname',
        'errormsg': 'errormsg',
        'endtime': 'endtime',
        'request': 'request',
        'starttime': 'starttime',
        'sessionstatus': 'sessionstatus'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, sessionid=None, filelocation=None, filesize=None, sessionname=None, errormsg=None, endtime=None, request=None, starttime=None, sessionstatus=None, *args, **kwargs):  # noqa: E501
        """PacketCaptureSession - a model defined in Swagger"""  # noqa: E501
        self._system_owned = None
        self._display_name = None
        self._description = None
        self._tags = None
        self._create_user = None
        self._protection = None
        self._create_time = None
        self._last_modified_time = None
        self._last_modified_user = None
        self._id = None
        self._resource_type = None
        self._sessionid = None
        self._filelocation = None
        self._filesize = None
        self._sessionname = None
        self._errormsg = None
        self._endtime = None
        self._request = None
        self._starttime = None
        self._sessionstatus = None
        self.discriminator = None
        if system_owned is not None:
            self.system_owned = system_owned
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if create_user is not None:
            self.create_user = create_user
        if protection is not None:
            self.protection = protection
        if create_time is not None:
            self.create_time = create_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if last_modified_user is not None:
            self.last_modified_user = last_modified_user
        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        self.sessionid = sessionid
        if filelocation is not None:
            self.filelocation = filelocation
        if filesize is not None:
            self.filesize = filesize
        if sessionname is not None:
            self.sessionname = sessionname
        if errormsg is not None:
            self.errormsg = errormsg
        if endtime is not None:
            self.endtime = endtime
        self.request = request
        if starttime is not None:
            self.starttime = starttime
        self.sessionstatus = sessionstatus
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this PacketCaptureSession.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this PacketCaptureSession.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this PacketCaptureSession.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this PacketCaptureSession.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this PacketCaptureSession.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PacketCaptureSession.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this PacketCaptureSession.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PacketCaptureSession.

        Description of this resource  # noqa: E501

        :param description: The description of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this PacketCaptureSession.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this PacketCaptureSession.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PacketCaptureSession.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this PacketCaptureSession.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this PacketCaptureSession.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this PacketCaptureSession.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this PacketCaptureSession.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this PacketCaptureSession.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this PacketCaptureSession.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this PacketCaptureSession.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PacketCaptureSession.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this PacketCaptureSession.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this PacketCaptureSession.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this PacketCaptureSession.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this PacketCaptureSession.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this PacketCaptureSession.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this PacketCaptureSession.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this PacketCaptureSession.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this PacketCaptureSession.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PacketCaptureSession.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this PacketCaptureSession.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PacketCaptureSession.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def sessionid(self):
        """Gets the sessionid of this PacketCaptureSession.  # noqa: E501

        Packet capture session id.  # noqa: E501

        :return: The sessionid of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._sessionid

    @sessionid.setter
    def sessionid(self, sessionid):
        """Sets the sessionid of this PacketCaptureSession.

        Packet capture session id.  # noqa: E501

        :param sessionid: The sessionid of this PacketCaptureSession.  # noqa: E501
        :type: str
        """
        if sessionid is None:
            raise ValueError("Invalid value for `sessionid`, must not be `None`")  # noqa: E501

        self._sessionid = sessionid

    @property
    def filelocation(self):
        """Gets the filelocation of this PacketCaptureSession.  # noqa: E501

        Packet capture file location.  # noqa: E501

        :return: The filelocation of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._filelocation

    @filelocation.setter
    def filelocation(self, filelocation):
        """Sets the filelocation of this PacketCaptureSession.

        Packet capture file location.  # noqa: E501

        :param filelocation: The filelocation of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._filelocation = filelocation

    @property
    def filesize(self):
        """Gets the filesize of this PacketCaptureSession.  # noqa: E501

        Packet capture file Size in bytes.  # noqa: E501

        :return: The filesize of this PacketCaptureSession.  # noqa: E501
        :rtype: int
        """
        return self._filesize

    @filesize.setter
    def filesize(self, filesize):
        """Sets the filesize of this PacketCaptureSession.

        Packet capture file Size in bytes.  # noqa: E501

        :param filesize: The filesize of this PacketCaptureSession.  # noqa: E501
        :type: int
        """

        self._filesize = filesize

    @property
    def sessionname(self):
        """Gets the sessionname of this PacketCaptureSession.  # noqa: E501

        Packet capture session name.  # noqa: E501

        :return: The sessionname of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._sessionname

    @sessionname.setter
    def sessionname(self, sessionname):
        """Sets the sessionname of this PacketCaptureSession.

        Packet capture session name.  # noqa: E501

        :param sessionname: The sessionname of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._sessionname = sessionname

    @property
    def errormsg(self):
        """Gets the errormsg of this PacketCaptureSession.  # noqa: E501

        Error messasge in capture.  # noqa: E501

        :return: The errormsg of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._errormsg

    @errormsg.setter
    def errormsg(self, errormsg):
        """Sets the errormsg of this PacketCaptureSession.

        Error messasge in capture.  # noqa: E501

        :param errormsg: The errormsg of this PacketCaptureSession.  # noqa: E501
        :type: str
        """

        self._errormsg = errormsg

    @property
    def endtime(self):
        """Gets the endtime of this PacketCaptureSession.  # noqa: E501

        Timestamp when session was stopped in epoch millisecond.  # noqa: E501

        :return: The endtime of this PacketCaptureSession.  # noqa: E501
        :rtype: int
        """
        return self._endtime

    @endtime.setter
    def endtime(self, endtime):
        """Sets the endtime of this PacketCaptureSession.

        Timestamp when session was stopped in epoch millisecond.  # noqa: E501

        :param endtime: The endtime of this PacketCaptureSession.  # noqa: E501
        :type: int
        """

        self._endtime = endtime

    @property
    def request(self):
        """Gets the request of this PacketCaptureSession.  # noqa: E501


        :return: The request of this PacketCaptureSession.  # noqa: E501
        :rtype: PacketCaptureRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this PacketCaptureSession.


        :param request: The request of this PacketCaptureSession.  # noqa: E501
        :type: PacketCaptureRequest
        """
        if request is None:
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

    @property
    def starttime(self):
        """Gets the starttime of this PacketCaptureSession.  # noqa: E501

        Timestamp when session was created in epoch millisecond.  # noqa: E501

        :return: The starttime of this PacketCaptureSession.  # noqa: E501
        :rtype: int
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime):
        """Sets the starttime of this PacketCaptureSession.

        Timestamp when session was created in epoch millisecond.  # noqa: E501

        :param starttime: The starttime of this PacketCaptureSession.  # noqa: E501
        :type: int
        """

        self._starttime = starttime

    @property
    def sessionstatus(self):
        """Gets the sessionstatus of this PacketCaptureSession.  # noqa: E501

        Packet capture session status.  # noqa: E501

        :return: The sessionstatus of this PacketCaptureSession.  # noqa: E501
        :rtype: str
        """
        return self._sessionstatus

    @sessionstatus.setter
    def sessionstatus(self, sessionstatus):
        """Sets the sessionstatus of this PacketCaptureSession.

        Packet capture session status.  # noqa: E501

        :param sessionstatus: The sessionstatus of this PacketCaptureSession.  # noqa: E501
        :type: str
        """
        if sessionstatus is None:
            raise ValueError("Invalid value for `sessionstatus`, must not be `None`")  # noqa: E501
        allowed_values = ["CREATED", "STARTED", "STOPPED", "FINISHED", "ERROR"]  # noqa: E501
        if sessionstatus not in allowed_values:
            raise ValueError(
                "Invalid value for `sessionstatus` ({0}), must be one of {1}"  # noqa: E501
                .format(sessionstatus, allowed_values)
            )

        self._sessionstatus = sessionstatus

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
        if issubclass(PacketCaptureSession, dict):
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
        if not isinstance(other, PacketCaptureSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
