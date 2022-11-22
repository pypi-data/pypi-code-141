# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/ransim/metrics/metrics.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterator, List, Optional

import betterproto
import grpclib


class EventType(betterproto.Enum):
    """Change event type"""

    # NONE indicates unknown event type
    NONE = 0
    # UPDATED indicates a metric value was set (updated)
    UPDATED = 1
    # DELETED indicates a metric was deleted
    DELETED = 2


@dataclass(eq=False, repr=False)
class Metric(betterproto.Message):
    entityid: int = betterproto.uint64_field(1)
    key: str = betterproto.string_field(2)
    value: str = betterproto.string_field(3)
    type: str = betterproto.string_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListRequest(betterproto.Message):
    entityid: int = betterproto.uint64_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListResponse(betterproto.Message):
    entityid: int = betterproto.uint64_field(1)
    metrics: List["Metric"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SetRequest(betterproto.Message):
    metric: "Metric" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SetResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetRequest(betterproto.Message):
    entityid: int = betterproto.uint64_field(1)
    name: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetResponse(betterproto.Message):
    metric: "Metric" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DeleteRequest(betterproto.Message):
    entityid: int = betterproto.uint64_field(1)
    name: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DeleteResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DeleteAllRequest(betterproto.Message):
    entityid: int = betterproto.uint64_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DeleteAllResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchResponse(betterproto.Message):
    metric: "Metric" = betterproto.message_field(1)
    type: "EventType" = betterproto.enum_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


class MetricsServiceStub(betterproto.ServiceStub):
    """
    Model provides means to create, delete and read RAN simulation model.
    """

    async def list(self, *, entityid: int = 0) -> "ListResponse":
        """
        List returns an array of all metrics for the specified entity (Node,
        Cell or UE)
        """

        request = ListRequest()
        request.entityid = entityid

        return await self._unary_unary(
            "/onos.ransim.metrics.MetricsService/List", request, ListResponse
        )

    async def set(self, *, metric: "Metric" = None) -> "SetResponse":
        """Set sets value of the named metric for the specified entity"""

        request = SetRequest()
        if metric is not None:
            request.metric = metric

        return await self._unary_unary(
            "/onos.ransim.metrics.MetricsService/Set", request, SetResponse
        )

    async def get(self, *, entityid: int = 0, name: str = "") -> "GetResponse":
        """Get retrieves the named metric for the specified entity"""

        request = GetRequest()
        request.entityid = entityid
        request.name = name

        return await self._unary_unary(
            "/onos.ransim.metrics.MetricsService/Get", request, GetResponse
        )

    async def delete(self, *, entityid: int = 0, name: str = "") -> "DeleteResponse":
        """Delete deletes the the named metric for the specified entity"""

        request = DeleteRequest()
        request.entityid = entityid
        request.name = name

        return await self._unary_unary(
            "/onos.ransim.metrics.MetricsService/Delete", request, DeleteResponse
        )

    async def delete_all(self, *, entityid: int = 0) -> "DeleteAllResponse":
        """DeleteAll deletes all metrics for the specified entity"""

        request = DeleteAllRequest()
        request.entityid = entityid

        return await self._unary_unary(
            "/onos.ransim.metrics.MetricsService/DeleteAll", request, DeleteAllResponse
        )

    async def watch(self) -> AsyncIterator["WatchResponse"]:
        """Watch returns a stream of ongoing changes to the metrics"""

        request = WatchRequest()

        async for response in self._unary_stream(
            "/onos.ransim.metrics.MetricsService/Watch",
            request,
            WatchResponse,
        ):
            yield response
