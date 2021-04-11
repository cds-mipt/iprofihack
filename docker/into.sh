#!/bin/bash
docker exec --user docker_iprofi -it iprofi_${USER} \
    /bin/bash -c ". /ros_entrypoint.sh; cd /home/docker_iprofi; /bin/bash"
