from ..event_type import EventType

from .viber_conversation_started_request import ViberConversationStartedRequest
from .viber_delivered_request import ViberDeliveredRequest
from .viber_failed_request import ViberFailedRequest
from .viber_message_request import ViberMessageRequest
from .viber_request import ViberRequest
from .viber_seen_request import ViberSeenRequest
from .viber_subscribed_request import ViberSubscribedRequest
from .viber_unsubscribed_request import ViberUnsubscribedRequest


EVENT_TYPE_TO_CLASS = {
    EventType.MESSAGE: ViberMessageRequest,
    EventType.FAILED: ViberFailedRequest,
    EventType.CONVERSATION_STARTED: ViberConversationStartedRequest,
    EventType.DELIVERED: ViberDeliveredRequest,
    EventType.SEEN: ViberSeenRequest,
    EventType.SUBSCRIBED: ViberSubscribedRequest,
    EventType.UNSUBSCRIBED: ViberUnsubscribedRequest,
    EventType.WEBHOOK: ViberRequest,
}

__all__ = [
    'ViberConversationStartedRequest', 'ViberDeliveredRequest', 'ViberFailedRequest', 'ViberMessageRequest',
    'ViberSeenRequest', 'ViberSubscribedRequest', 'ViberUnsubscribedRequest', 'EVENT_TYPE_TO_CLASS'
]
