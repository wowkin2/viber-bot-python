from future.utils import python_2_unicode_compatible

from ...api.event_type import EventType

from .viber_request import ViberRequest


class ViberUnsubscribedRequest(ViberRequest):
    """
    Class for ViberRequest with event_type = "unsubscribed".
    https://developers.viber.com/docs/api/rest-bot-api/#unsubscribed
    """

    def __init__(self):
        super(ViberUnsubscribedRequest, self).__init__(EventType.UNSUBSCRIBED)
        self._user_id = None

    def from_dict(self, request_dict):
        super(ViberUnsubscribedRequest, self).from_dict(request_dict)
        self._user_id = request_dict['user_id']
        return self

    @property
    def user_id(self):
        return self._user_id

    @python_2_unicode_compatible
    def __str__(self):
        return u"ViberUnsubscribedRequest [{0}, user_id={1}]".format(
            super(ViberUnsubscribedRequest, self).__str__(),
            self._user_id
        )
