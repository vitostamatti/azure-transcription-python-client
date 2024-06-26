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


class ErrorDetail(object):
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
    swagger_types = {"code": "str", "message": "str", "target": "str"}

    attribute_map = {"code": "code", "message": "message", "target": "target"}

    def __init__(
        self, code=None, message=None, target=None, _configuration=None
    ):  # noqa: E501
        """ErrorDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._message = None
        self._target = None
        self.discriminator = None

        self.code = code
        self.message = message
        if target is not None:
            self.target = target

    @property
    def code(self):
        """Gets the code of this ErrorDetail.  # noqa: E501

        A service-defined error code that should be human-readable.  This code serves as a more specific indicator of the error than  the HTTP error code specified in the response.  # noqa: E501

        :return: The code of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorDetail.

        A service-defined error code that should be human-readable.  This code serves as a more specific indicator of the error than  the HTTP error code specified in the response.  # noqa: E501

        :param code: The code of this ErrorDetail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and code is None:
            raise ValueError(
                "Invalid value for `code`, must not be `None`"
            )  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this ErrorDetail.  # noqa: E501

        A human-readable representation of the error. It is intended as  an aid to developers and is not suitable for exposure to end users.  # noqa: E501

        :return: The message of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorDetail.

        A human-readable representation of the error. It is intended as  an aid to developers and is not suitable for exposure to end users.  # noqa: E501

        :param message: The message of this ErrorDetail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and message is None:
            raise ValueError(
                "Invalid value for `message`, must not be `None`"
            )  # noqa: E501

        self._message = message

    @property
    def target(self):
        """Gets the target of this ErrorDetail.  # noqa: E501

        The target of the particular error (e.g., the name of the property in error).  # noqa: E501

        :return: The target of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ErrorDetail.

        The target of the particular error (e.g., the name of the property in error).  # noqa: E501

        :param target: The target of this ErrorDetail.  # noqa: E501
        :type: str
        """

        self._target = target

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
        if issubclass(ErrorDetail, dict):
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
        if not isinstance(other, ErrorDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorDetail):
            return True

        return self.to_dict() != other.to_dict()
