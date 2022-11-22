# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateContainerConfigurationDetails(object):
    """
    Update container configuration request details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateContainerConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_repository_created_on_first_push:
            The value to assign to the is_repository_created_on_first_push property of this UpdateContainerConfigurationDetails.
        :type is_repository_created_on_first_push: bool

        """
        self.swagger_types = {
            'is_repository_created_on_first_push': 'bool'
        }

        self.attribute_map = {
            'is_repository_created_on_first_push': 'isRepositoryCreatedOnFirstPush'
        }

        self._is_repository_created_on_first_push = None

    @property
    def is_repository_created_on_first_push(self):
        """
        Gets the is_repository_created_on_first_push of this UpdateContainerConfigurationDetails.
        Whether to create a new container repository when a container is pushed to a new repository path.
        Repositories created in this way belong to the root compartment.


        :return: The is_repository_created_on_first_push of this UpdateContainerConfigurationDetails.
        :rtype: bool
        """
        return self._is_repository_created_on_first_push

    @is_repository_created_on_first_push.setter
    def is_repository_created_on_first_push(self, is_repository_created_on_first_push):
        """
        Sets the is_repository_created_on_first_push of this UpdateContainerConfigurationDetails.
        Whether to create a new container repository when a container is pushed to a new repository path.
        Repositories created in this way belong to the root compartment.


        :param is_repository_created_on_first_push: The is_repository_created_on_first_push of this UpdateContainerConfigurationDetails.
        :type: bool
        """
        self._is_repository_created_on_first_push = is_repository_created_on_first_push

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
