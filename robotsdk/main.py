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

if __name__ == '__main__':
    name = sys.argv[0]
    argLen = len(sys.argv)
    action = ""

    for index in range(0, argLen):
        if index > 0:
            if (sys.argv[index] == '--action' or sys.argv[index] == '-a') and index + 1 < argLen:
                action = sys.argv[index + 1]

    if action == "":
        exit(0)

    sdkInit()

    api.ubtStartRobotAction(action, 1)

    sdkFinish(name)
    print "exit blockly"
    exit(0)
