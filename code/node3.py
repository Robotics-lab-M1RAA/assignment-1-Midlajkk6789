
#!/usr/bin/env/python3

import rospy 

from std_msgs.msg import String 

def print_message(msg): 

    rospy.loginfo("Message received") 
    
    rospy.loginfo(msg) 

def lab_subscriber1(): 

    rospy.init_node('CET') 
    
     
     
    rospy.Subscriber("hello_collage", String, print_message)  

    rospy.spin() 

if __name__=='__main__': 

    lab_subscriber1() 