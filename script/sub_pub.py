#!/usr/bin/env python
import rospy
from std_msgs.msg import String



def callback(msg):
    new_data = msg.data + " Manipulate the data"
    # rospy.loginfo(rospy.get_caller_id() + "I processed ", new_data)
    publisher.publish(new_data) #publish the manipulated data on a new topic
    #test if when the robot is not moving, the thrust_force is 0, then you move joystick it changes, then lastly, applying a surge value here, does it change the thrust_force


def subscriber():
    rospy.Subscriber("/published_topic_name", String, callback) #subscribe to a running topic and perform the callback




if __name__ == "__main__":
    rospy.init_node("sub_pub")
    publisher = rospy.Publisher("/publisher", String, queue_size=10)

    subscriber()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass