#!/usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *
from ubtinit import *

#---- define environment sensor class 
class UbtRobotTemperature(Structure):
	_fields_ = [
		#define field, array int type, 3 len
		("data", c_int*3)
	]


#---- define IR/Ultra-sonioc sensor class 
class UbtRobotIRorUltrasonic(Structure):
	_fields_ = [
		#define field, int type, len
		("data", c_int)
	]


#--------get sensor value function----------
def getRobotSensorValue(type):
	if "temperature" == type:
                ubtRobotEnv = pointer(UbtRobotTemperature())
		ret = api.ubtReadSensorValue("environment", ubtRobotEnv, sizeof(UbtRobotTemperature))
		if 0 != ret:
			return 0
		return ubtRobotEnv[0].data[0]

	elif "obstacle" == type:
                ubtIRorUltrasonic = pointer(UbtRobotIRorUltrasonic())
		ret = api.ubtReadSensorValue("ultrasonic", ubtIRorUltrasonic, sizeof(UbtRobotIRorUltrasonic))
		if 0 != ret:
			ret = api.ubtReadSensorValue("infrared", ubtIRorUltrasonic, sizeof(UbtRobotIRorUltrasonic))
			if 0 != ret:
				return 1501
		return ubtIRorUltrasonic[0].data / 10
	return 1501
