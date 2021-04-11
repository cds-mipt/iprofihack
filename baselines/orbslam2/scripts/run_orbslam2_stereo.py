#!/usr/bin/python3

import argparse
import orbslam2
import os
import cv2

from time import sleep


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vocab', type=str, required=True)
    parser.add_argument('--config', type=str, required=True)
    parser.add_argument('--seq', type=str, required=True)
    return parser


def main(args):
    sequence = []
    with open(os.path.join(args.seq, 'rgb_left.txt'), 'r') as f_left, open(os.path.join(args.seq, 'rgb_right.txt'), 'r') as f_right:
        for line_left, line_right in zip(f_left, f_right):
            line_left, line_right = line_left.strip(), line_right.strip()
            if line_left.startswith('#'):
                continue
            ts, img_left_path = line_left.split()
            _, img_right_path = line_right.split()
            sequence.append((float(ts), os.path.join(args.seq, img_left_path), os.path.join(args.seq, img_right_path)))

    slam = orbslam2.System(args.vocab, args.config, orbslam2.Sensor.STEREO)
    slam.set_use_viewer(True)
    slam.initialize()

    for ts, path_left, path_right in sequence:
        img_left = cv2.imread(path_left)
        img_right = cv2.imread(path_right)
        slam.process_image_stereo(img_left, img_right, ts)
        sleep(0.1)

    save_trajectory(slam.get_trajectory_points(),  'trajectory.txt')

    slam.shutdown()


def save_trajectory(trajectory, filename):
    with open(filename, 'w') as traj_file:
        traj_file.writelines('{time} {r00} {r01} {r02} {t0} {r10} {r11} {r12} {t1} {r20} {r21} {r22} {t2}\n'.format(
            time=repr(t),
            r00=repr(r00),
            r01=repr(r01),
            r02=repr(r02),
            t0=repr(t0),
            r10=repr(r10),
            r11=repr(r11),
            r12=repr(r12),
            t1=repr(t1),
            r20=repr(r20),
            r21=repr(r21),
            r22=repr(r22),
            t2=repr(t2)
        ) for t, r00, r01, r02, t0, r10, r11, r12, t1, r20, r21, r22, t2 in trajectory)


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    main(args)
