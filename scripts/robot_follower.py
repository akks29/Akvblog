#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Point,Twist
from nav_msgs.msg import Odometry
import numpy as np
from tf.transformations import euler_from_quaternion
from sensor_msgs.msg import LaserScan

class RobotController:
    #initialised values
    def __init__(self):

        rospy.init_node('controller')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/odom', Odometry, self.odom_callback)
        
        self.pose = []
        self.velocity_msg = Twist()

    #odmom callack function
    def odom_callback(self,data):
      x = data.pose.pose.orientation.x
      y = data.pose.pose.orientation.y
      z = data.pose.pose.orientation.z
      w = data.pose.pose.orientation.w
      self.pose = [data.pose.pose.position.x, data.pose.pose.position.y, euler_from_quaternion([x,y,z,w])[2]]

    #move function to move robot
    def move(self,linear,angular):
        self.velocity_msg.linear.x = linear
        #self.velocity_msg.angular.z = angular 
        self.pub.publish(self.velocity_msg)
        

   





if _name_ == "_main_":
    Robot = Robot_Controller()
    