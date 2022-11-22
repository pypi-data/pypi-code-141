# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .entity import Entity
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextSelectionEntity(Entity):
    """
    This lets the labeler highlight text, by specifying an offset and a length, and apply labels to it.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextSelectionEntity object with values from keyword arguments. The default value of the :py:attr:`~oci.data_labeling_service_dataplane.models.TextSelectionEntity.entity_type` attribute
        of this class is ``TEXTSELECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this TextSelectionEntity.
            Allowed values for this property are: "GENERIC", "IMAGEOBJECTSELECTION", "TEXTSELECTION"
        :type entity_type: str

        :param labels:
            The value to assign to the labels property of this TextSelectionEntity.
        :type labels: list[oci.data_labeling_service_dataplane.models.Label]

        :param text_span:
            The value to assign to the text_span property of this TextSelectionEntity.
        :type text_span: oci.data_labeling_service_dataplane.models.TextSpan

        :param extended_metadata:
            The value to assign to the extended_metadata property of this TextSelectionEntity.
        :type extended_metadata: dict(str, str)

        """
        self.swagger_types = {
            'entity_type': 'str',
            'labels': 'list[Label]',
            'text_span': 'TextSpan',
            'extended_metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'entity_type': 'entityType',
            'labels': 'labels',
            'text_span': 'textSpan',
            'extended_metadata': 'extendedMetadata'
        }

        self._entity_type = None
        self._labels = None
        self._text_span = None
        self._extended_metadata = None
        self._entity_type = 'TEXTSELECTION'

    @property
    def labels(self):
        """
        **[Required]** Gets the labels of this TextSelectionEntity.
        A collection of label entities.


        :return: The labels of this TextSelectionEntity.
        :rtype: list[oci.data_labeling_service_dataplane.models.Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this TextSelectionEntity.
        A collection of label entities.


        :param labels: The labels of this TextSelectionEntity.
        :type: list[oci.data_labeling_service_dataplane.models.Label]
        """
        self._labels = labels

    @property
    def text_span(self):
        """
        **[Required]** Gets the text_span of this TextSelectionEntity.

        :return: The text_span of this TextSelectionEntity.
        :rtype: oci.data_labeling_service_dataplane.models.TextSpan
        """
        return self._text_span

    @text_span.setter
    def text_span(self, text_span):
        """
        Sets the text_span of this TextSelectionEntity.

        :param text_span: The text_span of this TextSelectionEntity.
        :type: oci.data_labeling_service_dataplane.models.TextSpan
        """
        self._text_span = text_span

    @property
    def extended_metadata(self):
        """
        Gets the extended_metadata of this TextSelectionEntity.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :return: The extended_metadata of this TextSelectionEntity.
        :rtype: dict(str, str)
        """
        return self._extended_metadata

    @extended_metadata.setter
    def extended_metadata(self, extended_metadata):
        """
        Sets the extended_metadata of this TextSelectionEntity.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :param extended_metadata: The extended_metadata of this TextSelectionEntity.
        :type: dict(str, str)
        """
        self._extended_metadata = extended_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
