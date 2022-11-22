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
from services.apigateway.src.oci_cli_apigateway.generated import api_gateway_service_cli


@click.command(cli_util.override('subscribers.subscribers_root_group.command_name', 'subscribers'), cls=CommandGroupWithAlias, help=cli_util.override('subscribers.subscribers_root_group.help', """API for the API Gateway service. Use this API to manage gateways, deployments, and related items.
For more information, see
[Overview of API Gateway]."""), short_help=cli_util.override('subscribers.subscribers_root_group.short_help', """API Gateway API"""))
@cli_util.help_option_group
def subscribers_root_group():
    pass


@click.command(cli_util.override('subscribers.subscriber_group.command_name', 'subscriber'), cls=CommandGroupWithAlias, help="""A subscriber, which encapsulates a number of clients and usage plans that they are subscribed to.""")
@cli_util.help_option_group
def subscriber_group():
    pass


api_gateway_service_cli.api_gateway_service_group.add_command(subscribers_root_group)
subscribers_root_group.add_command(subscriber_group)


@subscriber_group.command(name=cli_util.override('subscribers.change_subscriber_compartment.command_name', 'change-compartment'), help=u"""Changes the subscriber compartment. \n[Command Reference](changeSubscriberCompartment)""")
@cli_util.option('--subscriber-id', required=True, help=u"""The ocid of the subscriber.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the resource is created.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_subscriber_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, subscriber_id, compartment_id, if_match):

    if isinstance(subscriber_id, six.string_types) and len(subscriber_id.strip()) == 0:
        raise click.UsageError('Parameter --subscriber-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('apigateway', 'subscribers', ctx)
    result = client.change_subscriber_compartment(
        subscriber_id=subscriber_id,
        change_subscriber_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('apigateway', 'work_requests', ctx)

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


@subscriber_group.command(name=cli_util.override('subscribers.create_subscriber.command_name', 'create'), help=u"""Creates a new subscriber. \n[Command Reference](createSubscriber)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the resource is created.""")
@cli_util.option('--clients', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The clients belonging to this subscriber.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--usage-plans', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of [OCID]s of usage plan resources.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My new resource`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'clients': {'module': 'apigateway', 'class': 'list[Client]'}, 'usage-plans': {'module': 'apigateway', 'class': 'list[string]'}, 'freeform-tags': {'module': 'apigateway', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apigateway', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'clients': {'module': 'apigateway', 'class': 'list[Client]'}, 'usage-plans': {'module': 'apigateway', 'class': 'list[string]'}, 'freeform-tags': {'module': 'apigateway', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apigateway', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apigateway', 'class': 'Subscriber'})
@cli_util.wrap_exceptions
def create_subscriber(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, clients, usage_plans, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['clients'] = cli_util.parse_json_parameter("clients", clients)
    _details['usagePlans'] = cli_util.parse_json_parameter("usage_plans", usage_plans)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apigateway', 'subscribers', ctx)
    result = client.create_subscriber(
        create_subscriber_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('apigateway', 'work_requests', ctx)

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


@subscriber_group.command(name=cli_util.override('subscribers.delete_subscriber.command_name', 'delete'), help=u"""Deletes the subscriber with the given identifier. \n[Command Reference](deleteSubscriber)""")
@cli_util.option('--subscriber-id', required=True, help=u"""The ocid of the subscriber.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_subscriber(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, subscriber_id, if_match):

    if isinstance(subscriber_id, six.string_types) and len(subscriber_id.strip()) == 0:
        raise click.UsageError('Parameter --subscriber-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apigateway', 'subscribers', ctx)
    result = client.delete_subscriber(
        subscriber_id=subscriber_id,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('apigateway', 'work_requests', ctx)

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
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@subscriber_group.command(name=cli_util.override('subscribers.get_subscriber.command_name', 'get'), help=u"""Gets a subscriber by identifier. \n[Command Reference](getSubscriber)""")
@cli_util.option('--subscriber-id', required=True, help=u"""The ocid of the subscriber.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apigateway', 'class': 'Subscriber'})
@cli_util.wrap_exceptions
def get_subscriber(ctx, from_json, subscriber_id):

    if isinstance(subscriber_id, six.string_types) and len(subscriber_id.strip()) == 0:
        raise click.UsageError('Parameter --subscriber-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apigateway', 'subscribers', ctx)
    result = client.get_subscriber(
        subscriber_id=subscriber_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@subscriber_group.command(name=cli_util.override('subscribers.list_subscribers.command_name', 'list'), help=u"""Returns a list of subscribers. \n[Command Reference](listSubscribers)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ocid of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state. Example: `ACTIVE`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'. The default order depends on the sortBy value.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for `timeCreated` is descending. Default order for `displayName` is ascending. The `displayName` sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apigateway', 'class': 'SubscriberCollection'})
@cli_util.wrap_exceptions
def list_subscribers(ctx, from_json, all_pages, page_size, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apigateway', 'subscribers', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_subscribers,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_subscribers,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_subscribers(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@subscriber_group.command(name=cli_util.override('subscribers.update_subscriber.command_name', 'update'), help=u"""Updates the subscriber with the given identifier. \n[Command Reference](updateSubscriber)""")
@cli_util.option('--subscriber-id', required=True, help=u"""The ocid of the subscriber.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My new resource`""")
@cli_util.option('--clients', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The clients belonging to the subscriber.

This option is a JSON list with items of type Client.  For documentation on Client please see our API reference: https://docs.cloud.oracle.com/api/#/en/subscribers/20190501/datatypes/Client.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--usage-plans', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of [OCID]s of usage plan resources.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'clients': {'module': 'apigateway', 'class': 'list[Client]'}, 'usage-plans': {'module': 'apigateway', 'class': 'list[string]'}, 'freeform-tags': {'module': 'apigateway', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apigateway', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'clients': {'module': 'apigateway', 'class': 'list[Client]'}, 'usage-plans': {'module': 'apigateway', 'class': 'list[string]'}, 'freeform-tags': {'module': 'apigateway', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apigateway', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_subscriber(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, subscriber_id, display_name, clients, usage_plans, freeform_tags, defined_tags, if_match):

    if isinstance(subscriber_id, six.string_types) and len(subscriber_id.strip()) == 0:
        raise click.UsageError('Parameter --subscriber-id cannot be whitespace or empty string')
    if not force:
        if clients or usage_plans or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to clients and usage-plans and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if clients is not None:
        _details['clients'] = cli_util.parse_json_parameter("clients", clients)

    if usage_plans is not None:
        _details['usagePlans'] = cli_util.parse_json_parameter("usage_plans", usage_plans)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apigateway', 'subscribers', ctx)
    result = client.update_subscriber(
        subscriber_id=subscriber_id,
        update_subscriber_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('apigateway', 'work_requests', ctx)

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
