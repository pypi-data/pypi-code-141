# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FieldLabel(object):
    """
    The label in a field.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FieldLabel object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this FieldLabel.
        :type name: str

        :param confidence:
            The value to assign to the confidence property of this FieldLabel.
        :type confidence: float

        """
        self.swagger_types = {
            'name': 'str',
            'confidence': 'float'
        }

        self.attribute_map = {
            'name': 'name',
            'confidence': 'confidence'
        }

        self._name = None
        self._confidence = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this FieldLabel.
        The name of the field label.


        :return: The name of this FieldLabel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FieldLabel.
        The name of the field label.


        :param name: The name of this FieldLabel.
        :type: str
        """
        self._name = name

    @property
    def confidence(self):
        """
        Gets the confidence of this FieldLabel.
        The confidence score between 0 and 1.


        :return: The confidence of this FieldLabel.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this FieldLabel.
        The confidence score between 0 and 1.


        :param confidence: The confidence of this FieldLabel.
        :type: float
        """
        self._confidence = confidence

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
