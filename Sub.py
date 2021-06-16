#!/usr/bin/python
from core_tool import *
import std_msgs.msg

def Run(ct,*args):
  ct.AddSub('chatter', 'chatter', std_msgs.msg.Float64MultiArray, lambda data: ct.SetAttr('obj1','position', data.data))
  ct.AddSub('UPorSIDE', 'UPorSIDE', std_msgs.msg.String, lambda str: ct.SetAttr('obj2','which', str.data))