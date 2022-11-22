# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClassificationType(object):
    """
    possible text classification modes
    """

    #: A constant which can be used with the classification_mode property of a ClassificationType.
    #: This constant has a value of "MULTI_CLASS"
    CLASSIFICATION_MODE_MULTI_CLASS = "MULTI_CLASS"

    #: A constant which can be used with the classification_mode property of a ClassificationType.
    #: This constant has a value of "MULTI_LABEL"
    CLASSIFICATION_MODE_MULTI_LABEL = "MULTI_LABEL"

    def __init__(self, **kwargs):
        """
        Initializes a new ClassificationType object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_language.models.ClassificationMultiClassModeDetails`
        * :class:`~oci.ai_language.models.ClassificationMultiLabelModeDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param classification_mode:
            The value to assign to the classification_mode property of this ClassificationType.
            Allowed values for this property are: "MULTI_CLASS", "MULTI_LABEL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type classification_mode: str

        """
        self.swagger_types = {
            'classification_mode': 'str'
        }

        self.attribute_map = {
            'classification_mode': 'classificationMode'
        }

        self._classification_mode = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['classificationMode']

        if type == 'MULTI_CLASS':
            return 'ClassificationMultiClassModeDetails'

        if type == 'MULTI_LABEL':
            return 'ClassificationMultiLabelModeDetails'
        else:
            return 'ClassificationType'

    @property
    def classification_mode(self):
        """
        **[Required]** Gets the classification_mode of this ClassificationType.
        classification Modes

        Allowed values for this property are: "MULTI_CLASS", "MULTI_LABEL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The classification_mode of this ClassificationType.
        :rtype: str
        """
        return self._classification_mode

    @classification_mode.setter
    def classification_mode(self, classification_mode):
        """
        Sets the classification_mode of this ClassificationType.
        classification Modes


        :param classification_mode: The classification_mode of this ClassificationType.
        :type: str
        """
        allowed_values = ["MULTI_CLASS", "MULTI_LABEL"]
        if not value_allowed_none_or_none_sentinel(classification_mode, allowed_values):
            classification_mode = 'UNKNOWN_ENUM_VALUE'
        self._classification_mode = classification_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
