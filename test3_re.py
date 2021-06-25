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
  q_now = ct.robot.Q()
  q_now[0] = theta
  x_FK = ct.robot.FK(q_now)
  q_IK = ct.robot.IK([a, b, c, x_FK[3], x_FK[4], x_FK[5], x_FK[6]])
  
  q = list(ct.robot.IK())
  q_1 = copy.deepcopy(q)
  q_traj = []
  t_traj = []
  q_traj.append(q_1)
  t_traj.append(0.0)
  a1 = (q_IK[0] - q_1[0])/50
  b1 = (q_IK[1] - q_1[1])/50
  c1 = (q_IK[2] - q_1[2])/50
  q1 = (q_IK[3] - q_1[3])/50
  q2 = (q_IK[4] - q_1[4])/50
  q3 = (q_IK[5] - q_1[5])/50
  q4 = (q_IK[6] - q_1[6])/50
  for i in range(1, 50):
    t_traj.append(0.1*i)
    x2 = copy.deepcopy(q)
    x2[0] += a1*i
    x2[1] += b1*i
    x2[2] += c1*i
    x2[3] += q1*i
    x2[4] += q2*i
    x2[5] += q3*i
    x2[6] += q4*i
    q_traj.append(x2)
  ct.robot.FollowQTraj(q_traj)