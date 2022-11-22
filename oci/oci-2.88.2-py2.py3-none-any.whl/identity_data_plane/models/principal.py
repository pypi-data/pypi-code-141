# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Principal(object):
    """
    Principal model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Principal object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subject_id:
            The value to assign to the subject_id property of this Principal.
        :type subject_id: str

        :param tenant_id:
            The value to assign to the tenant_id property of this Principal.
        :type tenant_id: str

        :param claims:
            The value to assign to the claims property of this Principal.
        :type claims: list[oci.identity_data_plane.models.Claim]

        """
        self.swagger_types = {
            'subject_id': 'str',
            'tenant_id': 'str',
            'claims': 'list[Claim]'
        }

        self.attribute_map = {
            'subject_id': 'subjectId',
            'tenant_id': 'tenantId',
            'claims': 'claims'
        }

        self._subject_id = None
        self._tenant_id = None
        self._claims = None

    @property
    def subject_id(self):
        """
        **[Required]** Gets the subject_id of this Principal.
        The user's OCID.


        :return: The subject_id of this Principal.
        :rtype: str
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """
        Sets the subject_id of this Principal.
        The user's OCID.


        :param subject_id: The subject_id of this Principal.
        :type: str
        """
        self._subject_id = subject_id

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this Principal.
        The tenancy OCID.


        :return: The tenant_id of this Principal.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this Principal.
        The tenancy OCID.


        :param tenant_id: The tenant_id of this Principal.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def claims(self):
        """
        **[Required]** Gets the claims of this Principal.
        The set of claims for this principal.


        :return: The claims of this Principal.
        :rtype: list[oci.identity_data_plane.models.Claim]
        """
        return self._claims

    @claims.setter
    def claims(self, claims):
        """
        Sets the claims of this Principal.
        The set of claims for this principal.


        :param claims: The claims of this Principal.
        :type: list[oci.identity_data_plane.models.Claim]
        """
        self._claims = claims

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
