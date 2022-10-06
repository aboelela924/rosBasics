#!/usr/bin/python3.8

import rospy
from basics.srv import WordCount;
import sys;

rospy.init_node('service_client')
rospy.wait_for_service('word_count_service')
wordCount = rospy.ServiceProxy('word_count_service', WordCount)
words = ' '.join(sys.argv[1:])
print(f"Word count is {wordCount(words).count}") 