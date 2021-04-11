#!/bin/bash
docker exec --user ${USER} -it orbslam_python_${USER} \
    /bin/bash -c "cd /home/${USER}; /bin/bash"
