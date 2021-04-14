FROM andsfonseca/orbslam2_python:1.0

RUN python3 -m pip install opencv-python

# add user and his password
ARG USER=docker_orbslam
ARG UID=1000
ARG GID=1000
# default password
ARG PW=user

RUN groupadd --gid ${GID} yaprofi2021 && useradd -m ${USER} --uid=${UID} --gid=${GID} && echo "${USER}:${PW}" | chpasswd
WORKDIR /home/${USER}
USER ${UID}:${GID}
