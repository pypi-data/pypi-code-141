# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RandomListFormatEntry(FormatEntry):
    """
    The Random List masking format randomly selects values from a list of values
    to replace the original values. To learn more, check Random List in the
    Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RandomListFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.RandomListFormatEntry.type` attribute
        of this class is ``RANDOM_LIST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this RandomListFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this RandomListFormatEntry.
        :type description: str

        :param random_list:
            The value to assign to the random_list property of this RandomListFormatEntry.
        :type random_list: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'random_list': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'random_list': 'randomList'
        }

        self._type = None
        self._description = None
        self._random_list = None
        self._type = 'RANDOM_LIST'

    @property
    def random_list(self):
        """
        **[Required]** Gets the random_list of this RandomListFormatEntry.
        A comma-separated list of values to be used to replace column values.
        The list can be of strings, numbers, or dates. The data type of each
        value in the list must be compatible with the data type of the column.
        The number of entries in the list cannot be more than 999.


        :return: The random_list of this RandomListFormatEntry.
        :rtype: list[str]
        """
        return self._random_list

    @random_list.setter
    def random_list(self, random_list):
        """
        Sets the random_list of this RandomListFormatEntry.
        A comma-separated list of values to be used to replace column values.
        The list can be of strings, numbers, or dates. The data type of each
        value in the list must be compatible with the data type of the column.
        The number of entries in the list cannot be more than 999.


        :param random_list: The random_list of this RandomListFormatEntry.
        :type: list[str]
        """
        self._random_list = random_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
