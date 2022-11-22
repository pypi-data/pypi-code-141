# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricData(object):
    """
    The set of aggregated data returned for a metric.
    For information about metrics, see `Metrics Overview`__.

    Limits information for returned data follows.

    * Data points: 100,000.
    * Metric streams* within data points: 2,000.
    * Time range returned for 1-day resolution: 90 days.
    * Time range returned for 1-hour resolution: 90 days.
    * Time range returned for 5-minute resolution: 30 days.
    * Time range returned for 1-minute resolution: 7 days.

    *A metric stream is an individual set of aggregated data for a metric with zero or more dimension values.
    Metric streams cannot be aggregated across metric groups.
    A metric group is the combination of a given metric, metric namespace, and tenancy for the purpose of determining limits.
    For more information about metric-related concepts, see `Monitoring Concepts`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MetricsOverview
    __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetricData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this MetricData.
        :type namespace: str

        :param resource_group:
            The value to assign to the resource_group property of this MetricData.
        :type resource_group: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MetricData.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this MetricData.
        :type name: str

        :param dimensions:
            The value to assign to the dimensions property of this MetricData.
        :type dimensions: dict(str, str)

        :param metadata:
            The value to assign to the metadata property of this MetricData.
        :type metadata: dict(str, str)

        :param resolution:
            The value to assign to the resolution property of this MetricData.
        :type resolution: str

        :param aggregated_datapoints:
            The value to assign to the aggregated_datapoints property of this MetricData.
        :type aggregated_datapoints: list[oci.monitoring.models.AggregatedDatapoint]

        """
        self.swagger_types = {
            'namespace': 'str',
            'resource_group': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'dimensions': 'dict(str, str)',
            'metadata': 'dict(str, str)',
            'resolution': 'str',
            'aggregated_datapoints': 'list[AggregatedDatapoint]'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'resource_group': 'resourceGroup',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'dimensions': 'dimensions',
            'metadata': 'metadata',
            'resolution': 'resolution',
            'aggregated_datapoints': 'aggregatedDatapoints'
        }

        self._namespace = None
        self._resource_group = None
        self._compartment_id = None
        self._name = None
        self._dimensions = None
        self._metadata = None
        self._resolution = None
        self._aggregated_datapoints = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this MetricData.
        The reference provided in a metric definition to indicate the source service or
        application that emitted the metric.

        Example: `oci_computeagent`


        :return: The namespace of this MetricData.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this MetricData.
        The reference provided in a metric definition to indicate the source service or
        application that emitted the metric.

        Example: `oci_computeagent`


        :param namespace: The namespace of this MetricData.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group(self):
        """
        Gets the resource_group of this MetricData.
        Resource group provided with the posted metric. A resource group is a custom string that you can match when retrieving custom metrics. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).

        Example: `frontend-fleet`


        :return: The resource_group of this MetricData.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this MetricData.
        Resource group provided with the posted metric. A resource group is a custom string that you can match when retrieving custom metrics. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).

        Example: `frontend-fleet`


        :param resource_group: The resource_group of this MetricData.
        :type: str
        """
        self._resource_group = resource_group

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MetricData.
        The `OCID`__ of the compartment containing the
        resources from which the aggregated data was returned.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MetricData.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MetricData.
        The `OCID`__ of the compartment containing the
        resources from which the aggregated data was returned.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MetricData.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MetricData.
        The name of the metric.

        Example: `CpuUtilization`


        :return: The name of this MetricData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MetricData.
        The name of the metric.

        Example: `CpuUtilization`


        :param name: The name of this MetricData.
        :type: str
        """
        self._name = name

    @property
    def dimensions(self):
        """
        **[Required]** Gets the dimensions of this MetricData.
        Qualifiers provided in the definition of the returned metric.
        Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair.

        Example: `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`


        :return: The dimensions of this MetricData.
        :rtype: dict(str, str)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this MetricData.
        Qualifiers provided in the definition of the returned metric.
        Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair.

        Example: `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`


        :param dimensions: The dimensions of this MetricData.
        :type: dict(str, str)
        """
        self._dimensions = dimensions

    @property
    def metadata(self):
        """
        Gets the metadata of this MetricData.
        The references provided in a metric definition to indicate extra information about the metric.

        Example: `\"unit\": \"bytes\"`


        :return: The metadata of this MetricData.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this MetricData.
        The references provided in a metric definition to indicate extra information about the metric.

        Example: `\"unit\": \"bytes\"`


        :param metadata: The metadata of this MetricData.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def resolution(self):
        """
        Gets the resolution of this MetricData.
        The time between calculated aggregation windows. Use with the query interval to vary the
        frequency at which aggregated data points are returned. For example, use a query interval of
        5 minutes with a resolution of 1 minute to retrieve five-minute aggregations at a one-minute
        frequency. The resolution must be equal or less than the interval in the query. The default
        resolution is 1m (one minute). Supported values: `1m`-`60m`, `1h`-`24h`, `1d`.

        Example: `5m`


        :return: The resolution of this MetricData.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this MetricData.
        The time between calculated aggregation windows. Use with the query interval to vary the
        frequency at which aggregated data points are returned. For example, use a query interval of
        5 minutes with a resolution of 1 minute to retrieve five-minute aggregations at a one-minute
        frequency. The resolution must be equal or less than the interval in the query. The default
        resolution is 1m (one minute). Supported values: `1m`-`60m`, `1h`-`24h`, `1d`.

        Example: `5m`


        :param resolution: The resolution of this MetricData.
        :type: str
        """
        self._resolution = resolution

    @property
    def aggregated_datapoints(self):
        """
        **[Required]** Gets the aggregated_datapoints of this MetricData.
        The list of timestamp-value pairs returned for the specified request. Metric values are rolled up to the start time specified in the request.
        For important limits information related to data points, see MetricData Reference at the top of this page.


        :return: The aggregated_datapoints of this MetricData.
        :rtype: list[oci.monitoring.models.AggregatedDatapoint]
        """
        return self._aggregated_datapoints

    @aggregated_datapoints.setter
    def aggregated_datapoints(self, aggregated_datapoints):
        """
        Sets the aggregated_datapoints of this MetricData.
        The list of timestamp-value pairs returned for the specified request. Metric values are rolled up to the start time specified in the request.
        For important limits information related to data points, see MetricData Reference at the top of this page.


        :param aggregated_datapoints: The aggregated_datapoints of this MetricData.
        :type: list[oci.monitoring.models.AggregatedDatapoint]
        """
        self._aggregated_datapoints = aggregated_datapoints

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
