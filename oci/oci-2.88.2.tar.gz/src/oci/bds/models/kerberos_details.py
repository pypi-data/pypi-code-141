# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KerberosDetails(object):
    """
    Details about the Kerberos principals.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KerberosDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param principal_name:
            The value to assign to the principal_name property of this KerberosDetails.
        :type principal_name: str

        :param keytab_file:
            The value to assign to the keytab_file property of this KerberosDetails.
        :type keytab_file: str

        """
        self.swagger_types = {
            'principal_name': 'str',
            'keytab_file': 'str'
        }

        self.attribute_map = {
            'principal_name': 'principalName',
            'keytab_file': 'keytabFile'
        }

        self._principal_name = None
        self._keytab_file = None

    @property
    def principal_name(self):
        """
        **[Required]** Gets the principal_name of this KerberosDetails.
        Name of the Kerberos principal.


        :return: The principal_name of this KerberosDetails.
        :rtype: str
        """
        return self._principal_name

    @principal_name.setter
    def principal_name(self, principal_name):
        """
        Sets the principal_name of this KerberosDetails.
        Name of the Kerberos principal.


        :param principal_name: The principal_name of this KerberosDetails.
        :type: str
        """
        self._principal_name = principal_name

    @property
    def keytab_file(self):
        """
        **[Required]** Gets the keytab_file of this KerberosDetails.
        Location of the keytab file


        :return: The keytab_file of this KerberosDetails.
        :rtype: str
        """
        return self._keytab_file

    @keytab_file.setter
    def keytab_file(self, keytab_file):
        """
        Sets the keytab_file of this KerberosDetails.
        Location of the keytab file


        :param keytab_file: The keytab_file of this KerberosDetails.
        :type: str
        """
        self._keytab_file = keytab_file

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
