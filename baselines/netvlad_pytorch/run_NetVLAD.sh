#!/bin/bash

python3 main.py \
   --mode test \
   --cacheBatchSize 1 \
   --resume /data/vgg16_netvlad_checkpoint \
   --metadata_json_file /home/docker_netvlad/metadata.json \
   --output_file /home/docker_netvlad/NetVLAD_query_top_40.txt 