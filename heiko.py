#!/usr/bin/env python
from core_tool import *
import rospy
import math
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  while not rospy.is_shutdown():
    position = ct.GetAttr('obj1','position')
    if position[0] >= 1.0:
        break
    x = list(ct.robot.FK())
    x1 = copy.deepcopy(x)
    ct.robot.MoveToX([position[0],position[1],position[2],x1[3],x1[4],x1[5],x1[6]], blocking = True)

  