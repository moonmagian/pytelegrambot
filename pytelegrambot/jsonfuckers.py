__author__ = 'moonmagian'
from botClasses import *
import pybotFuncs


def userfromjson(jsonedjson):
    return User(jsonedjson["id"], jsonedjson["first_name"], pybotFuncs.testfor(jsonedjson, "last_name"), pybotFuncs.testfor(jsonedjson, "username"))


def groupchatfromjson(jsonedjson):
    return GroupChat(jsonedjson["id"], jsonedjson["title"])


def photosizefromjson(jsonedjson):
    return PhotoSize(jsonedjson["file_id"], jsonedjson["width"], jsonedjson["height"], pybotFuncs.testfor(jsonedjson, "file_size", True))


def audiofromjson(jsonedjson):
    return Audio(jsonedjson["file_id"], jsonedjson["duration"], pybotFuncs.testfor(jsonedjson, "mime_type"), pybotFuncs.testfor(jsonedjson, "file_size", True))


def documentfromjson(jsonedjson):
    return Document(jsonedjson["file_id"], photosizefromjson(jsonedjson["thumb"]), pybotFuncs.testfor(jsonedjson, "filename"), pybotFuncs.testfor(jsonedjson, "mime_type"), pybotFuncs.testfor(jsonedjson, "file_size", True))


def stickerfromjson(jsonedjson):
    return Sticker(jsonedjson["file_id"], jsonedjson["width"], jsonedjson["height"], photosizefromjson(jsonedjson["thumb"]), pybotFuncs.testfor(jsonedjson, "file_size", True))


def videofromjson(jsonedjson):
    return Video(jsonedjson["file_id"], jsonedjson["width"], jsonedjson["height"], jsonedjson["duration"], photosizefromjson(jsonedjson["thumb"]), pybotFuncs.testfor(jsonedjson, "mime_type"), pybotFuncs.testfor(jsonedjson, "file_size", True), pybotFuncs.testfor(jsonedjson, "caption"))


def contactfromjson(jsonedjson):
    return Contact(jsonedjson["phone_number"], jsonedjson["first_name"], pybotFuncs.testfor(jsonedjson, "last_name"), pybotFuncs.testfor(jsonedjson, "user_id"))


def locationfromjson(jsonedjson):
    return Location(jsonedjson["longitude"], jsonedjson["latitude"])


def updatesfromjson(jsonedjson):
    """turn the returnedjson of getupdates in botFuncs into some Update instance."""
    results = jsonedjson["result"]
    returns = []
    for loop in range(len(results)):
        thisresult = results[loop]
        u = Update(thisresult["update_id"], messagefromjson(thisresult["message"]))
        returns.append(u)
    return returns


def messagefromjson(jsonedjson):
    """create message from json"""
    sender = userfromjson(jsonedjson["from"])
    if pybotFuncs.testfor(jsonedjson["chat"], "title") == UNDEFINED:
        chat = userfromjson(jsonedjson["chat"])
    else:
        chat = groupchatfromjson(jsonedjson["chat"])
    msgtype = pybotFuncs.checkmsgtype(jsonedjson)
    if msgtype == "text" or msgtype == "new_chat_title":
        contain = jsonedjson[msgtype]
    if msgtype == "audio":
        contain = audiofromjson(jsonedjson[msgtype])
    if msgtype == "document":
        contain = documentfromjson(jsonedjson[msgtype])
    if msgtype == "sticker":
        contain = stickerfromjson(jsonedjson[msgtype])
    if msgtype == "photo" or msgtype == "new_chat_photo":
        contain = "WIP"
    if msgtype == "video":
        contain = videofromjson(jsonedjson[msgtype])
    if msgtype == "contact":
        contain = contactfromjson(jsonedjson[msgtype])
    if msgtype == "location":
        contain = locationfromjson(jsonedjson[msgtype])
    if msgtype == "new_chat_participant" or msgtype == "left_chat_participant":
        contain = userfromjson(jsonedjson[msgtype])
    if msgtype == "delete_chat_photo" or msgtype == "group_chat_created":
        contain = True
    if pybotFuncs.testfor(jsonedjson, "forward_from") != UNDEFINED:
        forwardfrom = userfromjson(jsonedjson["forward_from"])
    else:
        forwardfrom = None
    if pybotFuncs.testfor(jsonedjson, "reply_to_message") != UNDEFINED:
        reply2msg = messagefromjson(jsonedjson["reply_to_message"])
    else:
        reply2msg = None
    return Message(jsonedjson["message_id"], sender, jsonedjson["date"], chat, contain, msgtype, forwardfrom, pybotFuncs.testfor(jsonedjson, "forward_date", True), reply2msg)