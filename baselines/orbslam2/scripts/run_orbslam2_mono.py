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
    with open(os.path.join(args.seq, 'rgb_left.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue
            ts, img_path = line.split()
            sequence.append((float(ts), os.path.join(args.seq, img_path)))

    slam = orbslam2.System(args.vocab, args.config, orbslam2.Sensor.MONOCULAR)
    slam.set_use_viewer(True)
    slam.initialize()

    for ts, path in sequence:
        img = cv2.imread(path)
        slam.process_image_mono(img, ts)
    
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
