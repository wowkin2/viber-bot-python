from .contact_message import ContactMessage
from .file_message import FileMessage
from .picture_message import PictureMessage
from .sticker_message import StickerMessage
from .url_message import URLMessage
from .video_message import VideoMessage
from .message_type import MessageType
from .text_message import TextMessage
from .location_message import LocationMessage
from .rich_media_message import RichMediaMessage
from .keyboard_message import KeyboardMessage

MESSAGE_TYPE_TO_CLASS = {
    MessageType.URL: URLMessage,
    MessageType.LOCATION: LocationMessage,
    MessageType.PICTURE: PictureMessage,
    MessageType.CONTACT: ContactMessage,
    MessageType.FILE: FileMessage,
    MessageType.TEXT: TextMessage,
    MessageType.VIDEO: VideoMessage,
    MessageType.STICKER: StickerMessage,
    MessageType.RICH_MEDIA: RichMediaMessage,
    MessageType.KEYBOARD: KeyboardMessage
}


def get_message(message_dict):
    if 'type' not in message_dict:
        raise Exception("message data doesn't contain a type")

    if message_dict['type'] not in MESSAGE_TYPE_TO_CLASS:
        raise Exception(u"message type '{0}' is not supported".format(message_dict['type']))

    return MESSAGE_TYPE_TO_CLASS[message_dict['type']]().from_dict(message_dict)


__all__ = [
    'TextMessage', 'ContactMessage', 'FileMessage', 'LocationMessage',
    'PictureMessage', 'StickerMessage', 'URLMessage', 'VideoMessage',
    'RichMediaMessage', 'MessageType', 'KeyboardMessage']
