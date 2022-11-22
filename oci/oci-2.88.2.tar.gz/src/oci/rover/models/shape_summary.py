# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeSummary(object):
    """
    A shape of a node on a Rover device.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param gpu_description:
            The value to assign to the gpu_description property of this ShapeSummary.
        :type gpu_description: str

        :param gpus:
            The value to assign to the gpus property of this ShapeSummary.
        :type gpus: int

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this ShapeSummary.
        :type memory_in_gbs: float

        :param networking_bandwidth_in_gbps:
            The value to assign to the networking_bandwidth_in_gbps property of this ShapeSummary.
        :type networking_bandwidth_in_gbps: float

        :param ocpus:
            The value to assign to the ocpus property of this ShapeSummary.
        :type ocpus: int

        :param processor_description:
            The value to assign to the processor_description property of this ShapeSummary.
        :type processor_description: str

        :param shape:
            The value to assign to the shape property of this ShapeSummary.
        :type shape: str

        :param usb_controller_description:
            The value to assign to the usb_controller_description property of this ShapeSummary.
        :type usb_controller_description: str

        :param number_of_usb_controllers:
            The value to assign to the number_of_usb_controllers property of this ShapeSummary.
        :type number_of_usb_controllers: int

        :param tags:
            The value to assign to the tags property of this ShapeSummary.
        :type tags: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ShapeSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ShapeSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ShapeSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'gpu_description': 'str',
            'gpus': 'int',
            'memory_in_gbs': 'float',
            'networking_bandwidth_in_gbps': 'float',
            'ocpus': 'int',
            'processor_description': 'str',
            'shape': 'str',
            'usb_controller_description': 'str',
            'number_of_usb_controllers': 'int',
            'tags': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'gpu_description': 'gpuDescription',
            'gpus': 'gpus',
            'memory_in_gbs': 'memoryInGBs',
            'networking_bandwidth_in_gbps': 'networkingBandwidthInGbps',
            'ocpus': 'ocpus',
            'processor_description': 'processorDescription',
            'shape': 'shape',
            'usb_controller_description': 'usbControllerDescription',
            'number_of_usb_controllers': 'numberOfUsbControllers',
            'tags': 'tags',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._gpu_description = None
        self._gpus = None
        self._memory_in_gbs = None
        self._networking_bandwidth_in_gbps = None
        self._ocpus = None
        self._processor_description = None
        self._shape = None
        self._usb_controller_description = None
        self._number_of_usb_controllers = None
        self._tags = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def gpu_description(self):
        """
        Gets the gpu_description of this ShapeSummary.
        A short description of the graphics processing unit (GPU) available for this shape.


        :return: The gpu_description of this ShapeSummary.
        :rtype: str
        """
        return self._gpu_description

    @gpu_description.setter
    def gpu_description(self, gpu_description):
        """
        Sets the gpu_description of this ShapeSummary.
        A short description of the graphics processing unit (GPU) available for this shape.


        :param gpu_description: The gpu_description of this ShapeSummary.
        :type: str
        """
        self._gpu_description = gpu_description

    @property
    def gpus(self):
        """
        Gets the gpus of this ShapeSummary.
        The number of GPUs available for this shape.


        :return: The gpus of this ShapeSummary.
        :rtype: int
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """
        Sets the gpus of this ShapeSummary.
        The number of GPUs available for this shape.


        :param gpus: The gpus of this ShapeSummary.
        :type: int
        """
        self._gpus = gpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this ShapeSummary.
        The default amount of memory available for this shape, in gigabytes.


        :return: The memory_in_gbs of this ShapeSummary.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this ShapeSummary.
        The default amount of memory available for this shape, in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this ShapeSummary.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def networking_bandwidth_in_gbps(self):
        """
        Gets the networking_bandwidth_in_gbps of this ShapeSummary.
        The networking bandwidth available for this shape, in gigabits per second.


        :return: The networking_bandwidth_in_gbps of this ShapeSummary.
        :rtype: float
        """
        return self._networking_bandwidth_in_gbps

    @networking_bandwidth_in_gbps.setter
    def networking_bandwidth_in_gbps(self, networking_bandwidth_in_gbps):
        """
        Sets the networking_bandwidth_in_gbps of this ShapeSummary.
        The networking bandwidth available for this shape, in gigabits per second.


        :param networking_bandwidth_in_gbps: The networking_bandwidth_in_gbps of this ShapeSummary.
        :type: float
        """
        self._networking_bandwidth_in_gbps = networking_bandwidth_in_gbps

    @property
    def ocpus(self):
        """
        Gets the ocpus of this ShapeSummary.
        The default number of OCPUs available for this shape.


        :return: The ocpus of this ShapeSummary.
        :rtype: int
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this ShapeSummary.
        The default number of OCPUs available for this shape.


        :param ocpus: The ocpus of this ShapeSummary.
        :type: int
        """
        self._ocpus = ocpus

    @property
    def processor_description(self):
        """
        Gets the processor_description of this ShapeSummary.
        A short description of the shape's processor (CPU).


        :return: The processor_description of this ShapeSummary.
        :rtype: str
        """
        return self._processor_description

    @processor_description.setter
    def processor_description(self, processor_description):
        """
        Sets the processor_description of this ShapeSummary.
        A short description of the shape's processor (CPU).


        :param processor_description: The processor_description of this ShapeSummary.
        :type: str
        """
        self._processor_description = processor_description

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this ShapeSummary.
        The name of the shape.


        :return: The shape of this ShapeSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this ShapeSummary.
        The name of the shape.


        :param shape: The shape of this ShapeSummary.
        :type: str
        """
        self._shape = shape

    @property
    def usb_controller_description(self):
        """
        Gets the usb_controller_description of this ShapeSummary.
        A short description of the USB controller available for this shape.


        :return: The usb_controller_description of this ShapeSummary.
        :rtype: str
        """
        return self._usb_controller_description

    @usb_controller_description.setter
    def usb_controller_description(self, usb_controller_description):
        """
        Sets the usb_controller_description of this ShapeSummary.
        A short description of the USB controller available for this shape.


        :param usb_controller_description: The usb_controller_description of this ShapeSummary.
        :type: str
        """
        self._usb_controller_description = usb_controller_description

    @property
    def number_of_usb_controllers(self):
        """
        Gets the number_of_usb_controllers of this ShapeSummary.
        The number of USB controllers available for this shape.


        :return: The number_of_usb_controllers of this ShapeSummary.
        :rtype: int
        """
        return self._number_of_usb_controllers

    @number_of_usb_controllers.setter
    def number_of_usb_controllers(self, number_of_usb_controllers):
        """
        Sets the number_of_usb_controllers of this ShapeSummary.
        The number of USB controllers available for this shape.


        :param number_of_usb_controllers: The number_of_usb_controllers of this ShapeSummary.
        :type: int
        """
        self._number_of_usb_controllers = number_of_usb_controllers

    @property
    def tags(self):
        """
        Gets the tags of this ShapeSummary.
        The tags associated with tagSlug.


        :return: The tags of this ShapeSummary.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ShapeSummary.
        The tags associated with tagSlug.


        :param tags: The tags of this ShapeSummary.
        :type: str
        """
        self._tags = tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ShapeSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ShapeSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ShapeSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ShapeSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ShapeSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ShapeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ShapeSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ShapeSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ShapeSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ShapeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ShapeSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ShapeSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
