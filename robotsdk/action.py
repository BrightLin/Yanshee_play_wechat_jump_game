#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from ctypes import *

isSetLed = False
ll = cdll.LoadLibrary
api = ll("/mnt/1xrobot/lib/librobot.so")


def sdkInit():
    # ---------init blockly function------------
    api.ubtRobotInitialize()
    ret = api.ubtRobotConnect("123", "sdk", "127.0.0.1")
    if (0 != ret):
        print ("Error --> ubtRobotConnect return value: %d" % ret)
        exit(1)


def sdkFinish(name):
    # ---------exit blockly function------------
    global isSetLed
    if isSetLed:
        api.ubtSetRobotLED("button", "blue", "breath")
    api.ubtReportStatusToApp(name, "finish")
    api.ubtRobotDisconnect("123", "sdk", "127.0.0.1")
    api.ubtRobotDeinitialize()


def runAction(name, actionName, repeat):

    if actionName == "":
        exit(0)

    api.ubtStartRobotAction(actionName, repeat)

