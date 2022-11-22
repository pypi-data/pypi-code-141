# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublishedObject(object):
    """
    The information about the published object.
    """

    #: A constant which can be used with the model_type property of a PublishedObject.
    #: This constant has a value of "INTEGRATION_TASK"
    MODEL_TYPE_INTEGRATION_TASK = "INTEGRATION_TASK"

    #: A constant which can be used with the model_type property of a PublishedObject.
    #: This constant has a value of "DATA_LOADER_TASK"
    MODEL_TYPE_DATA_LOADER_TASK = "DATA_LOADER_TASK"

    #: A constant which can be used with the model_type property of a PublishedObject.
    #: This constant has a value of "PIPELINE_TASK"
    MODEL_TYPE_PIPELINE_TASK = "PIPELINE_TASK"

    #: A constant which can be used with the model_type property of a PublishedObject.
    #: This constant has a value of "SQL_TASK"
    MODEL_TYPE_SQL_TASK = "SQL_TASK"

    #: A constant which can be used with the model_type property of a PublishedObject.
    #: This constant has a value of "OCI_DATAFLOW_TASK"
    MODEL_TYPE_OCI_DATAFLOW_TASK = "OCI_DATAFLOW_TASK"

    #: A constant which can be used with the model_type property of a PublishedObject.
    #: This constant has a value of "REST_TASK"
    MODEL_TYPE_REST_TASK = "REST_TASK"

    def __init__(self, **kwargs):
        """
        Initializes a new PublishedObject object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.PublishedObjectFromDataLoaderTask`
        * :class:`~oci.data_integration.models.PublishedObjectFromPipelineTask`
        * :class:`~oci.data_integration.models.PublishedObjectFromIntegrationTask`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this PublishedObject.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this PublishedObject.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this PublishedObject.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this PublishedObject.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this PublishedObject.
        :type name: str

        :param description:
            The value to assign to the description property of this PublishedObject.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this PublishedObject.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this PublishedObject.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this PublishedObject.
        :type identifier: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'DATA_LOADER_TASK':
            return 'PublishedObjectFromDataLoaderTask'

        if type == 'PIPELINE_TASK':
            return 'PublishedObjectFromPipelineTask'

        if type == 'INTEGRATION_TASK':
            return 'PublishedObjectFromIntegrationTask'
        else:
            return 'PublishedObject'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this PublishedObject.
        The type of the published object.

        Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this PublishedObject.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this PublishedObject.
        The type of the published object.


        :param model_type: The model_type of this PublishedObject.
        :type: str
        """
        allowed_values = ["INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this PublishedObject.
        Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.


        :return: The key of this PublishedObject.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this PublishedObject.
        Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.


        :param key: The key of this PublishedObject.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this PublishedObject.
        The object's model version.


        :return: The model_version of this PublishedObject.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this PublishedObject.
        The object's model version.


        :param model_version: The model_version of this PublishedObject.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this PublishedObject.

        :return: The parent_ref of this PublishedObject.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this PublishedObject.

        :param parent_ref: The parent_ref of this PublishedObject.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this PublishedObject.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this PublishedObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PublishedObject.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this PublishedObject.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PublishedObject.
        Detailed description for the object.


        :return: The description of this PublishedObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PublishedObject.
        Detailed description for the object.


        :param description: The description of this PublishedObject.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this PublishedObject.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this PublishedObject.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this PublishedObject.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this PublishedObject.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this PublishedObject.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this PublishedObject.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this PublishedObject.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this PublishedObject.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this PublishedObject.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this PublishedObject.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this PublishedObject.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this PublishedObject.
        :type: str
        """
        self._identifier = identifier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
