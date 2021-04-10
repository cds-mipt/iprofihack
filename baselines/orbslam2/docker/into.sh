#!/bin/bash
docker exec --user "docker_orbslam" -it orbslam_python \
    /bin/bash -c "cd /home/docker_orbslam; /bin/bash"
