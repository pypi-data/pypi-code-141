# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LicenseMetric(object):
    """
    Overview of product license and resources usage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LicenseMetric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_product_license_count:
            The value to assign to the total_product_license_count property of this LicenseMetric.
        :type total_product_license_count: int

        :param total_byol_instance_count:
            The value to assign to the total_byol_instance_count property of this LicenseMetric.
        :type total_byol_instance_count: int

        :param total_license_included_instance_count:
            The value to assign to the total_license_included_instance_count property of this LicenseMetric.
        :type total_license_included_instance_count: int

        :param license_record_expiring_soon_count:
            The value to assign to the license_record_expiring_soon_count property of this LicenseMetric.
        :type license_record_expiring_soon_count: int

        """
        self.swagger_types = {
            'total_product_license_count': 'int',
            'total_byol_instance_count': 'int',
            'total_license_included_instance_count': 'int',
            'license_record_expiring_soon_count': 'int'
        }

        self.attribute_map = {
            'total_product_license_count': 'totalProductLicenseCount',
            'total_byol_instance_count': 'totalByolInstanceCount',
            'total_license_included_instance_count': 'totalLicenseIncludedInstanceCount',
            'license_record_expiring_soon_count': 'licenseRecordExpiringSoonCount'
        }

        self._total_product_license_count = None
        self._total_byol_instance_count = None
        self._total_license_included_instance_count = None
        self._license_record_expiring_soon_count = None

    @property
    def total_product_license_count(self):
        """
        **[Required]** Gets the total_product_license_count of this LicenseMetric.
        Total number of product licenses in a particular compartment.


        :return: The total_product_license_count of this LicenseMetric.
        :rtype: int
        """
        return self._total_product_license_count

    @total_product_license_count.setter
    def total_product_license_count(self, total_product_license_count):
        """
        Sets the total_product_license_count of this LicenseMetric.
        Total number of product licenses in a particular compartment.


        :param total_product_license_count: The total_product_license_count of this LicenseMetric.
        :type: int
        """
        self._total_product_license_count = total_product_license_count

    @property
    def total_byol_instance_count(self):
        """
        **[Required]** Gets the total_byol_instance_count of this LicenseMetric.
        Total number of BYOL instances in a particular compartment.


        :return: The total_byol_instance_count of this LicenseMetric.
        :rtype: int
        """
        return self._total_byol_instance_count

    @total_byol_instance_count.setter
    def total_byol_instance_count(self, total_byol_instance_count):
        """
        Sets the total_byol_instance_count of this LicenseMetric.
        Total number of BYOL instances in a particular compartment.


        :param total_byol_instance_count: The total_byol_instance_count of this LicenseMetric.
        :type: int
        """
        self._total_byol_instance_count = total_byol_instance_count

    @property
    def total_license_included_instance_count(self):
        """
        **[Required]** Gets the total_license_included_instance_count of this LicenseMetric.
        Total number of License Included (LI) instances in a particular compartment.


        :return: The total_license_included_instance_count of this LicenseMetric.
        :rtype: int
        """
        return self._total_license_included_instance_count

    @total_license_included_instance_count.setter
    def total_license_included_instance_count(self, total_license_included_instance_count):
        """
        Sets the total_license_included_instance_count of this LicenseMetric.
        Total number of License Included (LI) instances in a particular compartment.


        :param total_license_included_instance_count: The total_license_included_instance_count of this LicenseMetric.
        :type: int
        """
        self._total_license_included_instance_count = total_license_included_instance_count

    @property
    def license_record_expiring_soon_count(self):
        """
        **[Required]** Gets the license_record_expiring_soon_count of this LicenseMetric.
        Total number of license records that will expire within 90 days in a particular compartment.


        :return: The license_record_expiring_soon_count of this LicenseMetric.
        :rtype: int
        """
        return self._license_record_expiring_soon_count

    @license_record_expiring_soon_count.setter
    def license_record_expiring_soon_count(self, license_record_expiring_soon_count):
        """
        Sets the license_record_expiring_soon_count of this LicenseMetric.
        Total number of license records that will expire within 90 days in a particular compartment.


        :param license_record_expiring_soon_count: The license_record_expiring_soon_count of this LicenseMetric.
        :type: int
        """
        self._license_record_expiring_soon_count = license_record_expiring_soon_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
