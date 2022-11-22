# coding: utf-8

"""
    Workspace Data Service

    This page lists both current and proposed APIs. The proposed APIs which have not yet been implemented are marked as deprecated. This is incongruous, but by using the deprecated flag, we can force swagger-ui to display those endpoints differently.  Error codes and responses for proposed APIs are likely to change as we gain more clarity on their implementation.  As of v0.2, all APIs are subject to change without notice.   # noqa: E501

    The version of the OpenAPI document: v0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wds_client.configuration import Configuration


class SearchRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'sort': 'SearchSortDirection',
        'sort_attribute': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'sort_attribute': 'sortAttribute'
    }

    def __init__(self, offset=0, limit=10, sort=None, sort_attribute=None, local_vars_configuration=None):  # noqa: E501
        """SearchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._offset = None
        self._limit = None
        self._sort = None
        self._sort_attribute = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort
        if sort_attribute is not None:
            self.sort_attribute = sort_attribute

    @property
    def offset(self):
        """Gets the offset of this SearchRequest.  # noqa: E501

        Pagination offset  # noqa: E501

        :return: The offset of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchRequest.

        Pagination offset  # noqa: E501

        :param offset: The offset of this SearchRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchRequest.  # noqa: E501

        Pagination limit  # noqa: E501

        :return: The limit of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchRequest.

        Pagination limit  # noqa: E501

        :param limit: The limit of this SearchRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                limit is not None and limit > 1000):  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                limit is not None and limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._limit = limit

    @property
    def sort(self):
        """Gets the sort of this SearchRequest.  # noqa: E501


        :return: The sort of this SearchRequest.  # noqa: E501
        :rtype: SearchSortDirection
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this SearchRequest.


        :param sort: The sort of this SearchRequest.  # noqa: E501
        :type: SearchSortDirection
        """

        self._sort = sort

    @property
    def sort_attribute(self):
        """Gets the sort_attribute of this SearchRequest.  # noqa: E501


        :return: The sort_attribute of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_attribute

    @sort_attribute.setter
    def sort_attribute(self, sort_attribute):
        """Sets the sort_attribute of this SearchRequest.


        :param sort_attribute: The sort_attribute of this SearchRequest.  # noqa: E501
        :type: str
        """

        self._sort_attribute = sort_attribute

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchRequest):
            return True

        return self.to_dict() != other.to_dict()
