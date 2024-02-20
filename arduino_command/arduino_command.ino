#include <ros.h>
#include "geometry_msgs/Twist.h" 
#include <std_msgs/Int16.h>
#include <std_msgs/String.h>


ros::NodeHandle  nh;
std_msgs::Int16 sensorData;
std_msgs::Int16 cmdBTN;
std_msgs::Int16 motion;
geometry_msgs::Twist msg;


void control_LED( const std_msgs::Int16& cmd_msg)
{
  int value = cmd_msg.data;
  digitalWrite(13, value);   // blink the led
}

ros::Publisher BTN("turtle1/cmd_vel", &msg );
ros::Subscriber<std_msgs::Int16> ledsub("Topic_LED_13", &control_LED );
ros::Publisher Status("Status",&motion);

void setup() 
{
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(7,INPUT);
  pinMode(6,INPUT);
  pinMode(5,INPUT);
  digitalWrite(13, 1); 
  nh.initNode();
  nh.subscribe(ledsub);
  nh.advertise(BTN);
  nh.advertise(Status);
}
int mode=0;
void loop() 
{
  // put your main code here, to run repeatedly:
  int BTN1 = digitalRead(7);
  int BTN2 = digitalRead(6);
  int BTN3 = digitalRead(5);
  int sensorData;
  if (BTN3 == 0)
  {
    mode=~mode;
  }
  if(BTN1==0&&BTN2==0)
  {
    if(mode == 0)
    {
      msg.linear.x = 1.0;
      motion.data = 1;
      Status.publish(&motion);
      delay(100);
    }
    else
    {
      msg.linear.x = -1.0;
      motion.data = 2;
      Status.publish(&motion);
      delay(100);
    }
  }
  else if (BTN2==0)
  {
    msg.angular.z= 1.0;
    motion.data = 3;
    Status.publish(&motion);
    delay(100);
  }
  else if (BTN1==0)
  {
    msg.angular.z= -1.0;
    motion.data = 4;
    Status.publish(&motion);
    delay(100);
  }
  BTN.publish(&msg);
  msg.linear.x = 0.0;
  msg.angular.z= 0.0;
  nh.spinOnce();
  delay(1);
}
