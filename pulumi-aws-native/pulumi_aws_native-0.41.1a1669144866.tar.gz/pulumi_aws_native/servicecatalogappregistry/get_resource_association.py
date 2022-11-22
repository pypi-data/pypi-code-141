# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'GetResourceAssociationResult',
    'AwaitableGetResourceAssociationResult',
    'get_resource_association',
    'get_resource_association_output',
]

@pulumi.output_type
class GetResourceAssociationResult:
    def __init__(__self__, application=None, application_arn=None, id=None, resource=None, resource_arn=None, resource_type=None):
        if application and not isinstance(application, str):
            raise TypeError("Expected argument 'application' to be a str")
        pulumi.set(__self__, "application", application)
        if application_arn and not isinstance(application_arn, str):
            raise TypeError("Expected argument 'application_arn' to be a str")
        pulumi.set(__self__, "application_arn", application_arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if resource and not isinstance(resource, str):
            raise TypeError("Expected argument 'resource' to be a str")
        pulumi.set(__self__, "resource", resource)
        if resource_arn and not isinstance(resource_arn, str):
            raise TypeError("Expected argument 'resource_arn' to be a str")
        pulumi.set(__self__, "resource_arn", resource_arn)
        if resource_type and not isinstance(resource_type, str):
            raise TypeError("Expected argument 'resource_type' to be a str")
        pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter
    def application(self) -> Optional[str]:
        """
        The name or the Id of the Application.
        """
        return pulumi.get(self, "application")

    @property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> Optional[str]:
        return pulumi.get(self, "application_arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        """
        The name or the Id of the Resource.
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[str]:
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional['ResourceAssociationResourceType']:
        """
        The type of the CFN Resource for now it's enum CFN_STACK.
        """
        return pulumi.get(self, "resource_type")


class AwaitableGetResourceAssociationResult(GetResourceAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceAssociationResult(
            application=self.application,
            application_arn=self.application_arn,
            id=self.id,
            resource=self.resource,
            resource_arn=self.resource_arn,
            resource_type=self.resource_type)


def get_resource_association(id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceAssociationResult:
    """
    Resource Schema for AWS::ServiceCatalogAppRegistry::ResourceAssociation
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:servicecatalogappregistry:getResourceAssociation', __args__, opts=opts, typ=GetResourceAssociationResult).value

    return AwaitableGetResourceAssociationResult(
        application=__ret__.application,
        application_arn=__ret__.application_arn,
        id=__ret__.id,
        resource=__ret__.resource,
        resource_arn=__ret__.resource_arn,
        resource_type=__ret__.resource_type)


@_utilities.lift_output_func(get_resource_association)
def get_resource_association_output(id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceAssociationResult]:
    """
    Resource Schema for AWS::ServiceCatalogAppRegistry::ResourceAssociation
    """
    ...
