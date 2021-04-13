#!/bin/bash

python main.py \
   --mode test \
   --cacheBatchSize 1 \
   --resume /data/vgg16_netvlad_checkpoint \
   --metadata_json_file /home/{USER}/netvlad_pytorch/metadata.json \
   --output_file /home/{USER}/netvlad_pytorch/NetVLAD_query_top_40.txt 
