FROM andsfonseca/orbslam2_python:1.0

RUN python3 -m pip install opencv-python

# add user and his password
ARG USER=docker_orbslam
ARG UID=1000
ARG GID=1000
# default password
ARG PW=user

RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd
WORKDIR /home/${USER}
USER ${UID}:${GID}
