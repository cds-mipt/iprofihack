#!/bin/bash

docker run -it -d --rm \
    --ipc host --net host --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --name iprofi_${USER} \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v `pwd`/../:/home/docker_iprofi/catkin_ws/src/yaprofi_hack:rw \
    -v /home/${USER}:/home/${USER}:rw \
    -v /data/${USER}:/data/${USER}:rw \
    -v /data_fast/${USER}:/data_fast/${USER}:rw \
    -v /data_fast/IPROFI:/data_fast/IPROFI:ro \
    iprofi_${USER}:latest

