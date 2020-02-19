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


class AppProfile(object):
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
        'app_profile_category': 'str',
        'default_app_profile': 'bool',
        'app_profile_criteria': 'list[str]'
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
        'app_profile_category': 'app_profile_category',
        'default_app_profile': 'default_app_profile',
        'app_profile_criteria': 'app_profile_criteria'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, app_profile_category=None, default_app_profile=None, app_profile_criteria=None, *args, **kwargs):  # noqa: E501
        """AppProfile - a model defined in Swagger"""  # noqa: E501
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
        self._app_profile_category = None
        self._default_app_profile = None
        self._app_profile_criteria = None
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
        if app_profile_category is not None:
            self.app_profile_category = app_profile_category
        if default_app_profile is not None:
            self.default_app_profile = default_app_profile
        self.app_profile_criteria = app_profile_criteria
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this AppProfile.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this AppProfile.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this AppProfile.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this AppProfile.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this AppProfile.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this AppProfile.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AppProfile.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this AppProfile.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this AppProfile.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this AppProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppProfile.

        Description of this resource  # noqa: E501

        :param description: The description of this AppProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this AppProfile.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this AppProfile.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AppProfile.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this AppProfile.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this AppProfile.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this AppProfile.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this AppProfile.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this AppProfile.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this AppProfile.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this AppProfile.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this AppProfile.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this AppProfile.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this AppProfile.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this AppProfile.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AppProfile.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this AppProfile.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this AppProfile.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this AppProfile.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this AppProfile.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this AppProfile.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this AppProfile.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this AppProfile.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this AppProfile.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this AppProfile.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this AppProfile.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this AppProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppProfile.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this AppProfile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this AppProfile.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this AppProfile.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AppProfile.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this AppProfile.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def app_profile_category(self):
        """Gets the app_profile_category of this AppProfile.  # noqa: E501

        Category of the app profile, value could be any string that describes the profile  # noqa: E501

        :return: The app_profile_category of this AppProfile.  # noqa: E501
        :rtype: str
        """
        return self._app_profile_category

    @app_profile_category.setter
    def app_profile_category(self, app_profile_category):
        """Sets the app_profile_category of this AppProfile.

        Category of the app profile, value could be any string that describes the profile  # noqa: E501

        :param app_profile_category: The app_profile_category of this AppProfile.  # noqa: E501
        :type: str
        """

        self._app_profile_category = app_profile_category

    @property
    def default_app_profile(self):
        """Gets the default_app_profile of this AppProfile.  # noqa: E501

        True if this App Profile is a default profile (automatically created by the system)  # noqa: E501

        :return: The default_app_profile of this AppProfile.  # noqa: E501
        :rtype: bool
        """
        return self._default_app_profile

    @default_app_profile.setter
    def default_app_profile(self, default_app_profile):
        """Sets the default_app_profile of this AppProfile.

        True if this App Profile is a default profile (automatically created by the system)  # noqa: E501

        :param default_app_profile: The default_app_profile of this AppProfile.  # noqa: E501
        :type: bool
        """

        self._default_app_profile = default_app_profile

    @property
    def app_profile_criteria(self):
        """Gets the app_profile_criteria of this AppProfile.  # noqa: E501

        Criteria of the app profile, value could be any string or \"*\" (match any string)   # noqa: E501

        :return: The app_profile_criteria of this AppProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_profile_criteria

    @app_profile_criteria.setter
    def app_profile_criteria(self, app_profile_criteria):
        """Sets the app_profile_criteria of this AppProfile.

        Criteria of the app profile, value could be any string or \"*\" (match any string)   # noqa: E501

        :param app_profile_criteria: The app_profile_criteria of this AppProfile.  # noqa: E501
        :type: list[str]
        """
        if app_profile_criteria is None:
            raise ValueError("Invalid value for `app_profile_criteria`, must not be `None`")  # noqa: E501

        self._app_profile_criteria = app_profile_criteria

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
        if issubclass(AppProfile, dict):
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
        if not isinstance(other, AppProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other