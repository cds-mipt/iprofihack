import argparse
import numpy as np


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gt', type=str, required=True)
    parser.add_argument('--result', type=str, required=True)
    return parser


def calc_metric(gt_xyz, result_xyz):
    return np.sqrt(np.square(gt_xyz - result_xyz).sum(axis=1)).mean()


def main(args):
    gt = np.loadtxt(args.gt)  # load from TUM
    gt_xyz = gt[:, 1:4]

    result_xyz = np.loadtxt(args.result)

    ATE = calc_metric(gt_xyz, result_xyz)

    print("ATE =", ATE)


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    main(args)
