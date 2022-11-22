# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployPipelineStage(object):
    """
    Stage used in the pipeline for an artifact or environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployPipelineStage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_stage_id:
            The value to assign to the deploy_stage_id property of this DeployPipelineStage.
        :type deploy_stage_id: str

        :param display_name:
            The value to assign to the display_name property of this DeployPipelineStage.
        :type display_name: str

        """
        self.swagger_types = {
            'deploy_stage_id': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'deploy_stage_id': 'deployStageId',
            'display_name': 'displayName'
        }

        self._deploy_stage_id = None
        self._display_name = None

    @property
    def deploy_stage_id(self):
        """
        **[Required]** Gets the deploy_stage_id of this DeployPipelineStage.
        The OCID of a stage


        :return: The deploy_stage_id of this DeployPipelineStage.
        :rtype: str
        """
        return self._deploy_stage_id

    @deploy_stage_id.setter
    def deploy_stage_id(self, deploy_stage_id):
        """
        Sets the deploy_stage_id of this DeployPipelineStage.
        The OCID of a stage


        :param deploy_stage_id: The deploy_stage_id of this DeployPipelineStage.
        :type: str
        """
        self._deploy_stage_id = deploy_stage_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DeployPipelineStage.
        Display name of the stage. Avoid entering confidential information.


        :return: The display_name of this DeployPipelineStage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeployPipelineStage.
        Display name of the stage. Avoid entering confidential information.


        :param display_name: The display_name of this DeployPipelineStage.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
