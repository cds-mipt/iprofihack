#!/bin/bash

docker run -it -d --rm \
    --ipc host --net host --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --name orbslam_python_${USER} \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v `pwd`/../:/home/${USER}/orbslam2:rw \
    -v /home/${USER}:/home/${USER}:rw \
    -v /data/${USER}:/data/${USER}:rw \
    -v /data_fast/${USER}:/data_fast/${USER}:rw \
    -v /data_fast/IPROFI:/data_fast/IPROFI:ro \
    orbslam_python_${USER}:latest

