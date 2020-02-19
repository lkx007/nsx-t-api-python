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


class LbHttpMonitor(object):
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
        'monitor_port': 'str',
        'fall_count': 'int',
        'interval': 'int',
        'rise_count': 'int',
        'timeout': 'int',
        'response_status_codes': 'list[int]',
        'request_method': 'str',
        'request_body': 'str',
        'response_body': 'str',
        'request_url': 'str',
        'request_version': 'str',
        'request_headers': 'list[LbHttpRequestHeader]'
    }
    if hasattr(LbActiveMonitor, "swagger_types"):
        swagger_types.update(LbActiveMonitor.swagger_types)

    attribute_map = {
        'monitor_port': 'monitor_port',
        'fall_count': 'fall_count',
        'interval': 'interval',
        'rise_count': 'rise_count',
        'timeout': 'timeout',
        'response_status_codes': 'response_status_codes',
        'request_method': 'request_method',
        'request_body': 'request_body',
        'response_body': 'response_body',
        'request_url': 'request_url',
        'request_version': 'request_version',
        'request_headers': 'request_headers'
    }
    if hasattr(LbActiveMonitor, "attribute_map"):
        attribute_map.update(LbActiveMonitor.attribute_map)

    def __init__(self, monitor_port=None, fall_count=3, interval=5, rise_count=3, timeout=15, response_status_codes=None, request_method='GET', request_body=None, response_body=None, request_url=None, request_version='HTTP_VERSION_1_1', request_headers=None, *args, **kwargs):  # noqa: E501
        """LbHttpMonitor - a model defined in Swagger"""  # noqa: E501
        self._monitor_port = None
        self._fall_count = None
        self._interval = None
        self._rise_count = None
        self._timeout = None
        self._response_status_codes = None
        self._request_method = None
        self._request_body = None
        self._response_body = None
        self._request_url = None
        self._request_version = None
        self._request_headers = None
        self.discriminator = None
        if monitor_port is not None:
            self.monitor_port = monitor_port
        if fall_count is not None:
            self.fall_count = fall_count
        if interval is not None:
            self.interval = interval
        if rise_count is not None:
            self.rise_count = rise_count
        if timeout is not None:
            self.timeout = timeout
        if response_status_codes is not None:
            self.response_status_codes = response_status_codes
        if request_method is not None:
            self.request_method = request_method
        if request_body is not None:
            self.request_body = request_body
        if response_body is not None:
            self.response_body = response_body
        if request_url is not None:
            self.request_url = request_url
        if request_version is not None:
            self.request_version = request_version
        if request_headers is not None:
            self.request_headers = request_headers
        LbActiveMonitor.__init__(self, *args, **kwargs)

    @property
    def monitor_port(self):
        """Gets the monitor_port of this LbHttpMonitor.  # noqa: E501

        If the monitor port is specified, it would override pool member port setting for healthcheck. A port range is not supported. For ICMP monitor, monitor_port is not required.   # noqa: E501

        :return: The monitor_port of this LbHttpMonitor.  # noqa: E501
        :rtype: str
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this LbHttpMonitor.

        If the monitor port is specified, it would override pool member port setting for healthcheck. A port range is not supported. For ICMP monitor, monitor_port is not required.   # noqa: E501

        :param monitor_port: The monitor_port of this LbHttpMonitor.  # noqa: E501
        :type: str
        """

        self._monitor_port = monitor_port

    @property
    def fall_count(self):
        """Gets the fall_count of this LbHttpMonitor.  # noqa: E501

        num of consecutive checks must fail before marking it down  # noqa: E501

        :return: The fall_count of this LbHttpMonitor.  # noqa: E501
        :rtype: int
        """
        return self._fall_count

    @fall_count.setter
    def fall_count(self, fall_count):
        """Sets the fall_count of this LbHttpMonitor.

        num of consecutive checks must fail before marking it down  # noqa: E501

        :param fall_count: The fall_count of this LbHttpMonitor.  # noqa: E501
        :type: int
        """

        self._fall_count = fall_count

    @property
    def interval(self):
        """Gets the interval of this LbHttpMonitor.  # noqa: E501

        the frequency at which the system issues the monitor check (in second)  # noqa: E501

        :return: The interval of this LbHttpMonitor.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this LbHttpMonitor.

        the frequency at which the system issues the monitor check (in second)  # noqa: E501

        :param interval: The interval of this LbHttpMonitor.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def rise_count(self):
        """Gets the rise_count of this LbHttpMonitor.  # noqa: E501

        num of consecutive checks must pass before marking it up  # noqa: E501

        :return: The rise_count of this LbHttpMonitor.  # noqa: E501
        :rtype: int
        """
        return self._rise_count

    @rise_count.setter
    def rise_count(self, rise_count):
        """Sets the rise_count of this LbHttpMonitor.

        num of consecutive checks must pass before marking it up  # noqa: E501

        :param rise_count: The rise_count of this LbHttpMonitor.  # noqa: E501
        :type: int
        """

        self._rise_count = rise_count

    @property
    def timeout(self):
        """Gets the timeout of this LbHttpMonitor.  # noqa: E501

        the number of seconds the target has in which to respond to the monitor request   # noqa: E501

        :return: The timeout of this LbHttpMonitor.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this LbHttpMonitor.

        the number of seconds the target has in which to respond to the monitor request   # noqa: E501

        :param timeout: The timeout of this LbHttpMonitor.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def response_status_codes(self):
        """Gets the response_status_codes of this LbHttpMonitor.  # noqa: E501

        The HTTP response status code should be a valid HTTP status code.   # noqa: E501

        :return: The response_status_codes of this LbHttpMonitor.  # noqa: E501
        :rtype: list[int]
        """
        return self._response_status_codes

    @response_status_codes.setter
    def response_status_codes(self, response_status_codes):
        """Sets the response_status_codes of this LbHttpMonitor.

        The HTTP response status code should be a valid HTTP status code.   # noqa: E501

        :param response_status_codes: The response_status_codes of this LbHttpMonitor.  # noqa: E501
        :type: list[int]
        """

        self._response_status_codes = response_status_codes

    @property
    def request_method(self):
        """Gets the request_method of this LbHttpMonitor.  # noqa: E501

        the health check method for HTTP monitor type  # noqa: E501

        :return: The request_method of this LbHttpMonitor.  # noqa: E501
        :rtype: str
        """
        return self._request_method

    @request_method.setter
    def request_method(self, request_method):
        """Sets the request_method of this LbHttpMonitor.

        the health check method for HTTP monitor type  # noqa: E501

        :param request_method: The request_method of this LbHttpMonitor.  # noqa: E501
        :type: str
        """
        allowed_values = ["GET", "OPTIONS", "POST", "HEAD", "PUT"]  # noqa: E501
        if request_method not in allowed_values:
            raise ValueError(
                "Invalid value for `request_method` ({0}), must be one of {1}"  # noqa: E501
                .format(request_method, allowed_values)
            )

        self._request_method = request_method

    @property
    def request_body(self):
        """Gets the request_body of this LbHttpMonitor.  # noqa: E501

        String to send as part of HTTP health check request body. Valid only for certain HTTP methods like POST.   # noqa: E501

        :return: The request_body of this LbHttpMonitor.  # noqa: E501
        :rtype: str
        """
        return self._request_body

    @request_body.setter
    def request_body(self, request_body):
        """Sets the request_body of this LbHttpMonitor.

        String to send as part of HTTP health check request body. Valid only for certain HTTP methods like POST.   # noqa: E501

        :param request_body: The request_body of this LbHttpMonitor.  # noqa: E501
        :type: str
        """

        self._request_body = request_body

    @property
    def response_body(self):
        """Gets the response_body of this LbHttpMonitor.  # noqa: E501

        If HTTP response body match string (regular expressions not supported) is specified (using LbHttpMonitor.response_body) then the healthcheck HTTP response body is matched against the specified string and server is considered healthy only if there is a match. If the response body string is not specified, HTTP healthcheck is considered successful if the HTTP response status code is 2xx, but it can be configured to accept other status codes as successful.   # noqa: E501

        :return: The response_body of this LbHttpMonitor.  # noqa: E501
        :rtype: str
        """
        return self._response_body

    @response_body.setter
    def response_body(self, response_body):
        """Sets the response_body of this LbHttpMonitor.

        If HTTP response body match string (regular expressions not supported) is specified (using LbHttpMonitor.response_body) then the healthcheck HTTP response body is matched against the specified string and server is considered healthy only if there is a match. If the response body string is not specified, HTTP healthcheck is considered successful if the HTTP response status code is 2xx, but it can be configured to accept other status codes as successful.   # noqa: E501

        :param response_body: The response_body of this LbHttpMonitor.  # noqa: E501
        :type: str
        """

        self._response_body = response_body

    @property
    def request_url(self):
        """Gets the request_url of this LbHttpMonitor.  # noqa: E501

        URL used for HTTP monitor  # noqa: E501

        :return: The request_url of this LbHttpMonitor.  # noqa: E501
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url):
        """Sets the request_url of this LbHttpMonitor.

        URL used for HTTP monitor  # noqa: E501

        :param request_url: The request_url of this LbHttpMonitor.  # noqa: E501
        :type: str
        """

        self._request_url = request_url

    @property
    def request_version(self):
        """Gets the request_version of this LbHttpMonitor.  # noqa: E501

        HTTP request version  # noqa: E501

        :return: The request_version of this LbHttpMonitor.  # noqa: E501
        :rtype: str
        """
        return self._request_version

    @request_version.setter
    def request_version(self, request_version):
        """Sets the request_version of this LbHttpMonitor.

        HTTP request version  # noqa: E501

        :param request_version: The request_version of this LbHttpMonitor.  # noqa: E501
        :type: str
        """
        allowed_values = ["HTTP_VERSION_1_0", "HTTP_VERSION_1_1", "HTTP_VERSION_2_0"]  # noqa: E501
        if request_version not in allowed_values:
            raise ValueError(
                "Invalid value for `request_version` ({0}), must be one of {1}"  # noqa: E501
                .format(request_version, allowed_values)
            )

        self._request_version = request_version

    @property
    def request_headers(self):
        """Gets the request_headers of this LbHttpMonitor.  # noqa: E501

        Array of HTTP request headers  # noqa: E501

        :return: The request_headers of this LbHttpMonitor.  # noqa: E501
        :rtype: list[LbHttpRequestHeader]
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """Sets the request_headers of this LbHttpMonitor.

        Array of HTTP request headers  # noqa: E501

        :param request_headers: The request_headers of this LbHttpMonitor.  # noqa: E501
        :type: list[LbHttpRequestHeader]
        """

        self._request_headers = request_headers

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
        if issubclass(LbHttpMonitor, dict):
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
        if not isinstance(other, LbHttpMonitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other