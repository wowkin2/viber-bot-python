from future.utils import python_2_unicode_compatible

from ..event_type import EventType
from ..user_profile import UserProfile
from .viber_request import ViberRequest


class ViberConversationStartedRequest(ViberRequest):
    """
    Class for ViberRequest with event_type = "conversation_started".
    https://developers.viber.com/docs/api/rest-bot-api/#conversation-started
    """

    def __init__(self):
        super(ViberConversationStartedRequest, self).__init__(EventType.CONVERSATION_STARTED)
        self._type = None
        self._context = None
        self._user = None
        self._api_version = None
        self._subscribed = None

    def from_dict(self, request_dict):
        super(ViberConversationStartedRequest, self).from_dict(request_dict)
        self._type = request_dict['type']
        if 'context' in request_dict:
            self._context = request_dict['context']
        self._user = UserProfile().from_dict(request_dict['user'])
        if 'api_version' in request_dict:
            self._api_version = request_dict['api_version']
        if 'subscribed' in request_dict:
            self._subscribed = request_dict['subscribed']
        return self

    @property
    def user(self):
        """UserProfile information (id, name, avatar, country, language, api_version)"""
        return self._user

    @property
    def user_id(self):
        """Shortcut to user.id property"""
        return self._user.id

    @property
    def type(self):
        """
        The specific type of conversation_started event.
        Possible values: "open". Additional types may be added in the future
        """
        return self._type

    @property
    def context(self):
        """
        Any additional parameters added to the deep link used to access the conversation passed as a string.
        See deep link section for additional information:
        https://developers.viber.com/docs/tools/deep-links
        """
        return self._context

    @property
    def api_version(self):
        """Max API version, matching the most updated user's device."""
        return self._api_version

    @property
    def subscribed(self):
        """Indicated whether a user is already subscribed. True if subscribed and False otherwise."""
        return self._subscribed

    @python_2_unicode_compatible
    def __str__(self):
        t = u"ViberConversationStartedRequest [{0}, message_token={1}, type={2}, context{3}, user={4} subscribed={5}]"
        return t.format(
            super(ViberConversationStartedRequest, self).__str__(),
            self._message_token,
            self._type,
            self._context,
            self._user,
            self._subscribed
        )
