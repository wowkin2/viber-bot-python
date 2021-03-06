import hashlib
import hmac
import json
import logging

from .api_request_sender import ApiRequestSender
from .consts import VIBER_BOT_API_URL, VIBER_BOT_USER_AGENT
from .message_sender import MessageSender
from .viber_requests import EVENT_TYPE_TO_CLASS


class Api(object):
    def __init__(self, bot_configuration):
        self._logger = logging.getLogger('viber.bot.api')
        self._bot_configuration = bot_configuration
        self._request_sender = ApiRequestSender(
            self._logger, VIBER_BOT_API_URL, bot_configuration, VIBER_BOT_USER_AGENT
        )
        self._message_sender = MessageSender(self._logger, self._request_sender, bot_configuration)

    @property
    def name(self):
        return self._bot_configuration.name

    @property
    def avatar(self):
        return self._bot_configuration.avatar

    def set_webhook(self, url, webhook_events=None, is_inline=False):
        self._logger.debug(u"setting webhook to url: %s", url)
        return self._request_sender.set_webhook(url, webhook_events, is_inline)

    def unset_webhook(self):
        self._logger.debug("unsetting webhook")
        return self._request_sender.set_webhook('')

    def get_online(self, ids):
        return self._request_sender.get_online_status(ids)

    def get_user_details(self, user_id):
        return self._request_sender.get_user_details(user_id)

    def get_account_info(self):
        self._logger.debug("requesting account info")
        account_info = self._request_sender.get_account_info()
        self._logger.debug(u"received account info: %s", account_info)
        return account_info

    def verify_signature(self, request_data, signature):
        return signature == self._calculate_message_signature(request_data)

    @staticmethod
    def create_request(request_dict):
        if 'event' not in request_dict:
            raise Exception("request is missing field 'event'")

        if request_dict['event'] not in EVENT_TYPE_TO_CLASS:
            raise Exception("event type '{0}' is not supported".format(request_dict['event']))

        return EVENT_TYPE_TO_CLASS[request_dict['event']]().from_dict(request_dict)

    def parse_request(self, request_data):
        self._logger.debug("parsing request")
        request_dict = json.loads(request_data.decode() if isinstance(request_data, bytes) else request_data)
        request = self.create_request(request_dict)
        self._logger.debug(u"parsed request=%s", request)
        return request

    def send_messages(self, to, messages, chat_id=None):
        """
        :param to: Viber user id
        :param messages: list of Message objects to be sent
        :param chat_id: Optional. String. Indicates that this is a message sent in inline conversation.
        :return: list of tokens of the sent messages
        """
        self._logger.debug("going to send messages: %s, to: %s", messages, to)
        if not isinstance(messages, list):
            messages = [messages]

        sent_messages_tokens = []

        for message in messages:
            token = self._message_sender.send_message(
                to, self._bot_configuration.name, self._bot_configuration.avatar, message, chat_id
            )
            sent_messages_tokens.append(token)

        return sent_messages_tokens

    def post_messages_to_public_account(self, sender, messages):
        if not isinstance(messages, list):
            messages = [messages]

        sent_messages_tokens = []

        for message in messages:
            token = self._message_sender.post_to_public_account(
                sender, self._bot_configuration.name, self._bot_configuration.avatar, message
            )
            sent_messages_tokens.append(token)

        return sent_messages_tokens

    def _calculate_message_signature(self, message):
        return hmac.new(
            bytes(self._bot_configuration.auth_token.encode('ascii')),
            msg=message,
            digestmod=hashlib.sha256
        ).hexdigest()
