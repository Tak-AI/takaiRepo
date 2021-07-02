#!/usr/bin/env python
from core_tool import *
import rospy
import math
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  x2 = input()
  y2 = input()
  z2 = input()
  if x2 == 0 and y2 > 0:
    theta2 = math.pi/2
  elif x2 == 0 and y2 < 0:
    theta2 = -math.pi/2
  else: 
    theta2 = math.atan2(x2, y2)
    print(theta2)
  q_now = ct.robot.Q()
  q_now[0] = theta2
  x_FK = ct.robot.FK(q_now)
  x = list(ct.robot.FK())
  x_now = copy.deepcopy(x)
  theta1 = math.atan2(x_now[1], x_now[0])
  x1 = x_now[0]
  y1 = x_now[1]
  z1 = x_now[2]
  a1 = ((x1**2*y2**2)-(x2**2*y1**2))/(y2**2-y1**2)
  b1 = ((x2**2*y1**2)-(x1**2*y2**2))/(x2**2-x1**2)
  print(a1, b1)
  a = math.sqrt(a1)
  b = math.sqrt(b1)
  x_traj = []
  t_traj = []
  x_traj.append(x_now)
  t_traj.append(0.0)
  x_t = copy.deepcopy(x)
  for i in range(1, 50):
      t_traj.append(0.1*i)
      x_t[0] = a*math.cos(theta2 + i*(theta1-theta2)/50)
      x_t[1] = b*math.sin(theta2 + i*(theta1-theta2)/50)
      x_t[2] += (z2-z1)/50
      x_traj.append(x_t)
  ct.robot.FollowXTraj(x_traj, t_traj)