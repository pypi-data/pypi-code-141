from __future__ import annotations
from typing import Optional
import types
import traceback


def handle_error(func):
    def wrapped(self, *args, **kwargs):
        try:
            x = func(self, *args, **kwargs)
        except Exception as e:
            local_client = self.client
            if local_client:
                # TODO: add more specific checks and error messages
                if (
                    local_client.config.api_key is None
                    or local_client.config.api_key == ""
                ):
                    print("error: no api key set")
                if local_client.config.debug == True:
                    traceback.print_exc()
                else:
                    print(f"error: {e}")
                if local_client.config.raise_exception:
                    raise e
            else:
                print(f"error: {e}")
            return
        return x

    return wrapped


class ManagerMeta(type):
    def __new__(cls, name, bases, namespace, **kwds):
        namespace = {
            k: v
            if (k.startswith("__") or not isinstance(v, types.FunctionType))
            else handle_error(v)
            for k, v in namespace.items()
        }
        return type.__new__(cls, name, bases, namespace)


class Manager(metaclass=ManagerMeta):
    """Base class for resource managers"""

    name_pattern: str
    parent: str
    client: client.Client

    def __init__(
        self, client: client.Client, parent: str = "", run_name: str = ""
    ) -> None:
        self.client = client
        self.parent = parent
        self.run_name = run_name

    def name(self, id: str, parent: Optional[str] = None) -> str:
        """Generates a resource name from parent and id.

        Adds wildcard for any missing parent elements.

        Arguments:
            id: Name or id of resource.
            parent: (Optional) Override parent name.
        """
        if "/" in id:
            # Don't allow names to override manager parent config since this is confusing
            # and is typically a bug in the user code.
            if parent is not None and parent != "" and not id.startswith(parent):
                raise ValueError(f"Resource {id} not a child of {parent}.")
            return id
        pattern_parts = self.name_pattern.split("/")
        parent = parent or self.parent or ""
        parent_parts = parent.split("/")
        out = []
        for i in range(len(pattern_parts)):
            if (i + 1) % 2 == 0:
                if i < len(parent_parts):
                    out.append(parent_parts[i])
                else:
                    out.append("-")
            else:
                out.append(pattern_parts[i])
        out[-1] = id
        return "/".join(out)
