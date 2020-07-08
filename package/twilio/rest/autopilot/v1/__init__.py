# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.autopilot.v1.assistant import AssistantList
from twilio.rest.autopilot.v1.restore_assistant import RestoreAssistantList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Autopilot

        :returns: V1 version of Autopilot
        :rtype: twilio.rest.autopilot.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._assistants = None
        self._restore_assistant = None

    @property
    def assistants(self):
        """
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantList
        """
        if self._assistants is None:
            self._assistants = AssistantList(self)
        return self._assistants

    @property
    def restore_assistant(self):
        """
        :rtype: twilio.rest.autopilot.v1.restore_assistant.RestoreAssistantList
        """
        if self._restore_assistant is None:
            self._restore_assistant = RestoreAssistantList(self)
        return self._restore_assistant

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1>'
