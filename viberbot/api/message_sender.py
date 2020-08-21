import json

from .consts import BotApiEndpoint


class MessageSender(object):
    def __init__(self, logger, request_sender, bot_configuration):
        self._logger = logger
        self._request_sender = request_sender
        self._bot_configuration = bot_configuration

    def send_message(self, to, sender_name, sender_avatar, message, chat_id=None):
        if not message.validate():
            self._logger.error(u"failed validating message: %s", message)
            raise Exception("failed validating message: {0}".format(message))

        payload = self._prepare_payload(
            message=message,
            receiver=to,
            sender_name=sender_name,
            sender_avatar=sender_avatar,
            chat_id=chat_id
        )

        self._logger.debug(u"going to send message: %s", payload)

        return self._post_request(BotApiEndpoint.SEND_MESSAGE, payload)

    def post_to_public_account(self, sender, sender_name, sender_avatar, message):
        if not message.validate():
            self._logger.error(u"failed validating message: %s", message)
            raise Exception("failed validating message: {0}".format(message))

        if sender is None:
            raise Exception(u"missing parameter sender")

        payload = self._prepare_payload(
            message=message,
            sender=sender,
            sender_name=sender_name,
            sender_avatar=sender_avatar
        )

        self._logger.debug(u"going to send message: %s", payload)

        return self._post_request(BotApiEndpoint.POST, payload)

    def _post_request(self, endpoint, payload):
        result = self._request_sender.post_request(
            endpoint, json.dumps(payload))

        if not result['status'] == 0:
            raise Exception(u"failed with status: %s, message: %s", result['status'], result['status_message'])

        return result['message_token']

    def _prepare_payload(self, message, sender_name, sender_avatar, sender=None, receiver=None, chat_id=None):
        payload = message.to_dict()
        payload.update({
            'auth_token': self._bot_configuration.auth_token,
            'from': sender,
            'receiver': receiver,
            'sender': {
                'name': sender_name,
                'avatar': sender_avatar
            },
            "chat_id": chat_id,
            "min_api_version": self._bot_configuration.min_api_version,
        })

        return self._remove_empty_fields(payload)

    @staticmethod
    def _remove_empty_fields(message):
        return {k: v for k, v in message.items() if v is not None}
