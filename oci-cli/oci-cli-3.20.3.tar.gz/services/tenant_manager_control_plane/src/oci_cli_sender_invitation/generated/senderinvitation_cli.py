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
from services.tenant_manager_control_plane.src.oci_cli_tenant_manager_control_plane.generated import organizations_service_cli


@click.command(cli_util.override('sender_invitation.sender_invitation_root_group.command_name', 'sender-invitation'), cls=CommandGroupWithAlias, help=cli_util.override('sender_invitation.sender_invitation_root_group.help', """The Organizations API allows you to consolidate multiple OCI tenancies into an organization, and centrally manage your tenancies and its resources."""), short_help=cli_util.override('sender_invitation.sender_invitation_root_group.short_help', """Organizations API"""))
@cli_util.help_option_group
def sender_invitation_root_group():
    pass


@click.command(cli_util.override('sender_invitation.sender_invitation_group.command_name', 'sender-invitation'), cls=CommandGroupWithAlias, help="""The invitation model that the sender owns.""")
@cli_util.help_option_group
def sender_invitation_group():
    pass


organizations_service_cli.organizations_service_group.add_command(sender_invitation_root_group)
sender_invitation_root_group.add_command(sender_invitation_group)


@sender_invitation_group.command(name=cli_util.override('sender_invitation.cancel_sender_invitation.command_name', 'cancel'), help=u"""Cancels a sender invitation. \n[Command Reference](cancelSenderInvitation)""")
@cli_util.option('--sender-invitation-id', required=True, help=u"""OCID of the sender invitation to cancel.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_sender_invitation(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, sender_invitation_id, if_match):

    if isinstance(sender_invitation_id, six.string_types) and len(sender_invitation_id.strip()) == 0:
        raise click.UsageError('Parameter --sender-invitation-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'sender_invitation', ctx)
    result = client.cancel_sender_invitation(
        sender_invitation_id=sender_invitation_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@sender_invitation_group.command(name=cli_util.override('sender_invitation.create_sender_invitation.command_name', 'create'), help=u"""Creates a sender invitation and asynchronously sends the invitation to the recipient. \n[Command Reference](createSenderInvitation)""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the sender tenancy.""")
@cli_util.option('--recipient-tenancy-id', required=True, help=u"""OCID of the recipient tenancy.""")
@cli_util.option('--recipient-email-address', help=u"""Email address of the recipient.""")
@cli_util.option('--display-name', help=u"""A user-created name to describe the invitation. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'tenant_manager_control_plane', 'class': 'SenderInvitation'})
@cli_util.wrap_exceptions
def create_sender_invitation(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, recipient_tenancy_id, recipient_email_address, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['recipientTenancyId'] = recipient_tenancy_id

    if recipient_email_address is not None:
        _details['recipientEmailAddress'] = recipient_email_address

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('tenant_manager_control_plane', 'sender_invitation', ctx)
    result = client.create_sender_invitation(
        create_sender_invitation_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@sender_invitation_group.command(name=cli_util.override('sender_invitation.get_sender_invitation.command_name', 'get'), help=u"""Gets information about the sender invitation. \n[Command Reference](getSenderInvitation)""")
@cli_util.option('--sender-invitation-id', required=True, help=u"""OCID of the sender invitation to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'SenderInvitation'})
@cli_util.wrap_exceptions
def get_sender_invitation(ctx, from_json, sender_invitation_id):

    if isinstance(sender_invitation_id, six.string_types) and len(sender_invitation_id.strip()) == 0:
        raise click.UsageError('Parameter --sender-invitation-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'sender_invitation', ctx)
    result = client.get_sender_invitation(
        sender_invitation_id=sender_invitation_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@sender_invitation_group.command(name=cli_util.override('sender_invitation.list_sender_invitations.command_name', 'list'), help=u"""Return a (paginated) list of sender invitations. \n[Command Reference](listSenderInvitations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--recipient-tenancy-id', help=u"""The tenancy that the invitation is addressed to.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]), help=u"""The lifecycle state of the resource.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["PENDING", "CANCELED", "ACCEPTED", "EXPIRED", "FAILED"]), help=u"""The status of the sender invitation.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'SenderInvitationCollection'})
@cli_util.wrap_exceptions
def list_sender_invitations(ctx, from_json, all_pages, page_size, compartment_id, recipient_tenancy_id, lifecycle_state, status, display_name, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if recipient_tenancy_id is not None:
        kwargs['recipient_tenancy_id'] = recipient_tenancy_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if status is not None:
        kwargs['status'] = status
    if display_name is not None:
        kwargs['display_name'] = display_name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'sender_invitation', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_sender_invitations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_sender_invitations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_sender_invitations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@sender_invitation_group.command(name=cli_util.override('sender_invitation.update_sender_invitation.command_name', 'update'), help=u"""Updates the SenderInvitation. \n[Command Reference](updateSenderInvitation)""")
@cli_util.option('--sender-invitation-id', required=True, help=u"""OCID of the sender invitation to update.""")
@cli_util.option('--display-name', help=u"""A user-created name to describe the invitation. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'tenant_manager_control_plane', 'class': 'SenderInvitation'})
@cli_util.wrap_exceptions
def update_sender_invitation(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, sender_invitation_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(sender_invitation_id, six.string_types) and len(sender_invitation_id.strip()) == 0:
        raise click.UsageError('Parameter --sender-invitation-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('tenant_manager_control_plane', 'sender_invitation', ctx)
    result = client.update_sender_invitation(
        sender_invitation_id=sender_invitation_id,
        update_sender_invitation_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_sender_invitation') and callable(getattr(client, 'get_sender_invitation')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_sender_invitation(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
