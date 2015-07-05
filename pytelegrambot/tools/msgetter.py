__author__ = 'moonmagian'
import json
import sys

from pytelegrambot import *
def getmessages(token):
    msgs = jsonfuckers.updatesfromjson(json.loads(botFuncs.getupdates(token).text))
    for loop in msgs:
        print pybotFuncs.encode2json(loop.message).replace("\\\"", "\"")