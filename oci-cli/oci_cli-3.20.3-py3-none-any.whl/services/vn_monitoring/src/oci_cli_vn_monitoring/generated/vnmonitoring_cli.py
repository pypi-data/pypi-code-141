# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('vn_monitoring.vn_monitoring_root_group.command_name', 'vn-monitoring'), cls=CommandGroupWithAlias, help=cli_util.override('vn_monitoring.vn_monitoring_root_group.help', """Use the Network Monitoring API to troubleshoot routing and security issues for resources such as virtual cloud networks (VCNs) and compute instances. For more information, see the console
documentation for the [Network Path Analyzer] tool."""), short_help=cli_util.override('vn_monitoring.vn_monitoring_root_group.short_help', """Network Monitoring API"""))
@cli_util.help_option_group
def vn_monitoring_root_group():
    pass


@click.command(cli_util.override('vn_monitoring.path_analysis_work_request_result_group.command_name', 'path-analysis-work-request-result'), cls=CommandGroupWithAlias, help="""Defines the configuration of the path analysis result.""")
@cli_util.help_option_group
def path_analysis_work_request_result_group():
    pass


@click.command(cli_util.override('vn_monitoring.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('vn_monitoring.path_analyzer_test_collection_group.command_name', 'path-analyzer-test-collection'), cls=CommandGroupWithAlias, help="""The results of a `ListPathAnalyzerTests` call in the current compartment.""")
@cli_util.help_option_group
def path_analyzer_test_collection_group():
    pass


@click.command(cli_util.override('vn_monitoring.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('vn_monitoring.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('vn_monitoring.work_request_result_group.command_name', 'work-request-result'), cls=CommandGroupWithAlias, help="""Ephemeral data resulting from an asynchronous operation.""")
@cli_util.help_option_group
def work_request_result_group():
    pass


@click.command(cli_util.override('vn_monitoring.path_analyzer_test_group.command_name', 'path-analyzer-test'), cls=CommandGroupWithAlias, help="""Defines the details saved in a `PathAnalyzerTest` resource. These configuration details are used to run a [Network Path Analyzer] analysis.""")
@cli_util.help_option_group
def path_analyzer_test_group():
    pass


vn_monitoring_root_group.add_command(path_analysis_work_request_result_group)
vn_monitoring_root_group.add_command(work_request_error_group)
vn_monitoring_root_group.add_command(path_analyzer_test_collection_group)
vn_monitoring_root_group.add_command(work_request_log_entry_group)
vn_monitoring_root_group.add_command(work_request_group)
vn_monitoring_root_group.add_command(work_request_result_group)
vn_monitoring_root_group.add_command(path_analyzer_test_group)


@path_analyzer_test_group.command(name=cli_util.override('vn_monitoring.change_path_analyzer_test_compartment.command_name', 'change-compartment'), help=u"""Moves a `PathAnalyzerTest` resource from one compartment to another based on the identifier. \n[Command Reference](changePathAnalyzerTestCompartment)""")
@cli_util.option('--path-analyzer-test-id', required=True, help=u"""The [OCID] of the `PathAnalyzerTest` resource.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the `PathAnalyzerTest` resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_path_analyzer_test_compartment(ctx, from_json, path_analyzer_test_id, compartment_id, if_match):

    if isinstance(path_analyzer_test_id, six.string_types) and len(path_analyzer_test_id.strip()) == 0:
        raise click.UsageError('Parameter --path-analyzer-test-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    result = client.change_path_analyzer_test_compartment(
        path_analyzer_test_id=path_analyzer_test_id,
        change_path_analyzer_test_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@path_analyzer_test_group.command(name=cli_util.override('vn_monitoring.create_path_analyzer_test.command_name', 'create'), help=u"""Creates a new `PathAnalyzerTest` resource. \n[Command Reference](createPathAnalyzerTest)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] for the `PathAnalyzerTest` resource's compartment.""")
@cli_util.option('--protocol', required=True, type=click.INT, help=u"""The IP protocol to use in the `PathAnalyzerTest` resource.""")
@cli_util.option('--source-endpoint', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--destination-endpoint', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--protocol-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--query-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'destination-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'protocol-parameters': {'module': 'vn_monitoring', 'class': 'ProtocolParameters'}, 'query-options': {'module': 'vn_monitoring', 'class': 'QueryOptions'}, 'freeform-tags': {'module': 'vn_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'vn_monitoring', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'destination-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'protocol-parameters': {'module': 'vn_monitoring', 'class': 'ProtocolParameters'}, 'query-options': {'module': 'vn_monitoring', 'class': 'QueryOptions'}, 'freeform-tags': {'module': 'vn_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'vn_monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'vn_monitoring', 'class': 'PathAnalyzerTest'})
@cli_util.wrap_exceptions
def create_path_analyzer_test(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, protocol, source_endpoint, destination_endpoint, display_name, protocol_parameters, query_options, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['protocol'] = protocol
    _details['sourceEndpoint'] = cli_util.parse_json_parameter("source_endpoint", source_endpoint)
    _details['destinationEndpoint'] = cli_util.parse_json_parameter("destination_endpoint", destination_endpoint)

    if display_name is not None:
        _details['displayName'] = display_name

    if protocol_parameters is not None:
        _details['protocolParameters'] = cli_util.parse_json_parameter("protocol_parameters", protocol_parameters)

    if query_options is not None:
        _details['queryOptions'] = cli_util.parse_json_parameter("query_options", query_options)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    result = client.create_path_analyzer_test(
        create_path_analyzer_test_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_path_analyzer_test') and callable(getattr(client, 'get_path_analyzer_test')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_path_analyzer_test(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@path_analyzer_test_group.command(name=cli_util.override('vn_monitoring.delete_path_analyzer_test.command_name', 'delete'), help=u"""Deletes a `PathAnalyzerTest` resource using its identifier. \n[Command Reference](deletePathAnalyzerTest)""")
@cli_util.option('--path-analyzer-test-id', required=True, help=u"""The [OCID] of the `PathAnalyzerTest` resource.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_path_analyzer_test(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, path_analyzer_test_id, if_match):

    if isinstance(path_analyzer_test_id, six.string_types) and len(path_analyzer_test_id.strip()) == 0:
        raise click.UsageError('Parameter --path-analyzer-test-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    result = client.delete_path_analyzer_test(
        path_analyzer_test_id=path_analyzer_test_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_path_analyzer_test') and callable(getattr(client, 'get_path_analyzer_test')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_path_analyzer_test(path_analyzer_test_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@path_analysis_work_request_result_group.command(name=cli_util.override('vn_monitoring.get_path_analysis.command_name', 'get-path-analysis'), help=u"""Use this method to initiate a [Network Path Analyzer] analysis. This method returns an opc-work-request-id, and you can poll the status of the work request until it either fails or succeeds.

If the work request status is successful, use [ListWorkRequestResults] with the work request ID to ask for the successful analysis results. If the work request status is failed, use [ListWorkRequestErrors] with the work request ID to ask for the analysis failure information. The information returned from either of these methods can be used to build a final report. \n[Command Reference](getPathAnalysis)""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["PERSISTED_QUERY", "ADHOC_QUERY"]), help=u"""The type of the `PathAnalysis` query.""")
@cli_util.option('--cache-control', help=u"""The Cache-Control HTTP header holds directives (instructions) for caching in both requests and responses.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_path_analysis(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, type, cache_control):

    kwargs = {}
    if cache_control is not None:
        kwargs['cache_control'] = cache_control
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    result = client.get_path_analysis(
        get_path_analysis_details=_details,
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


@path_analysis_work_request_result_group.command(name=cli_util.override('vn_monitoring.get_path_analysis_adhoc_get_path_analysis_details.command_name', 'get-path-analysis-adhoc-get-path-analysis-details'), help=u"""Use this method to initiate a [Network Path Analyzer] analysis. This method returns an opc-work-request-id, and you can poll the status of the work request until it either fails or succeeds.

If the work request status is successful, use [ListWorkRequestResults] with the work request ID to ask for the successful analysis results. If the work request status is failed, use [ListWorkRequestErrors] with the work request ID to ask for the analysis failure information. The information returned from either of these methods can be used to build a final report. \n[Command Reference](getPathAnalysis)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] for the compartment.""")
@cli_util.option('--protocol', required=True, type=click.INT, help=u"""The IP protocol to used for the path analysis.""")
@cli_util.option('--source-endpoint', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--destination-endpoint', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protocol-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--query-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cache-control', help=u"""The Cache-Control HTTP header holds directives (instructions) for caching in both requests and responses.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'destination-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'protocol-parameters': {'module': 'vn_monitoring', 'class': 'ProtocolParameters'}, 'query-options': {'module': 'vn_monitoring', 'class': 'QueryOptions'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'destination-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'protocol-parameters': {'module': 'vn_monitoring', 'class': 'ProtocolParameters'}, 'query-options': {'module': 'vn_monitoring', 'class': 'QueryOptions'}})
@cli_util.wrap_exceptions
def get_path_analysis_adhoc_get_path_analysis_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, protocol, source_endpoint, destination_endpoint, protocol_parameters, query_options, cache_control):

    kwargs = {}
    if cache_control is not None:
        kwargs['cache_control'] = cache_control
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['protocol'] = protocol
    _details['sourceEndpoint'] = cli_util.parse_json_parameter("source_endpoint", source_endpoint)
    _details['destinationEndpoint'] = cli_util.parse_json_parameter("destination_endpoint", destination_endpoint)

    if protocol_parameters is not None:
        _details['protocolParameters'] = cli_util.parse_json_parameter("protocol_parameters", protocol_parameters)

    if query_options is not None:
        _details['queryOptions'] = cli_util.parse_json_parameter("query_options", query_options)

    _details['type'] = 'ADHOC_QUERY'

    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    result = client.get_path_analysis(
        get_path_analysis_details=_details,
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


@path_analysis_work_request_result_group.command(name=cli_util.override('vn_monitoring.get_path_analysis_persisted_get_path_analysis_details.command_name', 'get-path-analysis-persisted-get-path-analysis-details'), help=u"""Use this method to initiate a [Network Path Analyzer] analysis. This method returns an opc-work-request-id, and you can poll the status of the work request until it either fails or succeeds.

If the work request status is successful, use [ListWorkRequestResults] with the work request ID to ask for the successful analysis results. If the work request status is failed, use [ListWorkRequestErrors] with the work request ID to ask for the analysis failure information. The information returned from either of these methods can be used to build a final report. \n[Command Reference](getPathAnalysis)""")
@cli_util.option('--path-analyzer-test-id', required=True, help=u"""The [OCID] of the `PathAnalyzerTest` resource.""")
@cli_util.option('--cache-control', help=u"""The Cache-Control HTTP header holds directives (instructions) for caching in both requests and responses.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_path_analysis_persisted_get_path_analysis_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, path_analyzer_test_id, cache_control):

    kwargs = {}
    if cache_control is not None:
        kwargs['cache_control'] = cache_control
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['pathAnalyzerTestId'] = path_analyzer_test_id

    _details['type'] = 'PERSISTED_QUERY'

    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    result = client.get_path_analysis(
        get_path_analysis_details=_details,
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


@path_analyzer_test_group.command(name=cli_util.override('vn_monitoring.get_path_analyzer_test.command_name', 'get'), help=u"""Gets a `PathAnalyzerTest` using its identifier. \n[Command Reference](getPathAnalyzerTest)""")
@cli_util.option('--path-analyzer-test-id', required=True, help=u"""The [OCID] of the `PathAnalyzerTest` resource.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vn_monitoring', 'class': 'PathAnalyzerTest'})
@cli_util.wrap_exceptions
def get_path_analyzer_test(ctx, from_json, path_analyzer_test_id):

    if isinstance(path_analyzer_test_id, six.string_types) and len(path_analyzer_test_id.strip()) == 0:
        raise click.UsageError('Parameter --path-analyzer-test-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    result = client.get_path_analyzer_test(
        path_analyzer_test_id=path_analyzer_test_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('vn_monitoring.get_work_request.command_name', 'get'), help=u"""Gets the details of a work request. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vn_monitoring', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@path_analyzer_test_collection_group.command(name=cli_util.override('vn_monitoring.list_path_analyzer_tests.command_name', 'list-path-analyzer-tests'), help=u"""Returns a list of all `PathAnalyzerTests` in a compartment. \n[Command Reference](listPathAnalyzerTests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""A filter that returns only resources whose `lifecycleState` matches the given `lifecycleState`.""")
@cli_util.option('--display-name', help=u"""A filter that returns only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vn_monitoring', 'class': 'PathAnalyzerTestCollection'})
@cli_util.wrap_exceptions
def list_path_analyzer_tests(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_path_analyzer_tests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_path_analyzer_tests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_path_analyzer_tests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('vn_monitoring.list_work_request_errors.command_name', 'list'), help=u"""Returns a (paginated) list of errors for the work request with the given ID. This information is used to build the final report output. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for `timeCreated` is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vn_monitoring', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('vn_monitoring.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Returns a (paginated) list of logs for the work request with the given ID. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for `timeCreated` is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vn_monitoring', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_result_group.command(name=cli_util.override('vn_monitoring.list_work_request_results.command_name', 'list'), help=u"""Returns a (paginated) list of results for a successful work request. This information is used to build the final report output. \n[Command Reference](listWorkRequestResults)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--result-type', type=custom_types.CliCaseInsensitiveChoice(["PATH_ANALYSIS"]), help=u"""The type of results to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vn_monitoring', 'class': 'WorkRequestResultCollection'})
@cli_util.wrap_exceptions
def list_work_request_results(ctx, from_json, all_pages, page_size, work_request_id, limit, page, result_type):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if result_type is not None:
        kwargs['result_type'] = result_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_results,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_results,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_results(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('vn_monitoring.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for `timeAccepted` is descending.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources whose `lifecycleState` matches the given `OperationStatus`.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource affected by the work request.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vn_monitoring', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, limit, page, sort_order, sort_by, status, resource_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if status is not None:
        kwargs['status'] = status
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@path_analyzer_test_group.command(name=cli_util.override('vn_monitoring.update_path_analyzer_test.command_name', 'update'), help=u"""Updates a `PathAnalyzerTest` using its identifier. \n[Command Reference](updatePathAnalyzerTest)""")
@cli_util.option('--path-analyzer-test-id', required=True, help=u"""The [OCID] of the `PathAnalyzerTest` resource.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--protocol', type=click.INT, help=u"""The IP protocol to use in the `PathAnalyzerTest` resource.""")
@cli_util.option('--source-endpoint', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--destination-endpoint', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protocol-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--query-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'destination-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'protocol-parameters': {'module': 'vn_monitoring', 'class': 'ProtocolParameters'}, 'query-options': {'module': 'vn_monitoring', 'class': 'QueryOptions'}, 'freeform-tags': {'module': 'vn_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'vn_monitoring', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'destination-endpoint': {'module': 'vn_monitoring', 'class': 'Endpoint'}, 'protocol-parameters': {'module': 'vn_monitoring', 'class': 'ProtocolParameters'}, 'query-options': {'module': 'vn_monitoring', 'class': 'QueryOptions'}, 'freeform-tags': {'module': 'vn_monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'vn_monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'vn_monitoring', 'class': 'PathAnalyzerTest'})
@cli_util.wrap_exceptions
def update_path_analyzer_test(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, path_analyzer_test_id, display_name, protocol, source_endpoint, destination_endpoint, protocol_parameters, query_options, freeform_tags, defined_tags, if_match):

    if isinstance(path_analyzer_test_id, six.string_types) and len(path_analyzer_test_id.strip()) == 0:
        raise click.UsageError('Parameter --path-analyzer-test-id cannot be whitespace or empty string')
    if not force:
        if source_endpoint or destination_endpoint or protocol_parameters or query_options or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source-endpoint and destination-endpoint and protocol-parameters and query-options and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if protocol is not None:
        _details['protocol'] = protocol

    if source_endpoint is not None:
        _details['sourceEndpoint'] = cli_util.parse_json_parameter("source_endpoint", source_endpoint)

    if destination_endpoint is not None:
        _details['destinationEndpoint'] = cli_util.parse_json_parameter("destination_endpoint", destination_endpoint)

    if protocol_parameters is not None:
        _details['protocolParameters'] = cli_util.parse_json_parameter("protocol_parameters", protocol_parameters)

    if query_options is not None:
        _details['queryOptions'] = cli_util.parse_json_parameter("query_options", query_options)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('vn_monitoring', 'vn_monitoring', ctx)
    result = client.update_path_analyzer_test(
        path_analyzer_test_id=path_analyzer_test_id,
        update_path_analyzer_test_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_path_analyzer_test') and callable(getattr(client, 'get_path_analyzer_test')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_path_analyzer_test(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
