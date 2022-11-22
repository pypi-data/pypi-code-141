# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageResponse(object):
    """
    The collection of image details for the product license.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ImageResponse.
        :type id: str

        :param listing_name:
            The value to assign to the listing_name property of this ImageResponse.
        :type listing_name: str

        :param publisher:
            The value to assign to the publisher property of this ImageResponse.
        :type publisher: str

        :param listing_id:
            The value to assign to the listing_id property of this ImageResponse.
        :type listing_id: str

        :param package_version:
            The value to assign to the package_version property of this ImageResponse.
        :type package_version: str

        """
        self.swagger_types = {
            'id': 'str',
            'listing_name': 'str',
            'publisher': 'str',
            'listing_id': 'str',
            'package_version': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'listing_name': 'listingName',
            'publisher': 'publisher',
            'listing_id': 'listingId',
            'package_version': 'packageVersion'
        }

        self._id = None
        self._listing_name = None
        self._publisher = None
        self._listing_id = None
        self._package_version = None

    @property
    def id(self):
        """
        Gets the id of this ImageResponse.
        The image ID associated with the product license.


        :return: The id of this ImageResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ImageResponse.
        The image ID associated with the product license.


        :param id: The id of this ImageResponse.
        :type: str
        """
        self._id = id

    @property
    def listing_name(self):
        """
        Gets the listing_name of this ImageResponse.
        The listing name associated with the product license.


        :return: The listing_name of this ImageResponse.
        :rtype: str
        """
        return self._listing_name

    @listing_name.setter
    def listing_name(self, listing_name):
        """
        Sets the listing_name of this ImageResponse.
        The listing name associated with the product license.


        :param listing_name: The listing_name of this ImageResponse.
        :type: str
        """
        self._listing_name = listing_name

    @property
    def publisher(self):
        """
        Gets the publisher of this ImageResponse.
        The image publisher.


        :return: The publisher of this ImageResponse.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher of this ImageResponse.
        The image publisher.


        :param publisher: The publisher of this ImageResponse.
        :type: str
        """
        self._publisher = publisher

    @property
    def listing_id(self):
        """
        Gets the listing_id of this ImageResponse.
        The image listing ID.


        :return: The listing_id of this ImageResponse.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this ImageResponse.
        The image listing ID.


        :param listing_id: The listing_id of this ImageResponse.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def package_version(self):
        """
        Gets the package_version of this ImageResponse.
        The image package version.


        :return: The package_version of this ImageResponse.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this ImageResponse.
        The image package version.


        :param package_version: The package_version of this ImageResponse.
        :type: str
        """
        self._package_version = package_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
