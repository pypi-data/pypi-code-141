import logging

from functools import wraps
from typing import Optional, Callable, Type, Generator
import requests
from contextlib import contextmanager
import asyncio
import time
import os


def async_retry(*exceptions: Type[Exception], retries: int = 3, cooldown: Optional[int] = 1,
                verbose: bool = True) -> Callable:
    """
    Decorate an async function to execute it a few times before giving up and raising a ``RetryExhaustedError``.

    :param exceptions: One or more exceptions expected during function execution, as positional arguments.
    :param retries: Number of retries of function execution.
    :param cooldown: Seconds to wait before retry. If None, does not cool down.
    :param verbose: Specifies if we should log about not successful attempts.
    """

    def wrap(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            _logger = logging.getLogger(__name__)
            retries_count = 0

            while True:
                try:
                    result = await func(*args, **kwargs)
                except exceptions as err:
                    retries_count += 1
                    message = "Exception {} during {} execution. " \
                              "{} of {} retries attempted".format(type(err), func, retries_count, retries)

                    if retries_count > retries:
                        verbose and _logger.exception(message)
                        raise RetryExhaustedError(func.__qualname__) from err
                    else:
                        verbose and _logger.warning(message)

                    if cooldown:
                        await asyncio.sleep(cooldown)
                else:
                    return result
        return inner
    return wrap


def retry(*exceptions: Type[Exception], retries: int = 3, cooldown: Optional[int] = 1,
          verbose: bool = True) -> Callable:
    """
    Decorate a non-async function to execute it a few times before giving up and raising a ``RetryExhaustedError``.

    :param exceptions: One or more exceptions expected during function execution, as positional arguments.
    :param retries: Number of retries of function execution.
    :param cooldown: Seconds to wait before retry. If None, does not cool down.
    :param verbose: Specifies if we should log about not successful attempts.
    """

    def wrap(func):
        @wraps(func)
        def inner(*args, **kwargs):
            _logger = logging.getLogger(__name__)
            retries_count = 0

            while True:
                try:
                    result = func(*args, **kwargs)
                except exceptions as err:
                    retries_count += 1
                    message = "Exception {} during {} execution. " \
                              "{} of {} retries attempted".format(type(err), func, retries_count, retries)

                    if retries_count > retries:
                        verbose and _logger.exception(message)
                        raise RetryExhaustedError(f'Exhausted retries of {func}') from err
                    else:
                        verbose and _logger.warning(message)

                    if cooldown:
                        time.sleep(cooldown)
                else:
                    return result
        return inner
    return wrap


class RetryExhaustedError(Exception):
    """
    Indicates that the retries have been exhausted and the decorated function has failed.
    """
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


@contextmanager
def modified_environ(*remove, **update):
    """
    Temporarily updates the ``os.environ`` dictionary in-place.

    The ``os.environ`` dictionary is updated in-place so that the modification
    is sure to work in all situations. Code obtained from
    https://stackoverflow.com/questions/2059482/python-temporarily-modify-the-current-processs-environment.

    :param remove: Environment variables to remove.
    :param update: Dictionary of environment variables and values to add/update.
    """
    env = os.environ
    update = update or {}
    remove = remove or []

    # List of environment variables being updated or removed.
    stomped = (set(update.keys()) | set(remove)) & set(env.keys())
    # Environment variables and values to restore on exit.
    update_after = {k: env[k] for k in stomped}
    # Environment variables and values to remove on exit.
    remove_after = frozenset(k for k in update if k not in env)

    try:
        env.update(update)
        [env.pop(k, None) for k in remove]
        yield
    finally:
        env.update(update_after)
        [env.pop(k) for k in remove_after]


@contextmanager
def request_get_with_retry(url: str, retries=10, cooldown: int | None = 5, timeout: float | None = 60) -> Generator[requests.Response, None, None]:
    """
    Context manager that opens a URL, retrying if unsuccessful, and generates a HTTPResponse.

    :param url: the URL to open (required).
    :param retries: the number of retries.
    :param cooldown: the cooldown period (None for no cooldown).
    :param timeout: the connection timeout (None for no timeout).
    :raises TimeoutError: if the final retry timed out.
    :raises URLError: if the final retry errored out.
    """
    logger = logging.getLogger(__name__)
    logger.debug('Connecting to URL %s', url)

    if not retries:
        retries = 0

    @retry(requests.exceptions.RequestException, retries=retries, cooldown=cooldown)
    def do_open() -> requests.Response:
        try:
            with requests.get(url, timeout=timeout) as response:
                return response
        except Exception as e:
            logger.exception(f'Error getting URL {url}')
            raise e
    response = do_open()
    try:
        yield response
    finally:
        response.close()
