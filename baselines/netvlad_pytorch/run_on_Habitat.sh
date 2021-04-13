#!/bin/bash

python main.py --mode test --cacheBatchSize 1 --resume /datasets/netvlad_v100_datasets/models/vgg16_netvlad_checkpoint --metadata_json_file /datasets/YaProfi/metadata_for_NetVLAD.json --output_json_file /datasets/YaProfi/NetVLAD_query_top_40.json 
