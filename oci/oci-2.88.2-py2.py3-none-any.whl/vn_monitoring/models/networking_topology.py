# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .topology import Topology
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkingTopology(Topology):
    """
    Defines the representation of a virtual network topology for a region.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkingTopology object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.NetworkingTopology.type` attribute
        of this class is ``NETWORKING`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this NetworkingTopology.
            Allowed values for this property are: "NETWORKING", "VCN", "SUBNET", "PATH"
        :type type: str

        :param entities:
            The value to assign to the entities property of this NetworkingTopology.
        :type entities: list[object]

        :param relationships:
            The value to assign to the relationships property of this NetworkingTopology.
        :type relationships: list[oci.vn_monitoring.models.TopologyEntityRelationship]

        :param time_created:
            The value to assign to the time_created property of this NetworkingTopology.
        :type time_created: datetime

        """
        self.swagger_types = {
            'type': 'str',
            'entities': 'list[object]',
            'relationships': 'list[TopologyEntityRelationship]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'entities': 'entities',
            'relationships': 'relationships',
            'time_created': 'timeCreated'
        }

        self._type = None
        self._entities = None
        self._relationships = None
        self._time_created = None
        self._type = 'NETWORKING'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
