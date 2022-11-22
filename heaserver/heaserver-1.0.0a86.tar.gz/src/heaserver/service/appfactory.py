from aiohttp import web
from multidict import istr
from typing import List
from heaserver.service import appproperty, requestproperty
from aiohttp_remotes import XForwardedRelaxed
from aiohttp_remotes.exceptions import TooManyHeaders


@web.middleware
async def new_wstl_builder(request: web.Request, handler) -> web.Response:
    wstl_builder_factory = request.app[appproperty.HEA_WSTL_BUILDER_FACTORY]
    request[requestproperty.HEA_WSTL_BUILDER] = wstl_builder_factory()
    response = await handler(request)
    return response


@web.middleware
async def x_forwarded_prefix(request: web.Request, handler) -> web.Response:
    X_FORWARDED_PREFIX = istr('X-Forwarded-Prefix')
    forwarded_prefix: List[str] = request.headers.getall(X_FORWARDED_PREFIX, [])
    if len(forwarded_prefix) > 1:
        raise TooManyHeaders(X_FORWARDED_PREFIX)
    if prefix := (forwarded_prefix[0] if forwarded_prefix else None):
        request = request.clone(rel_url=_prepend_path(prefix, request.path))
    return await handler(request)


def _prepend_path(prefix: str, path: str) -> str:
    return prefix.rstrip('/') + '/' + path.lstrip('/')


def new_app() -> web.Application:
    """
    Creates and returns an aiohttp Application object. Installs middleware that sets the HEA_WSTL_BUILDER request
    property, assuming that the HEA_WSTL_BUILDER_FACTORY app property has already been set.

    :return: the Application property.
    """
    return web.Application(middlewares=[new_wstl_builder, x_forwarded_prefix, XForwardedRelaxed().middleware])

