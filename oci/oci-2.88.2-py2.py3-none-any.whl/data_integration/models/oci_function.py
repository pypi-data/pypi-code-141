# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OciFunction(object):
    """
    The information about the OCI Function.
    """

    #: A constant which can be used with the model_type property of a OciFunction.
    #: This constant has a value of "OCI_FUNCTION"
    MODEL_TYPE_OCI_FUNCTION = "OCI_FUNCTION"

    #: A constant which can be used with the payload_format property of a OciFunction.
    #: This constant has a value of "JSON"
    PAYLOAD_FORMAT_JSON = "JSON"

    #: A constant which can be used with the payload_format property of a OciFunction.
    #: This constant has a value of "AVRO"
    PAYLOAD_FORMAT_AVRO = "AVRO"

    #: A constant which can be used with the payload_format property of a OciFunction.
    #: This constant has a value of "JSONBYTES"
    PAYLOAD_FORMAT_JSONBYTES = "JSONBYTES"

    def __init__(self, **kwargs):
        """
        Initializes a new OciFunction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param function_id:
            The value to assign to the function_id property of this OciFunction.
        :type function_id: str

        :param region_id:
            The value to assign to the region_id property of this OciFunction.
        :type region_id: str

        :param fn_config_definition:
            The value to assign to the fn_config_definition property of this OciFunction.
        :type fn_config_definition: oci.data_integration.models.ConfigDefinition

        :param input_shape:
            The value to assign to the input_shape property of this OciFunction.
        :type input_shape: oci.data_integration.models.Shape

        :param output_shape:
            The value to assign to the output_shape property of this OciFunction.
        :type output_shape: oci.data_integration.models.Shape

        :param model_type:
            The value to assign to the model_type property of this OciFunction.
            Allowed values for this property are: "OCI_FUNCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this OciFunction.
        :type key: str

        :param parent_ref:
            The value to assign to the parent_ref property of this OciFunction.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param model_version:
            The value to assign to the model_version property of this OciFunction.
        :type model_version: str

        :param object_version:
            The value to assign to the object_version property of this OciFunction.
        :type object_version: int

        :param payload_format:
            The value to assign to the payload_format property of this OciFunction.
            Allowed values for this property are: "JSON", "AVRO", "JSONBYTES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type payload_format: str

        :param fn_config_def:
            The value to assign to the fn_config_def property of this OciFunction.
        :type fn_config_def: oci.data_integration.models.FunctionConfigurationDefinition

        """
        self.swagger_types = {
            'function_id': 'str',
            'region_id': 'str',
            'fn_config_definition': 'ConfigDefinition',
            'input_shape': 'Shape',
            'output_shape': 'Shape',
            'model_type': 'str',
            'key': 'str',
            'parent_ref': 'ParentReference',
            'model_version': 'str',
            'object_version': 'int',
            'payload_format': 'str',
            'fn_config_def': 'FunctionConfigurationDefinition'
        }

        self.attribute_map = {
            'function_id': 'functionId',
            'region_id': 'regionId',
            'fn_config_definition': 'fnConfigDefinition',
            'input_shape': 'inputShape',
            'output_shape': 'outputShape',
            'model_type': 'modelType',
            'key': 'key',
            'parent_ref': 'parentRef',
            'model_version': 'modelVersion',
            'object_version': 'objectVersion',
            'payload_format': 'payloadFormat',
            'fn_config_def': 'fnConfigDef'
        }

        self._function_id = None
        self._region_id = None
        self._fn_config_definition = None
        self._input_shape = None
        self._output_shape = None
        self._model_type = None
        self._key = None
        self._parent_ref = None
        self._model_version = None
        self._object_version = None
        self._payload_format = None
        self._fn_config_def = None

    @property
    def function_id(self):
        """
        Gets the function_id of this OciFunction.
        Ocid of the OCI Function.


        :return: The function_id of this OciFunction.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this OciFunction.
        Ocid of the OCI Function.


        :param function_id: The function_id of this OciFunction.
        :type: str
        """
        self._function_id = function_id

    @property
    def region_id(self):
        """
        Gets the region_id of this OciFunction.
        Region where the OCI Function is deployed.


        :return: The region_id of this OciFunction.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this OciFunction.
        Region where the OCI Function is deployed.


        :param region_id: The region_id of this OciFunction.
        :type: str
        """
        self._region_id = region_id

    @property
    def fn_config_definition(self):
        """
        Gets the fn_config_definition of this OciFunction.

        :return: The fn_config_definition of this OciFunction.
        :rtype: oci.data_integration.models.ConfigDefinition
        """
        return self._fn_config_definition

    @fn_config_definition.setter
    def fn_config_definition(self, fn_config_definition):
        """
        Sets the fn_config_definition of this OciFunction.

        :param fn_config_definition: The fn_config_definition of this OciFunction.
        :type: oci.data_integration.models.ConfigDefinition
        """
        self._fn_config_definition = fn_config_definition

    @property
    def input_shape(self):
        """
        Gets the input_shape of this OciFunction.

        :return: The input_shape of this OciFunction.
        :rtype: oci.data_integration.models.Shape
        """
        return self._input_shape

    @input_shape.setter
    def input_shape(self, input_shape):
        """
        Sets the input_shape of this OciFunction.

        :param input_shape: The input_shape of this OciFunction.
        :type: oci.data_integration.models.Shape
        """
        self._input_shape = input_shape

    @property
    def output_shape(self):
        """
        Gets the output_shape of this OciFunction.

        :return: The output_shape of this OciFunction.
        :rtype: oci.data_integration.models.Shape
        """
        return self._output_shape

    @output_shape.setter
    def output_shape(self, output_shape):
        """
        Sets the output_shape of this OciFunction.

        :param output_shape: The output_shape of this OciFunction.
        :type: oci.data_integration.models.Shape
        """
        self._output_shape = output_shape

    @property
    def model_type(self):
        """
        Gets the model_type of this OciFunction.
        The type of the OCI Function object.

        Allowed values for this property are: "OCI_FUNCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this OciFunction.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this OciFunction.
        The type of the OCI Function object.


        :param model_type: The model_type of this OciFunction.
        :type: str
        """
        allowed_values = ["OCI_FUNCTION"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this OciFunction.
        The key identifying the OCI Function operator object, use this to identiy this instance within the dataflow.


        :return: The key of this OciFunction.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this OciFunction.
        The key identifying the OCI Function operator object, use this to identiy this instance within the dataflow.


        :param key: The key of this OciFunction.
        :type: str
        """
        self._key = key

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this OciFunction.

        :return: The parent_ref of this OciFunction.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this OciFunction.

        :param parent_ref: The parent_ref of this OciFunction.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def model_version(self):
        """
        Gets the model_version of this OciFunction.
        The model version of an object.


        :return: The model_version of this OciFunction.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this OciFunction.
        The model version of an object.


        :param model_version: The model_version of this OciFunction.
        :type: str
        """
        self._model_version = model_version

    @property
    def object_version(self):
        """
        Gets the object_version of this OciFunction.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this OciFunction.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this OciFunction.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this OciFunction.
        :type: int
        """
        self._object_version = object_version

    @property
    def payload_format(self):
        """
        Gets the payload_format of this OciFunction.
        The OCI Function payload format.

        Allowed values for this property are: "JSON", "AVRO", "JSONBYTES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The payload_format of this OciFunction.
        :rtype: str
        """
        return self._payload_format

    @payload_format.setter
    def payload_format(self, payload_format):
        """
        Sets the payload_format of this OciFunction.
        The OCI Function payload format.


        :param payload_format: The payload_format of this OciFunction.
        :type: str
        """
        allowed_values = ["JSON", "AVRO", "JSONBYTES"]
        if not value_allowed_none_or_none_sentinel(payload_format, allowed_values):
            payload_format = 'UNKNOWN_ENUM_VALUE'
        self._payload_format = payload_format

    @property
    def fn_config_def(self):
        """
        Gets the fn_config_def of this OciFunction.

        :return: The fn_config_def of this OciFunction.
        :rtype: oci.data_integration.models.FunctionConfigurationDefinition
        """
        return self._fn_config_def

    @fn_config_def.setter
    def fn_config_def(self, fn_config_def):
        """
        Sets the fn_config_def of this OciFunction.

        :param fn_config_def: The fn_config_def of this OciFunction.
        :type: oci.data_integration.models.FunctionConfigurationDefinition
        """
        self._fn_config_def = fn_config_def

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
