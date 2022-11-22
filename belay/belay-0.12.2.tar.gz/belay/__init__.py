# Don't manually change, let poetry-dynamic-versioning-plugin handle it.
__version__ = "0.12.2"

__all__ = [
    "AuthenticationError",
    "minify",
    "Device",
    "SpecialFunctionNameError",
    "PyboardException",
    "Implementation",
    "FeatureUnavailableError",
]
from ._minify import minify
from .device import Device, Implementation
from .exceptions import (
    AuthenticationError,
    ConnectionLost,
    FeatureUnavailableError,
    MaxHistoryLengthError,
    SpecialFunctionNameError,
)
from .pyboard import PyboardException
