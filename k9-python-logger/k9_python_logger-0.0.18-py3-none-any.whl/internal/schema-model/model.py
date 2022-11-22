import copy

import jsonpatch
import jsonschema

from . import exceptions


class Model(dict):
    def __init__(self, *args, **kwargs):
        d = dict(*args, **kwargs)

        try:
            self.validate(d)
        except exceptions.ValidationError as exc:
            raise ValueError(str(exc))
        else:
            dict.__init__(self, d)

        self.__dict__["changes"] = {}
        self.__dict__["__original__"] = copy.deepcopy(d)

    def __setitem__(self, key, value):
        mutation = dict(self.items())
        mutation[key] = value
        try:
            self.validate(mutation)
        except exceptions.ValidationError as exc:
            msg = "Unable to set '%s' to %r. Reason: %s" % (key, value, str(exc))
            raise exceptions.InvalidOperation(msg)

        dict.__setitem__(self, key, value)

        self.__dict__["changes"][key] = value

    def __delitem__(self, key):
        mutation = dict(self.items())
        del mutation[key]
        try:
            self.validate(mutation)
        except exceptions.ValidationError as exc:
            msg = "Unable to delete attribute '%s'. Reason: %s" % (key, str(exc))
            raise exceptions.InvalidOperation(msg)

        dict.__delitem__(self, key)

    def __getattr__(self, key):
        try:
            return self.__getitem__(key)
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __delattr__(self, key):
        self.__delitem__(key)

    # BEGIN dict compatibility methods

    def clear(self):
        raise exceptions.InvalidOperation()

    def pop(self, key, default=None):
        raise exceptions.InvalidOperation()

    def popitem(self):
        raise exceptions.InvalidOperation()

    def copy(self):
        return copy.deepcopy(dict(self))

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memo):
        return copy.deepcopy(dict(self), memo)

    def update(self, other):
        mutation = dict(self.items())
        mutation.update(other)
        try:
            self.validate(mutation)
        except exceptions.ValidationError as exc:
            raise exceptions.InvalidOperation(str(exc))
        dict.update(self, other)

    def items(self):
        return copy.deepcopy(dict(self)).items()

    def values(self):
        return copy.deepcopy(dict(self)).values()

    # END dict compatibility methods

    @property
    def patch(self):
        """Return a jsonpatch object representing the delta"""
        original = self.__dict__["__original__"]
        return jsonpatch.make_patch(original, dict(self)).to_string()

    def validate(self, obj):
        """Apply a JSON schema to an object"""
        try:
            self.validator_instance.validate(obj)

        except jsonschema.ValidationError as exc:
            raise exceptions.ValidationError(str(exc))