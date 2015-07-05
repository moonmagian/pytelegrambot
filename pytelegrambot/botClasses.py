UNDEFINED = "/UNDEFINED/"
UNDEFINEDINT = -10086
MSGTYPES = ["text", "audio", "document", "photo", "sticker", "video", "contact", "location", "new_chat_participant", "left_chat_participant", "new_chat_title", "new_chat_photo", "delete_chat_photo", "group_chat_created"]
# Here are origin classes in telegram robot API


class Update:
    def __init__(self, update_id, message):
        self.update_id = int(update_id)
        if message.__class__ != Message:
            raise TypeError
        self.message = message


class User:
    def __init__(self, id, firstname, lastname=UNDEFINED, username=UNDEFINED):
        self.id = int(id)
        self.firstname = str(firstname)
        self.lastname = str(lastname)
        self.username = str(username)


class GroupChat:
    def __init__(self, id, title):
        self.id = int(id)
        self.title = str(title)


class PhotoSize:
    def __init__(self, file_id, width, height, file_size=UNDEFINEDINT):
        self.file_id = file_id
        self.width = int(width)
        self.height = int(height)
        self.file_size = int(file_size)


class Audio:
    def __init__(self, file_id, duration, mime_type=UNDEFINED, file_size=UNDEFINEDINT):
        self.file_id = str(file_id)
        self.duration = str(duration)
        self.mime_type = str(mime_type)
        self.file_size = int(file_size)


class Document:
    def __init__(self, file_id, thumb, file_name = UNDEFINED, mime_type = UNDEFINED, file_size = UNDEFINEDINT):
        self.file_id = file_id
        if thumb.__class__ != PhotoSize:
            raise TypeError
        else:
            self.thumb = thumb
            self.file_name = str(file_name)
            self.mime_type = str(mime_type)
            self.file_size = int(file_size)


class Sticker:
    def __init__(self, file_id, width, height, thumb, file_size=UNDEFINEDINT):
        self.file_id = str(file_id)
        self.width = int(width)
        self.height = int(height)
        if thumb.__class__ != PhotoSize:
            raise TypeError
        else:
            self.thumb = thumb
            self.file_size = int(file_size)


class Video:
    def __init__(self, file_id, width, height, duration, thumb, mime_type=UNDEFINED, file_size=UNDEFINEDINT, caption=UNDEFINED):
        self.file_id = str(file_id)
        self.width = int(width)
        self.height = int(height)
        self.duration = int(duration)
        if thumb.__class__ != PhotoSize:
            raise TypeError
        else:
            self.thumb = thumb
            self.file_name = str(caption)
            self.mime_type = str(mime_type)
            self.file_size = int(file_size)


class Contact:
    def __init__(self, phone_number, first_name, last_name=UNDEFINED, user_id = UNDEFINED):
        self.phone_number = str(phone_number)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.user_id = str(user_id)


class Location:
    def __init__(self, longitude, latitude):
        self.longitude = float(longitude)
        self.latitude = float(latitude)


class UserProfilePhotos:
    def __init__(self, total_count, photos):
        self.total_count = int(total_count)
        self.photos = photos


class ReplyKeyboardMarkup:
    def __init__(self, keyboard, resize_keyboard, one_time_keyboard=False, selective=False):
        self.keyboard = keyboard
        self.resize_keyboard = bool(resize_keyboard)
        self.one_time_keyboard = bool(one_time_keyboard)
        self.selective = bool(selective)


class ReplyKeyboardHide:
    def __init__(self, hide_keyboard=True, selective=False):
        self.hide_keyboard = bool(hide_keyboard)
        self.selevtive = bool(selective)


class Message:
    def __init__(self, message_id, sender, date, chat, contain, msgtype=MSGTYPES[0], foward_from=None, foward_date=UNDEFINEDINT, reply_to_message=None):
        self.message_id = int(message_id)
        if sender.__class__ != User:
            raise TypeError
        self.sender = sender
        self.date = int(date)
        if chat.__class__ != User and chat.__class__ != GroupChat:
            raise TypeError
        self.chat = chat
        self.contain = contain
        if foward_from.__class__ != User and foward_from is not None:
            raise TypeError
        self.foward_from = foward_from
        self.foward_date = int(foward_date)
        if reply_to_message.__class__ != Message and reply_to_message is not None:
            raise TypeError
        self.reply_to_message = reply_to_message
        self.msgtype = msgtype


class ForceReply:
    def __init__(self, selective = False):
        self.force_reply = True
        self.selective = bool(selective)