from unittest import TestCase, IsolatedAsyncioTestCase
import asyncio as aio
import logging
import os
import time

from heaserver.service.util import modified_environ, retry, async_retry, RetryExhaustedError


class ModifiedEnvironmentTestCase(TestCase):
    def test_update_environment_variable(self) -> None:
        """Checks if modifying an environment variable actually modifies it in the context."""
        var_name = next(iter(os.environ.keys()), None)
        if var_name is None:
            self.skipTest('no environment variables available')
        value = os.environ[var_name]
        with modified_environ(**{var_name: 'foobar' + value}):
            self.assertEqual('foobar' + value, os.environ[var_name])

    def test_update_environment_variable_restored_after(self) -> None:
        """
        Checks if modifying an environment variable with the context manager does not modify it outside of the
        context.
        """
        var_name = next(iter(os.environ.keys()), None)
        if var_name is None:
            self.skipTest('no environment variables available')
        value = os.environ[var_name]
        with modified_environ(**{var_name: 'foobar' + value}):
            logging.info(f'{var_name}={os.environ[var_name]}')
        self.assertEqual(value, os.environ[var_name])

    def test_add_environment_variable(self) -> None:
        """Checks if adding the FOO environment variable (and setting it to 'bar') actually adds it in the context."""
        with modified_environ(FOO='bar'):
            self.assertEqual('bar', os.environ.get('FOO'))

    def test_add_environment_variable_removed_after(self) -> None:
        """
        Checks if adding the FOO environment variable (and setting it to 'bar') with the context manager does not
        add it outside of the context.
        """
        with modified_environ(FOO='bar'):
            logging.info(f'FOO={os.environ["FOO"]}')
        self.assertIsNone(os.environ.get('FOO'))

    def test_remove_environment_variable(self) -> None:
        """
        Checks if removing an environment variable actually removes it in the
        context.
        """
        var_name = next(iter(os.environ.keys()), None)
        if var_name is None:
            self.skipTest('no environment variables available')
        with modified_environ(var_name):
            self.assertIsNone(os.environ.get(var_name))

    def test_remove_environment_variable_restored_after(self) -> None:
        """
        Checks if removing the FPS_BROWSER_APP_PROFILE_STRING environment variable with the context manager does not
        remove it outside of the context.
        """
        var_name = next(iter(os.environ.keys()), None)
        if var_name is None:
            self.skipTest('no environment variables available')
        value = os.environ[var_name]
        with modified_environ(var_name):
            logging.info(f'{var_name}={os.environ.get(var_name)}')
        self.assertEqual(value, os.environ.get(var_name))


class ModifiedEnvironmentAsyncTestCase(IsolatedAsyncioTestCase):
    async def test_update_environment_variable_async_access_not_within_context(self) -> None:
        """
        Checks if accessing an environment variable updated with the context manager outside of the context while the
        context is running returns the old value.
        """

        var_name = next(iter(os.environ.keys()), None)
        if var_name is None:
            self.skipTest('no environment variables available')
        value = os.environ[var_name]

        async def change_env():
            nonlocal var_name
            with modified_environ(**{var_name: 'foobar' + value}):
                await aio.sleep(1)
                logging.info(f'{var_name}={os.environ[var_name]}')

        task = aio.create_task(change_env())

        new_value = os.environ[var_name]

        await task
        self.assertEqual(value, new_value)


class NonAsyncRetryTestCase(TestCase):
    def test_retry_success(self) -> None:
        """Checks if a success on a retry of a function with the retry decorator returns the expected value."""

        tried = False

        @retry(Exception, cooldown=None)
        def foo() -> str:
            nonlocal tried
            if tried:
                return 'foo'
            else:
                tried = True
                raise Exception

        try:
            self.assertEqual('foo', foo())
        except RetryExhaustedError as e:
            raise AssertionError(f'exception raised: {e}') from e

    def test_retry_cooldown(self) -> None:
        """Checks if there is a cooldown when a cooldown is specified in the retry decorator."""
        @retry(Exception, cooldown=1, retries=1)
        def foo() -> None:
            raise Exception

        start = time.perf_counter()

        try:
            foo()
        except RetryExhaustedError:
            pass

        self.assertGreaterEqual(time.perf_counter() - start, 0.9, 'cooldown not long enough')

    def test_retry_retries(self) -> None:
        """Checks if the number of retries that are attempted of a function with the retry decorator is correct."""

        count = 0

        @retry(Exception, retries=5, cooldown=None)
        def foo() -> None:
            nonlocal count
            count += 1
            raise Exception

        try:
            foo()
        except RetryExhaustedError:
            pass

        self.assertEqual(6, count)

    def test_retry_exhausted(self) -> None:
        """Checks if exhausting all the retries of a function raises ``RetryExhaustedError``."""
        @retry(Exception, cooldown=None)
        def foo() -> None:
            raise Exception

        self.assertRaises(RetryExhaustedError, foo)

    def test_retry_different_error(self) -> None:
        """
        Checks if an exception raised by the retrying function not matching an expected exception passed into the
        retry decorator propagates the exception.
        """
        @retry(ValueError, cooldown=None)
        def foo() -> None:
            raise TypeError

        self.assertRaises(TypeError, foo)


class AsyncRetryTestCase(IsolatedAsyncioTestCase):
    async def test_retry_success(self) -> None:
        """Checks if a success on a retry of a coroutine with the async_retry decorator returns the expected value."""

        tried = False

        @async_retry(Exception, cooldown=None)
        async def foo() -> str:
            nonlocal tried
            if tried:
                return 'foo'
            else:
                tried = True
                raise Exception

        try:
            self.assertEqual('foo', await foo())
        except RetryExhaustedError as e:
            raise AssertionError(f'exception raised: {e}') from e

    async def test_retry_cooldown(self) -> None:
        """Checks if there is a cooldown when a cooldown is specified in the async_retry decorator."""

        @async_retry(Exception, cooldown=1, retries=1)
        async def foo() -> None:
            raise Exception

        start = time.perf_counter()

        try:
            await foo()
        except RetryExhaustedError:
            pass

        self.assertGreaterEqual(time.perf_counter() - start, 0.9, 'cooldown not long enough')

    async def test_retry_retries(self) -> None:
        """
        Checks if the number of retries that are attempted of a function with the async_retry decorator is correct.
        """

        count = 0

        @async_retry(Exception, retries=5, cooldown=None)
        async def foo() -> None:
            nonlocal count
            count += 1
            raise Exception

        try:
            await foo()
        except RetryExhaustedError:
            pass

        self.assertEqual(6, count)

    async def test_retry_exhausted(self) -> None:
        """Checks if exhausting all the retries of a coroutine raises ``RetryExhaustedError``."""

        @async_retry(Exception, cooldown=None)
        async def foo() -> None:
            raise Exception

        with self.assertRaises(RetryExhaustedError):
            await foo()

    async def test_retry_different_error(self) -> None:
        """
        Checks if an exception raised by the retrying coroutine not matching an expected exception passed into the
        async_retry decorator propagates the exception.
        """

        @async_retry(ValueError, cooldown=None)
        async def foo() -> None:
            raise TypeError

        with self.assertRaises(TypeError):
            await foo()
