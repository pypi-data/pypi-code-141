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
    'GetWebACLResult',
    'AwaitableGetWebACLResult',
    'get_web_acl',
    'get_web_acl_output',
]

@pulumi.output_type
class GetWebACLResult:
    def __init__(__self__, arn=None, capacity=None, captcha_config=None, custom_response_bodies=None, default_action=None, description=None, id=None, label_namespace=None, rules=None, tags=None, visibility_config=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if capacity and not isinstance(capacity, int):
            raise TypeError("Expected argument 'capacity' to be a int")
        pulumi.set(__self__, "capacity", capacity)
        if captcha_config and not isinstance(captcha_config, dict):
            raise TypeError("Expected argument 'captcha_config' to be a dict")
        pulumi.set(__self__, "captcha_config", captcha_config)
        if custom_response_bodies and not isinstance(custom_response_bodies, dict):
            raise TypeError("Expected argument 'custom_response_bodies' to be a dict")
        pulumi.set(__self__, "custom_response_bodies", custom_response_bodies)
        if default_action and not isinstance(default_action, dict):
            raise TypeError("Expected argument 'default_action' to be a dict")
        pulumi.set(__self__, "default_action", default_action)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label_namespace and not isinstance(label_namespace, str):
            raise TypeError("Expected argument 'label_namespace' to be a str")
        pulumi.set(__self__, "label_namespace", label_namespace)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if visibility_config and not isinstance(visibility_config, dict):
            raise TypeError("Expected argument 'visibility_config' to be a dict")
        pulumi.set(__self__, "visibility_config", visibility_config)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter(name="captchaConfig")
    def captcha_config(self) -> Optional['outputs.WebACLCaptchaConfig']:
        return pulumi.get(self, "captcha_config")

    @property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(self) -> Optional['outputs.WebACLCustomResponseBodies']:
        return pulumi.get(self, "custom_response_bodies")

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional['outputs.WebACLDefaultAction']:
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="labelNamespace")
    def label_namespace(self) -> Optional[str]:
        return pulumi.get(self, "label_namespace")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.WebACLRule']]:
        """
        Collection of Rules.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.WebACLTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> Optional['outputs.WebACLVisibilityConfig']:
        return pulumi.get(self, "visibility_config")


class AwaitableGetWebACLResult(GetWebACLResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebACLResult(
            arn=self.arn,
            capacity=self.capacity,
            captcha_config=self.captcha_config,
            custom_response_bodies=self.custom_response_bodies,
            default_action=self.default_action,
            description=self.description,
            id=self.id,
            label_namespace=self.label_namespace,
            rules=self.rules,
            tags=self.tags,
            visibility_config=self.visibility_config)


def get_web_acl(id: Optional[str] = None,
                name: Optional[str] = None,
                scope: Optional['WebACLScope'] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebACLResult:
    """
    Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:wafv2:getWebACL', __args__, opts=opts, typ=GetWebACLResult).value

    return AwaitableGetWebACLResult(
        arn=__ret__.arn,
        capacity=__ret__.capacity,
        captcha_config=__ret__.captcha_config,
        custom_response_bodies=__ret__.custom_response_bodies,
        default_action=__ret__.default_action,
        description=__ret__.description,
        id=__ret__.id,
        label_namespace=__ret__.label_namespace,
        rules=__ret__.rules,
        tags=__ret__.tags,
        visibility_config=__ret__.visibility_config)


@_utilities.lift_output_func(get_web_acl)
def get_web_acl_output(id: Optional[pulumi.Input[str]] = None,
                       name: Optional[pulumi.Input[str]] = None,
                       scope: Optional[pulumi.Input['WebACLScope']] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebACLResult]:
    """
    Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.
    """
    ...
