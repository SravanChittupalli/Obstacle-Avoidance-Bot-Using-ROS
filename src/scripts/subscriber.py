#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(message):
    range=[min(min(message.ranges[0:102]) , 2),
        min(min(message.ranges[102:205]) , 2),
        min(min(message.ranges[205:307]) , 2),
        min(min(message.ranges[308:410]) , 2),
        min(min(message.ranges[411:513]) , 2),
        min(min(message.ranges[514:617]) , 2),
        min(min(message.ranges[618:719]) , 2)]

    print(range)



def listener():

    rospy.init_node('laser_scan_node' )
    rospy.Subscriber("/m2wr/laser/scan", LaserScan , callback )

    rospy.spin()    # spin() simply keeps python from exiting until this node is stopped

if __name__ == '__main__':
    listener()