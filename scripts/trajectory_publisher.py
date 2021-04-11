#!/usr/bin/python

import rospy
import tf
import numpy as np

from geometry_msgs.msg import PointStamped


def load_traj(path):
    data = np.loadtxt(path)
    if data.shape[1] == 12:  # KITTI
        rospy.loginfo('Loaded %d poses from KITTI', len(data))
        return data[:, [3, 7, 11]]
    elif data.shape[1] == 8:  # TUM
        rospy.loginfo('Loaded %d poses from TUM', len(data))
        return data[:, 1:4]
    elif data.shape[1] == 3:  # X Y Z
        rospy.loginfo('Loaded %d poses from X Y Z', len(data))
        return data
    else:
        rospy.logfatal('Unknown traj format')
        exit(0)


def main():
    rospy.init_node('trajectory_publisher')

    rate = rospy.Rate(float(rospy.get_param('~rate')))
    traj = load_traj(rospy.get_param('~traj'))

    pub = rospy.Publisher('traj_points', PointStamped, queue_size=10)

    br = tf.TransformBroadcaster()

    for x, y, z in traj:
        if rospy.is_shutdown():
            break

        t = rospy.Time.now()

        msg = PointStamped()
        msg.header.frame_id = 'map'
        msg.header.stamp = t
        msg.point.x = x
        msg.point.y = y
        msg.point.z = z
        pub.publish(msg)

        br.sendTransform([x, y, z],
                         [0, 0, 0, 1],
                         t,
                         'zed_left_camera_optcal_frame',
                         "map")

        rate.sleep()
    
    rospy.spin()


if __name__ == '__main__':
    main()
