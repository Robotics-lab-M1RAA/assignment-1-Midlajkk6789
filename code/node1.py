#!/usr/bin/env/python3   

import rospy 
from std_msgs.msg import String 
def print_message(msg): 

    rospy.loginfo("Message received") 
    
    rospy.loginfo(msg) 

def lab_publisher1():

    rospy.init_node('Midlaj')

    pub = rospy.Publisher('hello_class', String, queue_size=10) 

    rospy.Subscriber("welcome", String,print_message) 
    
    
    rate = rospy.Rate(10)  
    
    rospy.loginfo('')

    while not rospy.is_shutdown():
        
        msg = String() 
        msg.data = "Hello RAA 24_26!" 
        
        pub.publish(msg) 
        
        
        
        rate.sleep() 


if __name__=='__main__':
    try:
        lab_publisher1() 
        
    except rospy.ROSInterruptException: 
        
        pass 