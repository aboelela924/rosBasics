#!/usr/bin/python3.8

import rospy
from basics.srv import WordCount, WordCountResponse

def wordCount(request):
    return WordCountResponse(len(request.words.split()))


rospy.init_node('word_count_service')
service = rospy.Service("word_count_service", WordCount, wordCount)
rospy.spin()