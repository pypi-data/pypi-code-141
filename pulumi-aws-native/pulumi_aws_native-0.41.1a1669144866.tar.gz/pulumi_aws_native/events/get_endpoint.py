# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetEndpointResult',
    'AwaitableGetEndpointResult',
    'get_endpoint',
    'get_endpoint_output',
]

@pulumi.output_type
class GetEndpointResult:
    def __init__(__self__, arn=None, description=None, endpoint_id=None, endpoint_url=None, event_buses=None, replication_config=None, role_arn=None, routing_config=None, state=None, state_reason=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if endpoint_id and not isinstance(endpoint_id, str):
            raise TypeError("Expected argument 'endpoint_id' to be a str")
        pulumi.set(__self__, "endpoint_id", endpoint_id)
        if endpoint_url and not isinstance(endpoint_url, str):
            raise TypeError("Expected argument 'endpoint_url' to be a str")
        pulumi.set(__self__, "endpoint_url", endpoint_url)
        if event_buses and not isinstance(event_buses, list):
            raise TypeError("Expected argument 'event_buses' to be a list")
        pulumi.set(__self__, "event_buses", event_buses)
        if replication_config and not isinstance(replication_config, dict):
            raise TypeError("Expected argument 'replication_config' to be a dict")
        pulumi.set(__self__, "replication_config", replication_config)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if routing_config and not isinstance(routing_config, dict):
            raise TypeError("Expected argument 'routing_config' to be a dict")
        pulumi.set(__self__, "routing_config", routing_config)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_reason and not isinstance(state_reason, str):
            raise TypeError("Expected argument 'state_reason' to be a str")
        pulumi.set(__self__, "state_reason", state_reason)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[str]:
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> Optional[str]:
        return pulumi.get(self, "endpoint_url")

    @property
    @pulumi.getter(name="eventBuses")
    def event_buses(self) -> Optional[Sequence['outputs.EndpointEventBus']]:
        return pulumi.get(self, "event_buses")

    @property
    @pulumi.getter(name="replicationConfig")
    def replication_config(self) -> Optional['outputs.EndpointReplicationConfig']:
        return pulumi.get(self, "replication_config")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> Optional['outputs.EndpointRoutingConfig']:
        return pulumi.get(self, "routing_config")

    @property
    @pulumi.getter
    def state(self) -> Optional['EndpointState']:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> Optional[str]:
        return pulumi.get(self, "state_reason")


class AwaitableGetEndpointResult(GetEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEndpointResult(
            arn=self.arn,
            description=self.description,
            endpoint_id=self.endpoint_id,
            endpoint_url=self.endpoint_url,
            event_buses=self.event_buses,
            replication_config=self.replication_config,
            role_arn=self.role_arn,
            routing_config=self.routing_config,
            state=self.state,
            state_reason=self.state_reason)


def get_endpoint(name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEndpointResult:
    """
    Resource Type definition for AWS::Events::Endpoint.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:events:getEndpoint', __args__, opts=opts, typ=GetEndpointResult).value

    return AwaitableGetEndpointResult(
        arn=__ret__.arn,
        description=__ret__.description,
        endpoint_id=__ret__.endpoint_id,
        endpoint_url=__ret__.endpoint_url,
        event_buses=__ret__.event_buses,
        replication_config=__ret__.replication_config,
        role_arn=__ret__.role_arn,
        routing_config=__ret__.routing_config,
        state=__ret__.state,
        state_reason=__ret__.state_reason)


@_utilities.lift_output_func(get_endpoint)
def get_endpoint_output(name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEndpointResult]:
    """
    Resource Type definition for AWS::Events::Endpoint.
    """
    ...
