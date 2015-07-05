__author__ = 'moonmagian'
import json

import requests

from pytelegrambot.botClasses import *


def getapiurl(token):
    """
    :param token: token of the robot.
    :return:result of request.
    """
    # Returns the api url of token.
    return "https://api.telegram.org/bot" + token + "/"


def getme(token):
    """
    :param token: token of the robot.
    :return:result of request.
    """
    # Returns the information of the robot.
    return requests.post(getapiurl(token) + "getMe")


def getupdates(token, limit=100, timeout=0, offset=-1):
    """
    :param token: token of the robot
    :param limit: the count of message
    :param timeout: timeout time
    :param offset: start message id
    :return:result of request
    """
    # Get message updates.
    params = {"limit": limit, "timeout": timeout}
    if offset > 0:
        params["offset"] = offset
    return requests.post(getapiurl(token) + "getUpdates", params=params)


def sendmessage(token, chat_id, text, disable_web_page_preview=False,reply_to_message_id=UNDEFINEDINT, reply_markup = UNDEFINED):
    """
    :param token: token of the robot
    :param chat_id: chat_id to send message to
    :param text: send text
    :param disable_web_page_preview:if True, won't show preview
    :param reply_to_message_id:
    :param reply_markup: Can be instance of ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply
    :return:result of sending.
    """
    # Send a message.
    params = {"chat_id": int(chat_id), "text": str(text), "disable_web_page_preview": bool(disable_web_page_preview)}
    if reply_to_message_id != UNDEFINEDINT:
        params["reply_to_message_id"] = int(reply_to_message_id)
    if reply_markup != UNDEFINED:
        if reply_markup.__class__ != ReplyKeyboardMarkup and reply_markup.__class__ != ReplyKeyboardHide and reply_markup.__class__ != ForceReply:
            raise TypeError
        params["reply_markup"] = json.dumps(reply_markup.__dict__)
    return requests.post(getapiurl(token) + "sendMessage", params=params)


def forwardmessage(token, chat_id, from_chat_id, message_id):
    """
    :param token: token of the robot
    :param chat_id: chat_id to send message to
    :param from_chat_id:
    :param message_id:
    :return:result of forwarding
    """
    # Forward a message.
    params = {"chat_id": int(chat_id), "from_chat_id": int(from_chat_id), "message_id": int(message_id)}
    return requests.post(getapiurl(token) + "forwardMessage", params=params)


def sendphoto(token, chat_id, photo, caption=UNDEFINED, reply_to_message_id=UNDEFINEDINT, reply_markup=UNDEFINED):
    """
    :param token: token of the robot
    :param chat_id: chat_id to send message to
    :param photo: photo you want to send
    :param caption: I don't know
    :param reply_to_message_id:
    :param reply_markup:
    :return:result of sending
    """
    # Send a photo, photo should be opened with open()
    params = {"chat_id": int(chat_id)}
    if caption != UNDEFINED:
        params["caption"] = str(caption)
    if reply_to_message_id != UNDEFINEDINT:
        params["reply_to_message_id"] = reply_to_message_id
    if reply_markup != UNDEFINED:
        if reply_markup.__class__ != ReplyKeyboardMarkup and reply_markup.__class__ != ReplyKeyboardHide and reply_markup.__class__ != ForceReply:
            raise TypeError
        params["reply_markup"] = json.dumps(reply_markup.__dict__)
    return requests.post(getapiurl(token) + "sendPhoto", params=params, files={"photo": photo})


def sendaudio(token, chat_id, audio, reply_to_message_id=UNDEFINEDINT, reply_markup = UNDEFINED):
    """
    :param token: token of the robot
    :param chat_id: chat_id to send message to
    :param audio: audio you want to send
    :param reply_to_message_id:
    :param reply_markup:
    :return:result of sending
    """
    # Send audio, almost same as sendphoto.
    params = {"chat_id": int(chat_id)}
    if reply_to_message_id != UNDEFINEDINT:
        params["reply_to_message_id"] = reply_to_message_id
    if reply_markup != UNDEFINED:
        if reply_markup.__class__ != ReplyKeyboardMarkup and reply_markup.__class__ != ReplyKeyboardHide and reply_markup.__class__ != ForceReply:
            raise TypeError
        params["reply_markup"] = json.dumps(reply_markup.__dict__)
    return requests.post(getapiurl(token) + "sendAudio", params=params, files={"audio": audio})


