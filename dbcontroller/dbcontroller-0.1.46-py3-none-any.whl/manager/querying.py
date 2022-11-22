"""
    Class Tools
"""


class ClassPropertyDescriptor:
    """Used to generate the @classproperty"""

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError("can't set attribute")
        type_ = type(obj)
        return self.fset.__get__(obj, type_)(value)

    def setter(self, func):
        """Set Class-Property"""
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self


def classproperty(func):
    """Use to create a Class-Property"""

    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)
    return ClassPropertyDescriptor(func)

"""
    Model Querying
"""


class Manager:
    """Class: Create a Manager"""

    model = None

    @classproperty
    def engine(cls):
        """Return Controller"""
        return cls.model.__database__

    @classproperty
    def objects(cls):
        """Return Controller"""
        return cls.model.objects


def manager(cls):
    """Function: Create a Singleton"""
    custom_class = type(
        f"{cls.__name__}Manager",
        (cls, Manager),
        {},
    )
    return custom_class
