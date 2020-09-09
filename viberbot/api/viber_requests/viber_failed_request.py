import warnings
from future.utils import python_2_unicode_compatible

from ..event_type import EventType
from .viber_request import ViberRequest


class ViberFailedRequest(ViberRequest):
    """
    Class for ViberRequest with event_type = "failed".
    https://developers.viber.com/docs/api/rest-bot-api/#failed-callback
    """

    def __init__(self):
        super(ViberFailedRequest, self).__init__(EventType.FAILED)
        self._user_id = None
        self._desc = None

    def from_dict(self, request_dict):
        super(ViberFailedRequest, self).from_dict(request_dict)
        self._user_id = request_dict['user_id']
        self._desc = request_dict['desc']
        return self

    @property
    def meesage_token(self):  # TODO: remove this property in the next major release
        warnings.warn('Property `meesage_token` had typo and now is deprecated, please use `message_token` instead')
        return self._message_token

    @property
    def user_id(self):
        """Unique Viber user id"""
        return self._user_id

    @property
    def desc(self):
        """A string describing the failure"""
        return self._desc

    @python_2_unicode_compatible
    def __str__(self):
        return u"ViberFailedRequest [{0}, message_token={1}, user_id={2}, desc={3}]" .format(
            super(ViberFailedRequest, self).__str__(),
            self._message_token,
            self._user_id,
            self._desc
        )
