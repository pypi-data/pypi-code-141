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
    'GetBotVersionResult',
    'AwaitableGetBotVersionResult',
    'get_bot_version',
    'get_bot_version_output',
]

@pulumi.output_type
class GetBotVersionResult:
    def __init__(__self__, bot_version=None, description=None):
        if bot_version and not isinstance(bot_version, str):
            raise TypeError("Expected argument 'bot_version' to be a str")
        pulumi.set(__self__, "bot_version", bot_version)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> Optional[str]:
        return pulumi.get(self, "bot_version")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


class AwaitableGetBotVersionResult(GetBotVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBotVersionResult(
            bot_version=self.bot_version,
            description=self.description)


def get_bot_version(bot_id: Optional[str] = None,
                    bot_version: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBotVersionResult:
    """
    A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.
    """
    __args__ = dict()
    __args__['botId'] = bot_id
    __args__['botVersion'] = bot_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lex:getBotVersion', __args__, opts=opts, typ=GetBotVersionResult).value

    return AwaitableGetBotVersionResult(
        bot_version=__ret__.bot_version,
        description=__ret__.description)


@_utilities.lift_output_func(get_bot_version)
def get_bot_version_output(bot_id: Optional[pulumi.Input[str]] = None,
                           bot_version: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBotVersionResult]:
    """
    A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.
    """
    ...
