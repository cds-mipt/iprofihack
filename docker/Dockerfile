FROM osrf/ros:melodic-desktop-full

# add user and his password
ARG USER=docker_iprofi
ARG UID=1000
ARG GID=1000
# default password
ARG PW=user

RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd
WORKDIR /home/${USER}
RUN mkdir -p catkin_ws/src && chown -R ${UID}:${GID} /home/${USER}
USER ${UID}:${GID}
