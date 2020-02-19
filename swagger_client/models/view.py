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


class View(object):
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
        'include_roles': 'str',
        'exclude_roles': 'str',
        'weight': 'int',
        'widgets': 'list[WidgetItem]',
        'shared': 'bool'
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
        'include_roles': 'include_roles',
        'exclude_roles': 'exclude_roles',
        'weight': 'weight',
        'widgets': 'widgets',
        'shared': 'shared'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, include_roles=None, exclude_roles=None, weight=10000, widgets=None, shared=False, *args, **kwargs):  # noqa: E501
        """View - a model defined in Swagger"""  # noqa: E501
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
        self._include_roles = None
        self._exclude_roles = None
        self._weight = None
        self._widgets = None
        self._shared = None
        self.discriminator = None
        if system_owned is not None:
            self.system_owned = system_owned
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
        if include_roles is not None:
            self.include_roles = include_roles
        if exclude_roles is not None:
            self.exclude_roles = exclude_roles
        if weight is not None:
            self.weight = weight
        self.widgets = widgets
        if shared is not None:
            self.shared = shared
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def system_owned(self):
        """Gets the system_owned of this View.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this View.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this View.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this View.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this View.  # noqa: E501

        Title of the widget.  # noqa: E501

        :return: The display_name of this View.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this View.

        Title of the widget.  # noqa: E501

        :param display_name: The display_name of this View.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this View.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this View.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this View.

        Description of this resource  # noqa: E501

        :param description: The description of this View.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this View.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this View.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this View.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this View.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this View.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this View.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this View.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this View.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this View.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this View.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this View.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this View.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this View.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this View.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this View.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this View.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this View.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this View.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this View.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this View.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this View.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this View.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this View.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this View.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this View.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this View.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this View.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this View.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this View.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this View.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this View.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this View.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def include_roles(self):
        """Gets the include_roles of this View.  # noqa: E501

        Comma separated list of roles to which the shared view is visible. Allows user to specify the visibility of a shared view to the specified roles. User defined roles can also be specified in the list. The roles can be obtained via GET /api/v1/aaa/roles. Please visit API documentation for details about roles.  # noqa: E501

        :return: The include_roles of this View.  # noqa: E501
        :rtype: str
        """
        return self._include_roles

    @include_roles.setter
    def include_roles(self, include_roles):
        """Sets the include_roles of this View.

        Comma separated list of roles to which the shared view is visible. Allows user to specify the visibility of a shared view to the specified roles. User defined roles can also be specified in the list. The roles can be obtained via GET /api/v1/aaa/roles. Please visit API documentation for details about roles.  # noqa: E501

        :param include_roles: The include_roles of this View.  # noqa: E501
        :type: str
        """

        self._include_roles = include_roles

    @property
    def exclude_roles(self):
        """Gets the exclude_roles of this View.  # noqa: E501

        Comma separated list of roles to which the shared view is not visible. Allows user to prevent the visibility of a shared view to the specified roles. User defined roles can also be specified in the list. The roles can be obtained via GET /api/v1/aaa/roles. Please visit API documentation for details about roles. If include_roles is specified then exclude_roles cannot be specified.  # noqa: E501

        :return: The exclude_roles of this View.  # noqa: E501
        :rtype: str
        """
        return self._exclude_roles

    @exclude_roles.setter
    def exclude_roles(self, exclude_roles):
        """Sets the exclude_roles of this View.

        Comma separated list of roles to which the shared view is not visible. Allows user to prevent the visibility of a shared view to the specified roles. User defined roles can also be specified in the list. The roles can be obtained via GET /api/v1/aaa/roles. Please visit API documentation for details about roles. If include_roles is specified then exclude_roles cannot be specified.  # noqa: E501

        :param exclude_roles: The exclude_roles of this View.  # noqa: E501
        :type: str
        """

        self._exclude_roles = exclude_roles

    @property
    def weight(self):
        """Gets the weight of this View.  # noqa: E501

        Determines placement of view relative to other views. The lower the weight, the higher it is in the placement order.  # noqa: E501

        :return: The weight of this View.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this View.

        Determines placement of view relative to other views. The lower the weight, the higher it is in the placement order.  # noqa: E501

        :param weight: The weight of this View.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def widgets(self):
        """Gets the widgets of this View.  # noqa: E501

        Array of widgets that are part of the view.  # noqa: E501

        :return: The widgets of this View.  # noqa: E501
        :rtype: list[WidgetItem]
        """
        return self._widgets

    @widgets.setter
    def widgets(self, widgets):
        """Sets the widgets of this View.

        Array of widgets that are part of the view.  # noqa: E501

        :param widgets: The widgets of this View.  # noqa: E501
        :type: list[WidgetItem]
        """
        if widgets is None:
            raise ValueError("Invalid value for `widgets`, must not be `None`")  # noqa: E501

        self._widgets = widgets

    @property
    def shared(self):
        """Gets the shared of this View.  # noqa: E501

        Defaults to false. Set to true to publish the view to other users. The widgets of a shared view are visible to other users.  # noqa: E501

        :return: The shared of this View.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this View.

        Defaults to false. Set to true to publish the view to other users. The widgets of a shared view are visible to other users.  # noqa: E501

        :param shared: The shared of this View.  # noqa: E501
        :type: bool
        """

        self._shared = shared

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
        if issubclass(View, dict):
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
        if not isinstance(other, View):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
