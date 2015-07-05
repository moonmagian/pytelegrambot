__author__ = 'moonmagian'
from pytelegrambot import *
import sys


class bot(basicbot.BasicBot):
    def _onupdate(self):
        print "updated."

    def _onreceived(self, msgs):
        print "Message received!Here are these lovely guys:"
        print "********"
        for loop in msgs:
            print loop.message.message_id
TOKEN = sys.argv[1]
b = bot(TOKEN, 1, sys.argv[2])
b.start()