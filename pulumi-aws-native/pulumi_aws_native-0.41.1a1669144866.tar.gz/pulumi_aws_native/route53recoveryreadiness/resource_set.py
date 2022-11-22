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

__all__ = ['ResourceSetArgs', 'ResourceSet']

@pulumi.input_type
class ResourceSetArgs:
    def __init__(__self__, *,
                 resource_set_type: pulumi.Input[str],
                 resources: pulumi.Input[Sequence[pulumi.Input['ResourceSetResourceArgs']]],
                 resource_set_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceSetTagArgs']]]] = None):
        """
        The set of arguments for constructing a ResourceSet resource.
        :param pulumi.Input[str] resource_set_type: The resource type of the resources in the resource set. Enter one of the following values for resource type: 
               
               AWS: :AutoScaling: :AutoScalingGroup, AWS: :CloudWatch: :Alarm, AWS: :EC2: :CustomerGateway, AWS: :DynamoDB: :Table, AWS: :EC2: :Volume, AWS: :ElasticLoadBalancing: :LoadBalancer, AWS: :ElasticLoadBalancingV2: :LoadBalancer, AWS: :MSK: :Cluster, AWS: :RDS: :DBCluster, AWS: :Route53: :HealthCheck, AWS: :SQS: :Queue, AWS: :SNS: :Topic, AWS: :SNS: :Subscription, AWS: :EC2: :VPC, AWS: :EC2: :VPNConnection, AWS: :EC2: :VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource
        :param pulumi.Input[Sequence[pulumi.Input['ResourceSetResourceArgs']]] resources: A list of resource objects in the resource set.
        :param pulumi.Input[str] resource_set_name: The name of the resource set to create.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceSetTagArgs']]] tags: A tag to associate with the parameters for a resource set.
        """
        pulumi.set(__self__, "resource_set_type", resource_set_type)
        pulumi.set(__self__, "resources", resources)
        if resource_set_name is not None:
            pulumi.set(__self__, "resource_set_name", resource_set_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceSetType")
    def resource_set_type(self) -> pulumi.Input[str]:
        """
        The resource type of the resources in the resource set. Enter one of the following values for resource type: 

        AWS: :AutoScaling: :AutoScalingGroup, AWS: :CloudWatch: :Alarm, AWS: :EC2: :CustomerGateway, AWS: :DynamoDB: :Table, AWS: :EC2: :Volume, AWS: :ElasticLoadBalancing: :LoadBalancer, AWS: :ElasticLoadBalancingV2: :LoadBalancer, AWS: :MSK: :Cluster, AWS: :RDS: :DBCluster, AWS: :Route53: :HealthCheck, AWS: :SQS: :Queue, AWS: :SNS: :Topic, AWS: :SNS: :Subscription, AWS: :EC2: :VPC, AWS: :EC2: :VPNConnection, AWS: :EC2: :VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource
        """
        return pulumi.get(self, "resource_set_type")

    @resource_set_type.setter
    def resource_set_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_set_type", value)

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Input[Sequence[pulumi.Input['ResourceSetResourceArgs']]]:
        """
        A list of resource objects in the resource set.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: pulumi.Input[Sequence[pulumi.Input['ResourceSetResourceArgs']]]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="resourceSetName")
    def resource_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource set to create.
        """
        return pulumi.get(self, "resource_set_name")

    @resource_set_name.setter
    def resource_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_set_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceSetTagArgs']]]]:
        """
        A tag to associate with the parameters for a resource set.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceSetTagArgs']]]]):
        pulumi.set(self, "tags", value)


class ResourceSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_set_name: Optional[pulumi.Input[str]] = None,
                 resource_set_type: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSetResourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSetTagArgs']]]]] = None,
                 __props__=None):
        """
        Schema for the AWS Route53 Recovery Readiness ResourceSet Resource and API.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_set_name: The name of the resource set to create.
        :param pulumi.Input[str] resource_set_type: The resource type of the resources in the resource set. Enter one of the following values for resource type: 
               
               AWS: :AutoScaling: :AutoScalingGroup, AWS: :CloudWatch: :Alarm, AWS: :EC2: :CustomerGateway, AWS: :DynamoDB: :Table, AWS: :EC2: :Volume, AWS: :ElasticLoadBalancing: :LoadBalancer, AWS: :ElasticLoadBalancingV2: :LoadBalancer, AWS: :MSK: :Cluster, AWS: :RDS: :DBCluster, AWS: :Route53: :HealthCheck, AWS: :SQS: :Queue, AWS: :SNS: :Topic, AWS: :SNS: :Subscription, AWS: :EC2: :VPC, AWS: :EC2: :VPNConnection, AWS: :EC2: :VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSetResourceArgs']]]] resources: A list of resource objects in the resource set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSetTagArgs']]]] tags: A tag to associate with the parameters for a resource set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Schema for the AWS Route53 Recovery Readiness ResourceSet Resource and API.

        :param str resource_name: The name of the resource.
        :param ResourceSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_set_name: Optional[pulumi.Input[str]] = None,
                 resource_set_type: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSetResourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSetTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceSetArgs.__new__(ResourceSetArgs)

            __props__.__dict__["resource_set_name"] = resource_set_name
            if resource_set_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_set_type'")
            __props__.__dict__["resource_set_type"] = resource_set_type
            if resources is None and not opts.urn:
                raise TypeError("Missing required property 'resources'")
            __props__.__dict__["resources"] = resources
            __props__.__dict__["tags"] = tags
            __props__.__dict__["resource_set_arn"] = None
        super(ResourceSet, __self__).__init__(
            'aws-native:route53recoveryreadiness:ResourceSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResourceSet':
        """
        Get an existing ResourceSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResourceSetArgs.__new__(ResourceSetArgs)

        __props__.__dict__["resource_set_arn"] = None
        __props__.__dict__["resource_set_name"] = None
        __props__.__dict__["resource_set_type"] = None
        __props__.__dict__["resources"] = None
        __props__.__dict__["tags"] = None
        return ResourceSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resourceSetArn")
    def resource_set_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the resource set.
        """
        return pulumi.get(self, "resource_set_arn")

    @property
    @pulumi.getter(name="resourceSetName")
    def resource_set_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource set to create.
        """
        return pulumi.get(self, "resource_set_name")

    @property
    @pulumi.getter(name="resourceSetType")
    def resource_set_type(self) -> pulumi.Output[str]:
        """
        The resource type of the resources in the resource set. Enter one of the following values for resource type: 

        AWS: :AutoScaling: :AutoScalingGroup, AWS: :CloudWatch: :Alarm, AWS: :EC2: :CustomerGateway, AWS: :DynamoDB: :Table, AWS: :EC2: :Volume, AWS: :ElasticLoadBalancing: :LoadBalancer, AWS: :ElasticLoadBalancingV2: :LoadBalancer, AWS: :MSK: :Cluster, AWS: :RDS: :DBCluster, AWS: :Route53: :HealthCheck, AWS: :SQS: :Queue, AWS: :SNS: :Topic, AWS: :SNS: :Subscription, AWS: :EC2: :VPC, AWS: :EC2: :VPNConnection, AWS: :EC2: :VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource
        """
        return pulumi.get(self, "resource_set_type")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence['outputs.ResourceSetResource']]:
        """
        A list of resource objects in the resource set.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ResourceSetTag']]]:
        """
        A tag to associate with the parameters for a resource set.
        """
        return pulumi.get(self, "tags")

