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

__all__ = [
    'GetNetworkInsightsAccessScopeResult',
    'AwaitableGetNetworkInsightsAccessScopeResult',
    'get_network_insights_access_scope',
    'get_network_insights_access_scope_output',
]

@pulumi.output_type
class GetNetworkInsightsAccessScopeResult:
    def __init__(__self__, created_date=None, network_insights_access_scope_arn=None, network_insights_access_scope_id=None, tags=None, updated_date=None):
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if network_insights_access_scope_arn and not isinstance(network_insights_access_scope_arn, str):
            raise TypeError("Expected argument 'network_insights_access_scope_arn' to be a str")
        pulumi.set(__self__, "network_insights_access_scope_arn", network_insights_access_scope_arn)
        if network_insights_access_scope_id and not isinstance(network_insights_access_scope_id, str):
            raise TypeError("Expected argument 'network_insights_access_scope_id' to be a str")
        pulumi.set(__self__, "network_insights_access_scope_id", network_insights_access_scope_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if updated_date and not isinstance(updated_date, str):
            raise TypeError("Expected argument 'updated_date' to be a str")
        pulumi.set(__self__, "updated_date", updated_date)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[str]:
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="networkInsightsAccessScopeArn")
    def network_insights_access_scope_arn(self) -> Optional[str]:
        return pulumi.get(self, "network_insights_access_scope_arn")

    @property
    @pulumi.getter(name="networkInsightsAccessScopeId")
    def network_insights_access_scope_id(self) -> Optional[str]:
        return pulumi.get(self, "network_insights_access_scope_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.NetworkInsightsAccessScopeTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedDate")
    def updated_date(self) -> Optional[str]:
        return pulumi.get(self, "updated_date")


class AwaitableGetNetworkInsightsAccessScopeResult(GetNetworkInsightsAccessScopeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkInsightsAccessScopeResult(
            created_date=self.created_date,
            network_insights_access_scope_arn=self.network_insights_access_scope_arn,
            network_insights_access_scope_id=self.network_insights_access_scope_id,
            tags=self.tags,
            updated_date=self.updated_date)


def get_network_insights_access_scope(network_insights_access_scope_id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkInsightsAccessScopeResult:
    """
    Resource schema for AWS::EC2::NetworkInsightsAccessScope
    """
    __args__ = dict()
    __args__['networkInsightsAccessScopeId'] = network_insights_access_scope_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getNetworkInsightsAccessScope', __args__, opts=opts, typ=GetNetworkInsightsAccessScopeResult).value

    return AwaitableGetNetworkInsightsAccessScopeResult(
        created_date=__ret__.created_date,
        network_insights_access_scope_arn=__ret__.network_insights_access_scope_arn,
        network_insights_access_scope_id=__ret__.network_insights_access_scope_id,
        tags=__ret__.tags,
        updated_date=__ret__.updated_date)


@_utilities.lift_output_func(get_network_insights_access_scope)
def get_network_insights_access_scope_output(network_insights_access_scope_id: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkInsightsAccessScopeResult]:
    """
    Resource schema for AWS::EC2::NetworkInsightsAccessScope
    """
    ...
