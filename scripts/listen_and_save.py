#!/usr/bin/python

from __future__ import absolute_import, print_function, division

import argparse
import rospy
import os
import cv_bridge
import cv2
import tf

from sensor_msgs.msg import Image, CompressedImage
from nav_msgs.msg import Odometry
from message_filters import ApproximateTimeSynchronizer, Subscriber


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--outdir', type=str, required=True)
    parser.add_argument('--seq', type=str, required=True)
    return parser


outdir = None
br = None
seq = None
index = 0


def callback(image_left_msg, image_right_msg, depth_msg, odom_msg):
    global index

    image_left = br.compressed_imgmsg_to_cv2(image_left_msg)
    image_right = br.compressed_imgmsg_to_cv2(image_right_msg)
    depth = br.imgmsg_to_cv2(depth_msg)

    pose_msg = odom_msg.pose.pose
    tx, ty, tz = pose_msg.position.x, pose_msg.position.y, pose_msg.position.z
    qx, qy, qz, qw = pose_msg.orientation.x, pose_msg.orientation.y, pose_msg.orientation.z, pose_msg.orientation.w
    T = tf.transformations.quaternion_matrix([qx, qy, qz, qw])
    T[:3, 3] = tx, ty, tz

    odom_ts = '{}.{:0>9}'.format(odom_msg.header.stamp.secs, odom_msg.header.stamp.nsecs)
    img_ts = '{}.{:0>9}'.format(image_left_msg.header.stamp.secs, image_left_msg.header.stamp.nsecs)

    with open(os.path.join(outdir, 'gt_tum.txt'), 'a') as f:
        f.write("{} {} {} {} {} {} {} {}\n".format(odom_ts, tx, ty, tz, qx, qy, qz, qw))

    with open(os.path.join(outdir, 'gt_kitti.txt'), 'a') as f:
        f.write(" ".join(map(str, T[:3].flatten())) + '\n')

    left_filename = '{}_left_{:0>6}.png'.format(seq, index)
    left_rel_path = os.path.join('rgb_left', left_filename)
    cv2.imwrite(os.path.join(outdir, left_rel_path), image_left)
    with open(os.path.join(outdir, 'rgb_left.txt'), 'a') as f:
        f.write(img_ts + ' ' + left_rel_path + '\n')

    right_filename = '{}_right_{:0>6}.png'.format(seq, index)
    right_rel_path = os.path.join('rgb_right', right_filename)
    cv2.imwrite(os.path.join(outdir, right_rel_path), image_right)
    with open(os.path.join(outdir, 'rgb_right.txt'), 'a') as f:
        f.write(img_ts + ' ' + right_rel_path + '\n')

    depth_filename = '{}_depth_{:0>6}.exr'.format(seq, index)
    depth_rel_path = os.path.join('depth', depth_filename)
    cv2.imwrite(os.path.join(outdir, depth_rel_path), depth)
    with open(os.path.join(outdir, 'depth.txt'), 'a') as f:
        f.write(img_ts + ' ' + depth_rel_path + '\n')

    index += 1


def main(args):
    rospy.init_node('bag_to_yaprofi')

    global outdir, br, seq
    outdir = args.outdir
    br = cv_bridge.CvBridge()
    seq = args.seq

    os.makedirs(os.path.join(outdir, 'rgb_left'))
    os.makedirs(os.path.join(outdir, 'rgb_right'))
    os.makedirs(os.path.join(outdir, 'depth'))

    with open(os.path.join(outdir, 'rgb_left.txt'), 'w') as f:
        f.write('#\n' * 3)
    with open(os.path.join(outdir, 'rgb_right.txt'), 'w') as f:
        f.write('#\n' * 3)
    with open(os.path.join(outdir, 'depth.txt'), 'w') as f:
        f.write('#\n' * 3)
    with open(os.path.join(outdir, 'gt_tum.txt'), 'w') as f:
        pass
    with open(os.path.join(outdir, 'gt_kitti.txt'), 'w') as f:
        pass

    sub_image_left = Subscriber('/zed_node/left/image_rect_color/compressed', CompressedImage)
    sub_image_right = Subscriber('/zed_node/right/image_rect_color/compressed', CompressedImage)
    sub_depth = Subscriber('/zed_node/depth/depth_registered', Image)
    sub_odom = Subscriber('/groundtruth', Odometry)

    ats = ApproximateTimeSynchronizer([sub_image_left, sub_image_right, sub_depth, sub_odom], queue_size=5, slop=0.05)
    ats.registerCallback(callback)

    rospy.spin()


if __name__ == '__main__':
    parser = build_parser()
    args, _ = parser.parse_known_args()
    main(args)
