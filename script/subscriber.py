#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(msg):
    #get_caller_id(): Get fully resolved name of local node
    # msg has all the info coming from the topic
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)
    
def subscriber():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('subscriber', anonymous=True)


    # topic should match what you want to subscribe to 
    # change String to message type, 
    # and the callback is executed when a message is received
    rospy.Subscriber("/published_topic_name", String, callback) 

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
