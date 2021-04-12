#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
from ros_coppeliasim.msg import mob_rob_message
from std_msgs.msg import Float32
result = False

def chatter_callback(message):

    global result
    result = message.data
    # return result
    # print(result)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/sim_ros_interface/proximity_sensor_data", Bool, chatter_callback)
    # rospy.spin()

def vel_publisher(result):
    # print("Publishing")
    
    vel_pub = rospy.Publisher('/vel_topic', Float32, queue_size=10)
    rate = rospy.Rate(1)
    velocity = Float32()
    velocity.data = 4
    
    # vel_pub = rospy.Publisher('/vel_topic', mob_rob_message, queue_size=10)
    # while not rospy.is_shutdown():
    # velocity = mob_rob_message()
    # velocity.id = 1
    # velocity.name = "AMD007"
    # if result:
    #     velocity.right_motor_vel = -2
    #     velocity.left_motor_vel = -8
    # else:
    #     velocity.right_motor_vel = 4
    #     velocity.left_motor_vel =  4
    vel_pub.publish(velocity)
    rate.sleep()




if __name__ == '__main__':
    # rospy.init_node('vel_pub_node', anonymous=True)
    # result = True
    while not rospy.is_shutdown():
        listener()
        # print(result)
        # print("my name is subham")
        vel_publisher(result)
        # print("ok")
        # rospy.spin()