#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8
from controls.msg import keys_message

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    key_val=data.data
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('keypub', anonymous=True)

    rospy.Subscriber("key", Int8 , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    
    
def talker():
    pub = rospy.Publisher('keyvalue', keys_message, queue_size=10)
    rospy.init_node('controller', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    key_pub=keys_message()
    while not rospy.is_shutdown():
        if key_val== 119:
                surge=1
                sway=0
                heave=0
                roll=0
                pitch=0
                yaw=0
        	
        if key_val== 119:
                surge=1
                sway=0
                heave=0
                roll=0
                pitch=0
                yaw=0
        if key_val== 119:
                surge=1
                sway=0
                heave=0
                roll=0
                pitch=0
                yaw=0        	
        	

        pub.publish(keypub)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
