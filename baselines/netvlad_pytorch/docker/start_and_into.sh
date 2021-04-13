#!/bin/bash

if [ "$(docker ps -aq -f status=exited -f name=netvlad)" ]; then
    docker rm netvlad;
fi

docker run -it --rm -d\
    --gpus all \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --privileged \
    --name netvlad \
    --ipc=host \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v `pwd`/../:/home/${USER}/netvlad_pytorch:rw \
    -v /home/${USER}:/home/${USER}:rw \
    -v /data/${USER}:/data/${USER}:rw \
    -v /data_fast/${USER}:/data_fast/${USER}:rw \
    -v /data_fast/IPROFI:/data_fast/IPROFI:ro \

    x64/netvlad_pytorch:latest
    
docker exec --user "docker_netvlad" -it netvlad \
    /bin/bash -c "cd /home/docker_netvlad; /bin/bash"
