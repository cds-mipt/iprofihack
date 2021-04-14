#FROM ubuntu:18.04
FROM nvidia/cudagl:10.0-devel-ubuntu18.04
MAINTAINER naverlabs "kapture@naverlabs.com"

# setup environment
ENV     LANG C.UTF-8
ENV     LC_ALL C.UTF-8
ENV     DEBIAN_FRONTEND noninteractive
# arguments
ARG     MAKE_OPTIONS="-j8"


# Get dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    git \
    wget\
    curl \
    unzip \
    python3.6 python3-pip \
    pandoc asciidoctor \
    cmake \
    build-essential \
    libboost-all-dev \
    libsuitesparse-dev \
    libfreeimage-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libglew-dev \
    freeglut3-dev \
    libxmu-dev \
    libxi-dev \
    libatlas-base-dev \
    libsuitesparse-dev \
    libcgal-qt5-dev \
    libqt5opengl5-dev \
    qt5-default \
    x11-apps \
    mesa-utils \
  && rm -rf /var/lib/apt/lists/*


########################################################################################################################
# PYTHON-PIP ###########################################################################################################
# make sure pip 3 is >= 20.0 to enable use-feature=2020-resolver
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools wheel twine

########################################################################################################################
# install kapture from pip.
RUN      python3 -m pip install kapture

RUN      python3 -m pip install "torch==1.4.0" "torchvision==0.5.0" "scikit_learn==0.20.2"
RUN      pip install --upgrade ipykernel
RUN      pip install jupyter notebook

RUN mkdir /home/${USER}/repo
WORKDIR /home/${USER}/repo

RUN git clone https://github.com/naver/r2d2.git
RUN git clone https://github.com/naver/deep-image-retrieval.git
RUN git clone https://github.com/naver/kapture.git kapture
RUN git clone https://github.com/naver/kapture-localization.git


ARG USER=docker_kapture
ARG UID=1000
ARG GID=1000
# default password
ARG PW=user
RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd



### FINALIZE ###################################################################
# save space: purge apt-get
RUN     rm -rf /var/lib/apt/lists/*
WORKDIR /home/${USER}
USER ${UID}:${GID}
ENTRYPOINT jupyter notebook --ip 0.0.0.0 --port 8889 --no-browser --allow-root
