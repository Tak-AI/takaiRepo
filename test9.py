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
  if a == 0:
    theta = math.pi
  else: 
    theta = math.atan2(b, a)
  ct.robot.MoveToQ([theta, 0.027604753814144237, 0.02256845844164128, -2.2001560115435073, -0.00047772651727832574, 0.6569580325147487, 0.0010119170182285682], 2.0, blocking=True)
  rospy.sleep(3)
  x = list(ct.robot.FK())
  x1 = copy.deepcopy(x)
  x_traj = []
  t_traj = []
  x_traj.append(x1)
  t_traj.append(0.0)
  a1 = (float(a) - x1[0])/50
  b1 = (float(b) - x1[1])/50
  c1 = (float(c) - x1[2])/50

  for i in range(1, 50):
    t_traj.append(0.1*i)
    x2 = copy.deepcopy(x)
    x2[0] += a1*i
    x2[1] += b1*i
    x2[2] += c1*i
    x_traj.append(x2)
  #print t_traj
  #print x_traj
  rospy.sleep(3)
  ct.robot.FollowXTraj(x_traj, t_traj, blocking=True)
  rospy.sleep(2)
  ct.robot.OpenGripper()
  x2[2] += 0.1
  ct.robot.MoveToX(x1, 2.0, blocking = True)
  rospy.sleep(2)
  ct.robot.MoveToQ([-0.02225494707637879, 0.027604753814144237, 0.02256845844164128, -2.2001560115435073, -0.00047772651727832574, 0.6569580325147487, 0.0010119170182285682], 2.0, blocking=True)

  
