#!/usr/bin/env python
from core_tool import *
import rospy
import math
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  position = [0.5,0,0.5]
  while not rospy.is_shutdown():
    tmp = copy.deepcopy(position)
    position = ct.GetAttr('obj1','position')
    key = ct.GetAttr('obj3','key')
    if key == 'q':
      break
    if key == 'g':
      ct.robot.MoveGripper(0.07)
    if key == 'o':
      ct.robot.OpenGripper()
    if position[0] >= 1.0:
      break
    x = list(ct.robot.FK())
    x1 = copy.deepcopy(x)
    if position != tmp:
      t = math.sqrt((position[0]-tmp[0])**2 + (position[1]-tmp[1])**2 + (position[1]-tmp[1])**2) / 0.5
      ct.robot.MoveToXI([position[0],position[1],position[2],x1[3],x1[4],x1[5],x1[6]], t, blocking = True)
      print(t)



