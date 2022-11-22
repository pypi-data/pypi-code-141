# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4993
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class Portfolio(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'href': 'str',
        'id': 'ResourceId',
        'type': 'str',
        'display_name': 'str',
        'description': 'str',
        'created': 'datetime',
        'parent_portfolio_id': 'ResourceId',
        'version': 'Version',
        'is_derived': 'bool',
        'base_currency': 'str',
        'properties': 'dict(str, ModelProperty)',
        'relationships': 'list[Relationship]',
        'instrument_scopes': 'list[str]',
        'accounting_method': 'str',
        'amortisation_method': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'type': 'type',
        'display_name': 'displayName',
        'description': 'description',
        'created': 'created',
        'parent_portfolio_id': 'parentPortfolioId',
        'version': 'version',
        'is_derived': 'isDerived',
        'base_currency': 'baseCurrency',
        'properties': 'properties',
        'relationships': 'relationships',
        'instrument_scopes': 'instrumentScopes',
        'accounting_method': 'accountingMethod',
        'amortisation_method': 'amortisationMethod',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'id': 'required',
        'type': 'required',
        'display_name': 'required',
        'description': 'optional',
        'created': 'required',
        'parent_portfolio_id': 'optional',
        'version': 'optional',
        'is_derived': 'optional',
        'base_currency': 'optional',
        'properties': 'optional',
        'relationships': 'optional',
        'instrument_scopes': 'optional',
        'accounting_method': 'optional',
        'amortisation_method': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, id=None, type=None, display_name=None, description=None, created=None, parent_portfolio_id=None, version=None, is_derived=None, base_currency=None, properties=None, relationships=None, instrument_scopes=None, accounting_method=None, amortisation_method=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Portfolio - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param id:  (required)
        :type id: lusid.ResourceId
        :param type:  The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction (required)
        :type type: str
        :param display_name:  The name of the portfolio. (required)
        :type display_name: str
        :param description:  The long form description of the portfolio.
        :type description: str
        :param created:  The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. (required)
        :type created: datetime
        :param parent_portfolio_id: 
        :type parent_portfolio_id: lusid.ResourceId
        :param version: 
        :type version: lusid.Version
        :param is_derived:  Whether or not this is a derived portfolio.
        :type is_derived: bool
        :param base_currency:  The base currency of the portfolio.
        :type base_currency: str
        :param properties:  The requested portfolio properties. These will be from the 'Portfolio' domain.
        :type properties: dict[str, lusid.ModelProperty]
        :param relationships:  A set of relationships associated to the portfolio.
        :type relationships: list[lusid.Relationship]
        :param instrument_scopes:  The instrument scope resolution strategy of this portfolio.
        :type instrument_scopes: list[str]
        :param accounting_method:  . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst
        :type accounting_method: str
        :param amortisation_method:  The amortisation method the portfolio is using in the calculation. This can be 'NoAmortisation', 'StraightLine' or 'EffectiveYield'.
        :type amortisation_method: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._id = None
        self._type = None
        self._display_name = None
        self._description = None
        self._created = None
        self._parent_portfolio_id = None
        self._version = None
        self._is_derived = None
        self._base_currency = None
        self._properties = None
        self._relationships = None
        self._instrument_scopes = None
        self._accounting_method = None
        self._amortisation_method = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.id = id
        self.type = type
        self.display_name = display_name
        self.description = description
        self.created = created
        if parent_portfolio_id is not None:
            self.parent_portfolio_id = parent_portfolio_id
        if version is not None:
            self.version = version
        if is_derived is not None:
            self.is_derived = is_derived
        self.base_currency = base_currency
        self.properties = properties
        self.relationships = relationships
        self.instrument_scopes = instrument_scopes
        if accounting_method is not None:
            self.accounting_method = accounting_method
        self.amortisation_method = amortisation_method
        self.links = links

    @property
    def href(self):
        """Gets the href of this Portfolio.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Portfolio.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this Portfolio.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Portfolio.  # noqa: E501


        :return: The id of this Portfolio.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Portfolio.


        :param id: The id of this Portfolio.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Portfolio.  # noqa: E501

        The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction  # noqa: E501

        :return: The type of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Portfolio.

        The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction  # noqa: E501

        :param type: The type of this Portfolio.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Transaction", "Reference", "DerivedTransaction"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this Portfolio.  # noqa: E501

        The name of the portfolio.  # noqa: E501

        :return: The display_name of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Portfolio.

        The name of the portfolio.  # noqa: E501

        :param display_name: The display_name of this Portfolio.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Portfolio.  # noqa: E501

        The long form description of the portfolio.  # noqa: E501

        :return: The description of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Portfolio.

        The long form description of the portfolio.  # noqa: E501

        :param description: The description of this Portfolio.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def created(self):
        """Gets the created of this Portfolio.  # noqa: E501

        The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.  # noqa: E501

        :return: The created of this Portfolio.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Portfolio.

        The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.  # noqa: E501

        :param created: The created of this Portfolio.  # noqa: E501
        :type created: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def parent_portfolio_id(self):
        """Gets the parent_portfolio_id of this Portfolio.  # noqa: E501


        :return: The parent_portfolio_id of this Portfolio.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._parent_portfolio_id

    @parent_portfolio_id.setter
    def parent_portfolio_id(self, parent_portfolio_id):
        """Sets the parent_portfolio_id of this Portfolio.


        :param parent_portfolio_id: The parent_portfolio_id of this Portfolio.  # noqa: E501
        :type parent_portfolio_id: lusid.ResourceId
        """

        self._parent_portfolio_id = parent_portfolio_id

    @property
    def version(self):
        """Gets the version of this Portfolio.  # noqa: E501


        :return: The version of this Portfolio.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Portfolio.


        :param version: The version of this Portfolio.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def is_derived(self):
        """Gets the is_derived of this Portfolio.  # noqa: E501

        Whether or not this is a derived portfolio.  # noqa: E501

        :return: The is_derived of this Portfolio.  # noqa: E501
        :rtype: bool
        """
        return self._is_derived

    @is_derived.setter
    def is_derived(self, is_derived):
        """Sets the is_derived of this Portfolio.

        Whether or not this is a derived portfolio.  # noqa: E501

        :param is_derived: The is_derived of this Portfolio.  # noqa: E501
        :type is_derived: bool
        """

        self._is_derived = is_derived

    @property
    def base_currency(self):
        """Gets the base_currency of this Portfolio.  # noqa: E501

        The base currency of the portfolio.  # noqa: E501

        :return: The base_currency of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this Portfolio.

        The base currency of the portfolio.  # noqa: E501

        :param base_currency: The base_currency of this Portfolio.  # noqa: E501
        :type base_currency: str
        """

        self._base_currency = base_currency

    @property
    def properties(self):
        """Gets the properties of this Portfolio.  # noqa: E501

        The requested portfolio properties. These will be from the 'Portfolio' domain.  # noqa: E501

        :return: The properties of this Portfolio.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Portfolio.

        The requested portfolio properties. These will be from the 'Portfolio' domain.  # noqa: E501

        :param properties: The properties of this Portfolio.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def relationships(self):
        """Gets the relationships of this Portfolio.  # noqa: E501

        A set of relationships associated to the portfolio.  # noqa: E501

        :return: The relationships of this Portfolio.  # noqa: E501
        :rtype: list[lusid.Relationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this Portfolio.

        A set of relationships associated to the portfolio.  # noqa: E501

        :param relationships: The relationships of this Portfolio.  # noqa: E501
        :type relationships: list[lusid.Relationship]
        """

        self._relationships = relationships

    @property
    def instrument_scopes(self):
        """Gets the instrument_scopes of this Portfolio.  # noqa: E501

        The instrument scope resolution strategy of this portfolio.  # noqa: E501

        :return: The instrument_scopes of this Portfolio.  # noqa: E501
        :rtype: list[str]
        """
        return self._instrument_scopes

    @instrument_scopes.setter
    def instrument_scopes(self, instrument_scopes):
        """Sets the instrument_scopes of this Portfolio.

        The instrument scope resolution strategy of this portfolio.  # noqa: E501

        :param instrument_scopes: The instrument_scopes of this Portfolio.  # noqa: E501
        :type instrument_scopes: list[str]
        """

        self._instrument_scopes = instrument_scopes

    @property
    def accounting_method(self):
        """Gets the accounting_method of this Portfolio.  # noqa: E501

        . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst  # noqa: E501

        :return: The accounting_method of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._accounting_method

    @accounting_method.setter
    def accounting_method(self, accounting_method):
        """Sets the accounting_method of this Portfolio.

        . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst  # noqa: E501

        :param accounting_method: The accounting_method of this Portfolio.  # noqa: E501
        :type accounting_method: str
        """
        allowed_values = ["Default", "AverageCost", "FirstInFirstOut", "LastInFirstOut", "HighestCostFirst", "LowestCostFirst"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and accounting_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `accounting_method` ({0}), must be one of {1}"  # noqa: E501
                .format(accounting_method, allowed_values)
            )

        self._accounting_method = accounting_method

    @property
    def amortisation_method(self):
        """Gets the amortisation_method of this Portfolio.  # noqa: E501

        The amortisation method the portfolio is using in the calculation. This can be 'NoAmortisation', 'StraightLine' or 'EffectiveYield'.  # noqa: E501

        :return: The amortisation_method of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._amortisation_method

    @amortisation_method.setter
    def amortisation_method(self, amortisation_method):
        """Sets the amortisation_method of this Portfolio.

        The amortisation method the portfolio is using in the calculation. This can be 'NoAmortisation', 'StraightLine' or 'EffectiveYield'.  # noqa: E501

        :param amortisation_method: The amortisation_method of this Portfolio.  # noqa: E501
        :type amortisation_method: str
        """

        self._amortisation_method = amortisation_method

    @property
    def links(self):
        """Gets the links of this Portfolio.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this Portfolio.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Portfolio.

        Collection of links.  # noqa: E501

        :param links: The links of this Portfolio.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Portfolio):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Portfolio):
            return True

        return self.to_dict() != other.to_dict()
