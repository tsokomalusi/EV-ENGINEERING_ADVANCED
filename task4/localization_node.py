#!/usr/bin/env python

import rospy
from std_msgs.msg import String  # Import the necessary message type (replace with actual message type)

class LocalizationNode:
    def __init__(self):
        rospy.init_node('localization_node', anonymous=True)
        rospy.Subscriber('control_commands', String, self.process_control_commands)  # Replace 'String' with the actual message type

    def process_control_commands(self, data):
        rospy.loginfo(f"Received Control Command: {data.data}")  # Process the received control command here

if __name__ == '__main__':
    try:
        LocalizationNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
