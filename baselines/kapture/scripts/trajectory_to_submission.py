#!/usr/bin/python3

import argparse
import os
import cv2
import numpy as np

from time import sleep


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--traj', type=str, required=True)
    parser.add_argument('--seq', type=str, required=True)
    return parser


def main(args):
    ts, T = open_trajectory(args.traj)
    
    T_init = np.eye(4)
    T_init[:3] = np.loadtxt(os.path.join(args.seq, 'gt_kitti.txt')).reshape(-1, 3, 4)[0]

    T_transformed = np.array([T_init.dot(Ti) for Ti in T])

    xyz = T_transformed[:, :3, 3]
    np.savetxt('submission.txt', xyz)


def open_trajectory(filename):
    data = np.loadtxt(filename)
    ts = data[:, 0]
    T = np.zeros([len(ts), 4, 4])
    T[:, :3] = data[:, 1:].reshape(-1, 3, 4)
    T[:, 3, 3] = 1
    return ts, T


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    main(args)
