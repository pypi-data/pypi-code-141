# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ThickAuthorizationResponse(object):
    """
    ThickAuthorizationResponse model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ThickAuthorizationResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy:
            The value to assign to the policy property of this ThickAuthorizationResponse.
        :type policy: str

        :param policy_cache_duration:
            The value to assign to the policy_cache_duration property of this ThickAuthorizationResponse.
        :type policy_cache_duration: str

        :param groups:
            The value to assign to the groups property of this ThickAuthorizationResponse.
        :type groups: list[str]

        :param group_membership_cache_duration:
            The value to assign to the group_membership_cache_duration property of this ThickAuthorizationResponse.
        :type group_membership_cache_duration: str

        :param flush_all_caches:
            The value to assign to the flush_all_caches property of this ThickAuthorizationResponse.
        :type flush_all_caches: bool

        """
        self.swagger_types = {
            'policy': 'str',
            'policy_cache_duration': 'str',
            'groups': 'list[str]',
            'group_membership_cache_duration': 'str',
            'flush_all_caches': 'bool'
        }

        self.attribute_map = {
            'policy': 'policy',
            'policy_cache_duration': 'policyCacheDuration',
            'groups': 'groups',
            'group_membership_cache_duration': 'groupMembershipCacheDuration',
            'flush_all_caches': 'flushAllCaches'
        }

        self._policy = None
        self._policy_cache_duration = None
        self._groups = None
        self._group_membership_cache_duration = None
        self._flush_all_caches = None

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this ThickAuthorizationResponse.
        The policy string related to the request


        :return: The policy of this ThickAuthorizationResponse.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this ThickAuthorizationResponse.
        The policy string related to the request


        :param policy: The policy of this ThickAuthorizationResponse.
        :type: str
        """
        self._policy = policy

    @property
    def policy_cache_duration(self):
        """
        **[Required]** Gets the policy_cache_duration of this ThickAuthorizationResponse.
        The duration of how long this policy should be cached. Note that the type is of type java.time.Duration, not
        string.


        :return: The policy_cache_duration of this ThickAuthorizationResponse.
        :rtype: str
        """
        return self._policy_cache_duration

    @policy_cache_duration.setter
    def policy_cache_duration(self, policy_cache_duration):
        """
        Sets the policy_cache_duration of this ThickAuthorizationResponse.
        The duration of how long this policy should be cached. Note that the type is of type java.time.Duration, not
        string.


        :param policy_cache_duration: The policy_cache_duration of this ThickAuthorizationResponse.
        :type: str
        """
        self._policy_cache_duration = policy_cache_duration

    @property
    def groups(self):
        """
        **[Required]** Gets the groups of this ThickAuthorizationResponse.
        The policy string related to the request.


        :return: The groups of this ThickAuthorizationResponse.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this ThickAuthorizationResponse.
        The policy string related to the request.


        :param groups: The groups of this ThickAuthorizationResponse.
        :type: list[str]
        """
        self._groups = groups

    @property
    def group_membership_cache_duration(self):
        """
        **[Required]** Gets the group_membership_cache_duration of this ThickAuthorizationResponse.
        The duration of how long the user's group membership should be cached. Note that the type is of type
        java.time.Duration, not string.


        :return: The group_membership_cache_duration of this ThickAuthorizationResponse.
        :rtype: str
        """
        return self._group_membership_cache_duration

    @group_membership_cache_duration.setter
    def group_membership_cache_duration(self, group_membership_cache_duration):
        """
        Sets the group_membership_cache_duration of this ThickAuthorizationResponse.
        The duration of how long the user's group membership should be cached. Note that the type is of type
        java.time.Duration, not string.


        :param group_membership_cache_duration: The group_membership_cache_duration of this ThickAuthorizationResponse.
        :type: str
        """
        self._group_membership_cache_duration = group_membership_cache_duration

    @property
    def flush_all_caches(self):
        """
        Gets the flush_all_caches of this ThickAuthorizationResponse.
        If set to true, the SDK should clear the caches.


        :return: The flush_all_caches of this ThickAuthorizationResponse.
        :rtype: bool
        """
        return self._flush_all_caches

    @flush_all_caches.setter
    def flush_all_caches(self, flush_all_caches):
        """
        Sets the flush_all_caches of this ThickAuthorizationResponse.
        If set to true, the SDK should clear the caches.


        :param flush_all_caches: The flush_all_caches of this ThickAuthorizationResponse.
        :type: bool
        """
        self._flush_all_caches = flush_all_caches

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
