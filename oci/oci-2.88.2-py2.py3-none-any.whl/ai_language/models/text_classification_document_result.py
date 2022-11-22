# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextClassificationDocumentResult(object):
    """
    The document response for test classification detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextClassificationDocumentResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TextClassificationDocumentResult.
        :type key: str

        :param text_classification:
            The value to assign to the text_classification property of this TextClassificationDocumentResult.
        :type text_classification: list[oci.ai_language.models.TextClassification]

        :param language_code:
            The value to assign to the language_code property of this TextClassificationDocumentResult.
        :type language_code: str

        """
        self.swagger_types = {
            'key': 'str',
            'text_classification': 'list[TextClassification]',
            'language_code': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'text_classification': 'textClassification',
            'language_code': 'languageCode'
        }

        self._key = None
        self._text_classification = None
        self._language_code = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this TextClassificationDocumentResult.
        Document unique identifier defined by the user.


        :return: The key of this TextClassificationDocumentResult.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TextClassificationDocumentResult.
        Document unique identifier defined by the user.


        :param key: The key of this TextClassificationDocumentResult.
        :type: str
        """
        self._key = key

    @property
    def text_classification(self):
        """
        **[Required]** Gets the text_classification of this TextClassificationDocumentResult.
        List of detected text classes.


        :return: The text_classification of this TextClassificationDocumentResult.
        :rtype: list[oci.ai_language.models.TextClassification]
        """
        return self._text_classification

    @text_classification.setter
    def text_classification(self, text_classification):
        """
        Sets the text_classification of this TextClassificationDocumentResult.
        List of detected text classes.


        :param text_classification: The text_classification of this TextClassificationDocumentResult.
        :type: list[oci.ai_language.models.TextClassification]
        """
        self._text_classification = text_classification

    @property
    def language_code(self):
        """
        **[Required]** Gets the language_code of this TextClassificationDocumentResult.
        Language code per the `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :return: The language_code of this TextClassificationDocumentResult.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this TextClassificationDocumentResult.
        Language code per the `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :param language_code: The language_code of this TextClassificationDocumentResult.
        :type: str
        """
        self._language_code = language_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
