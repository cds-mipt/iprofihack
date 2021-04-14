import argparse
import os

parser = argparse.ArgumentParser(description='getting poses from database images')

parser.add_argument('--pairs_NetVLAD', type=str, default='/home/docker_netvlad/NetVLAD_query_top_40.txt', help='Path to the file that contains matched pairs of images')
parser.add_argument('--root_image_dir', type=str, default='/data_fast/IPROFI', help='Path to root directory, containing subfolders with images or images')
parser.add_argument('--output_file', type=str, default='/home/docker_netvlad/NetVLAD_submission', help='Text file with timestamps and poses')


if __name__ == "__main__":
    args = parser.parse_args()
    
    output_file = open(args.output_file, 'w')
    pairs_file = open(args.pairs_NetVLAD, 'r')
    pairs_lines = pairs_file.readlines()
    pairs_lines = [pairs_lines[i].split(' ') for i in range(len(pairs_lines))]
    for pair in sorted(pairs_lines):
        query_image = pair[0]
        db_image = pair[1]
        date_db = db_image.split('/')[3]
        date_query = query_image.split('/')[3]
        
        db_kitti_filename = os.path.join(args.root_image_dir, 'train', date_db, 'gt_kitti.txt')
        q_tum_filename = os.path.join(args.root_image_dir, 'train', date_db, 'gt_tum.txt')
        db_kitti_file = open(db_kitti_filename, 'r')
        q_tum_file = open(q_tum_filename, 'r')
        db_kitti_lines = db_kitti_file.readlines()
        q_tum_lines = q_tum_file.realines()

        num_db = db_image.split('/')[-1]
        num_db = int(num_db.rstrip('.png'))
        num_query = query_image.split('/')[-1]
        num_query = int(query_image.rstrip('.png'))

        timestamp = q_tum_lines[num_db]
        timestamp = timestamp.split(' ')[0]

        pose = db_kitti_lines[num_db]

        output_file.write("{} {}\n".format())
    output_file.close()
        

        