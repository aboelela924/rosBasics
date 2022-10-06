#!/usr/bin/python3.8

import rospy
import actionlib
from basics.msg import TimerAction, TimerGoal, TimerResult

rospy.init_node('timer_action_client')
action_client = actionlib.SimpleActionClient('timer', TimerAction)
action_client.wait_for_server()
goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)
action_client.send_goal(goal)
action_client.wait_for_result()
print('Time elapsed: %f'%(action_client.get_result().time_elapsed.to_sec()))