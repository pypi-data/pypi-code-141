# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.marketplace.src.oci_cli_marketplace.generated import marketplace_service_cli


@click.command(cli_util.override('account.account_root_group.command_name', 'account'), cls=CommandGroupWithAlias, help=cli_util.override('account.account_root_group.help', """Use the Marketplace API to manage applications in Oracle Cloud Infrastructure Marketplace. For more information, see [Overview of Marketplace]"""), short_help=cli_util.override('account.account_root_group.short_help', """Marketplace Service API"""))
@cli_util.help_option_group
def account_root_group():
    pass


@click.command(cli_util.override('account.third_party_paid_listing_eligibility_group.command_name', 'third-party-paid-listing-eligibility'), cls=CommandGroupWithAlias, help="""Tenant eligibility for using third party paid listings""")
@cli_util.help_option_group
def third_party_paid_listing_eligibility_group():
    pass


@click.command(cli_util.override('account.launch_eligibility_group.command_name', 'launch-eligibility'), cls=CommandGroupWithAlias, help="""Tenant eligibility and other information for launching a PIC image""")
@cli_util.help_option_group
def launch_eligibility_group():
    pass


marketplace_service_cli.marketplace_service_group.add_command(account_root_group)
account_root_group.add_command(third_party_paid_listing_eligibility_group)
account_root_group.add_command(launch_eligibility_group)


@launch_eligibility_group.command(name=cli_util.override('account.get_launch_eligibility.command_name', 'get'), help=u"""Returns Tenant eligibility and other information for launching a PIC image \n[Command Reference](getLaunchEligibility)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment.""")
@cli_util.option('--image-id', required=True, help=u"""Image ID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'LaunchEligibility'})
@cli_util.wrap_exceptions
def get_launch_eligibility(ctx, from_json, compartment_id, image_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'account', ctx)
    result = client.get_launch_eligibility(
        compartment_id=compartment_id,
        image_id=image_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@third_party_paid_listing_eligibility_group.command(name=cli_util.override('account.get_third_party_paid_listing_eligibility.command_name', 'get'), help=u"""Returns eligibility details of the tenancy to see and launch third party paid listings \n[Command Reference](getThirdPartyPaidListingEligibility)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'ThirdPartyPaidListingEligibility'})
@cli_util.wrap_exceptions
def get_third_party_paid_listing_eligibility(ctx, from_json, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'account', ctx)
    result = client.get_third_party_paid_listing_eligibility(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)
