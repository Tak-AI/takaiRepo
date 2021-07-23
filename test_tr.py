#!/usr/bin/env python
from core_tool import *
import rospy
import math
import numpy as np
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  z_90 = np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
  x__90 = np.array([[1,0,0,0],[0,0,1,0],[0,-1,0,0],[0,0,0,1]]) 
  R = np.dot(z_90,x__90)
  a = np.array([[1,0,0,1],[0,1,0,0],[0,0,1,0.5],[0,0,0,1]])
  position = ct.GetAttr('obj1','position')
  camera_vector = np.array([position[0],position[1],position[2],1])
  arm_vector = np.dot(a,np.dot(R,camera_vector))
  print(arm_vector[0],arm_vector[1],arm_vector[2])
  x = list(ct.robot.FK())
  x1 = copy.deepcopy(x)
  #ct.robot.MoveToX([arm_vector[0],arm_vector[1],arm_vector[2],x1[3],x1[4],x1[5],x1[6]], blocking = True)
  x_traj = []
  t_traj = []
  x_traj.append(x1)
  t_traj.append(0.0)
  a1 = (float(arm_vector[0]) - x1[0])/50
  b1 = (float(arm_vector[1]) - x1[1])/50
  c1 = (float(arm_vector[2]) - x1[2])/50
  for i in range(1, 50):
    t_traj.append(0.1*i)
    x2 = copy.deepcopy(x)
    x2[0] += a1*i
    x2[1] += b1*i
    x2[2] += c1*i
    x_traj.append(x2)
  #rospy.sleep(3)
  ct.robot.FollowXTraj(x_traj, t_traj)
