#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf import transformations
import math
from std_srvs.srv import *
from statistics import mean
from bot import *

sensor_l, sensor_c, sensor_r = 0, 0, 0
dir = 2
dirs = [180, -90, 0, 90] 