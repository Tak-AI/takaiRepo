#!/usr/bin/python
from core_tool import *
from std_msgs.msg import Float64MultiArray

def Run(ct,*args):
  ct.AddSub('chatter', 'chatter', std_msgs.msg.Float64MultiArray, lambda data: ct.SetAttr('obj1','position', data.data))
