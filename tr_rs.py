#!/usr/bin/env python
from core_tool import *
import rospy
import math
import numpy as np
import cv2
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  key = 'a'
  thx = 0
  thy = math.pi/2
  thz = -math.pi/2
  xr=np.array([[1,0,0,0],
               [0,math.cos(thx),math.sin(thx),0],
               [0,-math.sin(thx),math.cos(thx),0],
               [0,0,0,1]])
  yr=np.array([[math.cos(thy),0,-math.sin(thy),0],
               [0,1,0,0],
               [math.sin(thy),math.cos(thy),0,0],
               [0,0,0,1]])
  zr=np.array([[math.cos(thz),math.sin(thz),0,0],
               [-math.sin(thz),math.cos(thz),0,0],
               [0,0,1,0],
               [0,0,0,1]])
  R = np.dot(xr,np.dot(yr,zr))
  a = np.array([[1,0,0,1.0],
                [0,1,0,0],
                [0,0,1,0.5],
                [0,0,0,1]])
  arm_vector = np.array([0.5,
                         0.0,
                         0.5,
                           1])
  x = list(ct.robot.FK())
  x1 = copy.deepcopy(x)
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
    if position[3] >42  and position[3] <806  and position[4]>24 and position[4]<456:
      camera_vector = np.array([position[0]*0.001,
                                position[1]*0.001,
                                position[2]*0.001,
                                1])
      tmp = copy.deepcopy(arm_vector)
      arm_vector = np.dot(a,np.dot(R,camera_vector))
      print(position)
      print(arm_vector)
      #if arm_vector[0] <= 0:
       # break
      if arm_vector != tmp:
        t = np.linalg.norm(arm_vector-tmp) / 0.5
        ct.robot.MoveToXI([arm_vector[0],arm_vector[1],arm_vector[2],x1[3],x1[4],x1[5],x1[6]], t, blocking = True)