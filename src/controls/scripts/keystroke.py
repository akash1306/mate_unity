#!/usr/bin/env python3
import getch
import rospy
from std_msgs.msg import String #String message 
from std_msgs.msg import Int8



def keys():
    pub = rospy.Publisher('key',Int8,queue_size=10) 
    rospy.init_node('keypress',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        k=ord(getch.getch())
        
        
        rospy.loginfo(str(k))# to print on  terminal 
        pub.publish(k)#to publish

        rate.sleep()

#s=115,e=101,g=103,b=98

if __name__=='__main__':
    try:
        keys()
    except rospy.ROSInterruptException:
        pass
