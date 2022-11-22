# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateSourceScanHost(object):
    """
    Private source Scan Hostname model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateSourceScanHost object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scan_hostname:
            The value to assign to the scan_hostname property of this PrivateSourceScanHost.
        :type scan_hostname: str

        :param scan_port:
            The value to assign to the scan_port property of this PrivateSourceScanHost.
        :type scan_port: int

        :param description:
            The value to assign to the description property of this PrivateSourceScanHost.
        :type description: str

        """
        self.swagger_types = {
            'scan_hostname': 'str',
            'scan_port': 'int',
            'description': 'str'
        }

        self.attribute_map = {
            'scan_hostname': 'scanHostname',
            'scan_port': 'scanPort',
            'description': 'description'
        }

        self._scan_hostname = None
        self._scan_port = None
        self._description = None

    @property
    def scan_hostname(self):
        """
        **[Required]** Gets the scan_hostname of this PrivateSourceScanHost.
        Private Source Scan hostname. Ex: db01-scan.corp.example.com, prd-db01-scan.mycompany.com.


        :return: The scan_hostname of this PrivateSourceScanHost.
        :rtype: str
        """
        return self._scan_hostname

    @scan_hostname.setter
    def scan_hostname(self, scan_hostname):
        """
        Sets the scan_hostname of this PrivateSourceScanHost.
        Private Source Scan hostname. Ex: db01-scan.corp.example.com, prd-db01-scan.mycompany.com.


        :param scan_hostname: The scan_hostname of this PrivateSourceScanHost.
        :type: str
        """
        self._scan_hostname = scan_hostname

    @property
    def scan_port(self):
        """
        **[Required]** Gets the scan_port of this PrivateSourceScanHost.
        Private Source Scan host port. This is the source port where SCAN protocol will get connected (e.g. 1521).


        :return: The scan_port of this PrivateSourceScanHost.
        :rtype: int
        """
        return self._scan_port

    @scan_port.setter
    def scan_port(self, scan_port):
        """
        Sets the scan_port of this PrivateSourceScanHost.
        Private Source Scan host port. This is the source port where SCAN protocol will get connected (e.g. 1521).


        :param scan_port: The scan_port of this PrivateSourceScanHost.
        :type: int
        """
        self._scan_port = scan_port

    @property
    def description(self):
        """
        Gets the description of this PrivateSourceScanHost.
        Description of private source scan host zone.


        :return: The description of this PrivateSourceScanHost.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PrivateSourceScanHost.
        Description of private source scan host zone.


        :param description: The description of this PrivateSourceScanHost.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
