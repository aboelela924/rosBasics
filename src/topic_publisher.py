#!/usr/bin/python3.8

import rospy
from random import random
from basics.msg import Complex

rospy.init_node('topic_publisher')
pub = rospy.Publisher('counter', Complex)
rate = rospy.Rate(2)

# count = 0

while not rospy.is_shutdown():
    msg = Complex()
    msg.real = random()
    msg.imaginary = random()
    pub.publish(msg)
    # count += 1
    rate.sleep()