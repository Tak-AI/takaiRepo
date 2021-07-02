#!/usr/bin/env python
from core_tool import *
import rospy
import math
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  a = input()
  b = input()
  c = input()
  if a == 0 and b > 0:
    theta = math.pi/2
  elif a == 0 and b < 0:
    theta = -math.pi/2
  else: 
    theta = math.atan2(b, a)
  q_first = [theta, 0.0276047, 0.0225684, -2.2001560, -0.0004777, 0.6569580, 0.0010118]
  x_FK = ct.robot.FK(q_first)
  ct.robot.MoveToXI([a, b, c, x_FK[3], x_FK[4], x_FK[5], x_FK[6]], dt = 4)