#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ros1_template.msg import default


pub = rospy.Publisher('/published_topic_name', String, queue_size=10) # String is changed to the message type


def publisher():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node('publisher', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
        hello_str = "hello world %s"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

    # #keep publishing until a Ctrl-C is pressed
    # i = 0
    # while not rospy.is_shutdown():
    #     hello_str = "hello world %s" % i
    #     rospy.loginfo(hello_str)
    #     pub.publish(hello_str)
    #     rate.sleep()
    #     i=i+1

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass