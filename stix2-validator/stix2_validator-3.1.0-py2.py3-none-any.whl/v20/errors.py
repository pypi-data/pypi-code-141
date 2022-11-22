from collections import deque

from jsonschema import exceptions as schema_exceptions

from ..errors import (NoJSONFileFoundError, PatternError, SchemaError,  # noqa
                      SchemaInvalidError, ValidationError, pretty_error)
from .enums import CHECK_CODES


class JSONError(schema_exceptions.ValidationError):
    """Wrapper for errors thrown by iter_errors() in the jsonschema module.
    Makes errors generated by our functions look like those from jsonschema.
    """
    def __init__(self, msg=None, instance_id=None, check_code=None):
        if check_code is not None:
            # Get code number code from name
            code = list(CHECK_CODES.keys())[list(CHECK_CODES.values()).index(check_code)]
            msg = '{%s} %s' % (code, msg)
        super(JSONError, self).__init__(msg, path=deque([instance_id]))
