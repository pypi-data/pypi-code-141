# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_auto_scale_policy_details import UpdateAutoScalePolicyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMetricBasedHorizontalScalingPolicyDetails(UpdateAutoScalePolicyDetails):
    """
    Update details of a metric based horizontal autoscaling policy.

    In a metric-based autoscaling policy, an autoscaling action is triggered when a performance metric exceeds a threshold.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMetricBasedHorizontalScalingPolicyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.UpdateMetricBasedHorizontalScalingPolicyDetails.policy_type` attribute
        of this class is ``METRIC_BASED_HORIZONTAL_SCALING_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this UpdateMetricBasedHorizontalScalingPolicyDetails.
        :type policy_type: str

        :param scale_out_config:
            The value to assign to the scale_out_config property of this UpdateMetricBasedHorizontalScalingPolicyDetails.
        :type scale_out_config: oci.bds.models.MetricBasedHorizontalScaleOutConfig

        :param scale_in_config:
            The value to assign to the scale_in_config property of this UpdateMetricBasedHorizontalScalingPolicyDetails.
        :type scale_in_config: oci.bds.models.MetricBasedHorizontalScaleInConfig

        """
        self.swagger_types = {
            'policy_type': 'str',
            'scale_out_config': 'MetricBasedHorizontalScaleOutConfig',
            'scale_in_config': 'MetricBasedHorizontalScaleInConfig'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'scale_out_config': 'scaleOutConfig',
            'scale_in_config': 'scaleInConfig'
        }

        self._policy_type = None
        self._scale_out_config = None
        self._scale_in_config = None
        self._policy_type = 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'

    @property
    def scale_out_config(self):
        """
        Gets the scale_out_config of this UpdateMetricBasedHorizontalScalingPolicyDetails.

        :return: The scale_out_config of this UpdateMetricBasedHorizontalScalingPolicyDetails.
        :rtype: oci.bds.models.MetricBasedHorizontalScaleOutConfig
        """
        return self._scale_out_config

    @scale_out_config.setter
    def scale_out_config(self, scale_out_config):
        """
        Sets the scale_out_config of this UpdateMetricBasedHorizontalScalingPolicyDetails.

        :param scale_out_config: The scale_out_config of this UpdateMetricBasedHorizontalScalingPolicyDetails.
        :type: oci.bds.models.MetricBasedHorizontalScaleOutConfig
        """
        self._scale_out_config = scale_out_config

    @property
    def scale_in_config(self):
        """
        Gets the scale_in_config of this UpdateMetricBasedHorizontalScalingPolicyDetails.

        :return: The scale_in_config of this UpdateMetricBasedHorizontalScalingPolicyDetails.
        :rtype: oci.bds.models.MetricBasedHorizontalScaleInConfig
        """
        return self._scale_in_config

    @scale_in_config.setter
    def scale_in_config(self, scale_in_config):
        """
        Sets the scale_in_config of this UpdateMetricBasedHorizontalScalingPolicyDetails.

        :param scale_in_config: The scale_in_config of this UpdateMetricBasedHorizontalScalingPolicyDetails.
        :type: oci.bds.models.MetricBasedHorizontalScaleInConfig
        """
        self._scale_in_config = scale_in_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
