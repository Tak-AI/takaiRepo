#!/usr/bin/env python
from core_tool import *
import rospy
import time
#from test5 import position2

def Run(ct,*args):
  ct.robot.OpenGripper()
  position2 = ct.GetAttr('obj1','position')
  print(position2)
  if position2[0] == 0 and position2[1] > 0:
    theta = math.pi/2
  elif position2[0] == 0 and position2[1] < 0:
    theta = -math.pi/2
  else:
    theta = math.atan2(position2[1], position2[0])
  ct.robot.MoveToQ([theta, 0.027604753814144237, 0.02256845844164128, -2.2001560115435073, -0.00047772651727832574, 0.6569580325147487, 0.0010119170182285682], blocking=True)
  rospy.sleep(3)
  x = list(ct.robot.FK())
  x1 = copy.deepcopy(x)
  x_traj = []
  t_traj = []
  x_traj.append(x1)
  t_traj.append(0.0)
  a1 = (position2[0] - x1[0])/50
  b1 = (position2[1] - x1[1])/50
  c1 = (position2[2] - x1[2])/50
  for i in range(1, 50):
    t_traj.append(0.1*i)
    x2 = copy.deepcopy(x)
    x2[0] += a1*i
    x2[1] += b1*i
    x2[2] += c1*i
    x_traj.append(x2)
  ct.robot.FollowXTraj(x_traj, t_traj, blocking=True)
  rospy.sleep(3)
  ct.robot.MoveGripper(position2[3])
  rospy.sleep(3)
  x2[2] += 0.1
  ct.robot.MoveToX(x1, 2.0, blocking = True)
