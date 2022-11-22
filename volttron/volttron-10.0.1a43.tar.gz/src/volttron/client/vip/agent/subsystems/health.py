# -*- coding: utf-8 -*- {{{
# vim: set fenc=utf-8 ft=python sw=4 ts=4 sts=4 et:
#
# Copyright 2020, Battelle Memorial Institute.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This material was prepared as an account of work sponsored by an agency of
# the United States Government. Neither the United States Government nor the
# United States Department of Energy, nor Battelle, nor any of their
# employees, nor any jurisdiction or organization that has cooperated in the
# development of these materials, makes any warranty, express or
# implied, or assumes any legal liability or responsibility for the accuracy,
# completeness, or usefulness or any information, apparatus, product,
# software, or process disclosed, or represents that its use would not infringe
# privately owned rights. Reference herein to any specific commercial product,
# process, or service by trade name, trademark, manufacturer, or otherwise
# does not necessarily constitute or imply its endorsement, recommendation, or
# favoring by the United States Government or any agency thereof, or
# Battelle Memorial Institute. The views and opinions of authors expressed
# herein do not necessarily state or reflect those of the
# United States Government or any agency thereof.
#
# PACIFIC NORTHWEST NATIONAL LABORATORY operated by
# BATTELLE for the UNITED STATES DEPARTMENT OF ENERGY
# under Contract DE-AC05-76RL01830
# }}}

import weakref

from volttron.client.messaging import topics
from volttron.client.messaging.headers import DATE
from volttron.client.messaging.health import *
from volttron.client.vip.agent.subsystems.base import SubsystemBase
from volttron.utils.context import ClientContext as cc
"""
The health subsystem allows an agent to store it's health in a non-intrusive
way.
"""

__docformat__ = "reStructuredText"
__version__ = "1.1"

_log = logging.getLogger(__name__)


class Health(SubsystemBase):

    def __init__(self, owner, core, rpc):
        self._owner = owner
        self._core = weakref.ref(core)
        self._rpc = weakref.ref(rpc)
        self._statusobj = Status.build(STATUS_GOOD, status_changed_callback=self._status_changed)
        self._status_callbacks = set()

        def onsetup(sender, **kwargs):
            rpc.export(self.set_status, "health.set_status")
            rpc.export(self.get_status, "health.get_status")
            rpc.export(self.get_status, "health.get_status_json")
            rpc.export(self.send_alert, "health.send_alert")

        core.onsetup.connect(onsetup, self)

    def send_alert(self, alert_key: str, statusobj: Status):
        """
        An alert_key is a quasi-unique key.  A listener to the alert can
        determine whether to pass the alert on to a higher level based upon
        the frequency of this alert.

        :param statusobj: The status for the alert.
        :param alert_key:
        :return:
        """
        if not isinstance(statusobj, Status):
            raise ValueError("statusobj must be a Status object.")
        agent_class = self._owner.__class__.__name__
        fq_identity = cc.get_fq_identity(self._core().identity)
        # RMQ and other message buses can't handle '.' because it's used as the separator.  This
        # causes us to change the alert topic's agent_identity to have '_' rather than '.'.
        topic = topics.ALERTS(agent_class=agent_class,
                              agent_identity=fq_identity.replace(".", "_"))
        headers = dict(alert_key=alert_key)

        self._owner.vip.pubsub.publish("pubsub",
                                       topic=topic.format(),
                                       headers=headers,
                                       message=statusobj.as_json()).get(timeout=10)

    def add_status_callback(self, fn):
        """
        Add callbacks to the passed function.  The function must have the
        following interface

        .. code::python

            def status_callback(status, context):

        :param fn: The method to be executed when status is changed.
        :param fn: callable
        """
        self._status_callbacks.add(fn)

    def _status_changed(self):
        """Internal function that happens when the status changes state.
        :return:
        """
        remove = set()
        for fn in self._status_callbacks:
            try:
                fn(self._statusobj.status, self._statusobj.context)
            except NameError:
                remove.add(fn)
        # Removes the items that are in remove from the callbacks.
        self._status_callbacks.difference_update(remove)

        self._owner.vip.heartbeat.restart()

    def set_status(self, status, context=None):
        """RPC method

        Updates the agents status to the new value with the specified context.

        :param: status: str: GODD, BAD
        :param: context: str: A serializable that denotes the context of
        status.
        """
        self._statusobj.update_status(status, context)

    def get_status(self):
        """ "RPC method

        Returns the last updated status from the object with the context.

        The minimum output from the status would be:

            {
                "status": "GOOD",
                "context": None,
                "utc_last_update": "2016-03-31T15:40:32.685138+0000"
            }

        """
        return self._statusobj.as_dict()    # .as_json()

    # TODO fetch status value from status object
    def get_status_value(self):
        return self._statusobj.status

    def get_status_json(self):
        """ "RPC method

        Returns the last updated status from the object with the context.

        The minimum output from the status would be:

            {
                "status": "GOOD",
                "context": None,
                "utc_last_update": "2016-03-31T15:40:32.685138+0000"
            }

        """
        return self._statusobj.as_json()

    # TODO define publish for health messaging
    # TODO fix topic
    # TODO fix self.core
    def publish(self):
        topic = "heartbeat/" + self.core().identity
        headers = {DATE: format_timestamp(get_aware_utc_now())}
        message = self.get_status()

        self.pubsub().publish("pubsub", topic, headers, message)
