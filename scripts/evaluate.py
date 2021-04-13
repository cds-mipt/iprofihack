import argparse
from math import sqrt


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gt', type=str, required=True)
    parser.add_argument('--result', type=str, required=True)
    return parser


def calc_metric(gt_xyz, result_xyz):
    S = sum([sqrt((gt_x - result_x)**2 + (gt_y - result_y)**2 + (gt_z - result_z)**2)
            for (gt_x, gt_y, gt_z), (result_x, result_y, result_z) in zip(gt_xyz, result_xyz)])
    return S / len(gt_xyz)


def loadtxt(path):
    data = []
    with open(path, 'r') as f:
        for line in f:
            values = list(map(float, line.strip().split(' ')))
            data.append(values)
    return data


def main(args):
    gt = loadtxt(args.gt)  # load from TUM
    gt_xyz = [values[1:4] for values in gt]

    result_xyz = loadtxt(args.result)

    ATE = calc_metric(gt_xyz, result_xyz)

    print("ATE =", ATE)


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    main(args)
