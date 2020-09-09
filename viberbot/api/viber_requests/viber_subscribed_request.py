from future.utils import python_2_unicode_compatible

from ...api.event_type import EventType
from ...api.user_profile import UserProfile

from .viber_request import ViberRequest


class ViberSubscribedRequest(ViberRequest):
    """
    Class for ViberRequest with event_type = "subscribed".
    https://developers.viber.com/docs/api/rest-bot-api/#subscribed
    """
    def __init__(self):
        super(ViberSubscribedRequest, self).__init__(EventType.SUBSCRIBED)
        self._user = None
        self._api_version = None

    def from_dict(self, request_dict):
        super(ViberSubscribedRequest, self).from_dict(request_dict)
        self._user = UserProfile().from_dict(request_dict['user'])
        if 'api_version' in request_dict:
            self._api_version = request_dict['api_version']
        return self

    @property
    def user(self):
        return self._user

    @property
    def user_id(self):
        """Shortcut to user.id property"""
        return self._user.id

    @property
    def api_version(self):
        return self._api_version

    @python_2_unicode_compatible
    def __str__(self):
        return u"ViberSubscribedRequest [{0}, user={1}]".format(
            super(ViberSubscribedRequest, self).__str__(),
            self._user
        )
