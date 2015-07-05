__author__ = 'moonmagian'
import json

from jsonfuckers import *


def encode2json(ins):
    """
    :param ins: instance to encode to json
    :return:text json
    """
    d = ins.__dict__
    for loop in d:
        if d[loop].__class__ != str and d[loop].__class__ != int and d[loop].__class__ != float and d[loop].__class__ != bool and d[loop] != None and d[loop].__class__ != unicode:
            d[loop] = encode2json(d[loop])
    return json.dumps(d)


def isokay(returnedjson):
    """
    :param returnedjson: text json returned by telegram robot API.
    :return:whether the API is execed successfully.
    """
    if json.loads(returnedjson)["ok"]:
        return True
    else:
        return False


def checkmsgtype(jsonedjson):
    """
    :param jsonedjson: message json
    :return:message type with text.
    """
    for loop in MSGTYPES:
        if testfor(jsonedjson, loop) != UNDEFINED:
           return loop
    return UNDEFINED


def testfor(jsonedjson, k, returnint=False):
    """
    :param jsonedjson: json you want to test for
    :param k: key you want to test for
    :param returnint: if returnint is true, will return UNDEFINDINT instead of UNDEFINED
    :return:reuturn value if key called k is avaiable else return UNDEFINED or UNDEFINEDINT
    """
    try:
        jsonedjson[k]
        return jsonedjson[k]
    except:
        if returnint:
            return UNDEFINEDINT
        else:
            return UNDEFINED