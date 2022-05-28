#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Point,Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2

x = 0.0
y = 0.0 
theta = 0.0

class RobotController:
    #initialised values
    def __init__(self):

        rospy.init_node('controller')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/odom', Odometry, self.odom_callback)
        
        self.pose = []
        self.velocity_msg = Twist()
        

    #odmom callack function
    def odom_callback(msg):

        global x
        global y
        global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

    #move function to move robot
    def move(self,linear,angular):
        r = rospy.Rate(4)
        while not rospy.is_shutdown():
           self.velocity_msg.linear.x = 0.5
           self.velocity_msg.linear.z = 0.0
        

        self.pub.publish(self.velocity_msg)
        r.sleep()
    
    
   



if __name__ == "__main__":
    Robot = Robot_Controller()
    