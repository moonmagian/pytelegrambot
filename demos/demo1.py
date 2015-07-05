#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'moonmagian'
from pytelegrambot import *
import base64
import random
import os
import thread
import sys

class Bot(basicbot.BasicBot):
    def _onupdate(self):
        print "updated."

    def _onreceived(self, msgs):
        for loop in msgs:
            if loop.message.msgtype == "text":  # Make sure the type of message is text.
                # Here are command checks.
                if loop.message.contain.split(" ")[0] == "/base64encode" and len(loop.message.contain.split(" ")) >= 2:
                    thread.start_new_thread(lambda :botFuncs.sendmessage(TOKEN, loop.message.chat.id, base64.encodestring(" ".join(loop.message.contain.split(" ")[1:])), reply_to_message_id=loop.message.message_id), ())
                # Use thread to avoid message jam.
                elif loop.message.contain.split(" ")[0] == "/base64decode" and len(loop.message.contain.split(" ")) == 2:
                    thread.start_new_thread(lambda :botFuncs.sendmessage(TOKEN, loop.message.chat.id, base64.decodestring(" ".join(loop.message.contain.split(" ")[1:])), reply_to_message_id=loop.message.message_id), ())
                elif loop.message.contain.split(" ")[0] == "/random" and len(loop.message.contain.split(" ")) == 3:
                    try:
                        random.seed()
                        num = random.randint(int(loop.message.contain.split(" ")[1]), int(loop.message.contain.split(" ")[2]))
                        thread.start_new_thread(lambda :botFuncs.sendmessage(TOKEN, loop.message.chat.id, num, reply_to_message_id=loop.message.message_id), ())
                    except:
                        thread.start_new_thread(lambda :botFuncs.sendmessage(TOKEN, loop.message.chat.id, "RandomError", reply_to_message_id=loop.message.message_id), ())
                elif loop.message.contain.split(" ")[0] == "/randomimg" and len(loop.message.contain.split(" ")) == 1:
                    print "randimg request"
                    try:
                        files = os.listdir('randomimg/')
                        path = 'randomimg/' + files[random.randint(0, len(files) - 1)]
                        filex = open(path)
                        thread.start_new_thread(lambda :botFuncs.sendphoto(TOKEN, loop.message.chat.id, filex, reply_to_message_id=loop.message.message_id), ())
                    except:
                        thread.start_new_thread(lambda :botFuncs.sendmessage(TOKEN, loop.message.chat.id, "SendError", reply_to_message_id=loop.message.message_id), ())
                # Here ends.
TOKEN = sys.argv[1]  # This is my test token,don't do changes to it plz.
b = Bot(TOKEN, 1, sys.argv[2])  # Create the robot.
b.start()  # Start the robot.