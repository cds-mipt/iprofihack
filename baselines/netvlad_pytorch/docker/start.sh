#!/bin/bash

if [ "$(docker ps -aq -f status=exited -f name=netvlad_${USER})" ]; then
    docker rm netvlad_${USER};
fi

docker run -it --rm -d\
    --gpus all \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --privileged \
    --name netvlad_${USER} \
    --ipc=host \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v `pwd`/../:/home/docker_netvlad:rw \
    -v /data/${USER}:/data/docker_netvlad:rw \
    -v /data_fast/${USER}:/data_fast/docker_netvlad:rw \
    -v /data_fast/IPROFI:/data_fast/IPROFI:ro \
    x64/netvlad_pytorch:latest
