#!/usr/bin/env python
from core_tool import *
import rospy
import math
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  a = map(float, raw_input().split())
  if a == 0:
    theta = math.pi
  else: 
    theta = math.atan2(a[1], a[0])
  str = ct.GetAttr('obj2','which')
  if str == "side":
    ct.robot.MoveToQ([theta, 0.0276047, 0.0225684, -2.2001560, -0.0004777, 0.6569580, 0.0010118], 2.0, blocking=True)
  elif str == "up":
    ct.robot.MoveToQ([theta, 0.0276047, 0.0225684, -2.2001560, -0.0004777, -0.8569580, 0.0010118], 2.0, blocking=True)
  else:
    ct.robot.MoveToQ([theta, 0.0276047, 0.0225684, -2.2001560, -0.0004777, 0.6569580, 0.0010118], 2.0, blocking=True)
  rospy.sleep(3)
  x = list(ct.robot.FK())
  x1 = copy.deepcopy(x)
  x_traj = []
  t_traj = []
  x_traj.append(x1)
  t_traj.append(0.0)
  a1 = (float(a[0]) - x1[0])/50
  b1 = (float(a[1]) - x1[1])/50
  c1 = (float(a[2]) - x1[2])/50

  for i in range(1, 50):
    t_traj.append(0.1*i)
    x2 = copy.deepcopy(x)
    x2[0] += a1*i
    x2[1] += b1*i
    x2[2] += c1*i
    x_traj.append(x2)
  rospy.sleep(3)
  ct.robot.FollowXTraj(x_traj, t_traj, blocking=True)
  rospy.sleep(2)
  ct.robot.OpenGripper()
  x2[2] += 0.1
  ct.robot.MoveToX(x2, 2.0, blocking = True)
  rospy.sleep(2)
  ct.robot.MoveToQ([theta, 0.0276047, 0.0225684, -2.2001560, -0.0004777, 0.6569580, 0.0010118], 2.0, blocking=True)
