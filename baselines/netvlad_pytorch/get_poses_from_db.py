import argparse
import os
import json

parser = argparse.ArgumentParser(description='getting poses from database images')

parser.add_argument('--pairs_NetVLAD', type=str, default='/home/docker_netvlad/NetVLAD_query_top_40.txt', help='Path to the file that contains matched pairs of images')
parser.add_argument('--root_image_dir', type=str, default='/data_fast/IPROFI', help='Path to root directory, containing subfolders with images or images')
parser.add_argument('--metadata_for_NetVLAD', type=str, default='/home/docker_netvlad/metadata.json', help='Path to the file with dataset metadata, prepared for NetVLAD')
parser.add_argument('--output_file', type=str, default='/home/docker_netvlad/NetVLAD_submission', help='Text file with timestamps and poses')


if __name__ == "__main__":
    args = parser.parse_args()
    
    output_file = open(args.output_file, 'w')
    pairs_file = open(args.pairs_NetVLAD, 'r')
    metadata_file = open(args.metadata_for_NetVLAD)
    metadata = json.load(metadata_file)
    pairs_lines = pairs_file.readlines()
    pairs_lines = [pairs_lines[i].split(' ') for i in range(len(pairs_lines))]
    query_image_predictions = {}
    for pair in sorted(pairs_lines):
        query_image = pair[0]
        db_image = pair[1]
        if query_image in query_image_predictions.keys():
            query_image_predictions[query_image.rstrip('.png')].append(db_image.rstrip('.png'))
        else:
            query_image_predictions[query_image.rstrip('.png')] = [db_image.rstrip('.png')]
    for query_image in sorted(metadata['qImage']):
        # we take top 1 prediction from NetVLAD (there are 40 predictions sorted by similiarity)
        image_db = query_image_predictions[os.path.basename(query_image).rstrip('.png')][0]
        date_db = db_image.split('_')[0] # this should be like 2021-03-27-09-08-15
        date_query = query_image.split('_')[0]
        
        db_kitti_filename = os.path.join(args.root_image_dir, 'train', date_db, 'gt_kitti.txt')
        db_tum_filename = os.path.join(args.root_image_dir, 'train', date_db, 'gt_tum.txt')
        db_kitti_file = open(db_kitti_filename, 'r')
        db_tum_file = open(db_tum_filename, 'r')
        db_kitti_lines = db_kitti_file.readlines()
        db_tum_lines = db_tum_file.realines()

        num_db = db_image.split('/')[-1]
        num_db = int(num_db.rstrip('.png'))
        num_query = query_image.split('/')[-1]
        num_query = int(query_image.rstrip('.png'))

        timestamp = db_tum_lines[num_db]
        timestamp = timestamp.split(' ')[0]

        pose = db_kitti_lines[num_db]

        output_file.write("{} {}\n".format())
    output_file.close()
        

        