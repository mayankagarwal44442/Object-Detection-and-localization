#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
import time

#rospy.init_node('basic_shapes')
pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)

def pub_marker(frame_id, ns, id1, x, y, r, g, b, label):

	print("Publishing at: x:",x,"y:",y)

	marker = Marker()
	marker.header.frame_id = frame_id
	marker.type = marker.TEXT_VIEW_FACING
	marker.action = marker.ADD
	

	   
	marker.ns = ns
	marker.id = id1
	print("Before",label)
	label = label.split(":")
	label = label[1]
	print(label)
	marker.text = label
	marker.pose.position.x = x
	marker.pose.position.y = y
	marker.pose.position.z = 0;
	marker.pose.orientation.x = 0.0;
	marker.pose.orientation.y = 0.0;
	marker.pose.orientation.z = 0.0;
	marker.pose.orientation.w = 1.0;

	marker.scale.x = 0.1;
	marker.scale.y = 0.1;
	marker.scale.z = 0.1;

	marker.color.r = r
	marker.color.g = g
	marker.color.b = b
	marker.color.a = 1.0;

	t = rospy.Duration()
	marker.lifetime = t
	rate = rospy.Rate(1) # 10hz


	for i in range(2):
		pub.publish(marker)
		rate.sleep()

