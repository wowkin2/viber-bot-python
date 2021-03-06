from future.utils import python_2_unicode_compatible


class ViberRequest(object):
    """
    Base class for all Requests from Viber.
    """

    def __init__(self, event_type=None):
        self._event_type = event_type
        self._timestamp = None
        self._message_token = None

    def from_dict(self, request_dict):
        self._timestamp = request_dict['timestamp']
        if self._event_type is None:
            self._event_type = request_dict['event']

        if self._message_token is None:
            self._message_token = request_dict['message_token']
        return self

    @property
    def event_type(self):
        """Callback type - which event triggered the callback"""
        return self._event_type

    @property
    def timestamp(self):
        """Time of the event that triggered the callback"""
        return self._timestamp

    @property
    def message_token(self):
        """Unique ID of the message"""
        return self._message_token

    @python_2_unicode_compatible
    def __str__(self):
        return u"event_type={0}, timestamp={1}, message_token={2}".format(
            self._event_type, self._timestamp, self._message_token
        )
