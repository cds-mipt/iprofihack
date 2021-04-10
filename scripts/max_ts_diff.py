from __future__ import print_function, division

import argparse
import numpy as np


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=True)
    return parser


def main(args):
    ts_list = []
    with open(args.file, 'r') as f:
        for line in f:
            line = line.strip()
            tokens = line.split()
            if len(tokens) == 2:
                ts, path = tokens
                ts_list.append(float(ts))
    ts = np.array(ts_list)
    print("Max timestamp difference:", np.diff(ts).max())


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    main(args)
