__author__ = 'moonmagian'
from pytelegrambot import *
import sys
discusses = []
TOKEN = "121128695:AAFfJGdt__gxPCNWWsCsFPi4NfYkybD0J8E"
# A simple bbs robot.Really simple, you can add features in it.


class discuss:
    def __init__(self, name, contain):
        self.name = str(name)
        self.contain = str(contain)
        self.replys = []


class bot(basicbot.BasicBot):
    def _onupdate(self):
        print "updated."

    def _onreceived(self, msgs):
        for loop in msgs:
            if loop.message.msgtype == "text":
                command = loop.message.contain.split(" ")
                if command[0] == "/list":
                    botFuncs.sendmessage(TOKEN, loop.message.chat.id, getdtitles(discusses))
                if command[0] == "/see" and len(command) == 2:
                    try:
                        botFuncs.sendmessage(TOKEN, loop.message.chat.id, "title:" + discusses[int(command[1])].name + "\n*****\ncontain:" + discusses[int(command[1])].contain + "\n*****\nreplies:\n" + getreplies(discusses[int(command[1])].replys))
                    except:
                        botFuncs.sendmessage(TOKEN, loop.message.chat.id, "Error happens!Check your input!")
                if command[0] == "/createnew" and len(command) >= 2:
                    try:
                        c2 = " ".join(command[1:]).split("||")
                        discusses.append(discuss(c2[0], c2[1]))
                        botFuncs.sendmessage(TOKEN, loop.message.chat.id, "discuss created.")
                    except:
                        botFuncs.sendmessage(TOKEN, loop.message.chat.id, "Error happens!Check your input!Use /createnew title||contain")
                if command[0] == "/reply" and len(command) >= 3:
                    try:
                        discusses[int(command[1])].replys.append(" ".join(command[2:]))
                        botFuncs.sendmessage(TOKEN, loop.message.chat.id, "reply created.")
                    except:
                        botFuncs.sendmessage(TOKEN, loop.message.chat.id, "Error happens!Check your input!Use /reply discussid contain")


def getdtitles(dis, start=0, count=9):
    stri = ""
    for loop in range(len(dis)):
        stri = stri + str(loop) + "." + dis[loop].name + "\n"
    return stri


def getreplies(replys):
    stri = ""
    for loop in range(len(replys)):
        stri = stri + str(loop) + "." + replys[loop] + "\n"
    return stri
TOKEN = sys.argv[1]
b = bot(TOKEN, 1, sys.argv[2])
b.start()