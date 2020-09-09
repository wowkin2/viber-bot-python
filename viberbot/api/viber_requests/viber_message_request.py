from future.utils import python_2_unicode_compatible

from ...api import messages
from ...api.event_type import EventType
from ...api.user_profile import UserProfile

from .viber_request import ViberRequest


class ViberMessageRequest(ViberRequest):
    """
    Class for ViberRequest with event_type = "message".
    https://developers.viber.com/docs/api/rest-bot-api/#receive-message-from-user
    """
    def __init__(self):
        super(ViberMessageRequest, self).__init__(EventType.MESSAGE)
        self._message = None
        self._sender = None
        self._chat_id = None
        self._reply_type = None
        self._silent = None

    def from_dict(self, request_dict):
        super(ViberMessageRequest, self).from_dict(request_dict)
        self._message = messages.get_message(request_dict['message'])
        self._sender = UserProfile().from_dict(request_dict['sender'])
        self._silent = request_dict.get('silent', None)
        self._reply_type = request_dict.get('reply_type', None)
        self._chat_id = request_dict.get('chat_id', None)
        return self

    @property
    def message(self):
        return self._message

    @property
    def sender(self):
        """Unique Viber user id of the message sender"""
        return self._sender

    @property
    def user(self):
        """Shortcut/alias to 'sender' property, to make all user attributes unified."""
        return self.sender

    @property
    def user_id(self):
        """Shortcut to user.id property"""
        return self.sender.id

    @property
    def chat_id(self):  # No documentation about this field
        return self._chat_id

    @property
    def reply_type(self):  # No documentation about this field
        return self._reply_type

    @property
    def silent(self):
        return self._silent

    @python_2_unicode_compatible
    def __str__(self):
        t = u"ViberMessageRequest [" \
            u"{0}, message_token={1}, sender={2}, message={3}, chat_id={4}, reply_type={5}, silent={6}]"
        return t.format(
            super(ViberMessageRequest, self).__str__(),
            self._message_token,
            self._sender,
            self._message,
            self._chat_id,
            self._reply_type,
            self._silent
        )