def senddocument(token, chat_id, document, reply_to_message_id=UNDEFINEDINT, reply_markup=UNDEFINED):
    """
    :param token: token of the robot
    :param chat_id: chat_id to send message to
    :param document: document you want to send
    :param reply_to_message_id:
    :param reply_markup:
    :return:result of sending
    """
    # You know,they are just same.
    params = {"chat_id": int(chat_id)}
    if reply_to_message_id != UNDEFINEDINT:
        params["reply_to_message_id"] = reply_to_message_id
    if reply_markup != UNDEFINED:
        if reply_markup.__class__ != ReplyKeyboardMarkup and reply_markup.__class__ != ReplyKeyboardHide and reply_markup.__class__ != ForceReply:
            raise TypeError
        params["reply_markup"] = json.dumps(reply_markup.__dict__)
    return requests.post(getapiurl(token) + "sendDocument", params=params, files={"document": document})


def sendvideo(token, chat_id, video, reply_to_message_id=UNDEFINEDINT, reply_markup = UNDEFINED):
    """
    :param token: token of the robot
    :param chat_id: chat_id to send message to
    :param video: video you want to send
    :param reply_to_message_id:
    :param reply_markup:
    :return:result of sending
    """
    # Need to say anything?
    params = {"chat_id": int(chat_id)}
    if reply_to_message_id != UNDEFINEDINT:
        params["reply_to_message_id"] = reply_to_message_id
    if reply_markup != UNDEFINED:
        if reply_markup.__class__ != ReplyKeyboardMarkup and reply_markup.__class__ != ReplyKeyboardHide and reply_markup.__class__ != ForceReply:
            raise TypeError
        params["reply_markup"] = json.dumps(reply_markup.__dict__)
    return requests.post(getapiurl(token) + "sendVideo", params=params, files={"video": video})


def sendsticker(token, chat_id, sticker, reply_to_message_id=UNDEFINEDINT, reply_markup = UNDEFINED):
    """
    :param token: token of the robot
    :param chat_id: chat_id to send message to
    :param sticker: sticker you want to send
    :param reply_to_message_id:
    :param reply_markup:
    :return:result of sending
    """
    # Seems no.
    params = {"chat_id": int(chat_id)}
    if reply_to_message_id != UNDEFINEDINT:
        params["reply_to_message_id"] = reply_to_message_id
    if reply_markup != UNDEFINED:
        if reply_markup.__class__ != ReplyKeyboardMarkup and reply_markup.__class__ != ReplyKeyboardHide and reply_markup.__class__ != ForceReply:
            raise TypeError
        params["reply_markup"] = json.dumps(reply_markup.__dict__)
    return requests.post(getapiurl(token) + "sendSticker", params=params, files={"sticker": sticker})


def sendlocation(token, chat_id, latitude, longitude, reply_to_message_id=UNDEFINEDINT, reply_markup=UNDEFINED):
    """
    :param token: token of the robot
    :param chat_id: chat_id to send message to
    :param latitude:
    :param longitude:
    :param reply_to_message_id:
    :param reply_markup:
    :return:result of sending
    """
    params = {"chat_id": int(chat_id), "latitude": float(latitude), "longitude": float(longitude)}
    if reply_to_message_id != UNDEFINEDINT:
        params["reply_to_message_id"] = reply_to_message_id
    if reply_markup != UNDEFINED:
        if reply_markup.__class__ != ReplyKeyboardMarkup and reply_markup.__class__ != ReplyKeyboardHide and reply_markup.__class__ != ForceReply:
            raise TypeError
        params["reply_markup"] = json.dumps(reply_markup.__dict__)
    return requests.post(getapiurl(token) + "sendLocation", params=params)


def sendchataction(token, chat_id, action):
    """
    :param token: token of the robot
    :param chat_id: chat_id to send message to
    :param action: any of "typing", "upload_photo", "record_video", "upload_video", "record_audio", "upload_audio", "upload_document", "find_location"
    :return:
    """
    actions = ["typing", "upload_photo", "record_video", "upload_video", "record_audio", "upload_audio", "upload_document", "find_location"]
    actions.index(action)
    params = {"chat_id": int(chat_id), "action": action}
    return requests.post(getapiurl(token) + "sendChatAction", params=params)


def getuserprofilephotos(WIP):
    """HOW CAN I SAVE PHOTOS WITH ARRAY OF ARRAY OF PHOTOSIZE!?"""