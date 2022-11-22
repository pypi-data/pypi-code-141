# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetVPCEndpointServicePermissionsResult',
    'AwaitableGetVPCEndpointServicePermissionsResult',
    'get_vpc_endpoint_service_permissions',
    'get_vpc_endpoint_service_permissions_output',
]

@pulumi.output_type
class GetVPCEndpointServicePermissionsResult:
    def __init__(__self__, allowed_principals=None, id=None):
        if allowed_principals and not isinstance(allowed_principals, list):
            raise TypeError("Expected argument 'allowed_principals' to be a list")
        pulumi.set(__self__, "allowed_principals", allowed_principals)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="allowedPrincipals")
    def allowed_principals(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "allowed_principals")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetVPCEndpointServicePermissionsResult(GetVPCEndpointServicePermissionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVPCEndpointServicePermissionsResult(
            allowed_principals=self.allowed_principals,
            id=self.id)


def get_vpc_endpoint_service_permissions(id: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVPCEndpointServicePermissionsResult:
    """
    Resource Type definition for AWS::EC2::VPCEndpointServicePermissions
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getVPCEndpointServicePermissions', __args__, opts=opts, typ=GetVPCEndpointServicePermissionsResult).value

    return AwaitableGetVPCEndpointServicePermissionsResult(
        allowed_principals=__ret__.allowed_principals,
        id=__ret__.id)


@_utilities.lift_output_func(get_vpc_endpoint_service_permissions)
def get_vpc_endpoint_service_permissions_output(id: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVPCEndpointServicePermissionsResult]:
    """
    Resource Type definition for AWS::EC2::VPCEndpointServicePermissions
    """
    ...
