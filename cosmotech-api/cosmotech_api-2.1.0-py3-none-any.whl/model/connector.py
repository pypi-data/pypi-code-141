"""
    Cosmo Tech Plaform API

    Cosmo Tech Platform API  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: platform@cosmotech.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cosmotech_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from cosmotech_api.exceptions import ApiAttributeError


def lazy_import():
    from cosmotech_api.model.connector_parameter_group import ConnectorParameterGroup
    globals()['ConnectorParameterGroup'] = ConnectorParameterGroup


class Connector(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('io_types',): {
            'READ': "read",
            'WRITE': "write",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'key': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'repository': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'io_types': ([str],),  # noqa: E501
            'id': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
            'owner_id': (str,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'azure_managed_identity': (bool,),  # noqa: E501
            'azure_authentication_with_customer_app_registration': (bool,),  # noqa: E501
            'parameter_groups': ([ConnectorParameterGroup],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'key': 'key',  # noqa: E501
        'name': 'name',  # noqa: E501
        'repository': 'repository',  # noqa: E501
        'version': 'version',  # noqa: E501
        'io_types': 'ioTypes',  # noqa: E501
        'id': 'id',  # noqa: E501
        'description': 'description',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'owner_id': 'ownerId',  # noqa: E501
        'url': 'url',  # noqa: E501
        'azure_managed_identity': 'azureManagedIdentity',  # noqa: E501
        'azure_authentication_with_customer_app_registration': 'azureAuthenticationWithCustomerAppRegistration',  # noqa: E501
        'parameter_groups': 'parameterGroups',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'owner_id',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, key, name, repository, version, io_types, *args, **kwargs):  # noqa: E501
        """Connector - a model defined in OpenAPI

        Args:
            key (str): the Connector key which group Connector versions
            name (str): the Connector name
            repository (str): the registry repository containing the image
            version (str): the Connector version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag
            io_types ([str]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): the Connector version unique identifier. [optional]  # noqa: E501
            description (str): the Connector description. [optional]  # noqa: E501
            tags ([str]): the list of tags. [optional]  # noqa: E501
            owner_id (str): the user id which own this connector version. [optional]  # noqa: E501
            url (str): an optional URL link to connector page. [optional]  # noqa: E501
            azure_managed_identity (bool): whether or not the connector uses Azure Managed Identity. [optional]  # noqa: E501
            azure_authentication_with_customer_app_registration (bool): whether to authenticate against Azure using the app registration credentials provided by the customer. [optional]  # noqa: E501
            parameter_groups ([ConnectorParameterGroup]): the list of connector parameters groups. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.key = key
        self.name = name
        self.repository = repository
        self.version = version
        self.io_types = io_types
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, key, name, repository, version, io_types, *args, **kwargs):  # noqa: E501
        """Connector - a model defined in OpenAPI

        Args:
            key (str): the Connector key which group Connector versions
            name (str): the Connector name
            repository (str): the registry repository containing the image
            version (str): the Connector version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag
            io_types ([str]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): the Connector version unique identifier. [optional]  # noqa: E501
            description (str): the Connector description. [optional]  # noqa: E501
            tags ([str]): the list of tags. [optional]  # noqa: E501
            owner_id (str): the user id which own this connector version. [optional]  # noqa: E501
            url (str): an optional URL link to connector page. [optional]  # noqa: E501
            azure_managed_identity (bool): whether or not the connector uses Azure Managed Identity. [optional]  # noqa: E501
            azure_authentication_with_customer_app_registration (bool): whether to authenticate against Azure using the app registration credentials provided by the customer. [optional]  # noqa: E501
            parameter_groups ([ConnectorParameterGroup]): the list of connector parameters groups. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.key = key
        self.name = name
        self.repository = repository
        self.version = version
        self.io_types = io_types
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
