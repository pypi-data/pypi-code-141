# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetSqlWarehouseResult',
    'AwaitableGetSqlWarehouseResult',
    'get_sql_warehouse',
    'get_sql_warehouse_output',
]

@pulumi.output_type
class GetSqlWarehouseResult:
    """
    A collection of values returned by getSqlWarehouse.
    """
    def __init__(__self__, auto_stop_mins=None, channel=None, cluster_size=None, data_source_id=None, enable_photon=None, enable_serverless_compute=None, id=None, instance_profile_arn=None, jdbc_url=None, max_num_clusters=None, min_num_clusters=None, name=None, num_clusters=None, odbc_params=None, spot_instance_policy=None, state=None, tags=None):
        if auto_stop_mins and not isinstance(auto_stop_mins, int):
            raise TypeError("Expected argument 'auto_stop_mins' to be a int")
        pulumi.set(__self__, "auto_stop_mins", auto_stop_mins)
        if channel and not isinstance(channel, dict):
            raise TypeError("Expected argument 'channel' to be a dict")
        pulumi.set(__self__, "channel", channel)
        if cluster_size and not isinstance(cluster_size, str):
            raise TypeError("Expected argument 'cluster_size' to be a str")
        pulumi.set(__self__, "cluster_size", cluster_size)
        if data_source_id and not isinstance(data_source_id, str):
            raise TypeError("Expected argument 'data_source_id' to be a str")
        pulumi.set(__self__, "data_source_id", data_source_id)
        if enable_photon and not isinstance(enable_photon, bool):
            raise TypeError("Expected argument 'enable_photon' to be a bool")
        pulumi.set(__self__, "enable_photon", enable_photon)
        if enable_serverless_compute and not isinstance(enable_serverless_compute, bool):
            raise TypeError("Expected argument 'enable_serverless_compute' to be a bool")
        pulumi.set(__self__, "enable_serverless_compute", enable_serverless_compute)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_profile_arn and not isinstance(instance_profile_arn, str):
            raise TypeError("Expected argument 'instance_profile_arn' to be a str")
        pulumi.set(__self__, "instance_profile_arn", instance_profile_arn)
        if jdbc_url and not isinstance(jdbc_url, str):
            raise TypeError("Expected argument 'jdbc_url' to be a str")
        pulumi.set(__self__, "jdbc_url", jdbc_url)
        if max_num_clusters and not isinstance(max_num_clusters, int):
            raise TypeError("Expected argument 'max_num_clusters' to be a int")
        pulumi.set(__self__, "max_num_clusters", max_num_clusters)
        if min_num_clusters and not isinstance(min_num_clusters, int):
            raise TypeError("Expected argument 'min_num_clusters' to be a int")
        pulumi.set(__self__, "min_num_clusters", min_num_clusters)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if num_clusters and not isinstance(num_clusters, int):
            raise TypeError("Expected argument 'num_clusters' to be a int")
        pulumi.set(__self__, "num_clusters", num_clusters)
        if odbc_params and not isinstance(odbc_params, dict):
            raise TypeError("Expected argument 'odbc_params' to be a dict")
        pulumi.set(__self__, "odbc_params", odbc_params)
        if spot_instance_policy and not isinstance(spot_instance_policy, str):
            raise TypeError("Expected argument 'spot_instance_policy' to be a str")
        pulumi.set(__self__, "spot_instance_policy", spot_instance_policy)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="autoStopMins")
    def auto_stop_mins(self) -> int:
        """
        Time in minutes until an idle SQL warehouse terminates all clusters and stops.
        """
        return pulumi.get(self, "auto_stop_mins")

    @property
    @pulumi.getter
    def channel(self) -> 'outputs.GetSqlWarehouseChannelResult':
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter(name="clusterSize")
    def cluster_size(self) -> str:
        """
        The size of the clusters allocated to the warehouse: "2X-Small", "X-Small", "Small", "Medium", "Large", "X-Large", "2X-Large", "3X-Large", "4X-Large".
        """
        return pulumi.get(self, "cluster_size")

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> str:
        """
        ID of the data source for this warehouse. This is used to bind an Databricks SQL query to an warehouse.
        """
        return pulumi.get(self, "data_source_id")

    @property
    @pulumi.getter(name="enablePhoton")
    def enable_photon(self) -> bool:
        """
        Whether to enable [Photon](https://databricks.com/product/delta-engine).
        """
        return pulumi.get(self, "enable_photon")

    @property
    @pulumi.getter(name="enableServerlessCompute")
    def enable_serverless_compute(self) -> bool:
        """
        Whether this SQL warehouse is a Serverless warehouse. To use a Serverless SQL warehouse, you must enable Serverless SQL warehouses for the workspace.
        * `channel` block, consisting of following fields:
        """
        return pulumi.get(self, "enable_serverless_compute")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceProfileArn")
    def instance_profile_arn(self) -> str:
        return pulumi.get(self, "instance_profile_arn")

    @property
    @pulumi.getter(name="jdbcUrl")
    def jdbc_url(self) -> str:
        """
        JDBC connection string.
        """
        return pulumi.get(self, "jdbc_url")

    @property
    @pulumi.getter(name="maxNumClusters")
    def max_num_clusters(self) -> int:
        """
        Maximum number of clusters available when a SQL warehouse is running.
        """
        return pulumi.get(self, "max_num_clusters")

    @property
    @pulumi.getter(name="minNumClusters")
    def min_num_clusters(self) -> int:
        """
        Minimum number of clusters available when a SQL warehouse is running.
        """
        return pulumi.get(self, "min_num_clusters")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Databricks SQL release channel. Possible values are: `CHANNEL_NAME_PREVIEW` and `CHANNEL_NAME_CURRENT`. Default is `CHANNEL_NAME_CURRENT`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numClusters")
    def num_clusters(self) -> int:
        return pulumi.get(self, "num_clusters")

    @property
    @pulumi.getter(name="odbcParams")
    def odbc_params(self) -> 'outputs.GetSqlWarehouseOdbcParamsResult':
        """
        ODBC connection params: `odbc_params.hostname`, `odbc_params.path`, `odbc_params.protocol`, and `odbc_params.port`.
        """
        return pulumi.get(self, "odbc_params")

    @property
    @pulumi.getter(name="spotInstancePolicy")
    def spot_instance_policy(self) -> str:
        """
        The spot policy to use for allocating instances to clusters: `COST_OPTIMIZED` or `RELIABILITY_OPTIMIZED`.
        """
        return pulumi.get(self, "spot_instance_policy")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> 'outputs.GetSqlWarehouseTagsResult':
        """
        Databricks tags all warehouse resources with these tags.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSqlWarehouseResult(GetSqlWarehouseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlWarehouseResult(
            auto_stop_mins=self.auto_stop_mins,
            channel=self.channel,
            cluster_size=self.cluster_size,
            data_source_id=self.data_source_id,
            enable_photon=self.enable_photon,
            enable_serverless_compute=self.enable_serverless_compute,
            id=self.id,
            instance_profile_arn=self.instance_profile_arn,
            jdbc_url=self.jdbc_url,
            max_num_clusters=self.max_num_clusters,
            min_num_clusters=self.min_num_clusters,
            name=self.name,
            num_clusters=self.num_clusters,
            odbc_params=self.odbc_params,
            spot_instance_policy=self.spot_instance_policy,
            state=self.state,
            tags=self.tags)


def get_sql_warehouse(auto_stop_mins: Optional[int] = None,
                      channel: Optional[pulumi.InputType['GetSqlWarehouseChannelArgs']] = None,
                      cluster_size: Optional[str] = None,
                      data_source_id: Optional[str] = None,
                      enable_photon: Optional[bool] = None,
                      enable_serverless_compute: Optional[bool] = None,
                      id: Optional[str] = None,
                      instance_profile_arn: Optional[str] = None,
                      jdbc_url: Optional[str] = None,
                      max_num_clusters: Optional[int] = None,
                      min_num_clusters: Optional[int] = None,
                      name: Optional[str] = None,
                      num_clusters: Optional[int] = None,
                      odbc_params: Optional[pulumi.InputType['GetSqlWarehouseOdbcParamsArgs']] = None,
                      spot_instance_policy: Optional[str] = None,
                      state: Optional[str] = None,
                      tags: Optional[pulumi.InputType['GetSqlWarehouseTagsArgs']] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlWarehouseResult:
    """
    ## Example Usage

    Retrieve attributes of each SQL warehouses in a workspace

    ```python
    import pulumi
    import pulumi_databricks as databricks

    all_sql_warehouses = databricks.get_sql_warehouses()
    all_sql_warehouse = [databricks.get_sql_warehouse(id=__value) for __key, __value in data["databricks_sql"]["warehouses"]["ids"]]
    ```
    ## Related Resources

    The following resources are often used in the same context:

    * End to end workspace management guide.
    * InstanceProfile to manage AWS EC2 instance profiles that users can launch Cluster and access data, like databricks_mount.
    * SqlDashboard to manage Databricks SQL [Dashboards](https://docs.databricks.com/sql/user/dashboards/index.html).
    * SqlGlobalConfig to configure the security policy, databricks_instance_profile, and [data access properties](https://docs.databricks.com/sql/admin/data-access-configuration.html) for all get_sql_warehouse of workspace.
    * SqlPermissions to manage data object access control lists in Databricks workspaces for things like tables, views, databases, and [more](https://docs.databricks.com/security/access-control/table-acls/object-privileges.html).


    :param int auto_stop_mins: Time in minutes until an idle SQL warehouse terminates all clusters and stops.
    :param str cluster_size: The size of the clusters allocated to the warehouse: "2X-Small", "X-Small", "Small", "Medium", "Large", "X-Large", "2X-Large", "3X-Large", "4X-Large".
    :param str data_source_id: ID of the data source for this warehouse. This is used to bind an Databricks SQL query to an warehouse.
    :param bool enable_photon: Whether to enable [Photon](https://databricks.com/product/delta-engine).
    :param bool enable_serverless_compute: Whether this SQL warehouse is a Serverless warehouse. To use a Serverless SQL warehouse, you must enable Serverless SQL warehouses for the workspace.
           * `channel` block, consisting of following fields:
    :param str id: The id of the SQL warehouse
    :param str jdbc_url: JDBC connection string.
    :param int max_num_clusters: Maximum number of clusters available when a SQL warehouse is running.
    :param int min_num_clusters: Minimum number of clusters available when a SQL warehouse is running.
    :param str name: Name of the Databricks SQL release channel. Possible values are: `CHANNEL_NAME_PREVIEW` and `CHANNEL_NAME_CURRENT`. Default is `CHANNEL_NAME_CURRENT`.
    :param pulumi.InputType['GetSqlWarehouseOdbcParamsArgs'] odbc_params: ODBC connection params: `odbc_params.hostname`, `odbc_params.path`, `odbc_params.protocol`, and `odbc_params.port`.
    :param str spot_instance_policy: The spot policy to use for allocating instances to clusters: `COST_OPTIMIZED` or `RELIABILITY_OPTIMIZED`.
    :param pulumi.InputType['GetSqlWarehouseTagsArgs'] tags: Databricks tags all warehouse resources with these tags.
    """
    __args__ = dict()
    __args__['autoStopMins'] = auto_stop_mins
    __args__['channel'] = channel
    __args__['clusterSize'] = cluster_size
    __args__['dataSourceId'] = data_source_id
    __args__['enablePhoton'] = enable_photon
    __args__['enableServerlessCompute'] = enable_serverless_compute
    __args__['id'] = id
    __args__['instanceProfileArn'] = instance_profile_arn
    __args__['jdbcUrl'] = jdbc_url
    __args__['maxNumClusters'] = max_num_clusters
    __args__['minNumClusters'] = min_num_clusters
    __args__['name'] = name
    __args__['numClusters'] = num_clusters
    __args__['odbcParams'] = odbc_params
    __args__['spotInstancePolicy'] = spot_instance_policy
    __args__['state'] = state
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('databricks:index/getSqlWarehouse:getSqlWarehouse', __args__, opts=opts, typ=GetSqlWarehouseResult).value

    return AwaitableGetSqlWarehouseResult(
        auto_stop_mins=__ret__.auto_stop_mins,
        channel=__ret__.channel,
        cluster_size=__ret__.cluster_size,
        data_source_id=__ret__.data_source_id,
        enable_photon=__ret__.enable_photon,
        enable_serverless_compute=__ret__.enable_serverless_compute,
        id=__ret__.id,
        instance_profile_arn=__ret__.instance_profile_arn,
        jdbc_url=__ret__.jdbc_url,
        max_num_clusters=__ret__.max_num_clusters,
        min_num_clusters=__ret__.min_num_clusters,
        name=__ret__.name,
        num_clusters=__ret__.num_clusters,
        odbc_params=__ret__.odbc_params,
        spot_instance_policy=__ret__.spot_instance_policy,
        state=__ret__.state,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_sql_warehouse)
def get_sql_warehouse_output(auto_stop_mins: Optional[pulumi.Input[Optional[int]]] = None,
                             channel: Optional[pulumi.Input[Optional[pulumi.InputType['GetSqlWarehouseChannelArgs']]]] = None,
                             cluster_size: Optional[pulumi.Input[Optional[str]]] = None,
                             data_source_id: Optional[pulumi.Input[Optional[str]]] = None,
                             enable_photon: Optional[pulumi.Input[Optional[bool]]] = None,
                             enable_serverless_compute: Optional[pulumi.Input[Optional[bool]]] = None,
                             id: Optional[pulumi.Input[str]] = None,
                             instance_profile_arn: Optional[pulumi.Input[Optional[str]]] = None,
                             jdbc_url: Optional[pulumi.Input[Optional[str]]] = None,
                             max_num_clusters: Optional[pulumi.Input[Optional[int]]] = None,
                             min_num_clusters: Optional[pulumi.Input[Optional[int]]] = None,
                             name: Optional[pulumi.Input[Optional[str]]] = None,
                             num_clusters: Optional[pulumi.Input[Optional[int]]] = None,
                             odbc_params: Optional[pulumi.Input[Optional[pulumi.InputType['GetSqlWarehouseOdbcParamsArgs']]]] = None,
                             spot_instance_policy: Optional[pulumi.Input[Optional[str]]] = None,
                             state: Optional[pulumi.Input[Optional[str]]] = None,
                             tags: Optional[pulumi.Input[Optional[pulumi.InputType['GetSqlWarehouseTagsArgs']]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlWarehouseResult]:
    """
    ## Example Usage

    Retrieve attributes of each SQL warehouses in a workspace

    ```python
    import pulumi
    import pulumi_databricks as databricks

    all_sql_warehouses = databricks.get_sql_warehouses()
    all_sql_warehouse = [databricks.get_sql_warehouse(id=__value) for __key, __value in data["databricks_sql"]["warehouses"]["ids"]]
    ```
    ## Related Resources

    The following resources are often used in the same context:

    * End to end workspace management guide.
    * InstanceProfile to manage AWS EC2 instance profiles that users can launch Cluster and access data, like databricks_mount.
    * SqlDashboard to manage Databricks SQL [Dashboards](https://docs.databricks.com/sql/user/dashboards/index.html).
    * SqlGlobalConfig to configure the security policy, databricks_instance_profile, and [data access properties](https://docs.databricks.com/sql/admin/data-access-configuration.html) for all get_sql_warehouse of workspace.
    * SqlPermissions to manage data object access control lists in Databricks workspaces for things like tables, views, databases, and [more](https://docs.databricks.com/security/access-control/table-acls/object-privileges.html).


    :param int auto_stop_mins: Time in minutes until an idle SQL warehouse terminates all clusters and stops.
    :param str cluster_size: The size of the clusters allocated to the warehouse: "2X-Small", "X-Small", "Small", "Medium", "Large", "X-Large", "2X-Large", "3X-Large", "4X-Large".
    :param str data_source_id: ID of the data source for this warehouse. This is used to bind an Databricks SQL query to an warehouse.
    :param bool enable_photon: Whether to enable [Photon](https://databricks.com/product/delta-engine).
    :param bool enable_serverless_compute: Whether this SQL warehouse is a Serverless warehouse. To use a Serverless SQL warehouse, you must enable Serverless SQL warehouses for the workspace.
           * `channel` block, consisting of following fields:
    :param str id: The id of the SQL warehouse
    :param str jdbc_url: JDBC connection string.
    :param int max_num_clusters: Maximum number of clusters available when a SQL warehouse is running.
    :param int min_num_clusters: Minimum number of clusters available when a SQL warehouse is running.
    :param str name: Name of the Databricks SQL release channel. Possible values are: `CHANNEL_NAME_PREVIEW` and `CHANNEL_NAME_CURRENT`. Default is `CHANNEL_NAME_CURRENT`.
    :param pulumi.InputType['GetSqlWarehouseOdbcParamsArgs'] odbc_params: ODBC connection params: `odbc_params.hostname`, `odbc_params.path`, `odbc_params.protocol`, and `odbc_params.port`.
    :param str spot_instance_policy: The spot policy to use for allocating instances to clusters: `COST_OPTIMIZED` or `RELIABILITY_OPTIMIZED`.
    :param pulumi.InputType['GetSqlWarehouseTagsArgs'] tags: Databricks tags all warehouse resources with these tags.
    """
    ...
