# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .virtual_service_traffic_route_rule import VirtualServiceTrafficRouteRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpVirtualServiceTrafficRouteRule(VirtualServiceTrafficRouteRule):
    """
    Rule for routing incoming Virtual Service traffic with HTTP protocol
    """

    #: A constant which can be used with the path_type property of a HttpVirtualServiceTrafficRouteRule.
    #: This constant has a value of "PREFIX"
    PATH_TYPE_PREFIX = "PREFIX"

    def __init__(self, **kwargs):
        """
        Initializes a new HttpVirtualServiceTrafficRouteRule object with values from keyword arguments. The default value of the :py:attr:`~oci.service_mesh.models.HttpVirtualServiceTrafficRouteRule.type` attribute
        of this class is ``HTTP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this HttpVirtualServiceTrafficRouteRule.
            Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param destinations:
            The value to assign to the destinations property of this HttpVirtualServiceTrafficRouteRule.
        :type destinations: list[oci.service_mesh.models.VirtualDeploymentTrafficRuleTarget]

        :param path:
            The value to assign to the path property of this HttpVirtualServiceTrafficRouteRule.
        :type path: str

        :param path_type:
            The value to assign to the path_type property of this HttpVirtualServiceTrafficRouteRule.
            Allowed values for this property are: "PREFIX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type path_type: str

        :param is_grpc:
            The value to assign to the is_grpc property of this HttpVirtualServiceTrafficRouteRule.
        :type is_grpc: bool

        """
        self.swagger_types = {
            'type': 'str',
            'destinations': 'list[VirtualDeploymentTrafficRuleTarget]',
            'path': 'str',
            'path_type': 'str',
            'is_grpc': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'destinations': 'destinations',
            'path': 'path',
            'path_type': 'pathType',
            'is_grpc': 'isGrpc'
        }

        self._type = None
        self._destinations = None
        self._path = None
        self._path_type = None
        self._is_grpc = None
        self._type = 'HTTP'

    @property
    def path(self):
        """
        Gets the path of this HttpVirtualServiceTrafficRouteRule.
        Route to match


        :return: The path of this HttpVirtualServiceTrafficRouteRule.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this HttpVirtualServiceTrafficRouteRule.
        Route to match


        :param path: The path of this HttpVirtualServiceTrafficRouteRule.
        :type: str
        """
        self._path = path

    @property
    def path_type(self):
        """
        Gets the path_type of this HttpVirtualServiceTrafficRouteRule.
        Match type for the route

        Allowed values for this property are: "PREFIX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The path_type of this HttpVirtualServiceTrafficRouteRule.
        :rtype: str
        """
        return self._path_type

    @path_type.setter
    def path_type(self, path_type):
        """
        Sets the path_type of this HttpVirtualServiceTrafficRouteRule.
        Match type for the route


        :param path_type: The path_type of this HttpVirtualServiceTrafficRouteRule.
        :type: str
        """
        allowed_values = ["PREFIX"]
        if not value_allowed_none_or_none_sentinel(path_type, allowed_values):
            path_type = 'UNKNOWN_ENUM_VALUE'
        self._path_type = path_type

    @property
    def is_grpc(self):
        """
        Gets the is_grpc of this HttpVirtualServiceTrafficRouteRule.
        If true, the rule will check that the content-type header has a application/grpc
        or one of the various application/grpc+ values.


        :return: The is_grpc of this HttpVirtualServiceTrafficRouteRule.
        :rtype: bool
        """
        return self._is_grpc

    @is_grpc.setter
    def is_grpc(self, is_grpc):
        """
        Sets the is_grpc of this HttpVirtualServiceTrafficRouteRule.
        If true, the rule will check that the content-type header has a application/grpc
        or one of the various application/grpc+ values.


        :param is_grpc: The is_grpc of this HttpVirtualServiceTrafficRouteRule.
        :type: bool
        """
        self._is_grpc = is_grpc

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
