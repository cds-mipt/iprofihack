#!/bin/bash

docker build .. \
    --network host \
    -f Dockerfile \
    --build-arg UID=${UID} \
    --build-arg GID=$(id -g) \
    --build-arg USER=${USER} \
    -t orbslam_python_${USER}:latest

