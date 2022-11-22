# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .transcription_filter import TranscriptionFilter
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfanityTranscriptionFilter(TranscriptionFilter):
    """
    Profanity transcription filter to recognize profane words.
    """

    #: A constant which can be used with the mode property of a ProfanityTranscriptionFilter.
    #: This constant has a value of "MASK"
    MODE_MASK = "MASK"

    #: A constant which can be used with the mode property of a ProfanityTranscriptionFilter.
    #: This constant has a value of "REMOVE"
    MODE_REMOVE = "REMOVE"

    #: A constant which can be used with the mode property of a ProfanityTranscriptionFilter.
    #: This constant has a value of "TAG"
    MODE_TAG = "TAG"

    def __init__(self, **kwargs):
        """
        Initializes a new ProfanityTranscriptionFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_speech.models.ProfanityTranscriptionFilter.type` attribute
        of this class is ``PROFANITY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ProfanityTranscriptionFilter.
            Allowed values for this property are: "PROFANITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param mode:
            The value to assign to the mode property of this ProfanityTranscriptionFilter.
            Allowed values for this property are: "MASK", "REMOVE", "TAG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mode: str

        """
        self.swagger_types = {
            'type': 'str',
            'mode': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'mode': 'mode'
        }

        self._type = None
        self._mode = None
        self._type = 'PROFANITY'

    @property
    def mode(self):
        """
        **[Required]** Gets the mode of this ProfanityTranscriptionFilter.
        - `MASK`: Will mask detected profanity in transcription.
        - `REMOVE`: Will replace profane word with * in transcription.
        - `TAG`: Will tag profane word as profanity but will show actual word.

        Allowed values for this property are: "MASK", "REMOVE", "TAG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The mode of this ProfanityTranscriptionFilter.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this ProfanityTranscriptionFilter.
        - `MASK`: Will mask detected profanity in transcription.
        - `REMOVE`: Will replace profane word with * in transcription.
        - `TAG`: Will tag profane word as profanity but will show actual word.


        :param mode: The mode of this ProfanityTranscriptionFilter.
        :type: str
        """
        allowed_values = ["MASK", "REMOVE", "TAG"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            mode = 'UNKNOWN_ENUM_VALUE'
        self._mode = mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
