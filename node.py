#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Odometry
import numpy as np
import math
class node():
#f, g, and h values for A* and Ids, locations
	ids=0
	x=0
	y=0
	g=0
	f=0
	h=0
	status=0
	parent=0
	def __init__(self,ids,x,y,g,h,f,status,parent):
		self.ids=ids
		self.x=x
		self.y=y
		self.g=g
		self.h=h
		self.f=f
		self.status=status
		self.parent=parent

