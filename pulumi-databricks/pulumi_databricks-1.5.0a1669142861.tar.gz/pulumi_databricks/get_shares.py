# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetSharesResult',
    'AwaitableGetSharesResult',
    'get_shares',
    'get_shares_output',
]

@pulumi.output_type
class GetSharesResult:
    """
    A collection of values returned by getShares.
    """
    def __init__(__self__, id=None, shares=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if shares and not isinstance(shares, list):
            raise TypeError("Expected argument 'shares' to be a list")
        pulumi.set(__self__, "shares", shares)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def shares(self) -> Sequence[str]:
        """
        list of Share names.
        """
        return pulumi.get(self, "shares")


class AwaitableGetSharesResult(GetSharesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSharesResult(
            id=self.id,
            shares=self.shares)


def get_shares(shares: Optional[Sequence[str]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSharesResult:
    """
    ## Example Usage

    Getting all existing shares in the metastore

    ```python
    import pulumi
    import pulumi_databricks as databricks

    this = databricks.get_shares()
    pulumi.export("shareName", this.shares)
    ```
    ## Related Resources

    The following resources are used in the same context:

    * Share to create Delta Sharing shares.
    * Recipient to create Delta Sharing recipients.
    * Grants to manage Delta Sharing permissions.


    :param Sequence[str] shares: list of Share names.
    """
    __args__ = dict()
    __args__['shares'] = shares
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('databricks:index/getShares:getShares', __args__, opts=opts, typ=GetSharesResult).value

    return AwaitableGetSharesResult(
        id=__ret__.id,
        shares=__ret__.shares)


@_utilities.lift_output_func(get_shares)
def get_shares_output(shares: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSharesResult]:
    """
    ## Example Usage

    Getting all existing shares in the metastore

    ```python
    import pulumi
    import pulumi_databricks as databricks

    this = databricks.get_shares()
    pulumi.export("shareName", this.shares)
    ```
    ## Related Resources

    The following resources are used in the same context:

    * Share to create Delta Sharing shares.
    * Recipient to create Delta Sharing recipients.
    * Grants to manage Delta Sharing permissions.


    :param Sequence[str] shares: list of Share names.
    """
    ...
