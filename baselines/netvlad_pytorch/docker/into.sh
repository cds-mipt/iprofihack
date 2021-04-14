#!/bin/bash

   
docker exec -it x64/netvlad_pytorch_${USER}:latest \
    /bin/bash -c "cd /home/docker_netvlad; /bin/bash"
