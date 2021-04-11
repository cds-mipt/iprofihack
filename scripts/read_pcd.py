import argparse
import pypcd
import numpy as np


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pcd', type=str, required=True)
    return parser


def main(args):
    pc = pypcd.pypcd.PointCloud.from_path(args.pcd)
    print(pc.pc_data.dtype)
    print(pc.pc_data['x'].shape)  # y, z
    print(pc.get_metadata())


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    main(args)
