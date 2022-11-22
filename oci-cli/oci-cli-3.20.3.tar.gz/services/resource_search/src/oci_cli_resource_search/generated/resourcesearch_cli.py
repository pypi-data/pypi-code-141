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


@cli.command(cli_util.override('search.search_root_group.command_name', 'search'), cls=CommandGroupWithAlias, help=cli_util.override('search.search_root_group.help', """Search for resources in your cloud network."""), short_help=cli_util.override('search.search_root_group.short_help', """Search Service API"""))
@cli_util.help_option_group
def search_root_group():
    pass


@click.command(cli_util.override('search.resource_type_group.command_name', 'resource-type'), cls=CommandGroupWithAlias, help="""Defines a type of resource that you can find with a search or query.""")
@cli_util.help_option_group
def resource_type_group():
    pass


@click.command(cli_util.override('search.resource_summary_group.command_name', 'resource-summary'), cls=CommandGroupWithAlias, help="""A resource that exists in the cloud network that you're querying.""")
@cli_util.help_option_group
def resource_summary_group():
    pass


search_root_group.add_command(resource_type_group)
search_root_group.add_command(resource_summary_group)


@resource_type_group.command(name=cli_util.override('search.get_resource_type.command_name', 'get'), help=u"""Gets detailed information about a resource type by using the resource type name. \n[Command Reference](getResourceType)""")
@cli_util.option('--name', required=True, help=u"""The name of the resource type.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_search', 'class': 'ResourceType'})
@cli_util.wrap_exceptions
def get_resource_type(ctx, from_json, name):

    if isinstance(name, six.string_types) and len(name.strip()) == 0:
        raise click.UsageError('Parameter --name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_search', 'resource_search', ctx)
    result = client.get_resource_type(
        name=name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@resource_type_group.command(name=cli_util.override('search.list_resource_types.command_name', 'list'), help=u"""Lists all resource types that you can search or query for. \n[Command Reference](listResourceTypes)""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. The value must be between 1 and 1000.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_search', 'class': 'list[ResourceType]'})
@cli_util.wrap_exceptions
def list_resource_types(ctx, from_json, all_pages, page_size, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_search', 'resource_search', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_resource_types,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_resource_types,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_resource_types(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@resource_summary_group.command(name=cli_util.override('search.search_resources.command_name', 'search-resources'), help=u"""Queries any and all compartments in the specified tenancy to find resources that match the specified criteria. Results include resources that you have permission to view and can span different resource types. You can also sort results based on a specified resource attribute. \n[Command Reference](searchResources)""")
@cli_util.option('--type', required=True, help=u"""The type of SearchDetails, whether `FreeText` or `Structured`.""")
@cli_util.option('--matching-context-type', type=custom_types.CliCaseInsensitiveChoice(["NONE", "HIGHLIGHTS"]), help=u"""The type of matching context returned in the response. If you specify `HIGHLIGHTS`, then the service will highlight fragments in its response. (For more information, see ResourceSummary.searchContext and SearchContext.) The default setting is `NONE`.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. The value must be between 1 and 1000.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--tenant-id', help=u"""The tenancy ID, which can be used to specify a different tenancy (for cross-tenancy authorization) when searching for resources in a different tenancy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_search', 'class': 'ResourceSummaryCollection'})
@cli_util.wrap_exceptions
def search_resources(ctx, from_json, type, matching_context_type, limit, page, tenant_id):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if tenant_id is not None:
        kwargs['tenant_id'] = tenant_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    if matching_context_type is not None:
        _details['matchingContextType'] = matching_context_type

    client = cli_util.build_client('resource_search', 'resource_search', ctx)
    result = client.search_resources(
        search_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@resource_summary_group.command(name=cli_util.override('search.search_resources_structured_search_details.command_name', 'search-resources-structured-search-details'), help=u"""Queries any and all compartments in the specified tenancy to find resources that match the specified criteria. Results include resources that you have permission to view and can span different resource types. You can also sort results based on a specified resource attribute. \n[Command Reference](searchResources)""")
@cli_util.option('--query-parameterconflict', required=True, help=u"""The structured query describing which resources to search for.""")
@cli_util.option('--matching-context-type', type=custom_types.CliCaseInsensitiveChoice(["NONE", "HIGHLIGHTS"]), help=u"""The type of matching context returned in the response. If you specify `HIGHLIGHTS`, then the service will highlight fragments in its response. (For more information, see ResourceSummary.searchContext and SearchContext.) The default setting is `NONE`.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. The value must be between 1 and 1000.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--tenant-id', help=u"""The tenancy ID, which can be used to specify a different tenancy (for cross-tenancy authorization) when searching for resources in a different tenancy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_search', 'class': 'ResourceSummaryCollection'})
@cli_util.wrap_exceptions
def search_resources_structured_search_details(ctx, from_json, query_parameterconflict, matching_context_type, limit, page, tenant_id):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if tenant_id is not None:
        kwargs['tenant_id'] = tenant_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['query'] = query_parameterconflict

    if matching_context_type is not None:
        _details['matchingContextType'] = matching_context_type

    _details['type'] = 'Structured'

    client = cli_util.build_client('resource_search', 'resource_search', ctx)
    result = client.search_resources(
        search_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@resource_summary_group.command(name=cli_util.override('search.search_resources_free_text_search_details.command_name', 'search-resources-free-text-search-details'), help=u"""Queries any and all compartments in the specified tenancy to find resources that match the specified criteria. Results include resources that you have permission to view and can span different resource types. You can also sort results based on a specified resource attribute. \n[Command Reference](searchResources)""")
@cli_util.option('--text', required=True, help=u"""The text to search for.""")
@cli_util.option('--matching-context-type', type=custom_types.CliCaseInsensitiveChoice(["NONE", "HIGHLIGHTS"]), help=u"""The type of matching context returned in the response. If you specify `HIGHLIGHTS`, then the service will highlight fragments in its response. (For more information, see ResourceSummary.searchContext and SearchContext.) The default setting is `NONE`.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. The value must be between 1 and 1000.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--tenant-id', help=u"""The tenancy ID, which can be used to specify a different tenancy (for cross-tenancy authorization) when searching for resources in a different tenancy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_search', 'class': 'ResourceSummaryCollection'})
@cli_util.wrap_exceptions
def search_resources_free_text_search_details(ctx, from_json, text, matching_context_type, limit, page, tenant_id):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if tenant_id is not None:
        kwargs['tenant_id'] = tenant_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    if matching_context_type is not None:
        _details['matchingContextType'] = matching_context_type

    _details['type'] = 'FreeText'

    client = cli_util.build_client('resource_search', 'resource_search', ctx)
    result = client.search_resources(
        search_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
