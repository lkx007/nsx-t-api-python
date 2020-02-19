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


class MonthlyTelemetrySchedule(object):
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
        'frequency_type': 'str',
        'minutes': 'int',
        'day_of_month': 'int',
        'hour_of_day': 'int'
    }
    if hasattr(TelemetrySchedule, "swagger_types"):
        swagger_types.update(TelemetrySchedule.swagger_types)

    attribute_map = {
        'frequency_type': 'frequency_type',
        'minutes': 'minutes',
        'day_of_month': 'day_of_month',
        'hour_of_day': 'hour_of_day'
    }
    if hasattr(TelemetrySchedule, "attribute_map"):
        attribute_map.update(TelemetrySchedule.attribute_map)

    def __init__(self, frequency_type=None, minutes=0, day_of_month=None, hour_of_day=None, *args, **kwargs):  # noqa: E501
        """MonthlyTelemetrySchedule - a model defined in Swagger"""  # noqa: E501
        self._frequency_type = None
        self._minutes = None
        self._day_of_month = None
        self._hour_of_day = None
        self.discriminator = None
        self.frequency_type = frequency_type
        if minutes is not None:
            self.minutes = minutes
        self.day_of_month = day_of_month
        self.hour_of_day = hour_of_day
        TelemetrySchedule.__init__(self, *args, **kwargs)

    @property
    def frequency_type(self):
        """Gets the frequency_type of this MonthlyTelemetrySchedule.  # noqa: E501

        Specify one of DailyTelemetrySchedule, WeeklyTelemetrySchedule, or MonthlyTelemetrySchedule.  # noqa: E501

        :return: The frequency_type of this MonthlyTelemetrySchedule.  # noqa: E501
        :rtype: str
        """
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, frequency_type):
        """Sets the frequency_type of this MonthlyTelemetrySchedule.

        Specify one of DailyTelemetrySchedule, WeeklyTelemetrySchedule, or MonthlyTelemetrySchedule.  # noqa: E501

        :param frequency_type: The frequency_type of this MonthlyTelemetrySchedule.  # noqa: E501
        :type: str
        """
        if frequency_type is None:
            raise ValueError("Invalid value for `frequency_type`, must not be `None`")  # noqa: E501

        self._frequency_type = frequency_type

    @property
    def minutes(self):
        """Gets the minutes of this MonthlyTelemetrySchedule.  # noqa: E501

        Minute at which data will be collected. Specify a value between 0 through 59.   # noqa: E501

        :return: The minutes of this MonthlyTelemetrySchedule.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this MonthlyTelemetrySchedule.

        Minute at which data will be collected. Specify a value between 0 through 59.   # noqa: E501

        :param minutes: The minutes of this MonthlyTelemetrySchedule.  # noqa: E501
        :type: int
        """

        self._minutes = minutes

    @property
    def day_of_month(self):
        """Gets the day_of_month of this MonthlyTelemetrySchedule.  # noqa: E501

        Day of month on which data will be collected. Specify a value between 1 through 31.   # noqa: E501

        :return: The day_of_month of this MonthlyTelemetrySchedule.  # noqa: E501
        :rtype: int
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """Sets the day_of_month of this MonthlyTelemetrySchedule.

        Day of month on which data will be collected. Specify a value between 1 through 31.   # noqa: E501

        :param day_of_month: The day_of_month of this MonthlyTelemetrySchedule.  # noqa: E501
        :type: int
        """
        if day_of_month is None:
            raise ValueError("Invalid value for `day_of_month`, must not be `None`")  # noqa: E501

        self._day_of_month = day_of_month

    @property
    def hour_of_day(self):
        """Gets the hour_of_day of this MonthlyTelemetrySchedule.  # noqa: E501

        Hour at which data will be collected. Specify a value between 0 through 23.   # noqa: E501

        :return: The hour_of_day of this MonthlyTelemetrySchedule.  # noqa: E501
        :rtype: int
        """
        return self._hour_of_day

    @hour_of_day.setter
    def hour_of_day(self, hour_of_day):
        """Sets the hour_of_day of this MonthlyTelemetrySchedule.

        Hour at which data will be collected. Specify a value between 0 through 23.   # noqa: E501

        :param hour_of_day: The hour_of_day of this MonthlyTelemetrySchedule.  # noqa: E501
        :type: int
        """
        if hour_of_day is None:
            raise ValueError("Invalid value for `hour_of_day`, must not be `None`")  # noqa: E501

        self._hour_of_day = hour_of_day

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
        if issubclass(MonthlyTelemetrySchedule, dict):
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
        if not isinstance(other, MonthlyTelemetrySchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other