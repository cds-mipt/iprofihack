import json
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import cv2
import PIL
from PIL import Image
from PIL import ImageFont, ImageDraw
from tqdm import tqdm
import argparse

import getpass
USER = getpass.getuser()

parser = argparse.ArgumentParser(description='preparing metadata for NetVLAD')

parser.add_argument('--images_dir', type=str, default='/data_fast/IPROFI/', help='Path to root directory, containing subfolders with images or images')
parser.add_argument('--output_metadata', type=str, default='/home/{USER}/netvlad_pytorch/metadata.json', help='Path to root directory, containing subfolders with images or images')

if __name__ == "__main__":
    args = parser.parse_args()
    
    data = {}
    data['dbImage'] = []
    data['qImage'] = []
    
    for filename in Path(args.images_dir).rglob('*.png'):
        if filename.find('test') != -1:
            if filename.find('rgb_left') != -1:
                data['qImage'].append(filename.relpath(args.images_dir))
        elif filename.find('train') != -1:
            if filename.find('rgb_left') != -1:
                data['dbImage'].append(filename.relpath(args.images_dir))
    data['numDb'] = len(data['dbImage'])
    data['numQ'] = len(data['qImage'])
    
    with open(args.output_metadata, 'w') as fp:
        json.dump(data, fp)
