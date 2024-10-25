#!/usr/bin/env/python3   

import rospy 
from std_msgs.msg import String 

def lab_publisher1():

    rospy.init_node('Midlaj_node1',anonymous=True)

    pub = rospy.Publisher('Greetings', String, queue_size=10) 
    
    
    rate = rospy.Rate(10)  
    
    rospy.loginfo('')

    while not rospy.is_shutdown():
        
        msg = String() 
        msg.data = "Hello, I am Midlaj" 
        
        pub.publish(msg) 
        
        rospy.loginfo(msg)
        
        rate.sleep() 


if __name__=='__main__':
    try:
        lab_publisher1() 
        
    except rospy.ROSInterruptException: 
        
        pass 