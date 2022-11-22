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
from ._inputs import *

__all__ = ['BudgetArgs', 'Budget']

@pulumi.input_type
class BudgetArgs:
    def __init__(__self__, *,
                 budget: pulumi.Input['BudgetDataArgs'],
                 notifications_with_subscribers: Optional[pulumi.Input[Sequence[pulumi.Input['BudgetNotificationWithSubscribersArgs']]]] = None):
        """
        The set of arguments for constructing a Budget resource.
        """
        pulumi.set(__self__, "budget", budget)
        if notifications_with_subscribers is not None:
            pulumi.set(__self__, "notifications_with_subscribers", notifications_with_subscribers)

    @property
    @pulumi.getter
    def budget(self) -> pulumi.Input['BudgetDataArgs']:
        return pulumi.get(self, "budget")

    @budget.setter
    def budget(self, value: pulumi.Input['BudgetDataArgs']):
        pulumi.set(self, "budget", value)

    @property
    @pulumi.getter(name="notificationsWithSubscribers")
    def notifications_with_subscribers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BudgetNotificationWithSubscribersArgs']]]]:
        return pulumi.get(self, "notifications_with_subscribers")

    @notifications_with_subscribers.setter
    def notifications_with_subscribers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BudgetNotificationWithSubscribersArgs']]]]):
        pulumi.set(self, "notifications_with_subscribers", value)


warnings.warn("""Budget is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Budget(pulumi.CustomResource):
    warnings.warn("""Budget is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 budget: Optional[pulumi.Input[pulumi.InputType['BudgetDataArgs']]] = None,
                 notifications_with_subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BudgetNotificationWithSubscribersArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Budgets::Budget

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BudgetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Budgets::Budget

        :param str resource_name: The name of the resource.
        :param BudgetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BudgetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 budget: Optional[pulumi.Input[pulumi.InputType['BudgetDataArgs']]] = None,
                 notifications_with_subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BudgetNotificationWithSubscribersArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Budget is deprecated: Budget is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BudgetArgs.__new__(BudgetArgs)

            if budget is None and not opts.urn:
                raise TypeError("Missing required property 'budget'")
            __props__.__dict__["budget"] = budget
            __props__.__dict__["notifications_with_subscribers"] = notifications_with_subscribers
        super(Budget, __self__).__init__(
            'aws-native:budgets:Budget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Budget':
        """
        Get an existing Budget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BudgetArgs.__new__(BudgetArgs)

        __props__.__dict__["budget"] = None
        __props__.__dict__["notifications_with_subscribers"] = None
        return Budget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def budget(self) -> pulumi.Output['outputs.BudgetData']:
        return pulumi.get(self, "budget")

    @property
    @pulumi.getter(name="notificationsWithSubscribers")
    def notifications_with_subscribers(self) -> pulumi.Output[Optional[Sequence['outputs.BudgetNotificationWithSubscribers']]]:
        return pulumi.get(self, "notifications_with_subscribers")

