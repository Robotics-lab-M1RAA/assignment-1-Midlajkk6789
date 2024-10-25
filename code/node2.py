#!/usr/bin/env/python3   

import rospy 
from std_msgs.msg import String 

def print_message(msg): 

    rospy.loginfo("Message received") 
    
    rospy.loginfo(msg) 

def lab_publisher1():

    rospy.init_node('M1RAA_24_26')

    pub1= rospy.Publisher('welcome', String, queue_size=10) 
    pub2= rospy.Publisher('hello_collage', String, queue_size=10) 
    rospy.Subscriber("hello_class", String,print_message) 

    
    
    rate = rospy.Rate(10)  
    
    rospy.loginfo('')

    while not rospy.is_shutdown():
        
        msg1= String() 
        msg1.data = "Hello Midlaj Welcome!" 
        msg2=String()
        msg2.data="Hello CET!" 
        pub1.publish(msg1) 
        pub2.publish(msg2)
        
        # rospy.loginfo(msg1)
        # rospy.loginfo(msg2)
        
        rate.sleep() 


if __name__=='__main__':
    try:
        lab_publisher1() 
        
    except rospy.ROSInterruptException: 
        
        pass 