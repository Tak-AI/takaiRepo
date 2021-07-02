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
  q_IK = ct.robot.IK([a, b, c, x_FK[3], x_FK[4], x_FK[5], x_FK[6]])
  q = list(ct.robot.Q())
  q_now = copy.deepcopy(q)
  q_d = [0]*7
  q_traj = []
  t_traj = []
  q_traj.append(q_now)
  t_traj.append(0.0)
  for k in range(0, 6):
    q_d[k] = (q_IK[k] - q_now[k])/50
  for i in range(1, 50):
    t_traj.append(0.1*i)
    q_t = copy.deepcopy(q)
    for j in range(0, 6):
      q_t[j] += q_d[j]*i
    q_traj.append(q_t)
  ct.robot.FollowQTraj(q_traj, t_traj)