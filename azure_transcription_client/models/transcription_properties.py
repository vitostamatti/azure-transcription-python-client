# coding: utf-8

"""
    Speech to Text API v3.0

    Speech to Text API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from azure_transcription_client.configuration import Configuration


class TranscriptionProperties(object):
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
        "diarization_enabled": "bool",
        "word_level_timestamps_enabled": "bool",
        "duration": "str",
        "channels": "list[int]",
        "destination_container_url": "str",
        "punctuation_mode": "str",
        "profanity_filter_mode": "str",
        "time_to_live": "str",
        "email": "str",
        "error": "EntityError",
    }

    attribute_map = {
        "diarization_enabled": "diarizationEnabled",
        "word_level_timestamps_enabled": "wordLevelTimestampsEnabled",
        "duration": "duration",
        "channels": "channels",
        "destination_container_url": "destinationContainerUrl",
        "punctuation_mode": "punctuationMode",
        "profanity_filter_mode": "profanityFilterMode",
        "time_to_live": "timeToLive",
        "email": "email",
        "error": "error",
    }

    def __init__(
        self,
        diarization_enabled=None,
        word_level_timestamps_enabled=None,
        duration=None,
        channels=None,
        destination_container_url=None,
        punctuation_mode=None,
        profanity_filter_mode=None,
        time_to_live=None,
        email=None,
        error=None,
        _configuration=None,
    ):  # noqa: E501
        """TranscriptionProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._diarization_enabled = None
        self._word_level_timestamps_enabled = None
        self._duration = None
        self._channels = None
        self._destination_container_url = None
        self._punctuation_mode = None
        self._profanity_filter_mode = None
        self._time_to_live = None
        self._email = None
        self._error = None
        self.discriminator = None

        if diarization_enabled is not None:
            self.diarization_enabled = diarization_enabled
        if word_level_timestamps_enabled is not None:
            self.word_level_timestamps_enabled = word_level_timestamps_enabled
        if duration is not None:
            self.duration = duration
        if channels is not None:
            self.channels = channels
        if destination_container_url is not None:
            self.destination_container_url = destination_container_url
        if punctuation_mode is not None:
            self.punctuation_mode = punctuation_mode
        if profanity_filter_mode is not None:
            self.profanity_filter_mode = profanity_filter_mode
        if time_to_live is not None:
            self.time_to_live = time_to_live
        if email is not None:
            self.email = email
        if error is not None:
            self.error = error

    @property
    def diarization_enabled(self):
        """Gets the diarization_enabled of this TranscriptionProperties.  # noqa: E501

        A value indicating whether diarization (speaker separation) is requested.  # noqa: E501

        :return: The diarization_enabled of this TranscriptionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._diarization_enabled

    @diarization_enabled.setter
    def diarization_enabled(self, diarization_enabled):
        """Sets the diarization_enabled of this TranscriptionProperties.

        A value indicating whether diarization (speaker separation) is requested.  # noqa: E501

        :param diarization_enabled: The diarization_enabled of this TranscriptionProperties.  # noqa: E501
        :type: bool
        """

        self._diarization_enabled = diarization_enabled

    @property
    def word_level_timestamps_enabled(self):
        """Gets the word_level_timestamps_enabled of this TranscriptionProperties.  # noqa: E501

        A value indicating whether word level timestamps are requested.  # noqa: E501

        :return: The word_level_timestamps_enabled of this TranscriptionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._word_level_timestamps_enabled

    @word_level_timestamps_enabled.setter
    def word_level_timestamps_enabled(self, word_level_timestamps_enabled):
        """Sets the word_level_timestamps_enabled of this TranscriptionProperties.

        A value indicating whether word level timestamps are requested.  # noqa: E501

        :param word_level_timestamps_enabled: The word_level_timestamps_enabled of this TranscriptionProperties.  # noqa: E501
        :type: bool
        """

        self._word_level_timestamps_enabled = word_level_timestamps_enabled

    @property
    def duration(self):
        """Gets the duration of this TranscriptionProperties.  # noqa: E501

        The duration of the transcription. The duration is encoded as ISO 8601 duration  (\"PnYnMnDTnHnMnS\", see https://en.wikipedia.org/wiki/ISO_8601#Durations).  # noqa: E501

        :return: The duration of this TranscriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TranscriptionProperties.

        The duration of the transcription. The duration is encoded as ISO 8601 duration  (\"PnYnMnDTnHnMnS\", see https://en.wikipedia.org/wiki/ISO_8601#Durations).  # noqa: E501

        :param duration: The duration of this TranscriptionProperties.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def channels(self):
        """Gets the channels of this TranscriptionProperties.  # noqa: E501

        A collection of the requested channel numbers.  In the default case, the channels 0 and 1 are considered.  # noqa: E501

        :return: The channels of this TranscriptionProperties.  # noqa: E501
        :rtype: list[int]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this TranscriptionProperties.

        A collection of the requested channel numbers.  In the default case, the channels 0 and 1 are considered.  # noqa: E501

        :param channels: The channels of this TranscriptionProperties.  # noqa: E501
        :type: list[int]
        """

        self._channels = channels

    @property
    def destination_container_url(self):
        """Gets the destination_container_url of this TranscriptionProperties.  # noqa: E501

        The requested destination container.  # noqa: E501

        :return: The destination_container_url of this TranscriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._destination_container_url

    @destination_container_url.setter
    def destination_container_url(self, destination_container_url):
        """Sets the destination_container_url of this TranscriptionProperties.

        The requested destination container.  # noqa: E501

        :param destination_container_url: The destination_container_url of this TranscriptionProperties.  # noqa: E501
        :type: str
        """

        self._destination_container_url = destination_container_url

    @property
    def punctuation_mode(self):
        """Gets the punctuation_mode of this TranscriptionProperties.  # noqa: E501

        The requested punctuation mode.  # noqa: E501

        :return: The punctuation_mode of this TranscriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._punctuation_mode

    @punctuation_mode.setter
    def punctuation_mode(self, punctuation_mode):
        """Sets the punctuation_mode of this TranscriptionProperties.

        The requested punctuation mode.  # noqa: E501

        :param punctuation_mode: The punctuation_mode of this TranscriptionProperties.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "None",
            "Dictated",
            "Automatic",
            "DictatedAndAutomatic",
        ]  # noqa: E501
        if (
            self._configuration.client_side_validation
            and punctuation_mode not in allowed_values
        ):
            raise ValueError(
                "Invalid value for `punctuation_mode` ({0}), must be one of {1}".format(  # noqa: E501
                    punctuation_mode, allowed_values
                )
            )

        self._punctuation_mode = punctuation_mode

    @property
    def profanity_filter_mode(self):
        """Gets the profanity_filter_mode of this TranscriptionProperties.  # noqa: E501

        The requested profanity filter mode.  # noqa: E501

        :return: The profanity_filter_mode of this TranscriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._profanity_filter_mode

    @profanity_filter_mode.setter
    def profanity_filter_mode(self, profanity_filter_mode):
        """Sets the profanity_filter_mode of this TranscriptionProperties.

        The requested profanity filter mode.  # noqa: E501

        :param profanity_filter_mode: The profanity_filter_mode of this TranscriptionProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Removed", "Tags", "Masked"]  # noqa: E501
        if (
            self._configuration.client_side_validation
            and profanity_filter_mode not in allowed_values
        ):
            raise ValueError(
                "Invalid value for `profanity_filter_mode` ({0}), must be one of {1}".format(  # noqa: E501
                    profanity_filter_mode, allowed_values
                )
            )

        self._profanity_filter_mode = profanity_filter_mode

    @property
    def time_to_live(self):
        """Gets the time_to_live of this TranscriptionProperties.  # noqa: E501

        How long the transcription will be kept in the system. Once the transcription reaches the time to live  after completion (successful or failed) it will be automatically deleted. Not setting this value or setting  to 0 will disable automatic deletion.  The duration is encoded as ISO 8601 duration (\"PnYnMnDTnHnMnS\", see https://en.wikipedia.org/wiki/ISO_8601#Durations).  # noqa: E501

        :return: The time_to_live of this TranscriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this TranscriptionProperties.

        How long the transcription will be kept in the system. Once the transcription reaches the time to live  after completion (successful or failed) it will be automatically deleted. Not setting this value or setting  to 0 will disable automatic deletion.  The duration is encoded as ISO 8601 duration (\"PnYnMnDTnHnMnS\", see https://en.wikipedia.org/wiki/ISO_8601#Durations).  # noqa: E501

        :param time_to_live: The time_to_live of this TranscriptionProperties.  # noqa: E501
        :type: str
        """

        self._time_to_live = time_to_live

    @property
    def email(self):
        """Gets the email of this TranscriptionProperties.  # noqa: E501

        The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email.  # noqa: E501

        :return: The email of this TranscriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TranscriptionProperties.

        The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email.  # noqa: E501

        :param email: The email of this TranscriptionProperties.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def error(self):
        """Gets the error of this TranscriptionProperties.  # noqa: E501

        The details of the error in case the entity is in a failed state.  # noqa: E501

        :return: The error of this TranscriptionProperties.  # noqa: E501
        :rtype: EntityError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TranscriptionProperties.

        The details of the error in case the entity is in a failed state.  # noqa: E501

        :param error: The error of this TranscriptionProperties.  # noqa: E501
        :type: EntityError
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(TranscriptionProperties, dict):
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
        if not isinstance(other, TranscriptionProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranscriptionProperties):
            return True

        return self.to_dict() != other.to_dict()
