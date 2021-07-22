#!/usr/bin/env python2

import rospy

if __name__ == "__main__":
    rospy.init_node('practice_node')
    rospy.loginfo("practice node startd")

    rate = rospy.Rate(10)
    count = 0
    while not rospy.is_shutdown():
        rospy.loginfo("schmello")
