#!/usr/bin/python
from core_tool import *
#from sensor_msgs.msg import Joy
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  ct.AddPub('point', 'joy', std_msgs.msg.Float64)
  pos = float(input())
  #pos[1] = float(input())
  #pos[2]= float(input())
  ct.pub.point.publish(pos)
