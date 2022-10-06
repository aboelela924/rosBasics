#!/usr/bin/python3.8

import rospy
# from std_msgs.msg import Int32
from basics.msg import Complex

def callback(msg):
    print(f"Real: {msg.real}, Imaginary: {msg.imaginary}")

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('counter', Complex, callback)

rospy.spin()