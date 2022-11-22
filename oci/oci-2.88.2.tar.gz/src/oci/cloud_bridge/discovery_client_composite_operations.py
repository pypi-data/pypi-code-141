# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class DiscoveryClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.cloud_bridge.DiscoveryClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new DiscoveryClientCompositeOperations object

        :param DiscoveryClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def create_asset_source_and_wait_for_state(self, create_asset_source_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_bridge.DiscoveryClient.create_asset_source` and waits for the :py:class:`~oci.cloud_bridge.models.WorkRequest`
        to enter the given state(s).

        :param oci.cloud_bridge.models.CreateAssetSourceDetails create_asset_source_details: (required)
            Details for the new asset source.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_bridge.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_bridge.DiscoveryClient.create_asset_source`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_asset_source(create_asset_source_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_discovery_schedule_and_wait_for_state(self, create_discovery_schedule_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_bridge.DiscoveryClient.create_discovery_schedule` and waits for the :py:class:`~oci.cloud_bridge.models.DiscoverySchedule` acted upon
        to enter the given state(s).

        :param oci.cloud_bridge.models.CreateDiscoveryScheduleDetails create_discovery_schedule_details: (required)
            Information about the discovery schedule being created.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_bridge.models.DiscoverySchedule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_bridge.DiscoveryClient.create_discovery_schedule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_discovery_schedule(create_discovery_schedule_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        discovery_schedule_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_discovery_schedule(discovery_schedule_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_asset_source_and_wait_for_state(self, asset_source_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_bridge.DiscoveryClient.delete_asset_source` and waits for the :py:class:`~oci.cloud_bridge.models.WorkRequest`
        to enter the given state(s).

        :param str asset_source_id: (required)
            The `OCID`__ of the asset source.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_bridge.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_bridge.DiscoveryClient.delete_asset_source`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_asset_source(asset_source_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_discovery_schedule_and_wait_for_state(self, discovery_schedule_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_bridge.DiscoveryClient.delete_discovery_schedule` and waits for the :py:class:`~oci.cloud_bridge.models.DiscoverySchedule` acted upon
        to enter the given state(s).

        :param str discovery_schedule_id: (required)
            The `OCID`__ of the discovery schedule.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_bridge.models.DiscoverySchedule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_bridge.DiscoveryClient.delete_discovery_schedule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_discovery_schedule(discovery_schedule_id)
        operation_result = None
        try:
            operation_result = self.client.delete_discovery_schedule(discovery_schedule_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def refresh_asset_source_and_wait_for_state(self, asset_source_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_bridge.DiscoveryClient.refresh_asset_source` and waits for the :py:class:`~oci.cloud_bridge.models.WorkRequest`
        to enter the given state(s).

        :param str asset_source_id: (required)
            The `OCID`__ of the asset source.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_bridge.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_bridge.DiscoveryClient.refresh_asset_source`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.refresh_asset_source(asset_source_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_asset_source_and_wait_for_state(self, asset_source_id, update_asset_source_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_bridge.DiscoveryClient.update_asset_source` and waits for the :py:class:`~oci.cloud_bridge.models.WorkRequest`
        to enter the given state(s).

        :param str asset_source_id: (required)
            The `OCID`__ of the asset source.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.cloud_bridge.models.UpdateAssetSourceDetails update_asset_source_details: (required)
            Asset source information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_bridge.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_bridge.DiscoveryClient.update_asset_source`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_asset_source(asset_source_id, update_asset_source_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_discovery_schedule_and_wait_for_state(self, update_discovery_schedule_details, discovery_schedule_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.cloud_bridge.DiscoveryClient.update_discovery_schedule` and waits for the :py:class:`~oci.cloud_bridge.models.DiscoverySchedule` acted upon
        to enter the given state(s).

        :param oci.cloud_bridge.models.UpdateDiscoveryScheduleDetails update_discovery_schedule_details: (required)
            Discovery schedule information to be updated.

        :param str discovery_schedule_id: (required)
            The `OCID`__ of the discovery schedule.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.cloud_bridge.models.DiscoverySchedule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.cloud_bridge.DiscoveryClient.update_discovery_schedule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_discovery_schedule(update_discovery_schedule_details, discovery_schedule_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        discovery_schedule_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_discovery_schedule(discovery_schedule_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
