#!/usr/bin/env python
from core_tool import *
import rospy
import time
#from test5 import position

def Run(ct,*args):
  ct.robot.MoveToQ([-0.02225494707637879, 0.027604753814144237, 0.02256845844164128, -2.2001560115435073, -0.00047772651727832574, 0.6569580325147487, 0.0010119170182285682], 2.0, blocking=True)
  position = ct.GetAttr('obj1','position')
  print(position)
  if position[0] == 0 and position[1] > 0:
    theta = math.pi/2
  elif position[0] == 0 and position[1] < 0:
    theta = -math.pi/2
  else:
    theta = math.atan2(position[1], position[0])
  ct.robot.MoveToQ([theta, 0.027604753814144237, 0.02256845844164128, -2.2001560115435073, -0.00047772651727832574, 0.6569580325147487, 0.0010119170182285682], blocking=True)
  x = list(ct.robot.FK())
  x1 = copy.deepcopy(x)
  x_traj = []
  t_traj = []
  x_traj.append(x1)
  t_traj.append(0.0)
  a1 = (position[0] - x1[0])/50
  b1 = (position[1] - x1[1])/50
  c1 = (position[2] - x1[2])/50
  for i in range(1, 50):
    t_traj.append(0.1*i)
    x2 = copy.deepcopy(x)
    x2[0] += a1*i
    x2[1] += b1*i
    x2[2] += c1*i
    x_traj.append(x2)
  ct.robot.FollowXTraj(x_traj, t_traj)