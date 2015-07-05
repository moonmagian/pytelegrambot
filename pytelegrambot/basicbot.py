__author__ = 'moonmagian'
import botClasses,botFuncs,jsonfuckers,pybotFuncs
import json
import requests
import time


class BasicBot:
    def __init__(self, token, delaytime, logchatid, listenlimit=10):
        """
        :param token: token of the robot
        :param delaytime: delaytime of every update
        :param logchatid: chatid for special log
        :param listenlimit: limit of listened message
        :return:
        """
        # the lower delaytime means a faster update but needs more network resource.
        # logchatid is for getting newest offset,you can use the tools/msgetter.py to find one.
        # less listenlimit means a faster update but will be buggy if more than that number of messages are sent.
        self.delaytime = float(delaytime)
        self.logchatid = int(logchatid)
        self.token = token
        self._offset = botClasses.UNDEFINEDINT
        self._stopped = True
        self.listenlimit = int(listenlimit)

    def _initoffset(self, customtext="[Special]Robot launched"):
        # As you see here is initoffset method.
        launchinfo = jsonfuckers.messagefromjson(json.loads(botFuncs.sendmessage(self.token, self.logchatid, customtext).text)["result"]).message_id
        self._offset = launchinfo + 1

    def _listen(self):
        # _you needn't to change this if you just want a simple robot.
        while not self._stopped:
            newmsgs = botFuncs.getupdates(self.token, offset=self._offset, limit=self.listenlimit).text
            if not pybotFuncs.isokay(newmsgs):
                raise requests.ConnectionError
            msgs = jsonfuckers.updatesfromjson(json.loads(newmsgs))
            if len(msgs) != 0:
                self._onreceived(msgs)
                self._offset = msgs[-1].update_id + 1
            self._onupdate()
            time.sleep(self.delaytime)

    def _onreceived(self, msgs, argc, argv):
        # When there are new messages,the method will be called.Override it to change robot's main logic.
        pass

    def _onupdate(self):
        # Almost same as _onreceived.How ever this is called on update.
        pass

    def start(self):
        # Start the robot.
        self._initoffset()
        self._stopped = False
        self._listen()

    def stop(self):
        # Stop the robot.(useless for now)
        self._stopped = True