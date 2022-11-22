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


class AdjustHoldingForDateRequest(object):
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
        'effective_at': 'str',
        'instrument_identifiers': 'dict(str, str)',
        'sub_holding_keys': 'dict(str, PerpetualProperty)',
        'properties': 'dict(str, PerpetualProperty)',
        'tax_lots': 'list[TargetTaxLotRequest]',
        'currency': 'str'
    }

    attribute_map = {
        'effective_at': 'effectiveAt',
        'instrument_identifiers': 'instrumentIdentifiers',
        'sub_holding_keys': 'subHoldingKeys',
        'properties': 'properties',
        'tax_lots': 'taxLots',
        'currency': 'currency'
    }

    required_map = {
        'effective_at': 'required',
        'instrument_identifiers': 'required',
        'sub_holding_keys': 'optional',
        'properties': 'optional',
        'tax_lots': 'required',
        'currency': 'optional'
    }

    def __init__(self, effective_at=None, instrument_identifiers=None, sub_holding_keys=None, properties=None, tax_lots=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """AdjustHoldingForDateRequest - a model defined in OpenAPI"
        
        :param effective_at:  The Effective date that the target holding will be adjusted at. (required)
        :type effective_at: str
        :param instrument_identifiers:  A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. (required)
        :type instrument_identifiers: dict(str, str)
        :param sub_holding_keys:  Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the 'Transaction' domain.
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        :param properties:  Set of unique holding properties and associated values to store with the target holding. Each property must be from the 'Holding' domain.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param tax_lots:  The tax-lots that together make up the target holding. (required)
        :type tax_lots: list[lusid.TargetTaxLotRequest]
        :param currency:  The Holding currency. This needs to be equal with the one on the TaxLot -> cost if one is specified
        :type currency: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_at = None
        self._instrument_identifiers = None
        self._sub_holding_keys = None
        self._properties = None
        self._tax_lots = None
        self._currency = None
        self.discriminator = None

        self.effective_at = effective_at
        self.instrument_identifiers = instrument_identifiers
        self.sub_holding_keys = sub_holding_keys
        self.properties = properties
        self.tax_lots = tax_lots
        self.currency = currency

    @property
    def effective_at(self):
        """Gets the effective_at of this AdjustHoldingForDateRequest.  # noqa: E501

        The Effective date that the target holding will be adjusted at.  # noqa: E501

        :return: The effective_at of this AdjustHoldingForDateRequest.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this AdjustHoldingForDateRequest.

        The Effective date that the target holding will be adjusted at.  # noqa: E501

        :param effective_at: The effective_at of this AdjustHoldingForDateRequest.  # noqa: E501
        :type effective_at: str
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this AdjustHoldingForDateRequest.  # noqa: E501

        A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.  # noqa: E501

        :return: The instrument_identifiers of this AdjustHoldingForDateRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this AdjustHoldingForDateRequest.

        A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this AdjustHoldingForDateRequest.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this AdjustHoldingForDateRequest.  # noqa: E501

        Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the 'Transaction' domain.  # noqa: E501

        :return: The sub_holding_keys of this AdjustHoldingForDateRequest.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this AdjustHoldingForDateRequest.

        Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the 'Transaction' domain.  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this AdjustHoldingForDateRequest.  # noqa: E501
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def properties(self):
        """Gets the properties of this AdjustHoldingForDateRequest.  # noqa: E501

        Set of unique holding properties and associated values to store with the target holding. Each property must be from the 'Holding' domain.  # noqa: E501

        :return: The properties of this AdjustHoldingForDateRequest.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AdjustHoldingForDateRequest.

        Set of unique holding properties and associated values to store with the target holding. Each property must be from the 'Holding' domain.  # noqa: E501

        :param properties: The properties of this AdjustHoldingForDateRequest.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def tax_lots(self):
        """Gets the tax_lots of this AdjustHoldingForDateRequest.  # noqa: E501

        The tax-lots that together make up the target holding.  # noqa: E501

        :return: The tax_lots of this AdjustHoldingForDateRequest.  # noqa: E501
        :rtype: list[lusid.TargetTaxLotRequest]
        """
        return self._tax_lots

    @tax_lots.setter
    def tax_lots(self, tax_lots):
        """Sets the tax_lots of this AdjustHoldingForDateRequest.

        The tax-lots that together make up the target holding.  # noqa: E501

        :param tax_lots: The tax_lots of this AdjustHoldingForDateRequest.  # noqa: E501
        :type tax_lots: list[lusid.TargetTaxLotRequest]
        """
        if self.local_vars_configuration.client_side_validation and tax_lots is None:  # noqa: E501
            raise ValueError("Invalid value for `tax_lots`, must not be `None`")  # noqa: E501

        self._tax_lots = tax_lots

    @property
    def currency(self):
        """Gets the currency of this AdjustHoldingForDateRequest.  # noqa: E501

        The Holding currency. This needs to be equal with the one on the TaxLot -> cost if one is specified  # noqa: E501

        :return: The currency of this AdjustHoldingForDateRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AdjustHoldingForDateRequest.

        The Holding currency. This needs to be equal with the one on the TaxLot -> cost if one is specified  # noqa: E501

        :param currency: The currency of this AdjustHoldingForDateRequest.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

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
        if not isinstance(other, AdjustHoldingForDateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdjustHoldingForDateRequest):
            return True

        return self.to_dict() != other.to_dict()
