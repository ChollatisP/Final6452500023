#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
import os
from std_msgs.msg import String
from std_msgs.msg import Int16

frame = Tk()
frame.title("Turtle_Control")
frame.geometry("200x300")

def BTN(num):
     if num.data==1:
        text = "Forward"
        pub2.publish(text)
     elif num.data==2:
        text = "Backward"
        pub2.publish(text)
     elif num.data==3:
        text = "Turn Left"
        pub2.publish(text)
     elif num.data==4:
        text = "Turn Right"
        pub2.publish(text)
          
     
  
pub1 = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
pub2 = rospy.Publisher('motion', String, queue_size=10)
ledpub = rospy.Publisher("Topic_LED_13", Int16, queue_size = 10) 
BTNsub = rospy.Subscriber("status",Int16,callback=BTN)
rospy.init_node("Turtle_Control")
rate = rospy.Rate(10) # 10hz
def fw():
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z= 0.0
    pub1.publish(cmd)
    text = "Forward"
    pub2.publish(text)
        
def bw():
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z= 0.0
    pub1.publish(cmd)
    text = "Backword"
    pub2.publish(text)
       
def lt():
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 1.0
    pub1.publish(cmd)
    text = "Turn Left"
    pub2.publish(text)
   
def rt():
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= -1.0
    pub1.publish(cmd)
    text = "Turn Right"
    pub2.publish(text)

def Talker(val):
	cmd_val = Int16(val)
	rospy.loginfo(cmd_val)
	ledpub.publish(cmd_val)
    
def on():
    os.system('rosservice call /turtle1/set_pen 255 255 255 3 0')
    Talker(1)
    text = "PenON"
    pub2.publish(text)

def off():
    os.system('rosservice call /turtle1/set_pen 255 255 255 3 1')
    Talker(0)
    text = "PenOFF"
    pub2.publish(text)


B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=120)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=230)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=180)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=180)

B5 = Button(text = "PenON", command=on)
B5.place(x=100, y=250)

B6 = Button(text = "PenOFF", command=off)
B6.place(x=20, y=250)


frame.mainloop()    
    
    
    