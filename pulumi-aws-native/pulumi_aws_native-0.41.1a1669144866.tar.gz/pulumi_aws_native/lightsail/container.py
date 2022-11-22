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

__all__ = ['ContainerInitArgs', 'Container']

@pulumi.input_type
class ContainerInitArgs:
    def __init__(__self__, *,
                 power: pulumi.Input[str],
                 scale: pulumi.Input[int],
                 service_name: pulumi.Input[str],
                 container_service_deployment: Optional[pulumi.Input['ContainerServiceDeploymentArgs']] = None,
                 is_disabled: Optional[pulumi.Input[bool]] = None,
                 public_domain_names: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerPublicDomainNameArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerTagArgs']]]] = None):
        """
        The set of arguments for constructing a Container resource.
        :param pulumi.Input[str] power: The power specification for the container service.
        :param pulumi.Input[int] scale: The scale specification for the container service.
        :param pulumi.Input[str] service_name: The name for the container service.
        :param pulumi.Input['ContainerServiceDeploymentArgs'] container_service_deployment: Describes a container deployment configuration of an Amazon Lightsail container service.
        :param pulumi.Input[bool] is_disabled: A Boolean value to indicate whether the container service is disabled.
        :param pulumi.Input[Sequence[pulumi.Input['ContainerPublicDomainNameArgs']]] public_domain_names: The public domain names to use with the container service, such as example.com and www.example.com.
        :param pulumi.Input[Sequence[pulumi.Input['ContainerTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "power", power)
        pulumi.set(__self__, "scale", scale)
        pulumi.set(__self__, "service_name", service_name)
        if container_service_deployment is not None:
            pulumi.set(__self__, "container_service_deployment", container_service_deployment)
        if is_disabled is not None:
            pulumi.set(__self__, "is_disabled", is_disabled)
        if public_domain_names is not None:
            pulumi.set(__self__, "public_domain_names", public_domain_names)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def power(self) -> pulumi.Input[str]:
        """
        The power specification for the container service.
        """
        return pulumi.get(self, "power")

    @power.setter
    def power(self, value: pulumi.Input[str]):
        pulumi.set(self, "power", value)

    @property
    @pulumi.getter
    def scale(self) -> pulumi.Input[int]:
        """
        The scale specification for the container service.
        """
        return pulumi.get(self, "scale")

    @scale.setter
    def scale(self, value: pulumi.Input[int]):
        pulumi.set(self, "scale", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name for the container service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="containerServiceDeployment")
    def container_service_deployment(self) -> Optional[pulumi.Input['ContainerServiceDeploymentArgs']]:
        """
        Describes a container deployment configuration of an Amazon Lightsail container service.
        """
        return pulumi.get(self, "container_service_deployment")

    @container_service_deployment.setter
    def container_service_deployment(self, value: Optional[pulumi.Input['ContainerServiceDeploymentArgs']]):
        pulumi.set(self, "container_service_deployment", value)

    @property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        A Boolean value to indicate whether the container service is disabled.
        """
        return pulumi.get(self, "is_disabled")

    @is_disabled.setter
    def is_disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_disabled", value)

    @property
    @pulumi.getter(name="publicDomainNames")
    def public_domain_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerPublicDomainNameArgs']]]]:
        """
        The public domain names to use with the container service, such as example.com and www.example.com.
        """
        return pulumi.get(self, "public_domain_names")

    @public_domain_names.setter
    def public_domain_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerPublicDomainNameArgs']]]]):
        pulumi.set(self, "public_domain_names", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Container(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_service_deployment: Optional[pulumi.Input[pulumi.InputType['ContainerServiceDeploymentArgs']]] = None,
                 is_disabled: Optional[pulumi.Input[bool]] = None,
                 power: Optional[pulumi.Input[str]] = None,
                 public_domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerPublicDomainNameArgs']]]]] = None,
                 scale: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Lightsail::Container

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ContainerServiceDeploymentArgs']] container_service_deployment: Describes a container deployment configuration of an Amazon Lightsail container service.
        :param pulumi.Input[bool] is_disabled: A Boolean value to indicate whether the container service is disabled.
        :param pulumi.Input[str] power: The power specification for the container service.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerPublicDomainNameArgs']]]] public_domain_names: The public domain names to use with the container service, such as example.com and www.example.com.
        :param pulumi.Input[int] scale: The scale specification for the container service.
        :param pulumi.Input[str] service_name: The name for the container service.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContainerInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Lightsail::Container

        :param str resource_name: The name of the resource.
        :param ContainerInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_service_deployment: Optional[pulumi.Input[pulumi.InputType['ContainerServiceDeploymentArgs']]] = None,
                 is_disabled: Optional[pulumi.Input[bool]] = None,
                 power: Optional[pulumi.Input[str]] = None,
                 public_domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerPublicDomainNameArgs']]]]] = None,
                 scale: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerInitArgs.__new__(ContainerInitArgs)

            __props__.__dict__["container_service_deployment"] = container_service_deployment
            __props__.__dict__["is_disabled"] = is_disabled
            if power is None and not opts.urn:
                raise TypeError("Missing required property 'power'")
            __props__.__dict__["power"] = power
            __props__.__dict__["public_domain_names"] = public_domain_names
            if scale is None and not opts.urn:
                raise TypeError("Missing required property 'scale'")
            __props__.__dict__["scale"] = scale
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["container_arn"] = None
            __props__.__dict__["url"] = None
        super(Container, __self__).__init__(
            'aws-native:lightsail:Container',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Container':
        """
        Get an existing Container resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContainerInitArgs.__new__(ContainerInitArgs)

        __props__.__dict__["container_arn"] = None
        __props__.__dict__["container_service_deployment"] = None
        __props__.__dict__["is_disabled"] = None
        __props__.__dict__["power"] = None
        __props__.__dict__["public_domain_names"] = None
        __props__.__dict__["scale"] = None
        __props__.__dict__["service_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["url"] = None
        return Container(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerArn")
    def container_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "container_arn")

    @property
    @pulumi.getter(name="containerServiceDeployment")
    def container_service_deployment(self) -> pulumi.Output[Optional['outputs.ContainerServiceDeployment']]:
        """
        Describes a container deployment configuration of an Amazon Lightsail container service.
        """
        return pulumi.get(self, "container_service_deployment")

    @property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> pulumi.Output[Optional[bool]]:
        """
        A Boolean value to indicate whether the container service is disabled.
        """
        return pulumi.get(self, "is_disabled")

    @property
    @pulumi.getter
    def power(self) -> pulumi.Output[str]:
        """
        The power specification for the container service.
        """
        return pulumi.get(self, "power")

    @property
    @pulumi.getter(name="publicDomainNames")
    def public_domain_names(self) -> pulumi.Output[Optional[Sequence['outputs.ContainerPublicDomainName']]]:
        """
        The public domain names to use with the container service, such as example.com and www.example.com.
        """
        return pulumi.get(self, "public_domain_names")

    @property
    @pulumi.getter
    def scale(self) -> pulumi.Output[int]:
        """
        The scale specification for the container service.
        """
        return pulumi.get(self, "scale")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The name for the container service.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ContainerTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The publicly accessible URL of the container service.
        """
        return pulumi.get(self, "url")

