#!/bin/bash

docker build .. \
    --network host \
    -f Dockerfile \
    --build-arg UID=${UID} \
    --build-arg GID=$(id -g) \
    -t iprofi_${USER}:latest

