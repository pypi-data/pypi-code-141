# -*- coding: utf-8 -*-
"""Command line interface for Axonius API Client."""
from ...context import CONTEXT_SETTINGS, click
from ...options import ABORT, AUTH, add_options
from .grp_common import EXPORT_FORMATS, OPTS_EXPORT

METHOD = "delete-by-tags"
OPTIONS = [
    *AUTH,
    *OPTS_EXPORT,
    ABORT,
    click.option(
        "--tag",
        "-t",
        "value",
        help="Tags of saved queries to delete (multiple)",
        required=True,
        multiple=True,
        show_envvar=True,
        show_default=True,
    ),
]


@click.command(name="delete-by-tags", context_settings=CONTEXT_SETTINGS)
@add_options(OPTIONS)
@click.pass_context
def cmd(ctx, url, key, secret, export_format, table_format, value, abort):
    """Delete saved queries by tags."""
    client = ctx.obj.start_client(url=url, key=key, secret=secret)

    p_grp = ctx.parent.parent.command.name
    apiobj = getattr(client, p_grp)

    with ctx.obj.exc_wrap(wraperror=ctx.obj.wraperror):
        rows = apiobj.saved_query.get_by_tags(value=value, as_dataclass=True)
        data = apiobj.saved_query.delete(
            rows=rows, refetch=False, do_echo=True, errors=abort, as_dataclass=True
        )

    click.secho(EXPORT_FORMATS[export_format](data=data, table_format=table_format))
    ctx.exit(0)
