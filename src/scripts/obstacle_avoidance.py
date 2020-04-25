#!/usr/bin/env python

# aim is to subscribe to /m2wr/laser/scan  or  use the data for obstacle avoidance or then publish a Twist message to give the bot command to move

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

msg = Twist()
case = ''
linearx = 0
angularz = 0

def checkcase(range):
    if ( range["right"] >1  and range["center"] > 1 and range["left"] >1):
        case = 'NO OBSTACLE!'
        linearx=0.6
        angularz=0
    elif ( range["right"] > 1  and range["center"] < 1 and range["left"] > 1 ):
        case = 'OBSTACLE CENTER!'
        linearx=0
        angularz=-0.5
    elif ( range["right"] < 1  and range["center"] > 1 and range["left"] > 1 ):
        case = 'OBSTACLE RIGHT!'
        linearx=0
        angularz=0.5
    elif ( range["right"] > 1  and range["center"] > 1 and range["left"] < 1 ):
        case = 'OBSTACLE LEFT!'
        linearx=0
        angularz=-0.5
    elif ( range["right"] < 1  and range["center"] > 1 and range["left"] < 1 ):
        case = 'OBSTACLE RIGHT AND LEFT!'
        linearx=0.6
        angularz=0
    elif ( range["right"] > 1  and range["center"] < 1 and range["left"] < 1 ):
        case = 'OBSTACLE CENTER AND LEFT!'
        linearx=0
        angularz=-0.5
    elif ( range["right"] < 1  and range["center"] < 1 and range["left"] > 1 ):
        case = 'OBSTACLE CENTER AND RIGHT!'
        linearx=0
        angularz=0.5
    elif ( range["right"] < 1  and range["center"] < 1 and range["left"] < 1 ):
        case = 'OBSTACLE AHEAD!'
        linearx=0
        angularz=0.8


    rospy.loginfo(case)
    msg.linear.x = linearx
    msg.angular.z = angularz
    pub.publish(msg)


def callback(message):
    range={
        "right" : min(min(message.ranges[0:239]) , 2),
        "center" : min(min(message.ranges[240:479]) , 2),
        "left" : min(min(message.ranges[480:719]) , 2)
    }

    checkcase(range)

def listener():
    global pub
    rospy.init_node('obstacle_avoid', anonymous=False)
    pub = rospy.Publisher("/cmd_vel" , Twist , queue_size=1)
    sub = rospy.Subscriber("/m2wr/laser/scan", LaserScan , callback)
    
    rospy.spin()    

if __name__ == '__main__':
    listener()