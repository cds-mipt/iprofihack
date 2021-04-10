#!/bin/bash

docker run -it -d --rm \
    --ipc host --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --name orbslam_python \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v `pwd`/../../../:/home/docker_orbslam/catkin_ws/src/yaprofi_hack:rw \
    -v /home/${USER}:/home/${USER}:rw \
    orbslam_python:latest
